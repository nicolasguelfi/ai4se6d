---
title: Factorize any style used in 2+ blocks into custom/styles.py
category: style
scope: collection
origin: ai4se6d_vibecoding fix cycle (2026-04-05)
tags: [styles, factoring, DRY, custom-styles, refactoring]
---

## Context

During review of ai4se6d_vibecoding, three categories of duplicated styles were found:
- `_cell` (vertical_center + center_txt): identical in 23 blocks
- Table cell styles (`_header_cell`, `_normal_cell`, `_active_cell`): identical in 2 blocks
- Table text styles (`header_text`, `cell_text`, etc.): identical in 2 blocks

## Rule

**Any style composition used in 2 or more block files MUST be extracted to `custom/styles.py`** and referenced via `s.project.*`. Never duplicate `Style.create(...)` across files.

## Applied patterns

| Style | Location in custom/styles.py | Blocks using it |
|-------|------------------------------|-----------------|
| `grid_cell_centered` | `ContainerStylesCustom` | 23 balanced/grid blocks |
| `table_header_cell` | `ContainerStylesCustom` | `bck_ide_comparison`, `bck_vibeeng_spectrum` |
| `table_normal_cell` | `ContainerStylesCustom` | Same |
| `table_active_cell` | `ContainerStylesCustom` | Same |
| `table_header` | `TextStylesCustom` | Same |
| `table_cell` | `TextStylesCustom` | Same |
| `table_label` | `TextStylesCustom` | Same |
| `table_label_active` | `TextStylesCustom` | Same |

## How to detect

During `/stx-ce:review` (style-consistency-checker), grep for `Style.create(...)` definitions across block files. If the CSS composition is identical (ignoring style_id), flag as duplicate.

## Updates

Extends `2026-04-01-extract-grid-cell-styles.md` which covered only cell background styles. This solution covers all style compositions including text styles and layout compositions.
