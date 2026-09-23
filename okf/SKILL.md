---
name: okf
description: >-
  Author, validate, format, and bundle structured knowledge concepts according to the Open Knowledge Format
  (OKF Version 0.2) specification. Use this skill whenever extracting, managing, or synthesizing Customer,
  Stakeholder, or domain concepts from transcripts or data sources.
---

# Open Knowledge Format (OKF 0.2) Skill

This skill guides AI agents in authoring, maintaining, and verifying knowledge concepts adhering strictly to the **Open Knowledge Format (OKF 0.2)** specification.

The complete specification is available at [references/SPEC.md](./references/SPEC.md).

---

## 1. Core Principles

1. **Self-Describing Markdown**: Every concept is a UTF-8 Markdown file with a YAML frontmatter block enclosed in `---` at the top.
2. **First-Class Provenance**: Every concept derives from explicit sources recorded in the `sources` frontmatter field.
3. **Topics as Tags**: High-level categorical topics must be stored in the `tags` YAML list.
4. **Inter-Concept Graph**: Concepts link to each other using bundle-relative Markdown links (e.g., `[Jane Doe](/stakeholders/jane-doe.md)`).
5. **Human & Agent Readable**: Structural headings, clear executive narratives, and concise briefing sections.

---

## 2. Concept Document Structure

### 2.1 YAML Frontmatter

```yaml
---
type: Customer                      # REQUIRED. Descriptive type string (e.g., Customer, Stakeholder, Index)
title: Acme Corp                    # RECOMMENDED. Display title
description: Enterprise cloud user. # RECOMMENDED. One-line summary for progressive disclosure
resource: https://acme.example.com  # OPTIONAL. Canonical URI if concept binds to an asset
tags:                               # RECOMMENDED. Topics as tags
  - b2b-sales
  - cloud-migration
  - fintech
sources:                            # Provenance entries
  - resource: azure://stnordev/transcripts/2026/09/01/call.txt
    id: transcript-call-1
    title: Initial Discovery Call
    author: agent:agent_ed25519_a1b2c3d4
    last_modified: 2026-09-01T14:30:00Z
generated:
  by: agent-service/sales-intelligence
  at: 2026-09-09T18:00:00Z
---
```

### 2.2 Markdown Body Conventions

Structure the body logically with standard Markdown headings:
* `# Executive Briefing`
* `## Crucial Sales Signals` (Pains, Budget, Timeline, Objections, Competitors)
* `## Stakeholder Matrix` (Markdown table linking to `[Person](/stakeholders/person-slug.md)`)
* `## External Research & Market Intelligence`
* `## Recommended Strategy & Next Steps`

---

## 3. Go Tooling & Helper Scripts

The Go executable `okf-tool` is located at `./bin/okf-tool`. Use the helper scripts below to perform deterministic tasks:

### 3.1 Validate an OKF Concept or Bundle
Run the validation script to verify that a file or folder conforms to OKF 0.2:
```bash
./scripts/validate_okf.sh path/to/concept.md
```
Or validate an entire directory:
```bash
./scripts/validate_okf.sh path/to/bundle_dir/
```

### 3.2 Generate or Format a Customer Concept
```bash
./scripts/generate_customer.sh \
  --name "Acme Corp" \
  --industry "FinTech" \
  --domain "https://acme.com" \
  --out "customers/acme-corp.md"
```

### 3.3 Generate or Format a Stakeholder Concept
```bash
./scripts/generate_stakeholder.sh \
  --name "Sarah Connor" \
  --title "Director of Infrastructure" \
  --customer "Acme Corp" \
  --buying-role "Champion" \
  --out "stakeholders/sarah-connor.md"
```

### 3.4 Re-index a Knowledge Bundle
Scans all concepts in a directory and generates a compliant `index.md` for progressive disclosure:
```bash
./scripts/generate_index.sh path/to/bundle/
```

---

## 4. Reference Examples

* [Customer Concept Example](./examples/customer_example.md)
* [Stakeholder Concept Example](./examples/stakeholder_example.md)
* [Catalog Index Example](./examples/index_example.md)
