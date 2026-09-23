---
name: web-crawl
description: >-
  Deep crawl target corporate domains to discover key subpages (contact, about, investor portals),
  harvest operational emails and phone numbers, and download linked whitepapers and documents.
---

# Deep Web Crawling Skill

This skill instructs agents on how to systematically crawl a company's web domain to harvest operational intelligence and archival documents:
* **Contact Discovery**: Harvesting verified corporate email addresses and telephone numbers.
* **Key Page Mapping**: Identifying high-signal subpages (`/kontakt`, `/about`, `/investors`, `/team`).
* **Document Archival**: Discovering linked PDF reports, financial statements, and whitepapers.

---

## 1. Tooling & CLI Automation

Agents must execute the native `web-tools crawl` command:

### Standard Domain Crawl
```bash
web-tools crawl "https://acme.com" --depth 2 --max-pages 5 --json
```

### Domain Crawl with Document Archival
```bash
web-tools crawl "https://acme.com" --depth 2 --max-pages 5 --download-dir /home/azureadmin/data/downloads --json
```

---

## 2. Extraction Standards

* **Complete Canonical URLs**: All discovered subpages and documents must be resolved to complete absolute URLs (`https://...`).
* **Contact Verification**: Group verified email addresses and phone numbers under official corporate contacts.
* **Archival Provenance**: When documents are downloaded, record their SHA-256 checksum and local file path.
