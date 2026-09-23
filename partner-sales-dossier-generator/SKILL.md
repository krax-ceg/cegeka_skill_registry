---
name: partner-sales-dossier-generator
description: >-
  Compiles enterprise-grade, partner-tailored sales intelligence dossiers and closing plan slide decks
  for target client accounts. Directly supports Databricks, Microsoft (Azure/Fabric), Joint Azure Databricks,
  Snowflake, and custom cloud partners. Synthesizes Nordic market data, Bolagsverket legal registries,
  partner co-funding economics (AMMP, ECIF, DBU credits), stakeholder closing roadmaps, and authentic
  Cegeka reference cases into a standalone, 16:9 interactive HTML board presentation.
---

# Partner Sales Dossier & Closing Plan Generator Skill

This skill guides the autonomous agent through synthesizing high-impact enterprise sales intelligence dossiers and board-ready closing plans tailored to major cloud and data partners (**Databricks**, **Microsoft**, **Joint Azure Databricks**, **Snowflake**, or custom partners).

The output is a single, self-contained, light-mode, 16:9 McKinsey/Bain-grade interactive HTML presentation containing an Executive Deal Landing Page (Slide 0 prioritizing Top 5 deals by Expected Value $\text{EV} = P \times V$) followed by exactly **1 slide per client** across all accounts in the target client list.

---

## 1. Partner Qualification Gate (Mandatory First Step)

When this skill is triggered, the agent **MUST** inspect the user request to determine if the target partner ecosystem has been specified.

### Partner Identification Rules:
1. **If the user explicitly specifies the partner** (e.g., "Databricks", "Microsoft", "Azure Fabric", "Joint Azure Databricks", "Snowflake", "AWS", etc.), adopt that partner immediately and configure the partner theme and economics.
2. **If the target partner is NOT stated or ambiguous**, the agent **MUST STOP and ask the user** using the `ask_question` tool before proceeding:

```json
{
  "questions": [
    {
      "question": "Which partner ecosystem should this sales dossier or closing plan target?",
      "options": [
        "(Recommended) Databricks (Lakehouse, Unity Catalog, Mosaic AI, DBU Co-funding)",
        "Microsoft (Fabric, OneLake, Azure Synapse, Azure OpenAI, AMMP/ECIF Co-funding)",
        "Joint Azure Databricks (Unified lakehouse on Azure, dual AMMP + DBU vouchers)",
        "Snowflake (Data Cloud, Cortex AI, Snowpark, Snowflake Migration Subsidy)"
      ],
      "is_multi_select": false
    }
  ]
}
```

3. **If the user enters another partner via write-in** (e.g. AWS, GCP, Google Cloud, SAP, Oracle):
   - The skill dynamically resolves or provisions a partner profile using `reference/partner_ecosystem.json` or dynamic fallback in `scripts/partner_engine.py`.
   - The partner's brand color, logo, core tech pillars, and co-funding programs are automatically plugged into the compilation engine.

---

## 2. Execution Mode Selection

The skill supports two complementary executive presentation modes:

| Execution Mode | CLI Flag | Core Content & Slide Structure |
| :--- | :--- | :--- |
| **Sales Dossier Mode** *(Default)* | `--mode sales-dossier` | **8-Part Executive Strategic Sequence**:<br>1. Trendspaning (Customer & Competitor Trends)<br>2. FOMO & Urgency (Cost of Inaction)<br>3. Quantified Business Case & Economic Impact<br>4. Strategic Discovery Questions (CTO/CDO/CFO)<br>5. Priority Partner Use Cases (Workload Mapping)<br>6. Partner Co-Funding Economics (AMMP/ECIF/DBU & 120-Day Clock)<br>7. Migration Accelerators & Jumpstarts<br>8. Authentic Cegeka Reference Benchmarks |
| **Closing Plan Mode** | `--mode closing-plan` | **4-Pillar Executive Closing Framework**:<br>1. 4-Phase Closing Roadmap (Discovery $\to$ PoV $\to$ Business Case $\to$ Contract)<br>2. Stakeholder Decision Matrix (Champion, Economic Buyer, Blockers)<br>3. Partner Co-Sell & Funding Triggers (When to loop in partner PAM/AE)<br>4. Immediate Opening Moves (Next 5 Business Days action plan) |

If the user mentions "closing plan", "how to close", "deal roadmap", or "stakeholders", select `closing-plan`. Otherwise, default to `sales-dossier`.

---

## 3. End-to-End Workflow & Procedures

### Step 1: Input Account Ingestion
1. Locate the input client list file. Default path is `client_list.txt` in the workspace root, or `examples/sample_client_list.txt`.
2. Clean and parse account names, stripping numbers, OrgNr annotations, and regional suffixes:
   - Example: `1. Sandvik (Org.nr: 556234-6865)` $\to$ `Sandvik` (OrgNr: `556234-6865`).
3. Verify account count. Ensure zero accounts are omitted or truncated.

### Step 2: System Tools & Market Intelligence Gathering
For each account (or via cached catalog in `scripts/client_intelligence_catalog.py`):
1. **KYB Legal Verification (Swedish Bolagsverket)**:
   ```bash
   /usr/local/bin/web-tools kyb --org-nr <OrgNr> --json
   ```
   Extracts official legal entity name, domicile, corporate form, board chair, and VAT validation.
2. **Web Intelligence Search**:
   ```bash
   /usr/local/bin/web-tools search "<ClientName> cloud data architecture annual report" --limit 5
   ```
   Identifies legacy stack footprint (e.g. Teradata, on-prem SQL, SAP BW, Oracle, SAS), cloud hyperscaler presence (Azure, AWS), and active modernization initiatives.
3. **Reference Case Matching**:
   Inspect `reference/cegeka_reference_cases.json` to extract the most relevant Cegeka customer benchmark by industry (e.g., *Austrotherm* for manufacturing, *Fluvius* for energy, *LRM medEmotion* for healthcare, *Bridgestone* for supply chain).

### Step 3: Economic Valuation & Deal Prioritization
Calculate Expected Value ($\text{EV}$) for every account:
$$\text{Expected Value (EV)} = \text{Contract Value (EUR)} \times \text{Win Probability (\%)} \times \text{Urgency Factor}$$
Rank all clients in descending order. The top 5 accounts form the **Executive Landing Page (Slide 0)**.

### Step 4: Co-Funding & Partner Mechanics Computation
Reference `reference/partner_ecosystem.json` to compute partner-specific subsidies:
- **Databricks**:
  - DBU Proof-of-Value Credit: $25,000–$50,000 compute offset.
  - Mandatory 120-day delivery clock from funding approval to milestone sign-off.
  - Joint customer attestation required upon Delta Lake deployment.
- **Microsoft**:
  - AMMP (Azure Migration and Modernization Program): $15,000–$50,000 ACR voucher.
  - ECIF (Enterprise Customer Investment Fund): $20,000–$75,000 partner subsidy.
  - FastTrack for Azure co-engineering support.
- **Joint Azure Databricks**:
  - Dual subsidy: Microsoft ECIF/AMMP covers Cegeka professional services + Databricks DBU voucher covers Lakehouse compute consumption.

---

## 4. Automated Compilation Script Usage

The skill includes a production-grade compiler script that executes the complete generation pipeline:

```bash
python3 <skill_dir>/scripts/generate_partner_dossier.py \
  --partner <databricks|microsoft|joint|snowflake|custom> \
  --mode <sales-dossier|closing-plan> \
  --client-list <path_to_client_list.txt> \
  --output <output_filename.html>
```

### Options:
- `--partner`: `databricks` (default), `microsoft`, `joint`, `snowflake`, `aws`, `gcp`, or custom.
- `--mode`: `sales-dossier` (8-part strategic structure) or `closing-plan` (4-pillar deal closing execution plan).
- `--client-list`: Path to file containing target client accounts (e.g., `.tsv` or `.txt`).
- `--deck-title`: (Optional) Custom slide deck title (e.g., `"Raihan Chowdhury Microsoft kunder"`).
- `--lead-rep`: (Optional) Lead Account Executive or Cloud & AI Specialist attribution (e.g., `"Raihan Chowdhury / Mårten Palm"`).
- `--output`: Target HTML file path.
- `--clients`: (Optional) Comma-separated list of specific clients to compile.
- `--max-clients`: (Optional) Limit total clients for rapid testing.

---

## 4.1 Output Directory & Filename Conventions

When compiling client intelligence, manifests, sales dossiers, closing plans, or executive briefs for a specific partner and sales representative / account manager, always follow these structure and naming standards:

### 1. Hierarchical Directory Structure (`snake_case`):
Organize outputs into a top-level partner folder, followed by an account manager subfolder:
```
<workspace_root>/<partner_slug>/<account_manager_slug>/
```
*Examples:*
- `microsoft/raihan_chowdhury/`
- `databricks/marten_palm/`
- `joint_azure_databricks/marcus_eklund/`

### 2. Date-Stamped Filename Standards (`snake_case`):
Every generated artifact must include the execution date formatted as `<YYYY_MM_DD>` in `snake_case`:
- **Account Manifest (TSV)**: `<account_manager>_<partner>_kunder_<YYYY_MM_DD>.tsv`
  - *Example*: `microsoft/raihan_chowdhury/raihan_chowdhury_microsoft_kunder_2026_09_23.tsv`
- **Client Intelligence Catalog (Python)**: `<account_manager>_kunder_catalog_<YYYY_MM_DD>.py`
  - *Example*: `microsoft/raihan_chowdhury/raihan_kunder_catalog_2026_09_23.py`
- **Interactive Sales Dossier (HTML)**: `<account_manager>_<partner>_kunder_sales_dossier_<YYYY_MM_DD>.html`
  - *Example*: `microsoft/raihan_chowdhury/raihan_chowdhury_microsoft_kunder_sales_dossier_2026_09_23.html`
- **Interactive Closing Plan (HTML)**: `<account_manager>_<partner>_kunder_closing_plan_<YYYY_MM_DD>.html`
  - *Example*: `microsoft/raihan_chowdhury/raihan_chowdhury_microsoft_kunder_closing_plan_2026_09_23.html`
- **Executive Summary / Deal Brief (Markdown)**: `<account_manager>_<partner>_kunder_summary_<YYYY_MM_DD>.md`
  - *Example*: `microsoft/raihan_chowdhury/raihan_chowdhury_microsoft_kunder_summary_2026_09_23.md`

### 3. Dynamic Deal Prioritization:
For rep-specific portfolios, dynamically recalculate Expected Value ($\text{EV} = P \times V$) across the rep's client universe to rank the Top 5 priority deals directly on Slide 0, rather than relying on a static global top 5 list.

---

## 5. UI/UX & Visual Design Standards

The generated HTML presentation must adhere strictly to top-tier strategy consulting standards (McKinsey & Company, Bain & Company, BCG):

1. **Self-Contained Single File**:
   - Zero external stylesheet or script dependencies except approved CDNs (Tailwind CSS, Inter/Newsreader fonts, Lucide icons).
   - Inlined high-resolution SVG logos for Cegeka, Databricks, Microsoft, and Snowflake.
2. **Visual Hierarchy & Light Mode**:
   - Background: Pure White (`#FFFFFF`) with Canvas Slate (`#F8FAFC`).
   - Primary Headings: Deep McKinsey Navy (`#051C2C`), serif editorial font (`Newsreader`, `Georgia`, or `Merriweather`).
   - Body & Metadata: Crisp grotesque sans-serif (`Inter`, `system-ui`).
   - Numeric Metrics: Monospace (`JetBrains Mono`, `Consolas`) with semantic badges.
   - Partner Accent Colors:
     - Databricks: `#FF3621`
     - Microsoft: `#0078D4`
     - Joint: `#0078D4` with `#FF3621` dual badging
     - Snowflake: `#29B5E8`
3. **Interactive 16:9 Presentation Features**:
   - Keyboard navigation: Left Arrow (`←`) / Right Arrow (`→`).
   - Sticky navigation header with live progress bar, slide counter, and quick jump dropdown.
   - Fullscreen presentation mode toggle (`F` key or button).
   - Instant search & account filter to jump to any of the 64 clients.
4. **Clean Print & PDF Pagination**:
   - Media query `@media print` with `@page { size: A4 landscape; margin: 0; }`.
   - Each slide occupies exactly one physical page (`break-after: page; page-break-after: always`).
   - Interactive controls hidden in print mode.

---

## 6. Directory Layout & Key Reference Files

```
partner-sales-dossier-generator/
├── SKILL.md                                 # This specification and runbook
├── reference/
│   ├── partner_ecosystem.json              # Ecosystem metadata, funding programs, tech stacks
│   ├── cegeka_reference_cases.json         # Real Cegeka case studies (Austrotherm, Fluvius, etc.)
│   └── visual_design_tokens.json           # Color palette, font stacks, slide aspect ratios
├── scripts/
│   ├── partner_engine.py                   # Partner resolver, SVG logos, color themes
│   ├── client_intelligence_catalog.py      # Intelligence catalog for all 64 target accounts
│   ├── client_closing_strategy_catalog.py  # Closing strategies & stakeholder roadmaps
│   └── generate_partner_dossier.py         # Unified CLI compiler
└── examples/
    └── sample_client_list.txt              # Standard 64 Nordic enterprise accounts
```
