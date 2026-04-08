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

## Variant: exercise-as-teaser (2026-04-08)

When a short exercise (8-10 min) is redundant with a longer workshop the same day or the next day, transform it into a **teaser** instead:

### Layout (single slide, no timer, no sub-slides)

- Title: "This Afternoon: [theme]" or "Tomorrow: [theme]"
- Subtitle: "[Workshop name] — [duration] with [trainer]"
- AI image (reuse from original exercise)
- Intro text: 2 sentences framing what participants will experience
- Section "What to Watch For": 5 observation questions (reformulated from the original debrief)
- Transition line: "Keep these questions in mind — we'll debrief at [time]"

### Code skeleton

```python
def build():
    with st_block(_page_fill):
        st_write(bs.heading, "This Afternoon: Pure VibeCoding", tag=t.div, toc_lvl="1")
        st_write(bs.body, (bs.keyword, "FreeSelfApp Workshop"), " — 1h45 with Tiago")
        st_image(...)
        st_write(bs.body, "This afternoon, you will experience...")
        st_write(bs.body, (bs.keyword_warn, "What to Watch For"))
        with st_list(list_type=lt.ordered) as l:
            with l.item(): st_write(bs.watch_q, "Does the result work?")
            # ...
        st_write(bs.transition, "Keep these questions in mind — we'll debrief at 4:30 PM")
```

### When to use

- Exercise duration < 15 min AND a longer workshop covers the same goal the same day
- Time savings: ~10 min per exercise transformed (from 3 sub-slides to 1)

### Reference blocks

- `ai4se6d_vibecoding/blocks/bck_exercise_vibecoding.py` (teaser for FreeSelfApp PM)
- `ai4se6d_vibecoding/blocks/bck_exercise_vibeeng.py` (teaser for CalcApp Day 2)

## Applicability

Any training module with hands-on exercises. Should be a standard blueprint.
