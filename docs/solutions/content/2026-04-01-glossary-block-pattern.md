---
title: Glossary block as standard pattern for technical presentations
category: content
scope: collection
origin: ai4se6d (2026-04-01)
tags: [glossary, abbreviations, terminology, pattern, blueprint]
---

## Context

Technical presentations use abbreviations (LLM, RLHF, GenAI, NFR, V&V...) that not all audience members know.

## Problem

Two approaches exist: (a) define each term at first occurrence (fragile if slides are reordered, heavy), (b) create a glossary at the end. Without a standard pattern, each project reinvents the glossary.

## Solution

Standard `bck_glossary.py` pattern:

```python
_ENTRIES = [
    ("AI", "Artificial Intelligence — ..."),
    ("GenAI", "Generative AI — ..."),
    ("LLM", "Large Language Model — ..."),
]

def build():
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.heading, "Glossary", tag=t.div, toc_lvl="1")
    with st_block(_page_fill):
        for term, definition in _ENTRIES:
            st_write(bs.definition, (bs.term, term), (bs.separator, " — "), (bs.definition, definition.split(" — ", 1)[1]))
            st_space("v", 0.5)
```

The glossary establishes terminology conventions (e.g., "GenAI" = "Generative AI") without requiring inline definitions. Enriched incrementally as new terms are introduced.

## Future improvement

GitHub issue nicolasguelfi/streamtex#12: glossary with hover tooltips extending the bibliography system.

## Applicability

All technical presentations and courses. Should be a standard blueprint in block-blueprints.md.
