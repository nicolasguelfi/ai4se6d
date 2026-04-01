---
title: Extract grid cell styles to custom/styles.py
category: style
scope: collection
origin: ai4se6d (2026-04-01)
tags: [grid, table-roadmap, cells, RGBA, refactoring]
---

## Context

The table-roadmap pattern uses semi-transparent bordered cells with RGBA values derived from the project palette. These values are repeated inline in multiple blocks.

## Problem

Blocks define identical cell styles with hardcoded RGBA values (e.g., `rgba(122, 184, 245, 0.08)` for primary, `rgba(243, 156, 18, 0.15)` for active). Changing the palette requires updating multiple files.

## Solution

Add composable cell styles to `custom/styles.py`:

```python
cell_primary_bg = Style("background-color: rgba(122, 184, 245, 0.08); border: 1px solid rgba(122, 184, 245, 0.3); border-radius: 10px;", "cell_primary_bg")
cell_active_bg = Style("background-color: rgba(243, 156, 18, 0.15); border: 2px solid #F39C12; border-radius: 10px;", "cell_active_bg")
cell_accent_bg = Style("background-color: rgba(46, 196, 182, 0.2); border: 1px solid rgba(46, 196, 182, 0.5); border-radius: 10px;", "cell_accent_bg")
cell_pad_sm = Style("padding: 8px 12px;", "cell_pad_sm")
cell_pad_md = Style("padding: 12px 16px;", "cell_pad_md")
```

In blocks, compose: `s.project.containers.cell_primary_bg + s.project.containers.cell_pad_sm + s.container.layouts.vertical_center_layout + s.center_txt`

## Applicability

All StreamTeX projects using the table-roadmap pattern or any grid with themed cells.
