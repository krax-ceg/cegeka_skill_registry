package main

import (
	"encoding/json"
	"flag"
	"fmt"
	"os"
)

func main() {
	dataPath := flag.String("data", "", "path to SOW data JSON (required)")
	pdfPath := flag.String("pdf", "", "output path for the SOW PDF (required)")
	openItemsPath := flag.String("openitems", "", "output path for the Open Items Register DOCX (optional; skipped if open_items is empty)")
	flag.Parse()

	if *dataPath == "" || *pdfPath == "" {
		fmt.Fprintln(os.Stderr, "usage: sowgen -data <data.json> -pdf <out.pdf> [-openitems <out.docx>]")
		os.Exit(2)
	}

	raw, err := os.ReadFile(*dataPath)
	if err != nil {
		fmt.Fprintf(os.Stderr, "error: failed to read data file %q: %v\n", *dataPath, err)
		os.Exit(1)
	}

	var data SOWData
	if err := json.Unmarshal(raw, &data); err != nil {
		fmt.Fprintf(os.Stderr, "error: failed to parse JSON in %q: %v\n", *dataPath, err)
		os.Exit(1)
	}

	pdfBytes := BuildSOWPDF(&data)
	if err := os.WriteFile(*pdfPath, pdfBytes, 0o644); err != nil {
		fmt.Fprintf(os.Stderr, "error: failed to write PDF to %q: %v\n", *pdfPath, err)
		os.Exit(1)
	}
	fmt.Printf("Wrote SOW PDF: %s (%d bytes)\n", *pdfPath, len(pdfBytes))

	if *openItemsPath == "" {
		return
	}
	if len(data.OpenItems) == 0 {
		fmt.Fprintf(os.Stderr, "note: open_items is empty; skipping Open Items Register (%s not created)\n", *openItemsPath)
		return
	}
	docxBytes := BuildOpenItemsDocx(&data)
	if err := os.WriteFile(*openItemsPath, docxBytes, 0o644); err != nil {
		fmt.Fprintf(os.Stderr, "error: failed to write Open Items Register to %q: %v\n", *openItemsPath, err)
		os.Exit(1)
	}
	fmt.Printf("Wrote Open Items Register: %s (%d bytes)\n", *openItemsPath, len(docxBytes))
}
