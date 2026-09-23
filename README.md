# Cegeka Skill Registry

Version-controlled registry of autonomous AI agent skills used internally at Cegeka.

## Skills Catalog

| Skill | Directory | Description |
|---|---|---|
| **web-search** | `web-search/` | Programmatic web search via DuckDuckGo and Google News RSS; discovers financial statements, IR decks, 10-Ks, and downloads source PDFs with complete canonical URLs. |
| **web-crawl** | `web-crawl/` | Deep domain crawler; maps corporate websites, extracts operational contacts (emails, phones), and archives linked documents. |
| **kyb-verification** | `kyb-verification/` | Swedish & European corporate due diligence: Allabolag registry verification, EU VIES VAT validation, OpenSanctions screening, adverse media investigation, and audited financial report archiving. |
| **okf** | `okf/` | Open Knowledge Format (OKF 0.2) concept authoring, schema validation, and knowledge bundle compilation. |
| **sow-generator** | `sow-generator/` | Generates client-facing Statement of Work PDF (Data, AI & Knowledge Services) from call transcripts and direct inputs. |
| **partner-sales-dossier-generator** | `partner-sales-dossier-generator/` | Compiles partner-tailored (Databricks, Microsoft Fabric, Joint Azure Databricks, Snowflake) sales intelligence dossiers and closing plan 16:9 board presentations. |

## Installation & Agent Usage

Skills can be loaded by AI agents (Goose, Claude Code, Antigravity, or `agent-service`).

To install or symlink for local agent discovery:
```bash
mkdir -p ~/.agents/skills
for skill in web-search web-crawl kyb-verification okf sow-generator partner-sales-dossier-generator; do
  ln -sfn "$(pwd)/$skill" ~/.agents/skills/"$skill"
done
```
