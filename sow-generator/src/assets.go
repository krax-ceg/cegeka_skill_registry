package main

import (
	"fmt"

	_ "embed"
)

// Cegeka graphical profile assets, baked into the sowgen binary so the
// generator has no runtime file dependencies. Aptos/Aptos Display are the
// Microsoft 365 default typeface pair; the .ttf files here are the same
// ones Windows/Office resolve from the local Cloud Fonts cache when you
// open a document that uses them. Embedding a copy inside a generated PDF
// (as any "Save/Print to PDF" flow does) is the intended, licensed use.
var (
	//go:embed assets/Aptos-Regular.ttf
	aptosRegularTTF []byte
	//go:embed assets/Aptos-Bold.ttf
	aptosBoldTTF []byte
	//go:embed assets/AptosDisplay-Regular.ttf
	aptosDisplayTTF []byte
	//go:embed assets/cegeka_logo.png
	cegekaLogoPNG []byte
)

// fontKey identifies one of the four fonts used throughout the generated
// PDF. F3 reuses the Aptos-Regular outlines with a synthetic slant applied
// at draw time (see PDF.text) to stand in for an italic placeholder style,
// since no italic Aptos instance ships in the Cloud Fonts cache.
const (
	fontBody     = "F1" // Aptos Regular — body copy
	fontBodyBold = "F2" // Aptos Bold — emphasis, table headers, sub-headings
	fontPlaceholder = "F3" // Aptos Regular + synthetic italic — unresolved-field placeholders
	fontHeading  = "F4" // Aptos Display — section headings, cover title
)

var fontOrder = []string{fontBody, fontBodyBold, fontPlaceholder, fontHeading}

// italicFonts marks which font keys get a synthetic oblique shear applied
// when drawing text (see PDF.text).
var italicFonts = map[string]bool{fontPlaceholder: true}

func loadFonts() map[string]*TTFFont {
	reg, err := ParseTTF(aptosRegularTTF)
	if err != nil {
		panic(fmt.Sprintf("assets: parse Aptos-Regular.ttf: %v", err))
	}
	bold, err := ParseTTF(aptosBoldTTF)
	if err != nil {
		panic(fmt.Sprintf("assets: parse Aptos-Bold.ttf: %v", err))
	}
	display, err := ParseTTF(aptosDisplayTTF)
	if err != nil {
		panic(fmt.Sprintf("assets: parse AptosDisplay-Regular.ttf: %v", err))
	}
	return map[string]*TTFFont{
		fontBody:        reg,
		fontBodyBold:    bold,
		fontPlaceholder: reg,
		fontHeading:     display,
	}
}

func loadLogo() *PDFImage {
	img, err := DecodePNGImage(cegekaLogoPNG)
	if err != nil {
		panic(fmt.Sprintf("assets: decode cegeka_logo.png: %v", err))
	}
	return img
}
