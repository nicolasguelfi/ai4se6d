---
title: Use s.project.containers.* directly — no local _page_fill aliases
category: style
scope: collection
origin: ai4se6d_vibecoding fix cycle (2026-04-05)
tags: [styles, page-fill, aliases, refactoring, containers]
---

## Context

41 block files in ai4se6d_vibecoding defined local variables like `_page_fill = s.project.containers.page_fill_top` as aliases. Variable names were inconsistent: `_page_fill`, `_page_fill_center`, `_page_fill_billboard`, `_page_fill_content`.

## Problem

- Local aliases are pure indirection — no added value over the centralized path
- Naming was inconsistent across blocks (same style, different variable names)
- 2 blocks had custom overrides hidden behind generic alias names
- Every block added 2-3 lines of boilerplate

## Solution

**Use `s.project.containers.*` directly in `st_block()` calls. No local aliases.**

Before:
```python
_page_fill = s.project.containers.page_fill_top

def build():
    with st_block(_page_fill):
```

After:
```python
def build():
    with st_block(s.project.containers.page_fill_top):
```

For custom layout overrides that differ from the standard containers, factorize in `custom/styles.py`:
```python
# custom/styles.py
page_fill_center_noalign = Style(
    "display:flex;flex-direction:column;justify-content:center;"
    "min-height:85vh;gap:2rem;",
    "page_fill_center_noalign",
)
```

## Applies when

All block files. If you see `_page_fill = s.project.containers.*`, inline it.
