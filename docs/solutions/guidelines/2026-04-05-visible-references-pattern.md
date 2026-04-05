---
title: All external sources must have visible cite() — not just # REF comments
category: guidelines
scope: collection
origin: ai4se6d_vibecoding fix cycle (2026-04-05)
tags: [citations, bibliography, cite, references, transparency, visible]
---

## Context

During the fix phase, `# REF:` comments were initially added to tool-specific stats. The user corrected this: comments are not enough. Every external source MUST have a visible, clickable `cite()` call.

## Rule

Every block that references an external source MUST:
1. Have `# REF: <bib_key>` as a code comment (traceability for maintainers)
2. Have `cite("<bib_key>")` rendered visibly on the slide (transparency for audience)
3. Have a corresponding entry in `static/references.bib`

## Pattern

```python
from streamtex.bib import cite

class BlockStyles:
    source = s.project.titles.caption  # muted, 32pt — discreet but visible

def build():
    # ... slide content with stats ...
    
    # REF: cursor-ainative2025
    st_write(bs.source, cite("cursor-ainative2025"))
```

For slides citing multiple sources:
```python
    st_write(bs.source, cite("source1"), " · ", cite("source2"))
```

## Placement

- Bottom of each sub-slide, inside the last `with st_block(...)` container
- Before `st_slide_break()` or at end of `build()`
- Style: `bs.source` (caption, muted color, 32pt) — discreet but readable

## Applies when

Any block containing statistics, quotes, attributions, factual claims, or tool-specific data. No exceptions.
