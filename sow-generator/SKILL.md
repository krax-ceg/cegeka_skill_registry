---
name: sow-generator
description: Generate a client-facing Statement of Work PDF (Data, AI & Knowledge Services) from call transcripts, notes, or direct answers, styled like SOW_Template_Data_AI_Best_Practice.html. Asks the user about anything missing or ambiguous instead of inventing it, and writes unresolved items to a separate Open Items Register DOCX. Use when asked to draft/produce/generate a SOW, statement of work, or scope document for a Data/AI/Knowledge engagement, or to turn a call transcript/VTT/notes into a SOW.
---

# SOW Generator

Produces a signature-ready-format **client-facing SOW PDF** plus (when needed) a separate
**Open Items Register (DOCX)** for anything that could not be confirmed. The rendering
engine is a self-contained, pre-compiled Go binary (stdlib-only, no runtime dependencies)
bundled inside this skill — you never write the PDF/DOCX by hand, you only produce the
JSON data file it consumes.

This is a global skill: its files live under your Claude Code skills directory (e.g.
`~/.claude/skills/sow-generator/` on Linux/macOS/WSL, `%USERPROFILE%\.claude\skills\sow-generator\`
on Windows), **not** inside the user's current project. Every path below (`bin/`,
`schema/`, `reference/`) is relative to that skill directory, not the current working
directory — resolve the skill directory's absolute path first, then build the binary/data
paths off of it. Write the generated PDF/DOCX outputs into the user's project (current
working directory or wherever they specify), never into the skill directory itself.

The visual/structural reference is bundled at
`reference/SOW_Template_Data_AI_Best_Practice.html` inside this skill. That HTML is a
**dual-layer internal drafting document**: white "clause card" boxes are the actual
client-facing contract language, gold-bordered "Drafting Guidance" callouts are
internal-only commentary for whoever is drafting. **Never copy a gold callout, the "Why
Data/AI/Knowledge SOWs Are Different" section, or the "Pre-Flight Checklist" section into
the generated SOW** — those exist to guide you, the drafter, not to appear in a client
document. Do use the checklist as your own internal QA pass before you consider the SOW
ready (see step 5).

## Step 1 — Gather source material

Ask the user for whatever they have, if it isn't already provided:
- Call transcripts (`.vtt` — WebVTT timestamps + speaker text; strip the timestamp/cue
  lines, keep speaker text), meeting notes, emails, Slack threads, scoping docs (`.txt`,
  `.md`, or other plain text).
- Direct answers to your questions, if no written material exists yet.

Read every file the user points you to. For `.vtt` files, treat it as a rough transcript
of a scoping conversation: extract facts, not verbatim dialogue — attribute claims to
"per discussion" rather than quoting speakers.

## Step 2 — Extract into the data schema

The full field list is `schema/sow-data.schema.json`. Populate a JSON object matching it
from what you can actually ground in the source material. Rules:

- **Never invent** a client name, legal entity, fee amount, date, percentage, named
  individual, or metric target that isn't stated or clearly implied in the source. If
  it's not there, leave the field as an empty string/array — the renderer will show a
  gold `[Not yet confirmed]`-style placeholder, which is correct and intentional.
- Distinguish (per the template's own drafting guidance) **assumptions** (things priced
  on the belief they're true), **prerequisites** (dated pre-kickoff readiness gate), and
  **dependencies** (external factors neither party controls) — don't collapse these into
  one bucket.
- Tag every objective `tactical` or `strategic`.
- **Deliverables and their priority are the part to be most critical about.** For each
  deliverable, you must be able to state: what it is, its priority (`must-have` /
  `should-have` / `nice-to-have`), which milestone it ties to, and what "acceptance"
  concretely means. If the source material only gives a vague deliverable ("some kind of
  dashboard") with no way to test acceptance, that is a gap — surface it in Step 3, don't
  paper over it with generic acceptance language.
- If commercial model is outcome-based or hybrid, success metrics in Section 4 are not
  optional — if they're missing, that's a Step 3 question, not a skippable section. A
  metric with no quantifiable target is a gap, not something to leave vague — chase a
  number in Step 3 or route it to open_items. Where possible, also state who consumes
  the metric, through what workflow, and why it changes their behavior (`consumed_by`) —
  a number nobody acts on doesn't make the business case.
- Lead `exec_summary` with the client's own **vision statement** (their stated end-state,
  in their language), then the current-state problem that creates the gap to it, then
  what's delivered as the path across that gap. Don't open with architecture or
  technology — that reads as a technical brief that happens to mention business value,
  not a business case that happens to be delivered on the technology.
- `workstreams[].in_scope`/`out_of_scope` should say **why**, not just restate what —
  e.g. not "ERP integration is out of scope" but "...because this phase validates the
  single-source path first."
- A report/dashboard-style deliverable defaults to `should-have`/`nice-to-have`, not
  `must-have` — the underlying data/platform work behind it is usually the real
  must-have. If the engagement is meant to build a business case for further investment,
  consider whether a dedicated "Business Case / Value Quantification" deliverable
  belongs on the list.
- Any part of the fee that's a pass-through/reimbursed cost (e.g. cloud consumption)
  must read as clearly additive in `exec_summary.commercial_headline` — bold it and mark
  it as an addition, not folded silently into the headline number.
- If part of the fee is covered by a vendor co-funding program, don't blend the funded
  amount into the customer-paid milestone percentages — the customer-paid milestones
  should sum to 100% of the customer-payable (net) amount, and the funded amount gets
  its **own separate milestone line** (`funding_source` != "Client"), typically triggered
  on final engagement sign-off. Use the standard term **"Partner-Led Funding"** throughout
  once you've named the specific vendor program (e.g. Microsoft ECIF) once for clarity —
  don't switch between acronyms and the generic term inconsistently.
- Never default `data_protection` to "not applicable / no GDPR data" — most SOWs name at
  least one client contact (name, email, phone), which is itself personal data. Source
  standard clause text from Legal/the MSA rather than leaving the section blank or
  inventing legal language.
- `escalation` (owner role, response SLA, SLA reference) is a separate concept from the
  delivery `timeline` and from `commercial.milestone_payments` — keep the three visually
  and structurally distinct in the rendered SOW rather than conflating them under one
  heading. Default response SLA is 5 business days unless the engagement needs otherwise.
- The `signatories`/signature block is deliberately **not** a schema field — the renderer
  always leaves it blank so the document remains signable. Never try to fill it in.

## Step 3 — Ask about what's missing or ambiguous

Before generating anything, review your draft JSON critically, the same way a delivery
lead would red-team a fixed-fee SOW before it goes out:

- Is every deliverable's acceptance criterion something a third party could adjudicate
  pass/fail on, without either party's testimony?
- Does the commercial model actually match how scope is written (no "fixed fee" pricing
  an open-ended outcome)?
- Are dates, fees, and named individuals present where the engagement genuinely needs
  them (not every field needs a value — a Discovery-only proposal may not need a full
  milestone payment table yet, but it does need at least one).
- Is there a real ambiguity a reasonable reviewer would flag (e.g., data volumes never
  mentioned, no named client SME, LLM/compute cost ownership unstated)?

Group these into a small number of concrete questions and ask the user directly (prefer
the AskUserQuestion tool for discrete choices — commercial model, project type,
priority ranking — and plain questions for open-ended facts like fee amounts or names).
Don't ask about things you can reasonably classify yourself from context (e.g. tagging
an objective tactical vs strategic) — reserve questions for things only the user can
know or decide.

**Do not loop indefinitely.** One round of clarifying questions is normal; if the user
doesn't have an answer to something ("don't know yet," "TBD," "ask the client"), stop
asking and move it to Step 4 instead of re-asking.

## Step 4 — Route unresolved items to the Open Items Register

Anything still unknown after Step 3 goes into the JSON's `open_items` array — not into
the SOW body as an invented value, and not as a gold placeholder standing in for
something that should have been chased down. For each open item state:
- `section` — which SOW section it affects,
- `question` — precisely what's needed,
- `why_it_matters` — why this specific engagement needs it decided,
- `risk_if_unresolved` — what goes wrong on a fixed-fee/outcome-based deal if it ships
  undecided (margin erosion, unenforceable acceptance, uncapped pass-through cost, etc.
  — be specific to the item, not generic),
- `suggested_owner` — Client / Cegeka / Joint.

Be genuinely critical here, especially on deliverables and their priority — a deliverable
with a fuzzy acceptance criterion or unclear priority is exactly the kind of gap that
turns into a margin-losing dispute later, so it belongs in this register even if the
client would rather you "just put something reasonable."

## Step 5 — Generate the documents

Write the JSON to a scratch path, then run the platform-appropriate binary using the
**absolute path to this skill's own `bin/` directory** (e.g.
`~/.claude/skills/sow-generator/bin/sowgen-linux-amd64` — do not assume it's on `PATH` or
relative to the current directory):

```
<skill_dir>/bin/sowgen-linux-amd64 -data <path/to/data.json> -pdf <output/SOW_<Client>.pdf> [-openitems <output/SOW_<Client>_OpenItems.docx>]
```

(On Windows, use `sowgen-windows-amd64.exe` — same flags.) Only pass `-openitems` if
`open_items` is non-empty; the binary skips creating that file otherwise. Save outputs to
a location the user specifies, or their current project directory if unspecified — never
write into the skill directory itself.

Before handing back, run your own pass against the "Pre-Flight Checklist" section of
`reference/SOW_Template_Data_AI_Best_Practice.html` (internal use only — don't put it in
the output) and confirm nothing on it is silently broken by your draft.

## Step 6 — Report back

Tell the user:
- Where the SOW PDF was written.
- Whether an Open Items Register was produced, and a one-line summary of what's in it
  (count and the highest-risk items) if so.
- That the signature section is intentionally blank and the document should go through
  Legal review before it's sent to a client, per the template's own footer disclaimer.

## Rebuilding the binaries

Source is in `src/` (Go, stdlib only, no external modules — builds offline). To rebuild
after a source change:

```
GOOS=linux   GOARCH=amd64 go build -o bin/sowgen-linux-amd64     ./src
GOOS=windows GOARCH=amd64 go build -o bin/sowgen-windows-amd64.exe ./src
```
