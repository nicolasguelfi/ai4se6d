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

## Updates

Refines `2026-04-01-glossary-block-pattern.md` which established the glossary pattern but included bibliography inline.
