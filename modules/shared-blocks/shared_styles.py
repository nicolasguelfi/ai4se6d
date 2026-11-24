"""Shared presentation styles — single source of truth for all ai4se6d modules.

Optimised for live projection at 10-20m distance.

Usage in blocks:
    from custom.styles import Styles as s
    st_write(s.project.titles.slide_title, "My Title")
    st_write(s.project.colors.primary, "Highlighted text")
    st_write(s.project.citation + s.large, cite("author2024"))

Font size hierarchy (projection-safe):
    slide_title   — 96pt (Huge)   — one per slide
    section_title — 80pt (huge)   — section headers
    subtitle      — 48pt (Large)  — slide subtitles
    body          — 48pt (Large)  — all readable content
    caption       — 32pt (large)  — sources, attributions only
    table text    — 36pt (pt36)   — grid cells
"""

from streamtex.styles import Container, StxStyles, Style, Text

# Line spacing of 48pt (Large) text — one place for the whole project (NG, 2026-11-22: line spacing
# too large on almost every slide). s.text.leading comes from streamtex#158
# (https://github.com/nicolasguelfi/streamtex/issues/158), shipped in streamtex 0.7.85.
_LARGE = Text.sizes.Large_size + Text.leading.snug   # 48pt, line-height 1.25


class ColorsCustom:
    """Presentation text colors — high contrast only."""
    primary = Style("color: #7AB8F5;", "primary")
    accent = Style("color: #2EC4B6;", "accent")
    highlight = Style("color: #F39C12;", "highlight")
    success = Style("color: #27AE60;", "success")
    muted = Style("color: #95A5A6;", "muted")
    critical = Style("color: #E74C3C;", "critical")


class BackgroundsCustom:
    """Presentation backgrounds."""
    callout_bg = Style("background-color: rgba(122, 184, 245, 0.12);", "callout_bg")


class TextStylesCustom:
    """Presentation title hierarchy — large fonts for projection."""
    slide_title = Style.create(
        ColorsCustom.primary + Text.weights.bold_weight + Text.sizes.Huge_size,
        "slide_title"
    )
    section_title = Style.create(
        ColorsCustom.accent + Text.weights.bold_weight + Text.sizes.huge_size,
        "section_title"
    )
    subtitle = Style.create(
        ColorsCustom.highlight + Text.weights.bold_weight + _LARGE,
        "subtitle"
    )
    body = Style.create(
        _LARGE,
        "body"
    )
    body_accent = Style.create(
        ColorsCustom.accent + Text.weights.bold_weight + _LARGE,
        "body_accent"
    )
    caption = Style.create(
        ColorsCustom.muted + Text.sizes.large_size,
        "caption"
    )

    # Factored block styles (used in 2+ blocks — define here, not in BlockStyles)
    heading = Style.create(
        ColorsCustom.primary + Text.weights.bold_weight + Text.sizes.Huge_size
        + StxStyles.center_txt,
        "heading"
    )
    keyword = Style.create(
        Text.weights.bold_weight + ColorsCustom.accent + _LARGE,
        "keyword"
    )
    label = Style.create(
        Text.weights.bold_weight + ColorsCustom.primary + _LARGE,
        "label"
    )
    stat = Style.create(
        Text.weights.bold_weight + ColorsCustom.highlight + _LARGE,
        "stat"
    )

    # Stat-hero variants — giant centered stats for keynote/billboard slides
    stat_hero = Style.create(
        Text.sizes.GIANT_size + Text.weights.bold_weight
        + ColorsCustom.highlight + StxStyles.center_txt,
        "stat_hero",
    )
    stat_hero_primary = Style.create(
        Text.sizes.GIANT_size + Text.weights.bold_weight
        + ColorsCustom.primary + StxStyles.center_txt,
        "stat_hero_primary",
    )
    stat_hero_critical = Style.create(
        Text.sizes.GIANT_size + Text.weights.bold_weight
        + ColorsCustom.critical + StxStyles.center_txt,
        "stat_hero_critical",
    )

    # Table-roadmap text styles (shared across comparison/spectrum tables)
    table_header = Style.create(
        Text.sizes.pt36 + Text.weights.bold_weight + ColorsCustom.accent + Text.wrap.hyphens,
        "table_header",
    )
    table_cell = Style.create(
        Text.sizes.pt36 + Text.wrap.hyphens,
        "table_cell",
    )
    table_label = Style.create(
        Text.sizes.pt36 + Text.weights.bold_weight + ColorsCustom.primary + Text.wrap.hyphens,
        "table_label",
    )
    table_label_active = Style.create(
        Text.sizes.pt36 + Text.weights.bold_weight + ColorsCustom.highlight + Text.wrap.hyphens,
        "table_label_active",
    )


class ContainerStylesCustom:
    """Presentation containers."""
    callout = Style.create(
        BackgroundsCustom.callout_bg
        + Container.borders.solid_border
        + Style("border-color: #7AB8F5; border-width: 0 0 0 4px;", "callout_border")
        + Container.paddings.medium_padding,
        "callout"
    )

    # Responsive grid presets
    responsive_2col = "repeat(auto-fit, minmax(350px, 1fr))"

    # Layout gaps
    gap_32 = Style("gap: 32px;", "gap_32")
    gap_24 = Style("gap: 24px;", "gap_24")

    # Table-roadmap cell backgrounds (shared across grid blocks)
    cell_primary_bg = Style(
        "background-color: rgba(122, 184, 245, 0.08); "
        "border: 1px solid rgba(122, 184, 245, 0.3); "
        "border-radius: 10px;",
        "cell_primary_bg",
    )
    cell_active_bg = Style(
        "background-color: rgba(243, 156, 18, 0.15); "
        "border: 2px solid #F39C12; "
        "border-radius: 10px;",
        "cell_active_bg",
    )
    cell_accent_bg = Style(
        "background-color: rgba(46, 196, 182, 0.2); "
        "border: 1px solid rgba(46, 196, 182, 0.5); "
        "border-radius: 10px;",
        "cell_accent_bg",
    )
    cell_pad_sm = Style("padding: 8px 12px;", "cell_pad_sm")
    cell_pad_md = Style("padding: 12px 16px;", "cell_pad_md")

    # Alternating row fills — motif « lignes-alternées » (L2 + fonds f1) of streamtex-all-trainings
    # (_project/MOTIFS.md §2; trainings_pack palette row_1/row_2, _base.make_rows). NG, 2026-11-22.
    # Neutral fills, so the text keeps its own colours. Usage in a block:
    #     cols = "5% 90% 5%"; cells = s.project.containers.rows(len(ITEMS), cols, filled=(2,))
    #     with st_grid(cols=cols, gap="2vh 1vw", cell_styles=cells) as g: ...
    row_fill_1 = Style("background-color: #1F2531; padding: 0.3vh 1vw; border-radius: 0.6vw;", "row_fill_1")
    row_fill_2 = Style("background-color: #2A3242; padding: 0.3vh 1vw; border-radius: 0.6vw;", "row_fill_2")
    row_cell_left = Style.create(Container.layouts.vertical_center_layout + Style("text-align: left;", "txt_left_rows"),
                                 "row_cell_left")

    @staticmethod
    def rows(n_rows, cols, filled=(2,), fills=None, base=None):
        """Cell styles of a grid with ALTERNATING ROW FILLS, row after row: row i takes fills[i % len(fills)]
        on the `filled` columns (numbered from 1); the other columns stay plain (margins)."""
        ncols = len(cols.split()) if isinstance(cols, str) else int(cols)
        fills = fills or (ContainerStylesCustom.row_fill_1, ContainerStylesCustom.row_fill_2)
        base = base or ContainerStylesCustom.row_cell_left
        return [base + fills[i % len(fills)] if j + 1 in filled else base
                for i in range(n_rows) for j in range(ncols)]

    # Grid cell centering (shared across all balanced/grid blocks)
    grid_cell_centered = Style.create(
        Container.layouts.vertical_center_layout + StxStyles.center_txt,
        "grid_cell_centered",
    )

    # Table-roadmap composed cell styles (shared across comparison/spectrum tables)
    table_header_cell = Style.create(
        cell_accent_bg + cell_pad_sm
        + Container.layouts.vertical_center_layout + StxStyles.center_txt,
        "table_header_cell",
    )
    table_normal_cell = Style.create(
        cell_primary_bg + cell_pad_sm
        + Container.layouts.vertical_center_layout + StxStyles.center_txt,
        "table_normal_cell",
    )
    table_active_cell = Style.create(
        cell_active_bg + cell_pad_sm
        + Container.layouts.vertical_center_layout + StxStyles.center_txt,
        "table_active_cell",
    )

    # Viewport-filling page layouts (shared across all blocks)
    page_fill_top = Style(
        "display:flex;flex-direction:column;justify-content:flex-start;"
        "min-height:85vh;gap:1.5rem;",
        "page_fill_top",
    )
    page_fill_center = Style(
        "display:flex;flex-direction:column;justify-content:center;"
        "align-items:center;min-height:85vh;gap:1.5rem;",
        "page_fill_center",
    )
    page_fill_center_wide = Style(
        "display:flex;flex-direction:column;justify-content:center;"
        "align-items:center;min-height:85vh;gap:2rem;",
        "page_fill_center_wide",
    )
    page_fill_center_noalign = Style(
        "display:flex;flex-direction:column;justify-content:center;"
        "min-height:85vh;gap:2rem;",
        "page_fill_center_noalign",
    )


class DiagramTone:
    """Styles of ONE colour of a native diagram (NG, 2026-11-24: diagrams drawn with StreamTeX instead of PNGs).

    Usage: blue = s.project.tone("122, 184, 245", "#7AB8F5", "blue") then blue.card, blue.title, blue.fg,
    blue.chip, blue.dot, blue.line. Same key = same CSS class, so a colour can be shared by several blocks.
    """

    def __init__(self, rgb, hexa, key):
        self.fg = Style(f"color: {hexa};", f"tone_fg_{key}")
        self.card = Style.create(
            Style(f"background-color: rgba({rgb}, 0.13); border: 3px solid {hexa}; border-radius: 16px; "
                  "padding: 2.5vh 0.8vw; box-sizing: border-box;", f"tone_card_{key}")
            + Container.layouts.vertical_center_layout + StxStyles.center_txt,
            f"tone_card_{key}_c",
        )
        self.title = Style.create(TextStylesCustom.table_label + StxStyles.bold + self.fg, f"tone_title_{key}")
        self.chip = Style(f"background-color: rgba({rgb}, 0.28); border-radius: 8px; padding: 2px 10px; "
                          "margin: 3px 4px; white-space: nowrap; display: inline-block;", f"tone_chip_{key}")
        self.dot = Style(f"background-color: {hexa}; border-radius: 50%; padding: 4px 12px; margin: 0 3px; "
                         "font-weight: bold; display: inline-block;", f"tone_dot_{key}")
        self.line = Style(f"background-color: {hexa}; height: 8px; border-radius: 4px; width: 100%;",
                          f"tone_line_{key}")


# The four diagram colours of the course (blue, amber, green, purple)
TONE_BLUE = DiagramTone("122, 184, 245", "#7AB8F5", "blue")
TONE_AMBER = DiagramTone("243, 156, 18", "#F39C12", "amber")
TONE_GREEN = DiagramTone("39, 174, 96", "#27AE60", "green")
TONE_PURPLE = DiagramTone("155, 89, 182", "#B07CD8", "purple")


class Custom:
    """Aggregation class for all presentation-specific styles."""
    colors = ColorsCustom
    backgrounds = BackgroundsCustom
    titles = TextStylesCustom
    containers = ContainerStylesCustom
    tone = DiagramTone
    tone_blue, tone_amber, tone_green, tone_purple = TONE_BLUE, TONE_AMBER, TONE_GREEN, TONE_PURPLE
    citation = Style("color: #81C784; font-style: italic;", "citation")


class Styles(StxStyles):
    """Main Styles class — inherits all StreamTeX styles + presentation overrides."""
    project = Custom
    # s.Large carries the project's line spacing too (211 blocks write s.Large directly).
    Large = Style.create(_LARGE, "Large_snug")
