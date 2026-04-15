---
title: "Pattern: stat-hero — giant statistic with context"
category: guidelines
scope: collection
origin: ai4se6d (2026-04-01)
tags: [pattern, visual, statistics, keynote, hero]
---

## Pattern: stat-hero

A large statistic displayed prominently (96pt, highlight color) with supporting context below. Classic keynote/TED pattern for memorable data points.

## Layout

- Statistic: `s.Giant + s.bold + s.project.colors.highlight`, centered
- Context: `s.Large`, centered, below the stat
- Optional: source attribution in `s.project.titles.caption`

## Code

```python
class BlockStyles:
    stat = Style.create(s.Giant + s.bold + s.project.colors.highlight + s.center_txt, "my_stat")
    context = Style.create(s.Large + s.center_txt, "my_context")
    source = s.project.titles.caption + s.center_txt

def build():
    with st_block(_page_fill_center):
        st_write(bs.stat, "84%", tag=t.div)
        st_space("v", 1)
        st_write(bs.context, "of developers use or plan to use AI tools")
        st_write(bs.source, "Stack Overflow 2025")
```

## Reference blocks

- `ai4se6d_genai_intro/blocks/bck_poll_ai_result.py`
- `ai4se6d_vibecoding/blocks/bck_vibecoding_reality.py`

## Variant: stat-hero with perception gap (2026-04-08)

For counter-intuitive statistics where perception contradicts reality, use a **2-column layout**:

### Layout

- Left column: Giant stat + factual context (N, tool, task, source)
- Right column: "Perception vs Reality" narrative (what people expected, what actually happened, why the gap exists)

### Code skeleton

```python
def build():
    with st_block(_page_fill):
        st_write(bs.heading, "The METR Paradox", tag=t.div, toc_lvl="1")
        with st_grid(cols="2fr 3fr", gap="24px", cell_styles=_cell) as g:
            with g.cell():
                st_write(bs.stat, "-19%")
                st_write(bs.body, "Experienced devs completed tasks 19% slower with AI")
                st_write(bs.source, cite("metr2025"))
            with g.cell():
                st_write(bs.body, "Before: predicted ", (bs.keyword, "+24%"), " speedup")
                st_write(bs.body, "After: ", (bs.keyword_warn, "still believed"), " +20% faster")
                st_write(bs.body, "Reality: <44% of generations accepted")
```

### When to use

Whenever presenting data that contradicts common assumptions (paradoxes, declining trends, surprising study results). More effective than a simple stat-hero for engaging critical thinking.

### Reference blocks

- `ai4se6d_vibecoding/blocks/bck_vibecoding_danger_metr.py`
- `ai4se6d_vibecoding/blocks/bck_vibecoding_danger_trust.py`

## Anti-pattern: stat-hero abuse (2026-04-14)

**Problem**: Using `stat_hero` / `s.Giant` / `s.GIANT` for non-statistical content such as status labels ("NEW — PRIMARY SKILL"), task descriptions, or section transitions. This produces 128-196pt text that is visually overwhelming and communicates nothing meaningful.

**Rule**: `stat_hero` is ONLY for impactful numeric statistics (percentages, counts, durations). Status labels use `s.huge` (80pt) maximum. Body descriptions use `s.Large` (48pt).

| Content type | Correct style | Size |
|---|---|---|
| Key statistic | `stat_hero` | 128-196pt |
| Status label | `s.huge` | 80pt |
| Body text | `s.Large` | 48pt |
| Module title | `s.Huge` | 96pt |

**Discovered in**: `ai4se6d_gensem` Sequence 1.1 — status labels for critical tasks (T1-T14) were rendered at 450pt, making the slides unreadable.

## Applicability

Any presentation with impactful statistics. Should be a standard blueprint. Use sparingly — reserve for 1-2 slides per sequence, not every slide.
