# Pattern Library — ai4se6d

This folder catalogs the **streamtex-patterns** (reusable graphic design
primitives) available for the `ai4se6d` collection of trainings.

> **Source**: these patterns come from the central
> [`streamtex-patterns`](../../../stx.toml) repo, preset `ai4se6d`
> (= `slides` preset = `core` + `slides`). See `.patterns-meta.json`
> for the exact source paths and SHA of each installed pattern.
>
> To update from the central repo: `stx patterns update`.
> To check drift: `stx patterns status`.
> To promote a local edit upstream: `stx patterns promote <name>`.

Each pattern is one `.md` file at the root of this folder. The table below
is **auto-generated** by `stx patterns install/update` from each pattern's
frontmatter.

<!-- BEGIN AUTO -->
| Name | Description | Tags | Extrapolable |
|---|---|---|---|
| ptn_callout | Highlighted box for emphasized content (info / warning / critical / success variants) | callout, container, emphasis | ✓ |
| ptn_card_grid | Grid of equal-size cards with title and body, used for taxonomies and inventories | grid, cards, taxonomy | ✓ |
| ptn_categorized_grid | Grid of cards organised in named categories with category headers | grid, cards, categories, taxonomy | ✓ |
| ptn_cite | Inline source citation with author, year, and optional URL — placed under a quote, stat, or claim | citation, evidence, footer | ✗ |
| ptn_comparison_table | Multi-column comparison table with header row and aligned rows | grid, table, comparison | ✓ |
| ptn_evidence_insight | Slide template combining a hero stat, a body explanation, key takeaways, and a source citation | template, evidence, slide | ✓ |
| ptn_exercise_flow | Slide template for a timed exercise: briefing, action, debrief | template, exercise, practice, slide | ✓ |
| ptn_inline_emphasis | Inline keyword/label/accent variants for mixed-style text inside a single st_write | inline, text, emphasis | ✓ |
| ptn_slide_heading | Two-cell heading row (title + tooltip icon) at the top of a slide | atom, heading, layout | ✓ |
| ptn_stat_hero | Slide centerpiece — a single oversized statistic with body and source | stat, evidence, hero | ✓ |
| ptn_takeaways | Numbered list of 3–5 key takeaways with bold lead and explanation | list, summary, conclusion | ✓ |
| ptn_title_slide | Title slide with hero image, course/section title, subtitle, and author | template, title, slide | ✓ |
<!-- END AUTO -->

## Application rules (manual)

### Priority

1. If the user explicitly names a pattern, apply it.
2. If multiple patterns match the request, ask the user to choose.
3. If no pattern matches, generate the block freely; if the rendering looks
   reusable, propose `/stx-pattern:new` to capture it.

### Combination

A block can combine several patterns. Typical combinations seen in `ai4se6d`:

- `ptn_slide_heading` + (`grid_boston` or `ptn_card_grid` or `ptn_comparison_table`)
- `ptn_slide_heading` + `ptn_callout` (`info` / `critical`) + `ptn_cite`
- `ptn_evidence_insight` (template) → composes `ptn_slide_heading` + `ptn_stat_hero` +
  `ptn_takeaways` + `ptn_cite`
- `ptn_exercise_flow` (template) → composes `ptn_slide_heading` + `ptn_card_grid`

### Project palette

This collection uses the project styles defined in `custom/styles.py`. When a
pattern's code skeleton uses generic colors or fonts, **adapt** them to:

- `s.project.titles.*` for headings and emphasis
- `s.project.containers.callout` for callout backgrounds
- `s.project.colors.*` for accent / highlight / critical / success
- `s.project.cell_*_bg` for grid cell backgrounds (`primary`, `active`, `accent`)

Never hardcode hex colors or font sizes in a block — always reach into
`custom/styles.py` first; if a style is missing there, propose adding it.

### Cite shorthand

Sources are added through `from streamtex.bib import cite`. Use the existing
`refs/` bibliography (BibTeX) — do not duplicate citations inline.

### Fallback for unknown references

If a pattern mentions another pattern that is not yet in this catalog,
generate the equivalent inline and propose `/stx-pattern:new` to capture
the missing pattern.
