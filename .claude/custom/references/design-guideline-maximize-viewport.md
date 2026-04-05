# Design Guideline — maximize-viewport

Shared guideline for all ai4se6d modules optimized for auditorium projection.

## Target Environment
- Auditorium projection (10-20m distance)
- 16:9 ratio, dark theme
- Professional training audience: software developers

## Font Size Hierarchy

### Named sizes (primary)
| Name | Size | Usage |
|------|------|-------|
| GIANT | 196pt | Decorative stats, billboard numbers |
| Giant | 128pt | Key messages, closing statements |
| Huge | 96pt | Slide title |
| huge | 80pt | Section title |
| Large | 48pt | Body text, subtitles, table cells |
| large | 32pt | Captions, secondary text, sources |
| big | 24pt | Minimum projection-safe size |

### Intermediate sizes
When a named size doesn't fit the visual context (e.g., dense table cells,
inline labels), use any `s.text.sizes.pt<N>` value. Common intermediates:

| Size | Typical usage |
|------|---------------|
| pt36 | Dense table cells (between large 32pt and Large 48pt) |
| s.LARGE (~64pt) | Emphasized inline labels (between Large 48pt and huge 80pt) |

The minimum projection-safe size remains **24pt** (`s.big`).

## Layout Rules

### justify-content by slide type
- **Billboard / transition slides** (single large title or question, no other content): use `justify-content: center` to vertically center the text
- **All other slides** (content, balanced, lists, grids, etc.): use `justify-content: flex-start` (top-aligned)

### Viewport-filling containers (centralized in custom/styles.py)
- `s.project.containers.page_fill_top` — top-aligned, gap 1.5rem
- `s.project.containers.page_fill_center` — centered, gap 1.5rem
- `s.project.containers.page_fill_center_wide` — centered, gap 2rem
- Override locally only when layout differs (e.g., no `align-items:center`, custom gap)

### AI image orientation by slide type
- **Balanced slides** (image in a 40% column alongside text): `ai_size="1024x1536"` portrait, prompt suffix uses `"2:3 portrait aspect ratio"`
- **Image-dominant slides** (full-width image): `ai_size="1536x1024"` landscape, prompt suffix uses `"16:9 aspect ratio"`

### Sub-slides and navigation
- When a block contains multiple sub-slides separated by `st_slide_break()`, the first `st_write()` after each break MUST have `toc_lvl="2"` to enable keyboard navigation via `auto_marker_on_toc`
- In `SlideBreakMode.HIDDEN`, the slide break itself produces no marker — navigation relies entirely on `toc_lvl`

## Patterns

### table-roadmap

A responsive multi-column table with individually bordered and colored cells,
vertically and horizontally centered content, and row-level active/inactive styling.
Suitable for schedules, roadmaps, comparison tables, feature matrices.

#### Layout
- Grid: `repeat(auto-fit, minmax(250px, 1fr))` — fully responsive, columns stack on narrow screens
- Gap: `12px`
- One `st_grid` per row — each row is an independent grid (allows per-row active styling)

#### Cell styling (MANDATORY pattern)
- Pass cell styles via `cell_styles=` parameter on `st_grid` — never via `st_block()` wrappers
- Use `g.cell()` context manager for each cell — never bare `st_block()` inside a grid
- Compose cell style with:
  - Background: semi-transparent tinted color (`rgba(...)`)
  - Border: visible, rounded (`border-radius: 10px`)
  - Centering: `s.container.layouts.vertical_center_layout + s.center_txt`
  - Padding: `8px 12px`

```python
cell_style = Style.create(
    ns("background-color: rgba(122, 184, 245, 0.08); "
       "border: 1px solid rgba(122, 184, 245, 0.3); "
       "border-radius: 10px; padding: 8px 12px;", "cell_bg")
    + s.container.layouts.vertical_center_layout
    + s.center_txt,
    "my_cell",
)
```

#### Active row variant
- Amber tinted background: `rgba(243, 156, 18, 0.15)`
- Amber border: `2px solid #F39C12`
- Text color: `s.project.colors.highlight`

#### Text styling
- Font size: `s.Large` (48pt) for all columns — uniform size
- First column (label): bold + primary/highlight color
- Other columns: normal weight
- Hyphens: `s.text.wrap.hyphens` on all text — long words break cleanly

#### Usage template

```python
with st_grid(
    cols="repeat(auto-fit, minmax(250px, 1fr))",
    gap="12px",
    cell_styles=cell_style,
) as g:
    with g.cell():
        st_write(label_style, "Row label")
    with g.cell():
        st_write(content_style, "Column 2")
    with g.cell():
        st_write(content_style, "Column 3")
```

## Citation Rules

All factual claims, statistics, and attributions MUST be traceable to a verifiable source.

### Bibliography system (MANDATORY for all modules)

All modules MUST use the StreamTeX bibliography system (`cite()` + `st_bibliography()`), not manual `link=` on `st_write()`.

#### Setup (book.py)

```python
from streamtex.bib import BibConfig, BibFormat, CitationStyle, set_bib_config

set_bib_config(BibConfig(
    format=BibFormat.APA,
    citation_style=CitationStyle.AUTHOR_YEAR,
    hover_enabled=True,
    hover_show_abstract=True,
    sort_by="author",
))

st_book(
    [...],
    bib_sources=[str(_module_dir / "static" / "references.bib")],
)
```

#### .bib file (static/references.bib)

Every module MUST have a `static/references.bib` with BibTeX entries for all cited sources.

#### Inline citation in blocks

```python
from streamtex.bib import cite

# REF: https://arxiv.org/abs/2404.18353
st_write(bs.source, cite("tihanyi2024formai"))
```

- `cite("key")` renders as clickable `(Author, Year)` with hover preview
- Use `bs.source` style (muted, small font) for the citation line
- `# REF:` comment MUST appear above for source code traceability
- The finding text stays in a separate `st_write(bs.body, ...)` — never merge citation and finding in one call

#### Bibliography block

Each module MUST render `st_bibliography()` in the glossary or a dedicated references block:

```python
from streamtex.bib import st_bibliography

st_bibliography(
    title="References",
    title_style=bs.heading,
    entry_style=s.large,
    toc_lvl="1",
    only_cited=True,
)
```

### Traceability rules

1. Every statistic (percentage, date, projection) MUST have a `# REF:` comment in the block source
2. Every `# REF:` comment MUST have a corresponding entry in `static/references.bib`
3. Every .bib entry MUST have a valid `url` field (verified per scientific-excellence.md)
4. Projections and future claims MUST specify the source and year
5. Historical facts MUST cite the primary source
