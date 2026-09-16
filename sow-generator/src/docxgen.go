package main

import (
	"archive/zip"
	"bytes"
	"encoding/xml"
	"fmt"
	"strings"
)

func xmlEscape(s string) string {
	var b bytes.Buffer
	_ = xml.EscapeText(&b, []byte(s))
	return b.String()
}

const contentTypesXML = `<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
<Default Extension="xml" ContentType="application/xml"/>
<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
</Types>`

const rootRelsXML = `<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>`

const docRelsXML = `<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
</Relationships>`

const stylesXML = `<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
<w:style w:type="paragraph" w:default="1" w:styleId="Normal">
  <w:name w:val="Normal"/>
  <w:rPr><w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/><w:sz w:val="21"/></w:rPr>
</w:style>
<w:style w:type="paragraph" w:styleId="Title">
  <w:name w:val="Title"/>
  <w:basedOn w:val="Normal"/>
  <w:rPr><w:b/><w:sz w:val="36"/><w:color w:val="002B49"/></w:rPr>
</w:style>
<w:style w:type="paragraph" w:styleId="Heading1">
  <w:name w:val="Heading 1"/>
  <w:basedOn w:val="Normal"/>
  <w:rPr><w:b/><w:sz w:val="26"/><w:color w:val="002B49"/></w:rPr>
</w:style>
</w:styles>`

func wPara(styleID, text string, bold bool) string {
	rpr := ""
	if bold {
		rpr = "<w:rPr><w:b/></w:rPr>"
	}
	pPr := ""
	if styleID != "" {
		pPr = fmt.Sprintf("<w:pPr><w:pStyle w:val=\"%s\"/></w:pPr>", styleID)
	}
	return fmt.Sprintf("<w:p>%s<w:r>%s<w:t xml:space=\"preserve\">%s</w:t></w:r></w:p>", pPr, rpr, xmlEscape(text))
}

func wCell(text string, header bool, widthTwips int) string {
	shading := ""
	rpr := ""
	if header {
		shading = `<w:shd w:val="clear" w:color="auto" w:fill="002B49"/>`
		rpr = `<w:rPr><w:b/><w:color w:val="FFFFFF"/></w:rPr>`
	}
	return fmt.Sprintf(
		`<w:tc><w:tcPr><w:tcW w:w="%d" w:type="dxa"/>%s</w:tcPr><w:p><w:r>%s<w:t xml:space="preserve">%s</w:t></w:r></w:p></w:tc>`,
		widthTwips, shading, rpr, xmlEscape(text))
}

func wRow(cells []string, header bool, widths []int) string {
	var b strings.Builder
	b.WriteString("<w:tr>")
	for i, c := range cells {
		w := 2000
		if i < len(widths) {
			w = widths[i]
		}
		b.WriteString(wCell(c, header, w))
	}
	b.WriteString("</w:tr>")
	return b.String()
}

// BuildOpenItemsDocx renders the Open Items Register as a minimal, valid
// OOXML .docx built with stdlib archive/zip + encoding/xml only.
func BuildOpenItemsDocx(d *SOWData) []byte {
	var body strings.Builder
	body.WriteString(wPara("Title", "Open Items Register", false))
	body.WriteString(wPara("Normal", fmt.Sprintf("SOW Reference: %s   |   Client: %s", firstNonEmpty(d.Meta.Ref, "TBD"), firstNonEmpty(d.DocControl.ClientLegalName, "TBD")), false))
	body.WriteString(wPara("Normal", "Items below must be resolved before this SOW is finalized and signed. They are intentionally excluded from the SOW PDF itself.", false))
	body.WriteString(`<w:p/>`)

	widths := []int{1400, 2600, 2600, 2200, 1200}
	tbl := `<w:tbl><w:tblPr><w:tblW w:w="10000" w:type="dxa"/><w:tblBorders>` +
		`<w:top w:val="single" w:sz="4" w:color="E2E8F0"/><w:left w:val="single" w:sz="4" w:color="E2E8F0"/>` +
		`<w:bottom w:val="single" w:sz="4" w:color="E2E8F0"/><w:right w:val="single" w:sz="4" w:color="E2E8F0"/>` +
		`<w:insideH w:val="single" w:sz="4" w:color="E2E8F0"/><w:insideV w:val="single" w:sz="4" w:color="E2E8F0"/>` +
		`</w:tblBorders></w:tblPr><w:tblGrid>`
	for _, w := range widths {
		tbl += fmt.Sprintf(`<w:gridCol w:w="%d"/>`, w)
	}
	tbl += "</w:tblGrid>"
	tbl += wRow([]string{"Section", "Question", "Why it matters", "Risk if unresolved", "Owner"}, true, widths)
	for _, it := range d.OpenItems {
		tbl += wRow([]string{it.Section, it.Question, it.WhyItMatters, it.RiskIfUnresolved, it.SuggestedOwner}, false, widths)
	}
	tbl += "</w:tbl>"
	body.WriteString(tbl)
	body.WriteString(`<w:p/>`)

	documentXML := fmt.Sprintf(`<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
<w:body>%s<w:sectPr><w:pgSz w:w="16838" w:h="11906" w:orient="landscape"/><w:pgMar w:top="1000" w:right="1000" w:bottom="1000" w:left="1000"/></w:sectPr></w:body>
</w:document>`, body.String())

	var buf bytes.Buffer
	zw := zip.NewWriter(&buf)
	files := map[string]string{
		"[Content_Types].xml":          contentTypesXML,
		"_rels/.rels":                  rootRelsXML,
		"word/document.xml":            documentXML,
		"word/_rels/document.xml.rels": docRelsXML,
		"word/styles.xml":              stylesXML,
	}
	for _, name := range []string{"[Content_Types].xml", "_rels/.rels", "word/document.xml", "word/_rels/document.xml.rels", "word/styles.xml"} {
		w, err := zw.Create(name)
		if err != nil {
			panic(err)
		}
		if _, err := w.Write([]byte(files[name])); err != nil {
			panic(err)
		}
	}
	if err := zw.Close(); err != nil {
		panic(err)
	}
	return buf.Bytes()
}
