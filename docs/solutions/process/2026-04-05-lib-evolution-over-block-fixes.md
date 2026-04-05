---
title: Evolve the lib when a finding affects 5+ blocks with the same pattern
category: process
scope: collection
origin: ai4se6d_vibecoding fix — breaks parameter (2026-04-05)
tags: [CE, fix, lib, streamtex, evolution, systemic]
---

## Context

The review flagged `<br>` HTML tags in ~8 blocks as a "no raw HTML" violation. The standard fix would have been to replace `<br>` with `st_write()` + `st_br()` in each block — a tedious, repetitive change that would also make the code less readable.

## Problem

Fixing findings block by block when the root cause is a missing lib feature:
- Creates verbose, less readable code
- Doesn't solve the underlying issue (no way to express line breaks in text naturally)
- Future blocks will hit the same problem

## Solution

**If a finding touches 5+ blocks with the same pattern AND the fix has potential interest for all lib users → evolve the lib first, then the finding is resolved by design.**

Applied example: Added `breaks: bool = True` parameter to `st_write()` in `streamtex/write.py`:
- `breaks=True` (default): `\n` → `<br>` — newlines preserved visually
- `breaks=False`: all `\n` and `<br>` collapsed to spaces
- Result: existing `<br>` tags became compliant, and future blocks can use natural `\n` in triple-quoted strings

## Decision criteria

| Criteria | Fix blocks | Evolve lib |
|----------|-----------|------------|
| Number of blocks affected | < 5 | 5+ |
| Is it a recurring pattern? | No (one-off) | Yes |
| Would lib users benefit? | No | Yes |
| Implementation complexity | Low | Low to medium |

Only evolve the lib if the feature has **general interest for lib users**, not just for this project.

## Applies when

During `/stx-ce:fix`, when a batch of similar findings suggests a missing or inadequate lib feature.
