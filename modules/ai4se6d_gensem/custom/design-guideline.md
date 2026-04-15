# Design Guideline — ai4se6d_gensem

## Module Context

- **Training**: AI for Software Engineering — 6-Day Professional Training (DLH Luxembourg)
- **Module**: GSE-One — Generative Software Engineering Methods
- **Sessions**: 3-4 (Days 3-6), 4 sessions × 3h = 12h total
- **Audience**: 5-20 software developers with basic IT/programming background
- **Prerequisite**: Participants completed genai_intro + vibecoding modules (Days 1-2)
- **Projection**: Dark room, 16:9, 10-20m viewing distance
- **Zoom**: 90%

## Guideline

```
minimalist-visual + maximize-viewport
```

**minimalist-visual** takes priority (content philosophy), **maximize-viewport** complements (viewport-filling, projection-safe constraints).

## Guideline Rationale

This module teaches a methodology (GSE-One). The slides must:
- **Convey one idea per slide** — methodology concepts are sequential, not parallel
- **Use images to carry the message** — illustrative, symbolic images for each key concept
- **Keep text telegraphic** — the presenter explains, the slide anchors the idea
- **Provide depth via tooltips** — `st_hover_tooltip` for scientific sources, definitions, details
- **Fill the viewport** — no small content lost in empty space (from maximize-viewport)
- **Be projection-safe** — minimum 48pt body text, high-contrast colors

## Overrides

None. All blocks follow the combined guideline unless annotated otherwise.

## Module-Specific Design Rules

### R1 — One Idea Per Slide
Each slide has exactly one focal point. If a concept needs elaboration, use a tooltip or a separate slide — never cram two ideas onto one slide.

### R2 — Images Are Primary Content Carriers
Every concept slide should have an illustrative image (AI-generated or managed) that visually represents the idea. The image occupies 50-80% of the slide when it is the main element.

### R3 — Text Is Telegraphic
- Headlines: 3-7 words
- Body statements: 1-2 sentences maximum
- Bullets: 5 maximum per slide, 7 words maximum per bullet
- Complete explanations go in `st_hover_tooltip`, not on the slide

### R4 — Tooltips for Depth
Every slide that presents a fact, statistic, or concept must have an `st_hover_tooltip` **placed immediately after the slide title** (never at the bottom of the slide — tooltips open downward and would be clipped or invisible at the bottom).

Content:
- Source reference (paper, study, section)
- 2-4 term/definition entries that connect logically to the slide content
- A "GSE-One link" entry when the concept maps to a specific command or principle

### R5 — Font Size Discipline
| Usage | Style | Size | When |
|---|---|---|---|
| Slide title | `s.project.titles.slide_title` | 96pt | Every slide heading |
| Section subtitle | `s.project.titles.section_title` | 80pt | Group/category labels |
| Key statement | `s.huge` | 80pt | Slide's main message (1 per slide max) |
| Body text | `s.Large` | 48pt | Descriptions, bullet items |
| Captions/sources | `s.large` | 32pt | Citations, metadata |
| **NEVER on slide** | `s.Giant` / `s.GIANT` / `stat_hero` | 128-196pt | Reserved exclusively for the module title slide |

### R6 — Responsive Grids
All grids use `repeat(auto-fit, minmax(Npx, 1fr))` with:
- `minmax(350px, 1fr)` — standard cards with text
- `minmax(280px, 1fr)` — compact cards (3 pillars, features)
- `minmax(250px, 1fr)` — table columns
- Every grid cell uses `g.cell()` context manager
- Every grid cell has background (`cell_primary_bg`, `cell_accent_bg`, or `cell_active_bg`) + `cell_pad_md`

### R7 — Image Centering
When a slide contains a single image as its main element, the image is always centered (`s.center_txt` on the image style). This is a universal graphic design rule — no exceptions.

### R8 — Tooltip Positioning
- `position="center"` by default (safe for any icon position)
- `position="right"` only when the icon is at the far left of the viewport
- `position="left"` only when the icon is at the far right of the viewport
- Tooltip `width` never exceeds `50vw` to avoid clipping

### R9 — Slide Break Pattern
When a block contains multiple slides separated by `st_slide_break()`:
```python
def build():
    # FIRST sub-slide: needs trailing space to prevent auto-scroll
    with st_block(_page_fill):
        # ... first slide content ...

    st_space("v", "30vh")       # MANDATORY after first sub-slide only
    st_slide_break()

    # SUBSEQUENT sub-slides: no trailing space needed
    with st_block(_page_fill):
        # ... next slide content ...

    st_slide_break()            # directly after closing st_block
```
- `st_slide_break()` is called AFTER closing the `st_block()` — never inside it
- The FIRST sub-slide needs `st_space("v", "30vh")` after its `st_block` closes — this pushes the next sub-slide below the viewport and prevents the auto-scroll
- Subsequent sub-slides do NOT need trailing space
- Each slide's content is wrapped in its own `with st_block(_page_fill):` context

### R10 — GSE-One Branding
- Module title slide: GSE-One promo video (autoplay, loop) + title
- Transition slides (between sequences): GSE-One logo (`logo-gse-geni-with-shield.webp`) at 12-15% width
- Section title slides: GSE mascot can be used as visual anchor
- Available assets: `static/images/managed/GSE/images/` (logos) and `static/images/managed/GSE/videos/` (promos)

### R11 — Color Semantics
| Color | Style | Meaning |
|---|---|---|
| Blue `#7AB8F5` | `s.project.colors.primary` | Labels, identifiers, structure |
| Teal `#2EC4B6` | `s.project.colors.accent` | Key concepts, positive emphasis |
| Amber `#F39C12` | `s.project.colors.highlight` | Warnings, new items, attention |
| Green `#27AE60` | `s.project.colors.success` | Positive results, gains |
| Red `#E74C3C` | `s.project.colors.critical` | Risks, losses, critical warnings |
| Gray `#95A5A6` | `s.project.colors.muted` | Metadata, captions, secondary info |

### R12 — AI Image Prompts
All AI-generated images use the shared prompt templates from `custom/prompts.py`:
- Palette: electric blue, teal, amber, white on dark background (#1A1A2E)
- Style: flat vector, soft gradients, geometric shapes
- No text, no watermarks, no photorealism
- Portrait (`1024x1536`) for image+text layouts, Landscape (`1536x1024`) for full-width

## Named Patterns

### `task-card`
A responsive grid of task/feature cards with colored backgrounds:
```python
with st_grid(
    cols="repeat(auto-fit, minmax(350px, 1fr))",
    gap="16px",
    cell_styles=bg_style + s.project.containers.cell_pad_md + s.center_txt,
) as g:
    for item in items:
        with g.cell():
            st_write(body, (label, "ID "), (body, "Name — Description"))
```

### `critical-task`
A single-concept slide for an important task or principle:
```python
with st_block(page_fill):
    st_write(heading, "TX — Task Name", tag=t.div, toc_lvl="2")
    st_space("v", 2)
    st_write(status_style, "Status Label")     # s.huge (80pt), NOT stat_hero
    st_space("v", 2)
    st_write(body, "One-sentence description")
    st_hover_tooltip(title="...", entries=[...])
```

### `transition-gse`
A transition slide with GSE-One logo:
```python
with st_block(page_fill_center):
    st_write(highlight + huge + center, "Key takeaway message")
    st_space("v", 2)
    st_image(center, width="12%", uri="images/managed/GSE/images/logo-gse-geni-with-shield.webp")
    st_write(accent + huge + center, "→ Next topic")
```

### `evidence-insight`
A slide presenting a key finding with supporting detail in tooltip:
```python
with st_block(page_fill):
    st_write(heading, "Topic: Transformed/Key Finding", tag=t.div, toc_lvl="2")
    st_space("v", 2)
    st_write(accent, "The key insight in one sentence.")  # s.Large bold accent
    st_space("v", 2)
    st_write(body, "Supporting explanation connecting to the methodology.")
    st_hover_tooltip(title="...", entries=[
        ("Study", "..."),
        ("Result", "..."),
        ("GSE-One link", "/gse:command does X"),
    ])
```
