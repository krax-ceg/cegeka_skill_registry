# Cegeka Skill Registry

Version-controlled registry of Claude Code skills used internally at Cegeka.

## Skills

- **sow-generator** — Generates a client-facing Statement of Work PDF (Data, AI & Knowledge Services)
  from call transcripts, notes, or direct answers, plus a separate Open Items Register DOCX for anything
  unresolved. See `sow-generator/SKILL.md` for full usage details.

## Local install

The live copy Claude Code loads from is `~/.claude/skills/<skill-name>`, symlinked into this repo so
edits to either location stay in sync:

```
ln -s "$(pwd)/sow-generator" ~/.claude/skills/sow-generator
```
