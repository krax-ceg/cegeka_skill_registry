---
name: web-search
description: >-
  Conduct advanced corporate reconnaissance using programmatic web search to discover financial statements,
  investor relations disclosures, 10-K/10-Q filings, C-suite strategic bets, active cloud migrations,
  and stakeholder buying history. Download source PDFs and append complete URLs.
---

# Advanced Web Reconnaissance Skill

This skill instructs agents on how to execute targeted web searches and download source documents:
* **Financial Statements & Earnings**: 10-K filings, annual balance sheets, and quarterly revenue streams.
* **Investor Relations (IR) Presentations**: Multi-year strategic bets, CAPEX guidance, and cost-reduction mandates.
* **Technical Footprints**: Active migration vacancies (job boards), engineering war stories, and existing vendor contracts.
* **Decision-Maker Profiling**: Executive interviews, previous vendor track records, and architectural biases.

---

## 1. Search Query Syntax

| Purpose | Search Query Example | Tactical Outcome |
|---|---|---|
| **Annual Reports / PDFs** | `"Acme Corp" annual report filetype:pdf` | Direct link to official filing. Automatically downloaded when `--download-dir` is provided. |
| **Investor Relations** | `site:investor.acme.com "strategic priorities"` | Restricts search to corporate investor portal. |
| **SEC Edgar Filings** | `site:sec.gov/edgar "Acme Corp" "10-K"` | Official regulatory 10-K filings and financial tables. |
| **Executive Profiling** | `"Sarah Connor" "Acme Corp" ("interview" OR "podcast")` | Leadership priorities and public statements. |

---

## 2. Tooling & CLI Automation

Agents must execute the native `web-tools` CLI:

### Quick Search (JSON Output)
```bash
web-tools search "Acme Corp financial results 2024" --max 5 --json
```

### Search with Automatic Document Archival (PDFs / Financials)
```bash
web-tools search "Acme Corp annual report filetype:pdf" --download-dir /home/azureadmin/data/downloads --json
```

This returns complete canonical URLs and downloads matching files, computing their SHA-256 provenance hash.

---

## 3. Strict Citations & Source Document Requirements

1. **Complete Canonical URLs**: Always cite the complete absolute URL (`https://...`). Never use truncated links.
2. **Archived Artifacts**: When financial reports or PDFs are downloaded, record their SHA-256 hash, byte size, and local archive path:
   ```yaml
   sources:
     - id: annual-report-2023
       resource: "https://investor.acme.com/reports/annual-2023.pdf"
       title: "Acme Corp Annual Report 2023 (SHA256: 3a2f...)"
   ```
