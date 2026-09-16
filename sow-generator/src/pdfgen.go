package main

import (
	"bytes"
	"fmt"
	"strings"
)

// ---- palette ----

type rgb struct{ r, g, b float64 }

var (
	colNavy    = rgb{0.0, 0.169, 0.286}   // #002B49
	colGold    = rgb{0.722, 0.525, 0.043} // #B8860B
	colSlate   = rgb{0.290, 0.325, 0.404} // #4A5568
	colDivider = rgb{0.886, 0.906, 0.933} // #E2E8F0
	colWhite   = rgb{1, 1, 1}
	colBlack   = rgb{0, 0, 0}
)

// ---- Helvetica AFM widths (per 1000 em), ASCII 32-126 ----
var helveticaWidths = [95]int{
	278, 278, 355, 556, 556, 889, 667, 191, 333, 333, 389, 584, 278, 333, 278, 278,
	556, 556, 556, 556, 556, 556, 556, 556, 556, 556, 278, 278, 584, 584, 584, 556,
	1015, 667, 667, 722, 722, 667, 611, 778, 722, 278, 500, 667, 556, 833, 722, 778,
	667, 778, 722, 667, 611, 722, 667, 944, 667, 667, 611, 278, 278, 278, 469, 556,
	333, 556, 556, 500, 556, 556, 278, 556, 556, 222, 222, 500, 222, 833, 556, 556,
	556, 556, 333, 500, 278, 556, 500, 722, 500, 500, 500, 334, 260, 334, 584,
}

func charWidth(font string, c byte) float64 {
	if font == "F5" { // Courier is monospace
		return 600
	}
	if c < 32 || c > 126 {
		return 556
	}
	return float64(helveticaWidths[c-32])
}

func textWidth(font string, size float64, s string) float64 {
	w := 0.0
	for i := 0; i < len(s); i++ {
		w += charWidth(font, s[i])
	}
	return w * size / 1000.0
}

// sanitize maps runes outside WinAnsi's safe ASCII range to reasonable
// stand-ins so the base-14 fonts (which we use unembedded) render
// correctly on every PDF viewer without embedding a WinAnsi diff table.
func sanitize(s string) string {
	var b strings.Builder
	for _, r := range s {
		switch r {
		case '‘', '’':
			b.WriteByte('\'')
		case '“', '”':
			b.WriteByte('"')
		case '–', '—':
			b.WriteString("-")
		case '…':
			b.WriteString("...")
		case '•':
			b.WriteString("-")
		case '≥':
			b.WriteString(">=")
		case '≤':
			b.WriteString("<=")
		case '€':
			b.WriteString("EUR")
		default:
			if r >= 32 && r <= 126 {
				b.WriteRune(r)
			} else if r == '\n' || r == '\t' {
				b.WriteByte(' ')
			} else {
				b.WriteByte('?')
			}
		}
	}
	return b.String()
}

func escapePDFString(s string) string {
	s = strings.ReplaceAll(s, `\`, `\\`)
	s = strings.ReplaceAll(s, `(`, `\(`)
	s = strings.ReplaceAll(s, `)`, `\)`)
	return s
}

// wrapText greedily wraps sanitized text to fit maxWidth given font/size.
func wrapText(font string, size float64, text string, maxWidth float64) []string {
	text = sanitize(text)
	if strings.TrimSpace(text) == "" {
		return nil
	}
	words := strings.Fields(text)
	var lines []string
	cur := ""
	for _, w := range words {
		trial := w
		if cur != "" {
			trial = cur + " " + w
		}
		if textWidth(font, size, trial) <= maxWidth || cur == "" {
			cur = trial
		} else {
			lines = append(lines, cur)
			cur = w
		}
	}
	if cur != "" {
		lines = append(lines, cur)
	}
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
}

func NewPDF() *PDF {
	p := &PDF{}
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

// text draws a single line at absolute (x,y) using current font/color.
func (p *PDF) text(x, y float64, s string) {
	s = escapePDFString(sanitize(s))
	fmt.Fprintf(p.cur, "q %.3f %.3f %.3f rg BT /%s %.2f Tf 1 0 0 1 %.2f %.2f Tm (%s) Tj ET Q\n",
		p.fill.r, p.fill.g, p.fill.b, p.font, p.size, x, y, s)
}

// Paragraph writes wrapped text starting at (x, p.y), advancing p.y and
// paginating as needed. Returns total height consumed.
func (p *PDF) Paragraph(x, width float64, s string) float64 {
	lines := wrapText(p.font, p.size, s, width)
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

// Bullets writes a "- " prefixed wrapped list.
func (p *PDF) Bullets(x, width float64, items []string) {
	for _, it := range items {
		lines := wrapText(p.font, p.size, it, width-14)
		if len(lines) == 0 {
			continue
		}
		lh := p.lineHeight()
		for i, ln := range lines {
			p.EnsureSpace(lh)
			p.y -= lh
			prefix := "  "
			if i == 0 {
				prefix = "- "
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

// WriteValue renders val in slate, or an italic gold placeholder if empty.
func (p *PDF) WriteValue(x, width float64, val string) {
	if strings.TrimSpace(val) == "" {
		p.SetFont("F3", 9.5)
		p.SetColor(colGold)
		p.Paragraph(x, width, "[Not yet confirmed]")
		return
	}
	p.SetFont("F1", 9.5)
	p.SetColor(colSlate)
	p.Paragraph(x, width, val)
}

// WriteLead renders val as a distinct bold, slightly larger lead line (used
// for the exec-summary vision statement), or an italic gold placeholder if
// empty, consistent with WriteValue's placeholder convention.
func (p *PDF) WriteLead(x, width float64, val string) {
	if strings.TrimSpace(val) == "" {
		p.SetFont("F3", 9.5)
		p.SetColor(colGold)
		p.Paragraph(x, width, "[Not yet confirmed]")
		return
	}
	p.SetFont("F2", 11)
	p.SetColor(colNavy)
	p.Paragraph(x, width, val)
}

// styledWord is a word plus whether it should render bold.
type styledWord struct {
	text string
	bold bool
}

// parseBoldWords sanitizes s and splits it on "**...**" markers into a flat
// list of words, each tagged with whether it falls inside a bold span.
func parseBoldWords(s string) []styledWord {
	s = sanitize(s)
	var words []styledWord
	parts := strings.Split(s, "**")
	for i, part := range parts {
		bold := i%2 == 1
		for _, w := range strings.Fields(part) {
			words = append(words, styledWord{text: w, bold: bold})
		}
	}
	return words
}

// ParagraphBold renders text that may contain "**bold**" spans, wrapping and
// paginating like Paragraph. The current font is used for non-bold runs; F2
// (Helvetica-Bold) is used for bold runs. Text has already been sanitized by
// the time it reaches drawing (via parseBoldWords), so no double-escaping.
func (p *PDF) ParagraphBold(x, width float64, s string) float64 {
	words := parseBoldWords(s)
	if len(words) == 0 {
		return 0
	}
	normalFont := p.font
	size := p.size
	lh := p.lineHeight()
	spaceW := textWidth(normalFont, size, " ")

	var lines [][]styledWord
	cur := []styledWord{}
	curWidth := 0.0
	for _, w := range words {
		font := normalFont
		if w.bold {
			font = "F2"
		}
		ww := textWidth(font, size, w.text)
		extra := ww
		if len(cur) > 0 {
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
		i := 0
		first := true
		for i < len(line) {
			j := i
			bold := line[i].bold
			var parts []string
			for j < len(line) && line[j].bold == bold {
				parts = append(parts, line[j].text)
				j++
			}
			runText := strings.Join(parts, " ")
			if !first {
				runText = " " + runText
			}
			font := normalFont
			if bold {
				font = "F2"
			}
			p.SetFont(font, size)
			p.text(cx, p.y, runText)
			cx += textWidth(font, size, runText)
			first = false
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
		p.SetFont("F3", 9.5)
		p.SetColor(colGold)
		p.Paragraph(x, width, "[Not yet confirmed]")
		return
	}
	p.SetFont("F1", 9.5)
	p.SetColor(colSlate)
	p.ParagraphBold(x, width, val)
}

func (p *PDF) WriteValueList(x, width float64, vals []string) {
	if len(vals) == 0 {
		p.SetFont("F3", 9.5)
		p.SetColor(colGold)
		p.Paragraph(x, width, "[Not yet confirmed]")
		return
	}
	p.SetFont("F1", 9.5)
	p.SetColor(colSlate)
	p.Bullets(x, width, vals)
}

// SectionHeading draws the navy-bullet + bold section title used throughout.
func (p *PDF) SectionHeading(title string) {
	p.Gap(14)
	p.EnsureSpace(24)
	p.FilledRect(marginX, p.y-10, 6, 14, colNavy)
	p.SetFont("F4", 15)
	p.SetColor(colNavy)
	p.text(marginX+14, p.y-10, title)
	p.y -= 16
	p.HLine(marginX, pageW-marginX, p.y, colDivider, 0.75)
	p.Gap(8)
}

func (p *PDF) SubHeading(title string) {
	p.Gap(4)
	p.EnsureSpace(16)
	p.SetFont("F2", 10.5)
	p.SetColor(colNavy)
	p.Paragraph(marginX, pageW-2*marginX, title)
	p.Gap(2)
}

// Table draws a navy-header table. widths are proportional (sum need not be 1;
// they're normalized against the available content width). An optional
// boldCol argument marks one column index (e.g. the row's lead label) to
// render in F2 (Helvetica-Bold) instead of the regular body font.
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
	headerH := 20.0

	drawHeader := func() {
		p.EnsureSpace(headerH + 4)
		y0 := p.y
		p.FilledRect(marginX, y0-headerH, contentW, headerH, colNavy)
		x := marginX
		p.SetFont("F2", 8.5)
		p.SetColor(colWhite)
		for i, h := range headers {
			p.text(x+pad, y0-headerH+6, strings.ToUpper(h))
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
			cellFont := "F1"
			if i == bcol {
				cellFont = "F2"
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
			cellFont := "F1"
			if i == bcol {
				cellFont = "F2"
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

	out.WriteString("%PDF-1.4\n%\xE2\xE3\xCF\xD3\n")

	catalogNum := newObjNum()
	pagesNum := newObjNum()

	fontNames := []string{"Helvetica", "Helvetica-Bold", "Helvetica-Oblique", "Times-Bold", "Courier"}
	fontObjNums := map[string]int{}
	fontKeys := []string{"F1", "F2", "F3", "F4", "F5"}
	for i := range fontNames {
		n := newObjNum()
		fontObjNums[fontKeys[i]] = n
	}

	resourceDict := "<< /Font << "
	for _, k := range fontKeys {
		resourceDict += fmt.Sprintf("/%s %d 0 R ", k, fontObjNums[k])
	}
	resourceDict += ">> >>"

	pageObjNums := make([]int, len(p.pages))
	contentObjNums := make([]int, len(p.pages))
	for i := range p.pages {
		contentObjNums[i] = newObjNum()
		pageObjNums[i] = newObjNum()
	}

	// write font objects
	for i, fn := range fontNames {
		n := fontObjNums[fontKeys[i]]
		body := fmt.Sprintf("<< /Type /Font /Subtype /Type1 /BaseFont /%s /Encoding /WinAnsiEncoding >>", fn)
		write(n, body)
	}

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
