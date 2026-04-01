---
title: Interactive vs batch modes for CE cycle skills
category: process
scope: collection
origin: ai4se6d (2026-04-01)
tags: [CE, workflow, interactive, batch, plan, fix, produce, validation]
---

## Context

CE cycle skills (/stx-ce:plan, /stx-ce:fix, /stx-ce:produce) currently run in batch mode — executing everything at once and presenting the final result.

## Problem

Batch mode has limitations:
- **Plan**: User receives a 1800-line plan as fait accompli, cannot influence choices during construction
- **Fix**: May modify things the user wants to keep (e.g., zoom=90 by design)
- **Produce**: If one block is poorly oriented, subsequent blocks follow the same direction without correction

## Solution: Dual-mode support (--interactive / --batch)

### /stx-ce:plan --interactive

Three progressive passes:
1. **Structure pass**: Propose sequence/block list (titles only). User validates, reorders, adds, removes before continuing.
2. **Content pass**: For each validated block, propose detailed content (text, layout, image prompt). User validates or modifies block by block.
3. **Consolidation pass**: Assemble final plan. User reviews the whole before saving.

This approach ensures the user takes ownership of the plan content and can iterate before production starts.

### /stx-ce:fix --interactive

Present each fix one by one: problem description, proposed correction, "accept/skip/modify". Trace all decisions (FIXED/SKIP/MODIFIED) in the review report.

### /stx-ce:produce --interactive

Offer flexible granularity:
- **By individual block**: Show each block after production, wait for validation
- **By sequence/group**: Produce a group of related blocks (e.g., "VibeCoding principles" = 3 blocks), present them together for validation before moving to next group
- **Batch**: Produce all blocks at once (current behavior)

The user chooses granularity at launch, or the skill proposes based on document size:
- Small documents (<10 blocks): per-block default
- Medium (10-25 blocks): per-sequence default
- Large (25+ blocks): batch with checkpoints

### Producer profile integration

Store the preferred mode in `docs/solutions/producer-profile.md`:

```markdown
## Workflow Preferences
- CE fix mode: interactive
- CE plan mode: interactive (3-pass)
- CE produce mode: per-sequence
```

Skills read this preference to propose the right default.

## Applicability

All CE cycle users. Should be implemented in streamtex-claude skills (ce-plan.md, ce-fix.md, ce-produce.md).
