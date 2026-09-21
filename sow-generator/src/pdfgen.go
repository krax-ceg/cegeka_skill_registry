package main

import (
	"bytes"
	"fmt"
	"strings"
)

// ---- Cegeka palette (sampled from the reference SOW docx) ----

type rgb struct{ r, g, b float64 }

var (
	colNavy    = rgb{0.0 / 255, 30.0 / 255, 36.0 / 255}    // #001E24 — headings, body copy
	colBrand   = rgb{0.0 / 255, 149.0 / 255, 187.0 / 255}  // #0095BB — subtitle/placeholder accent
	colCyan    = rgb{0.0 / 255, 199.0 / 255, 249.0 / 255}  // #00C7F9 — rule lines, footer bar
	colSlate   = rgb{0.290, 0.325, 0.404}                  // body copy on white
	colDivider = rgb{0.886, 0.906, 0.933}
	colWhite   = rgb{1, 1, 1}
)

// sanitize normalizes whitespace/control characters only; the embedded
// Aptos fonts cover the full range of punctuation (curly quotes, en/em
// dash, ellipsis, bullet, ≥/≤, €, …) natively, so — unlike a base-14-only
// PDF writer — there's no need to down-convert those to ASCII stand-ins.
// sanitize does NOT collapse/trim whitespace: ParagraphBold's run splitter
// (see below) deliberately builds run strings with a meaningful single
// leading space at bold/non-bold boundaries, and text() re-sanitizes every
// string right before drawing it — trimming here would silently eat that
// boundary space (and, since the caller's width measurement still counted
// it, shift the next run to visibly overshoot by one space-width instead).
func sanitize(s string) string {
	var b strings.Builder
	for _, r := range s {
		switch r {
		case '\n', '\t':
			b.WriteByte(' ')
		case '\r':
			// drop
		default:
			if r < 32 {
				b.WriteByte(' ')
			} else {
				b.WriteRune(r)
			}
		}
	}
	return b.String()
}

// glyphsFor maps sanitized text to a slice of glyph IDs in the given font,
// substituting the .notdef-adjacent '?' glyph for any rune the font has no
// mapping for (in practice: never, for the Latin/punctuation ranges this
// document uses).
func glyphsFor(f *TTFFont, s string) []uint16 {
	out := make([]uint16, 0, len(s))
	for _, r := range s {
		gid := f.GlyphID(r)
		if gid == 0 && r != ' ' {
			gid = f.GlyphID('?')
		}
		out = append(out, gid)
	}
	return out
}

func textWidth(f *TTFFont, size float64, s string) float64 {
	w := 0.0
	for _, gid := range glyphsFor(f, s) {
		w += f.WidthEm1000(gid)
	}
	return w * size / 1000.0
}

// wrapText greedily wraps sanitized text to fit maxWidth given font/size.
func wrapText(f *TTFFont, size float64, text string, maxWidth float64) []string {
	words := strings.Fields(sanitize(text))
	if len(words) == 0 {
		return nil
	}
	var lines []string
	cur := ""
	pushLine := func() {
		if cur != "" {
			lines = append(lines, cur)
			cur = ""
		}
	}
	for _, w := range words {
		if textWidth(f, size, w) <= maxWidth {
			trial := w
			if cur != "" {
				trial = cur + " " + w
			}
			if cur == "" || textWidth(f, size, trial) <= maxWidth {
				cur = trial
			} else {
				pushLine()
				cur = w
			}
			continue
		}
		// w alone is wider than the column (a long unbroken token, e.g. in a
		// narrow table cell). Never let it overflow past the column edge and
		// never drop characters to make it fit: flush whatever's pending,
		// then hard-break it at rune boundaries into maxWidth-fitting chunks.
		pushLine()
		chunk := ""
		for _, r := range w {
			trial := chunk + string(r)
			if chunk == "" || textWidth(f, size, trial) <= maxWidth {
				chunk = trial
			} else {
				lines = append(lines, chunk)
				chunk = string(r)
			}
		}
		cur = chunk
	}
	pushLine()
	return lines
}

// ---- page/document model ----

const (
	pageW     = 595.0
	pageH     = 842.0
	marginX   = 50.0
	marginTop = 60.0
	marginBot = 55.0
)

type PDF struct {
	pages     []*bytes.Buffer
	cur       *bytes.Buffer
	y         float64
	font      string
	size      float64
	fill      rgb
	pageCount int

	fonts map[string]*TTFFont
	logo  *PDFImage
}

func NewPDF() *PDF {
	p := &PDF{fonts: loadFonts(), logo: loadLogo()}
	p.newPage()
	return p
}

func (p *PDF) newPage() {
	if p.cur != nil {
		p.cur.WriteString("\n")
	}
	buf := &bytes.Buffer{}
	p.pages = append(p.pages, buf)
	p.cur = buf
	p.y = pageH - marginTop
	p.pageCount++
}

// EnsureSpace starts a new page if there isn't h points of room left.
func (p *PDF) EnsureSpace(h float64) {
	if p.y-h < marginBot {
		p.newPage()
	}
}

func (p *PDF) SetFont(font string, size float64) {
	p.font = font
	p.size = size
}

func (p *PDF) SetColor(c rgb) { p.fill = c }

func (p *PDF) lineHeight() float64 { return p.size * 1.35 }

func (p *PDF) font_() *TTFFont { return p.fonts[p.font] }

// text draws a single line at absolute (x,y) using current font/color, into
// whichever buffer is currently active (p.cur, or an explicit chrome
// target set via drawOn).
func (p *PDF) text(x, y float64, s string) {
	f := p.font_()
	glyphs := glyphsFor(f, sanitize(s))
	if len(glyphs) == 0 {
		return
	}
	var hex strings.Builder
	for _, g := range glyphs {
		fmt.Fprintf(&hex, "%04X", g)
	}
	shear := ""
	if italicFonts[p.font] {
		shear = "0.24 " // synthetic oblique: Tm = [1 0 shear 1 x y]
	} else {
		shear = "0.00 "
	}
	fmt.Fprintf(p.cur, "q %.3f %.3f %.3f rg BT /%s %.2f Tf 1 0 %s1 %.2f %.2f Tm <%s> Tj ET Q\n",
		p.fill.r, p.fill.g, p.fill.b, p.font, p.size, shear, x, y, hex.String())
}

// Paragraph writes wrapped text starting at (x, p.y), advancing p.y and
// paginating as needed. Returns total height consumed.
func (p *PDF) Paragraph(x, width float64, s string) float64 {
	lines := wrapText(p.font_(), p.size, s, width)
	lh := p.lineHeight()
	total := 0.0
	for _, ln := range lines {
		p.EnsureSpace(lh)
		p.y -= lh
		p.text(x, p.y, ln)
		total += lh
	}
	return total
}

// Bullets writes a round-bullet-prefixed wrapped list.
func (p *PDF) Bullets(x, width float64, items []string) {
	for _, it := range items {
		lines := wrapText(p.font_(), p.size, it, width-14)
		if len(lines) == 0 {
			continue
		}
		lh := p.lineHeight()
		for i, ln := range lines {
			p.EnsureSpace(lh)
			p.y -= lh
			prefix := "   "
			if i == 0 {
				prefix = "•  "
			}
			p.text(x, p.y, prefix+ln)
		}
	}
}

func (p *PDF) Gap(h float64) {
	p.EnsureSpace(h)
	p.y -= h
}

func (p *PDF) FilledRect(x, y, w, h float64, c rgb) {
	fmt.Fprintf(p.cur, "q %.3f %.3f %.3f rg %.2f %.2f %.2f %.2f re f Q\n", c.r, c.g, c.b, x, y, w, h)
}

func (p *PDF) StrokeRect(x, y, w, h float64, c rgb, lw float64) {
	fmt.Fprintf(p.cur, "q %.3f %.3f %.3f RG %.2f w %.2f %.2f %.2f %.2f re S Q\n", c.r, c.g, c.b, lw, x, y, w, h)
}

func (p *PDF) HLine(x1, x2, y float64, c rgb, lw float64) {
	fmt.Fprintf(p.cur, "q %.3f %.3f %.3f RG %.2f w %.2f %.2f m %.2f %.2f l S Q\n", c.r, c.g, c.b, lw, x1, y, x2, y)
}

// DrawLogo places the embedded Cegeka logo at (x,y) (bottom-left corner)
// sized w x h, preserving the source aspect ratio expectations of the
// caller (callers pass w/h already computed from the logo's native ratio).
func (p *PDF) DrawLogo(x, y, w, h float64) {
	fmt.Fprintf(p.cur, "q %.2f 0 0 %.2f %.2f %.2f cm /Im1 Do Q\n", w, h, x, y)
}

// WriteValue renders val in slate, or an italic placeholder if empty.
func (p *PDF) WriteValue(x, width float64, val string) {
	if strings.TrimSpace(val) == "" {
		p.SetFont(fontPlaceholder, 9.5)
		p.SetColor(colBrand)
		p.Paragraph(x, width, "Not yet confirmed")
		return
	}
	p.SetFont(fontBody, 9.5)
	p.SetColor(colSlate)
	p.Paragraph(x, width, val)
}

// WriteLead renders val as a distinct bold, slightly larger lead line (used
// for the exec-summary vision statement), or an italic placeholder if
// empty, consistent with WriteValue's placeholder convention.
func (p *PDF) WriteLead(x, width float64, val string) {
	if strings.TrimSpace(val) == "" {
		p.SetFont(fontPlaceholder, 9.5)
		p.SetColor(colBrand)
		p.Paragraph(x, width, "Not yet confirmed")
		return
	}
	p.SetFont(fontBodyBold, 11)
	p.SetColor(colNavy)
	p.Paragraph(x, width, val)
}

// styledWord is a word plus whether it should render bold and whether a
// space preceded it in the source text (a "**" bold marker is zero-width
// and not itself a word separator, so e.g. "costs**." must stay glued with
// no space, while "Pilot **+" must keep its space — spaceBefore carries
// that distinction through wrapping and run-grouping).
type styledWord struct {
	text        string
	bold        bool
	spaceBefore bool
}

// parseBoldWords sanitizes s and splits it on "**...**" markers into a flat
// list of words, each tagged with whether it falls inside a bold span and
// whether it was actually preceded by whitespace in the source.
func parseBoldWords(s string) []styledWord {
	runes := []rune(sanitize(s))
	var words []styledWord
	bold := false
	pendingSpace := false
	var cur []rune
	nextSpaceBefore := false
	flush := func() {
		if len(cur) > 0 {
			words = append(words, styledWord{text: string(cur), bold: bold, spaceBefore: nextSpaceBefore})
			cur = nil
		}
	}
	for i := 0; i < len(runes); i++ {
		if i+1 < len(runes) && runes[i] == '*' && runes[i+1] == '*' {
			flush()
			bold = !bold
			i++
			continue
		}
		if runes[i] == ' ' {
			flush()
			pendingSpace = true
			continue
		}
		if len(cur) == 0 {
			nextSpaceBefore = pendingSpace
			pendingSpace = false
		}
		cur = append(cur, runes[i])
	}
	flush()
	return words
}

// ParagraphBold renders text that may contain "**bold**" spans, wrapping and
// paginating like Paragraph. The current font is used for non-bold runs;
// fontBodyBold is used for bold runs.
func (p *PDF) ParagraphBold(x, width float64, s string) float64 {
	words := parseBoldWords(s)
	if len(words) == 0 {
		return 0
	}
	normalFont := p.font
	size := p.size
	lh := p.lineHeight()
	spaceW := textWidth(p.fonts[normalFont], size, " ")

	var lines [][]styledWord
	cur := []styledWord{}
	curWidth := 0.0
	for _, w := range words {
		font := normalFont
		if w.bold {
			font = fontBodyBold
		}
		ww := textWidth(p.fonts[font], size, w.text)
		extra := ww
		if len(cur) > 0 && w.spaceBefore {
			extra += spaceW
		}
		if curWidth+extra > width && len(cur) > 0 {
			lines = append(lines, cur)
			cur = []styledWord{w}
			curWidth = ww
		} else {
			cur = append(cur, w)
			curWidth += extra
		}
	}
	if len(cur) > 0 {
		lines = append(lines, cur)
	}

	total := 0.0
	for _, line := range lines {
		p.EnsureSpace(lh)
		p.y -= lh
		cx := x
		// Draw runs of consecutive same-style words as a single Tj call with
		// real space characters, rather than one Tj per word: word-per-Tj
		// relies purely on positional (Tm) offsets for inter-word gaps, with
		// no literal space glyph in the content stream, which many PDF text
		// extractors collapse (words appear glued together on copy/paste).
		// Each word's own spaceBefore (not just "is this the first run of
		// the line") decides whether a space precedes it, so a run-boundary
		// word that was glued to the previous word in the source (e.g. the
		// "." right after a "**bold**" close) stays glued here too.
		i := 0
		for i < len(line) {
			j := i
			bold := line[i].bold
			var sb strings.Builder
			for j < len(line) && line[j].bold == bold {
				if j > 0 && line[j].spaceBefore {
					sb.WriteString(" ")
				}
				sb.WriteString(line[j].text)
				j++
			}
			runText := sb.String()
			font := normalFont
			if bold {
				font = fontBodyBold
			}
			p.SetFont(font, size)
			p.text(cx, p.y, runText)
			cx += textWidth(p.fonts[font], size, runText)
			i = j
		}
		total += lh
	}
	p.SetFont(normalFont, size)
	return total
}

// WriteValueBold behaves like WriteValue but renders "**bold**" spans in val
// as bold text, for fields (like commercial_headline) whose description
// mandates bold call-outs for pass-through/additive costs.
func (p *PDF) WriteValueBold(x, width float64, val string) {
	if strings.TrimSpace(val) == "" {
		p.SetFont(fontPlaceholder, 9.5)
		p.SetColor(colBrand)
		p.Paragraph(x, width, "Not yet confirmed")
		return
	}
	p.SetFont(fontBody, 9.5)
	p.SetColor(colSlate)
	p.ParagraphBold(x, width, val)
}

func (p *PDF) WriteValueList(x, width float64, vals []string) {
	if len(vals) == 0 {
		p.SetFont(fontPlaceholder, 9.5)
		p.SetColor(colBrand)
		p.Paragraph(x, width, "Not yet confirmed")
		return
	}
	p.SetFont(fontBody, 9.5)
	p.SetColor(colSlate)
	p.Bullets(x, width, vals)
}

// SectionHeading draws the navy-bullet + bold section title used throughout.
func (p *PDF) SectionHeading(title string) {
	p.Gap(14)
	p.EnsureSpace(24)
	p.FilledRect(marginX, p.y-10, 6, 14, colNavy)
	p.SetFont(fontHeading, 15)
	p.SetColor(colNavy)
	p.text(marginX+14, p.y-10, title)
	p.y -= 16
	p.HLine(marginX, pageW-marginX, p.y, colCyan, 1.25)
	p.Gap(8)
}

func (p *PDF) SubHeading(title string) {
	p.Gap(4)
	p.EnsureSpace(16)
	p.SetFont(fontBodyBold, 10.5)
	p.SetColor(colNavy)
	p.Paragraph(marginX, pageW-2*marginX, title)
	p.Gap(2)
}

// Table draws a navy-header table. widths are proportional (sum need not be 1;
// they're normalized against the available content width). An optional
// boldCol argument marks one column index (e.g. the row's lead label) to
// render in fontBodyBold instead of the regular body font.
func (p *PDF) Table(headers []string, widths []float64, rows [][]string, boldCol ...int) {
	bcol := -1
	if len(boldCol) > 0 {
		bcol = boldCol[0]
	}
	contentW := pageW - 2*marginX
	sum := 0.0
	for _, w := range widths {
		sum += w
	}
	colW := make([]float64, len(widths))
	for i, w := range widths {
		colW[i] = contentW * w / sum
	}
	pad := 4.0
	headerLH := 8.5 * 1.35

	// Headers wrap exactly like body cells (never draw a header as one
	// unwrapped Tj) so a long column title can't bleed into its neighbor
	// the same way an unwrapped body cell used to.
	headerLines := make([][]string, len(headers))
	headerMaxLines := 1
	for i, h := range headers {
		lines := wrapText(p.fonts[fontBodyBold], 8.5, strings.ToUpper(h), colW[i]-2*pad)
		if len(lines) == 0 {
			lines = []string{""}
		}
		headerLines[i] = lines
		if len(lines) > headerMaxLines {
			headerMaxLines = len(lines)
		}
	}
	headerH := headerLH*float64(headerMaxLines) + 2*pad

	drawHeader := func() {
		p.EnsureSpace(headerH + 4)
		y0 := p.y
		p.FilledRect(marginX, y0-headerH, contentW, headerH, colNavy)
		x := marginX
		p.SetFont(fontBodyBold, 8.5)
		p.SetColor(colWhite)
		for i, lines := range headerLines {
			ly := y0 - pad - 7
			for _, ln := range lines {
				p.text(x+pad, ly, ln)
				ly -= headerLH
			}
			x += colW[i]
		}
		p.y = y0 - headerH
	}

	drawHeader()

	for _, row := range rows {
		// compute row height from wrapped cell content
		cellLines := make([][]string, len(row))
		maxLines := 1
		for i, cell := range row {
			w := colW[i] - 2*pad
			cellFont := p.fonts[fontBody]
			if i == bcol {
				cellFont = p.fonts[fontBodyBold]
			}
			lines := wrapText(cellFont, 8.5, cell, w)
			if len(lines) == 0 {
				lines = []string{""}
			}
			cellLines[i] = lines
			if len(lines) > maxLines {
				maxLines = len(lines)
			}
		}
		lh := 8.5 * 1.35
		rowH := lh*float64(maxLines) + 2*pad

		if p.y-rowH < marginBot {
			p.newPage()
			drawHeader()
		}

		y0 := p.y
		p.StrokeRect(marginX, y0-rowH, contentW, rowH, colDivider, 0.5)
		x := marginX
		p.SetColor(colSlate)
		for i, lines := range cellLines {
			cellFont := fontBody
			if i == bcol {
				cellFont = fontBodyBold
			}
			p.SetFont(cellFont, 8.5)
			ly := y0 - pad - 7
			for _, ln := range lines {
				p.text(x+pad, ly, ln)
				ly -= lh
			}
			x += colW[i]
		}
		// column separators
		x = marginX
		for i := 0; i < len(colW)-1; i++ {
			x += colW[i]
			p.HLine(x, x, y0, colDivider, 0.5)
			fmt.Fprintf(p.cur, "q %.3f %.3f %.3f RG 0.5 w %.2f %.2f m %.2f %.2f l S Q\n",
				colDivider.r, colDivider.g, colDivider.b, x, y0, x, y0-rowH)
		}
		p.y = y0 - rowH
	}
	p.Gap(6)
}

// ---- running header/footer chrome ----

// onPage temporarily redirects drawing calls to buf instead of p.cur so
// ApplyChrome can paint fixed-position header/footer elements onto an
// already-built page without disturbing p.y-based content flow.
func (p *PDF) onPage(buf *bytes.Buffer, fn func()) {
	saved := p.cur
	p.cur = buf
	fn()
	p.cur = saved
}

// logoSize returns a w x h in points for the embedded logo at the given
// height, preserving its native aspect ratio.
func (p *PDF) logoSize(h float64) (w, height float64) {
	ratio := float64(p.logo.W) / float64(p.logo.H)
	return h * ratio, h
}

// ApplyChrome paints the cover branding lockup on page 1 and a repeating
// header (small logo + document title + cyan rule) and footer (cyan bar +
// title/version + page number) on every subsequent page, mirroring the
// layout of the reference Cegeka SOW docx (logo top-right on continuation
// pages, title bar bottom, wordmark top-left on the cover).
func (p *PDF) ApplyChrome(footerTitle string) {
	total := len(p.pages)
	for i, buf := range p.pages {
		if i == 0 {
			continue // cover branding is drawn inline by BuildSOWPDF
		}
		pageNum := i + 1
		p.onPage(buf, func() {
			// small logo, top-right
			lw, lh := p.logoSize(20)
			lx := pageW - marginX - lw
			ly := pageH - 40
			p.DrawLogo(lx, ly, lw, lh)

			// document title, top-left, vertically centered against the logo
			p.SetFont(fontBody, 8)
			p.SetColor(colNavy)
			p.text(marginX, ly+lh/2-3, footerTitle)

			p.HLine(marginX, pageW-marginX, pageH-48, colCyan, 1.25)

			// footer bar
			barH := 16.0
			barY := 26.0
			p.FilledRect(marginX, barY, pageW-2*marginX, barH, colCyan)
			p.SetFont(fontBodyBold, 7.5)
			p.SetColor(colNavy)
			p.text(marginX+8, barY+5, footerTitle)
			pageLabel := fmt.Sprintf("Page %d of %d", pageNum, total)
			pw := textWidth(p.fonts[fontBodyBold], 7.5, pageLabel)
			p.text(pageW-marginX-8-pw, barY+5, pageLabel)
		})
	}
}

// ---- low-level PDF file assembly ----

func (p *PDF) Bytes() []byte {
	var out bytes.Buffer
	offsets := map[int]int{}
	objNum := 0
	newObjNum := func() int { objNum++; return objNum }

	write := func(num int, body string) {
		offsets[num] = out.Len()
		out.WriteString(fmt.Sprintf("%d 0 obj\n%s\nendobj\n", num, body))
	}
	writeBytes := func(num int, head string, stream []byte, tail string) {
		offsets[num] = out.Len()
		out.WriteString(fmt.Sprintf("%d 0 obj\n%s\nstream\n", num, head))
		out.Write(stream)
		out.WriteString("\nendstream\n" + tail + "endobj\n")
	}

	out.WriteString("%PDF-1.4\n%\xE2\xE3\xCF\xD3\n")

	catalogNum := newObjNum()
	pagesNum := newObjNum()

	// ---- embedded fonts: one Type0/CIDFontType2 stack per font key ----
	type fontObjSet struct {
		type0, cidFont, descriptor, fontFile, toUnicode int
	}
	fontObjs := map[string]fontObjSet{}
	for _, key := range fontOrder {
		fontObjs[key] = fontObjSet{
			type0:      newObjNum(),
			cidFont:    newObjNum(),
			descriptor: newObjNum(),
			fontFile:   newObjNum(),
			toUnicode:  newObjNum(),
		}
	}

	// ---- logo image (+ optional soft mask) ----
	logoImgNum := newObjNum()
	logoSMaskNum := 0
	if p.logo.Alpha != nil {
		logoSMaskNum = newObjNum()
	}

	resourceDict := "<< /Font << "
	for _, key := range fontOrder {
		resourceDict += fmt.Sprintf("/%s %d 0 R ", key, fontObjs[key].type0)
	}
	resourceDict += fmt.Sprintf(">> /XObject << /Im1 %d 0 R >> >>", logoImgNum)

	pageObjNums := make([]int, len(p.pages))
	contentObjNums := make([]int, len(p.pages))
	for i := range p.pages {
		contentObjNums[i] = newObjNum()
		pageObjNums[i] = newObjNum()
	}

	// ---- write font objects ----
	for _, key := range fontOrder {
		f := p.fonts[key]
		obj := fontObjs[key]
		baseName := "Aptos-" + key

		compressed := deflate(f.Raw)
		writeBytes(obj.fontFile,
			fmt.Sprintf("<< /Length %d /Length1 %d /Filter /FlateDecode >>", len(compressed), len(f.Raw)),
			compressed, "")

		scale := 1000.0 / float64(f.UnitsPerEm)
		ascent := int(float64(f.Ascender) * scale)
		descent := int(float64(f.Descender) * scale)
		write(obj.descriptor, fmt.Sprintf(
			"<< /Type /FontDescriptor /FontName /%s /Flags 32 /FontBBox [-200 %d 1200 %d] "+
				"/ItalicAngle 0 /Ascent %d /Descent %d /CapHeight %d /StemV 80 /FontFile2 %d 0 R >>",
			baseName, descent, ascent, ascent, descent, ascent, obj.fontFile))

		// A /W array entry of the form "cFirst [w0 w1 ... wN-1]" assigns
		// widths to consecutive CIDs starting at cFirst — not alternating
		// (CID, width) pairs, which most PDF renderers misparse as ad hoc
		// (cFirst, cLast, w) range triples and desync every width after it.
		var wArr strings.Builder
		wArr.WriteString("[0 [")
		for gid := 0; gid < f.NumGlyphs; gid++ {
			fmt.Fprintf(&wArr, "%d ", int(f.WidthEm1000(uint16(gid))))
		}
		wArr.WriteString("]]")

		write(obj.cidFont, fmt.Sprintf(
			"<< /Type /Font /Subtype /CIDFontType2 /BaseFont /%s "+
				"/CIDSystemInfo << /Registry (Adobe) /Ordering (Identity) /Supplement 0 >> "+
				"/FontDescriptor %d 0 R /DW 500 /W %s /CIDToGIDMap /Identity >>",
			baseName, obj.descriptor, wArr.String()))

		toUni := buildToUnicodeCMap(f)
		writeBytes(obj.toUnicode, fmt.Sprintf("<< /Length %d >>", len(toUni)), toUni, "")

		write(obj.type0, fmt.Sprintf(
			"<< /Type /Font /Subtype /Type0 /BaseFont /%s /Encoding /Identity-H "+
				"/DescendantFonts [%d 0 R] /ToUnicode %d 0 R >>",
			baseName, obj.cidFont, obj.toUnicode))
	}

	// ---- write logo image object(s) ----
	if logoSMaskNum != 0 {
		compressedAlpha := deflate(p.logo.Alpha)
		writeBytes(logoSMaskNum, fmt.Sprintf(
			"<< /Type /XObject /Subtype /Image /Width %d /Height %d /ColorSpace /DeviceGray "+
				"/BitsPerComponent 8 /Filter /FlateDecode /Length %d >>",
			p.logo.W, p.logo.H, len(compressedAlpha)), compressedAlpha, "")
	}
	compressedRGB := deflate(p.logo.RGB)
	smaskRef := ""
	if logoSMaskNum != 0 {
		smaskRef = fmt.Sprintf(" /SMask %d 0 R", logoSMaskNum)
	}
	writeBytes(logoImgNum, fmt.Sprintf(
		"<< /Type /XObject /Subtype /Image /Width %d /Height %d /ColorSpace /DeviceRGB "+
			"/BitsPerComponent 8 /Filter /FlateDecode%s /Length %d >>",
		p.logo.W, p.logo.H, smaskRef, len(compressedRGB)), compressedRGB, "")

	// write content streams + page objects
	kids := []string{}
	for i, buf := range p.pages {
		content := buf.Bytes()
		body := fmt.Sprintf("<< /Length %d >>\nstream\n%s\nendstream", len(content), content)
		write(contentObjNums[i], body)

		pageBody := fmt.Sprintf("<< /Type /Page /Parent %d 0 R /MediaBox [0 0 %.0f %.0f] /Resources %s /Contents %d 0 R >>",
			pagesNum, pageW, pageH, resourceDict, contentObjNums[i])
		write(pageObjNums[i], pageBody)
		kids = append(kids, fmt.Sprintf("%d 0 R", pageObjNums[i]))
	}

	pagesBody := fmt.Sprintf("<< /Type /Pages /Kids [%s] /Count %d >>", strings.Join(kids, " "), len(p.pages))
	write(pagesNum, pagesBody)

	catalogBody := fmt.Sprintf("<< /Type /Catalog /Pages %d 0 R >>", pagesNum)
	write(catalogNum, catalogBody)

	xrefStart := out.Len()
	out.WriteString(fmt.Sprintf("xref\n0 %d\n", objNum+1))
	out.WriteString("0000000000 65535 f \n")
	for i := 1; i <= objNum; i++ {
		out.WriteString(fmt.Sprintf("%010d 00000 n \n", offsets[i]))
	}
	out.WriteString(fmt.Sprintf("trailer\n<< /Size %d /Root %d 0 R >>\nstartxref\n%d\n%%%%EOF\n", objNum+1, catalogNum, xrefStart))

	return out.Bytes()
}

// buildToUnicodeCMap emits a minimal Identity-ish ToUnicode CMap mapping
// each glyph ID actually reachable via the font's cmap back to its source
// codepoint, so copy/paste and text search work on the generated PDF.
func buildToUnicodeCMap(f *TTFFont) []byte {
	var b strings.Builder
	b.WriteString("/CIDInit /ProcSet findresource begin\n12 dict begin\nbegincmap\n")
	b.WriteString("/CIDSystemInfo << /Registry (Adobe) /Ordering (UCS) /Supplement 0 >> def\n")
	b.WriteString("/CMapName /Adobe-Identity-UCS def\n/CMapType 2 def\n")
	b.WriteString("1 begincodespacerange\n<0000> <FFFF>\nendcodespacerange\n")

	type pair struct {
		gid uint16
		r   rune
	}
	var pairs []pair
	for r, gid := range f.cmap {
		pairs = append(pairs, pair{gid, r})
	}
	// stable, deterministic output
	for i := 1; i < len(pairs); i++ {
		for j := i; j > 0 && pairs[j-1].gid > pairs[j].gid; j-- {
			pairs[j-1], pairs[j] = pairs[j], pairs[j-1]
		}
	}
	const chunk = 100
	for i := 0; i < len(pairs); i += chunk {
		end := i + chunk
		if end > len(pairs) {
			end = len(pairs)
		}
		fmt.Fprintf(&b, "%d beginbfchar\n", end-i)
		for _, pr := range pairs[i:end] {
			fmt.Fprintf(&b, "<%04X> <%04X>\n", pr.gid, pr.r)
		}
		b.WriteString("endbfchar\n")
	}
	b.WriteString("endcmap\nCMapName currentdict /CMap defineresource pop\nend\nend\n")
	return []byte(b.String())
}
