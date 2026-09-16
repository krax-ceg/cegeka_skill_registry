---
name: kyb-verification
description: >-
  Conduct Know Your Business (KYB) corporate due diligence on Swedish and European entities.
  Audits official corporate registries (Allabolag), verifies EU VIES VAT status, screens against
  OpenSanctions databases, checks adverse media, and downloads official annual reports & financial statements.
---

# Know Your Business (KYB) Corporate Verification Skill

This specialized skill defines standard operating procedures for autonomous B2B corporate verification and compliance auditing:
1. **Registry Verification**: Inspect official Swedish company registries (Bolagsverket via Allabolag) for active legal status, registered seat (`säte`), registered address, and official board officers/signatories.
2. **Tax & Fiscal Compliance**: Verify EU VAT registration number via the European Commission VIES REST API.
3. **Global Sanctions & PEP Screening**: Screen the legal entity and its leadership against global sanctions lists, PEP databases, and regulatory enforcement registers using OpenSanctions.
4. **Adverse Media Profiling**: Search targeted adverse media for litigation, bankruptcy, fraud, or insolvency proceedings.
5. **Document Archival**: Automatically search for and download official audited annual reports (`årsredovisning`, `bokslut`) and financial statements to `/home/azureadmin/data/downloads`.

---

## 1. Tooling & CLI Automation

Agents must execute the native `web-tools kyb` command:

### Generate OKF 0.2 Markdown Dossier
```bash
web-tools kyb "556703-7485" --download-dir /home/azureadmin/data/downloads --okf
```

### Programmatic JSON Audit
```bash
web-tools kyb "556703-7485" --download-dir /home/azureadmin/data/downloads --json
```

---

## 2. Standard Operating Procedure (SOP)

When assigned a company or transcript mentioning a customer:
1. **Identify the Organization Number (OrgNr)**:
   - If not directly provided, search for it using:
     ```bash
     web-tools search "site:allabolag.se <Company Name>" --max 3 --json
     ```
2. **Execute Full KYB Audit**:
   - Run `web-tools kyb "<OrgNr>" --download-dir /home/azureadmin/data/downloads --json`.
3. **Correlate Stakeholders**:
   - Match transcript participants against the official list of registered board members and signatories returned in `.officers`.
4. **Inspect Risk Flags**:
   - Verify that `.legal_status` is `ACTIVE` (flag `Konkurs`, `Likvidation`, or `Avregistrerat`).
   - Check that `.sanctions_hits` is empty (flag any score >= 0.70).
   - Check `.adverse_media_findings` for legal disputes.
5. **Verify Complete URL References**:
   - Ensure every cited source contains the full, complete URL (`https://www.allabolag.se/...`, `https://ec.europa.eu/...`).
