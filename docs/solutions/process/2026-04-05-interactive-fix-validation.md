---
title: Interactive fix-by-fix validation is mandatory
category: process
scope: collection
origin: ai4se6d_vibecoding review cycle (2026-04-05)
tags: [CE, fix, interactive, validation, workflow]
---

## Context

During the /stx-ce:fix phase on ai4se6d_vibecoding (54 findings, 3 phases), batch mode was accidentally used for a sequence of fixes. The user immediately corrected this: every fix must be presented individually for validation.

## Problem

Batch-fixing multiple findings without per-fix validation leads to:
- Fixes applied that the user would have modified or skipped
- Lost opportunity for the user to redirect (e.g., "change the text too" or "actually this isn't a problem")
- Decisions made without user input that require backtracking

## Solution

**Always present one fix at a time** with this structure:

```
## Fix #N — Ref : Description

| | |
|---|---|
| **Ref** | finding ID |
| **Severity** | CRITICAL / MAJOR / MINOR |
| **File** | block path |
| **Problem** | what's wrong and why |
| **Fix** | what will change (before/after) |

**Accept / Skip / Modify ?**
```

Wait for explicit validation before applying. Never batch multiple fixes.

## Applies when

Every `/stx-ce:fix` session, regardless of finding count. The user explicitly rejected batch mode even for MINOR fixes.

## Updates

Supersedes the suggestion in `2026-04-01-interactive-ce-modes.md` that batch mode is acceptable for MINOR fixes. Per user preference: always interactive, no exceptions.
