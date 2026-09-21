package main

import (
	"encoding/binary"
	"fmt"
)

// TTFFont holds just enough of a parsed TrueType font (sfnt) to drive PDF
// CIDFontType2 embedding: the raw bytes (embedded as-is, unsubsetted, as
// FontFile2), a unicode->glyph-id map from the cmap table, and per-glyph
// advance widths from hmtx, scaled to a 1000-unit em to match the rest of
// this package's width arithmetic.
type TTFFont struct {
	Raw        []byte
	UnitsPerEm int
	NumGlyphs  int
	Ascender   int // hhea ascender, raw font units
	Descender  int // hhea descender, raw font units (negative)
	widths     []int // per glyph ID, in raw font units
	cmap       map[rune]uint16
}

type sfntTable struct {
	tag            string
	offset, length uint32
}

// ParseTTF parses the subset of sfnt tables (head, hhea, maxp, hmtx, cmap)
// needed to embed the font as a PDF CIDFontType2 and measure text.
func ParseTTF(data []byte) (*TTFFont, error) {
	if len(data) < 12 {
		return nil, fmt.Errorf("ttf: file too short")
	}
	numTables := int(binary.BigEndian.Uint16(data[4:6]))
	tables := map[string]sfntTable{}
	for i := 0; i < numTables; i++ {
		rec := data[12+i*16 : 12+i*16+16]
		tag := string(rec[0:4])
		off := binary.BigEndian.Uint32(rec[8:12])
		length := binary.BigEndian.Uint32(rec[12:16])
		tables[tag] = sfntTable{tag, off, length}
	}

	req := func(tag string) (sfntTable, error) {
		t, ok := tables[tag]
		if !ok {
			return sfntTable{}, fmt.Errorf("ttf: missing required table %q", tag)
		}
		return t, nil
	}

	headT, err := req("head")
	if err != nil {
		return nil, err
	}
	unitsPerEm := int(binary.BigEndian.Uint16(data[headT.offset+18 : headT.offset+20]))
	indexToLocFormat := int16(binary.BigEndian.Uint16(data[headT.offset+50 : headT.offset+52]))
	_ = indexToLocFormat

	hheaT, err := req("hhea")
	if err != nil {
		return nil, err
	}
	numHMetrics := int(binary.BigEndian.Uint16(data[hheaT.offset+34 : hheaT.offset+36]))
	ascender := int(int16(binary.BigEndian.Uint16(data[hheaT.offset+4 : hheaT.offset+6])))
	descender := int(int16(binary.BigEndian.Uint16(data[hheaT.offset+6 : hheaT.offset+8])))

	maxpT, err := req("maxp")
	if err != nil {
		return nil, err
	}
	numGlyphs := int(binary.BigEndian.Uint16(data[maxpT.offset+4 : maxpT.offset+6]))

	hmtxT, err := req("hmtx")
	if err != nil {
		return nil, err
	}
	widths := make([]int, numGlyphs)
	lastWidth := 0
	off := hmtxT.offset
	for gid := 0; gid < numGlyphs; gid++ {
		if gid < numHMetrics {
			lastWidth = int(binary.BigEndian.Uint16(data[off : off+2]))
			off += 4 // advanceWidth (2) + lsb (2)
		}
		widths[gid] = lastWidth
	}

	cmapT, err := req("cmap")
	if err != nil {
		return nil, err
	}
	cm, err := parseCmap(data, cmapT.offset)
	if err != nil {
		return nil, err
	}

	return &TTFFont{
		Raw:        data,
		UnitsPerEm: unitsPerEm,
		NumGlyphs:  numGlyphs,
		Ascender:   ascender,
		Descender:  descender,
		widths:     widths,
		cmap:       cm,
	}, nil
}

// parseCmap picks the best available unicode subtable (prefers format 12,
// falls back to format 4) and decodes it into a rune->glyph-id map.
func parseCmap(data []byte, cmapOff uint32) (map[rune]uint16, error) {
	numTables := int(binary.BigEndian.Uint16(data[cmapOff+2 : cmapOff+4]))
	type sub struct {
		platformID, encodingID uint16
		offset                 uint32
	}
	var subs []sub
	for i := 0; i < numTables; i++ {
		rec := data[cmapOff+4+uint32(i)*8 : cmapOff+4+uint32(i)*8+8]
		subs = append(subs, sub{
			platformID: binary.BigEndian.Uint16(rec[0:2]),
			encodingID: binary.BigEndian.Uint16(rec[2:4]),
			offset:     cmapOff + binary.BigEndian.Uint32(rec[4:8]),
		})
	}

	pick := func(pid, eid uint16) (uint32, bool) {
		for _, s := range subs {
			if s.platformID == pid && s.encodingID == eid {
				return s.offset, true
			}
		}
		return 0, false
	}

	// Prefer Windows Unicode BMP (3,1) format 4, then Windows full Unicode
	// (3,10) or Unicode platform (0,4/0,6) format 12.
	if off, ok := pick(3, 10); ok {
		if m, err := decodeCmapSubtable(data, off); err == nil {
			return m, nil
		}
	}
	if off, ok := pick(0, 4); ok {
		if m, err := decodeCmapSubtable(data, off); err == nil {
			return m, nil
		}
	}
	if off, ok := pick(3, 1); ok {
		if m, err := decodeCmapSubtable(data, off); err == nil {
			return m, nil
		}
	}
	if off, ok := pick(0, 3); ok {
		if m, err := decodeCmapSubtable(data, off); err == nil {
			return m, nil
		}
	}
	return nil, fmt.Errorf("ttf: no usable cmap subtable found")
}

func decodeCmapSubtable(data []byte, off uint32) (map[rune]uint16, error) {
	format := binary.BigEndian.Uint16(data[off : off+2])
	m := map[rune]uint16{}
	switch format {
	case 4:
		segCountX2 := binary.BigEndian.Uint16(data[off+6 : off+8])
		segCount := int(segCountX2 / 2)
		endCodesOff := off + 14
		startCodesOff := endCodesOff + uint32(segCountX2) + 2
		idDeltaOff := startCodesOff + uint32(segCountX2)
		idRangeOff := idDeltaOff + uint32(segCountX2)
		for i := 0; i < segCount; i++ {
			endCode := binary.BigEndian.Uint16(data[endCodesOff+uint32(i)*2:])
			startCode := binary.BigEndian.Uint16(data[startCodesOff+uint32(i)*2:])
			idDelta := int16(binary.BigEndian.Uint16(data[idDeltaOff+uint32(i)*2:]))
			idRangeOffset := binary.BigEndian.Uint16(data[idRangeOff+uint32(i)*2:])
			if startCode == 0xFFFF && endCode == 0xFFFF {
				continue
			}
			for c := uint32(startCode); c <= uint32(endCode) && c != 0xFFFF; c++ {
				var gid uint16
				if idRangeOffset == 0 {
					gid = uint16(int32(c) + int32(idDelta))
				} else {
					glyphIndexAddr := idRangeOff + uint32(i)*2 + uint32(idRangeOffset) + (uint32(c)-uint32(startCode))*2
					if int(glyphIndexAddr)+2 > len(data) {
						continue
					}
					g := binary.BigEndian.Uint16(data[glyphIndexAddr:])
					if g == 0 {
						continue
					}
					gid = uint16(int32(g) + int32(idDelta))
				}
				if gid != 0 {
					m[rune(c)] = gid
				}
			}
		}
		return m, nil
	case 12:
		numGroups := binary.BigEndian.Uint32(data[off+12 : off+16])
		base := off + 16
		for i := uint32(0); i < numGroups; i++ {
			g := data[base+i*12 : base+i*12+12]
			startChar := binary.BigEndian.Uint32(g[0:4])
			endChar := binary.BigEndian.Uint32(g[4:8])
			startGID := binary.BigEndian.Uint32(g[8:12])
			for c := startChar; c <= endChar; c++ {
				m[rune(c)] = uint16(startGID + (c - startChar))
			}
		}
		return m, nil
	default:
		return nil, fmt.Errorf("ttf: unsupported cmap format %d", format)
	}
}

// GlyphID returns the glyph index for r, or 0 (the .notdef glyph) if the
// font has no mapping for it.
func (f *TTFFont) GlyphID(r rune) uint16 {
	return f.cmap[r]
}

// WidthEm1000 returns gid's advance width scaled to a 1000-unit em, matching
// the convention used throughout pdfgen.go for the base-14 fonts.
func (f *TTFFont) WidthEm1000(gid uint16) float64 {
	if int(gid) >= len(f.widths) {
		if len(f.widths) == 0 {
			return 0
		}
		return float64(f.widths[len(f.widths)-1]) * 1000.0 / float64(f.UnitsPerEm)
	}
	return float64(f.widths[gid]) * 1000.0 / float64(f.UnitsPerEm)
}
