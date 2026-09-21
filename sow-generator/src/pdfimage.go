package main

import (
	"bytes"
	"compress/zlib"
	"fmt"
	"image"
	"image/color"
	_ "image/png"
)

// PDFImage holds a decoded raster image ready to be embedded as a PDF Image
// XObject: raw (uncompressed) RGB samples for the base image, deflated at
// write time, plus an optional deflated alpha channel for a soft mask so
// logos with transparency composite correctly over the page background.
type PDFImage struct {
	W, H  int
	RGB   []byte // W*H*3, row-major, top-to-bottom
	Alpha []byte // W*H, or nil if the source has no transparency
}

// DecodePNGImage decodes PNG bytes into a PDFImage. Any Go stdlib-supported
// PNG color model works; the alpha channel (if present and not fully opaque)
// is split out into Alpha for use as an SMask.
func DecodePNGImage(data []byte) (*PDFImage, error) {
	img, _, err := image.Decode(bytes.NewReader(data))
	if err != nil {
		return nil, fmt.Errorf("pdfimage: decode png: %w", err)
	}
	b := img.Bounds()
	w, h := b.Dx(), b.Dy()
	rgb := make([]byte, w*h*3)
	alpha := make([]byte, w*h)
	hasAlpha := false
	i := 0
	for y := b.Min.Y; y < b.Max.Y; y++ {
		for x := b.Min.X; x < b.Max.X; x++ {
			r, g, bl, a := img.At(x, y).RGBA()
			// img.At returns alpha-premultiplied 16-bit components; un-premultiply
			// against alpha so the RGB we embed matches what a straight-alpha
			// PDF SMask composite expects.
			nrgba := color.NRGBAModel.Convert(color.RGBA64{R: uint16(r), G: uint16(g), B: uint16(bl), A: uint16(a)}).(color.NRGBA)
			rgb[i*3+0] = nrgba.R
			rgb[i*3+1] = nrgba.G
			rgb[i*3+2] = nrgba.B
			alpha[i] = nrgba.A
			if nrgba.A != 255 {
				hasAlpha = true
			}
			i++
		}
	}
	pi := &PDFImage{W: w, H: h, RGB: rgb}
	if hasAlpha {
		pi.Alpha = alpha
	}
	return pi, nil
}

func deflate(data []byte) []byte {
	var buf bytes.Buffer
	w := zlib.NewWriter(&buf)
	w.Write(data)
	w.Close()
	return buf.Bytes()
}
