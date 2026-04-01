---
title: "Pattern: exercise-flow — 3-phase exercise structure for training"
category: guidelines
scope: collection
origin: ai4se6d_vibecoding (2026-04-01)
tags: [pattern, exercise, training, pedagogy, timer, debrief]
---

## Pattern: exercise-flow

A 3-phase structure for hands-on exercises in training presentations: briefing, timer, debrief.

## Layout

### Sub-slide 1: Briefing
- Title: exercise name
- Numbered instructions (st_list ordered)
- Duration mentioned
- Optional: AI image for visual context

### Sub-slide 2: Timer
- Duration in Giant font, centered (billboard layout)
- Minimal instruction below

### Sub-slide 3: Debrief
- Title: "Debrief" or "Compare"
- 4-5 discussion questions as bullet list
- Open-ended, reflective questions

## Code skeleton

```python
def build():
    # Briefing
    with st_block(_page_fill):
        st_write(bs.heading, "Exercise: ...", tag=t.div, toc_lvl="1")
        with st_list(list_type=lt.ordered) as l:
            with l.item(): st_write(bs.body, "Step 1...")
            # ...
    st_slide_break()

    # Timer
    with st_block(_page_fill_center):
        st_write(bs.timer, "10:00", tag=t.div)
    st_slide_break()

    # Debrief
    with st_block(_page_fill):
        st_write(bs.heading, "Debrief", tag=t.div)
        with st_list(list_type=lt.unordered) as l:
            with l.item(): st_write(bs.body, "Question 1?")
            # ...
```

## Reference blocks

- `ai4se6d_vibecoding/blocks/bck_exercise_vibecoding.py`
- `ai4se6d_vibecoding/blocks/bck_exercise_vibeeng.py`

## Applicability

Any training module with hands-on exercises. Should be a standard blueprint.
