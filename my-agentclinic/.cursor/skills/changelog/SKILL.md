---
name: changelog
description: >-
  Maintains CHANGELOG.md in the project root with a heading per date.
  Use when the user invokes this skill, asks to update the changelog, or
  wants the changelog updated before merging. If no changelog exists,
  examine git commits and add bullets for each date. Otherwise add only
  commits newer than the latest heading.
disable-model-invocation: true
---

# Changelog

Manually invoke this skill before merging. Keep `CHANGELOG.md` in the project root, with headings for dates.

## Workflow

Run this from the project root (the directory that contains `CHANGELOG.md`):

```bash
python .cursor/skills/changelog/scripts/changelog.py
```

The script covers both cases:

- **No changelog:** examine git commits and add bullets for each date.
- **Changelog exists:** read the newest `## YYYY-MM-DD` heading and prepend commits dated after it.

If the git root is a parent of this project, the script limits history to files in this directory.

Review the bullets. Commit subjects are copied as written. Edit wording when a subject is unclear, then leave `CHANGELOG.md` to be committed with the merge.

Re-running when nothing is new leaves the file unchanged.

## Format

```markdown
# Changelog

## 2026-10-22

- Ship the Hello Hono phase so clone-and-run serves the home page.

## 2026-10-19

- Add my-agentclinic Video05 starter scaffold for SDD course work.
```

- One `# Changelog` title
- Date headings as `## YYYY-MM-DD`, newest first
- One bullet per commit
