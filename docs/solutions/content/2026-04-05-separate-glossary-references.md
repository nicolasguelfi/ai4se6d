---
title: Separate glossary and references into distinct blocks
category: content
scope: collection
origin: ai4se6d_vibecoding + ai4se6d_genai_intro (2026-04-05)
tags: [glossary, references, bibliography, separation, blocks]
---

## Context

Both modules had glossary + bibliography combined in a single `bck_glossary.py`. The glossary (19 terms in vibecoding, 12 in genai_intro) scrolls beyond viewport, and the bibliography is a distinct concern.

## Problem

Combining glossary and references in one block:
- Creates an excessively long block file
- Couples two independent functions (terminology vs. sourcing)
- Makes it hard to skip one without the other
- The `_page_fill` container was inappropriate (content scrolls naturally)

## Solution

Split into two blocks per module:
- `bck_glossary.py` — terms and definitions only, no `_page_fill` (scrollable)
- `bck_references.py` — `st_bibliography()` only

Wire in book.py: glossary → references (last two blocks).

### bck_references.py template

```python
"""References — Bibliography of all cited sources."""
from streamtex import *
from streamtex.bib import st_bibliography
from custom.styles import Styles as s

class BlockStyles:
    heading = s.project.titles.section_title + s.center_txt
bs = BlockStyles

def build():
    st_bibliography(
        title="References",
        title_style=bs.heading,
        entry_style=s.large,
        toc_lvl="1",
        only_cited=True,
    )
```

## Update 2026-04-08: Centralized shared bibliography

The separation pattern was extended to full centralization across modules:

### Shared glossary
- Single `shared-blocks/blocks/bck_shared_glossary.py` (37 terms)
- Each module's `book.py` references `blocks.bck_shared_glossary` (resolved via chained registry)
- Local `bck_glossary.py` files removed from all modules

### Shared bibliography
- Single `shared-blocks/static/references.bib` (48 entries)
- Each module's `book.py` uses `bib_sources=[str(_shared_static / "references.bib")]`
- Local `.bib` files deleted from all 3 modules

### Fusion procedure
1. **Inventory** all `.bib` files across modules (count entries per module)
2. **Detect identical entries** — same bibkey in multiple modules (keep the most complete version)
3. **Detect equivalent entries** — same source, different bibkeys (e.g., `gartner2025aiassistants` vs `gartner-aidev2027`). Choose one bibkey (prefer KBSCI convention).
4. **Rename `cite()` calls** in all block files that used the deprecated bibkeys
5. **Update `bib_sources`** in all `book.py` files
6. **Delete local `.bib` files**
7. **Verify**: grep for orphaned `cite()` keys not in the central `.bib`

### Bibkey naming convention
Align with KBSCI document: `author-topic-year` (e.g., `tihanyi-secure2024`, `spracklen-packages2025`).
For web sources consulted recently: use consultation year (e.g., `stackoverflow-survey2026`).

## Updates

Refines `2026-04-01-glossary-block-pattern.md` which established the glossary pattern but included bibliography inline.
