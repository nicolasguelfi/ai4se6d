---
title: "Pattern: spectrum-bar — gradient bar for visualizing a continuum"
category: guidelines
scope: collection
origin: ai4se6d_vibecoding (2026-04-01)
tags: [pattern, visual, gradient, spectrum, continuum]
---

## Pattern: spectrum-bar

A horizontal gradient bar visualizing a continuum between two extremes. Suitable for scales, adoption levels, risk spectrums, competence levels.

## Layout

- Container: `border-radius: 12px; padding: 16px 32px;`
- Background: `linear-gradient(90deg, rgba(color1, 0.3) 0%, rgba(color2, 0.3) 100%)`
- Labels at extremes: bold + contrasting colors (e.g., amber left, teal right)
- Optional: explanatory text below

## Code

```python
_spectrum_bar = ns(
    "background:linear-gradient(90deg, rgba(243,156,18,0.3) 0%, rgba(46,196,182,0.3) 100%);"
    "border-radius:12px;padding:16px 32px;",
    "my_spectrum_bar",
)

with st_block(_spectrum_bar):
    st_write(bs.body, (bs.left_label, "0%"), (bs.body, "  ↔  "), (bs.right_label, "100%"))
```

## Reference block

`ai4se6d_vibecoding/blocks/bck_intro_review_habits.py`

## Applicability

Any presentation comparing two extremes on a scale.
