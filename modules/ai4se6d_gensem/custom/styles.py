"""Presentation styles — optimised for live projection at 10-20m distance.

Usage in blocks:
    from custom.styles import Styles as s
    st_write(s.project.titles.slide_title, "My Title")
    st_write(s.project.titles.heading, "Section heading")
    st_write(s.project.titles.keyword, (s.project.titles.keyword, "Bold"), " normal")

Font size hierarchy (projection-safe):
    slide_title   — 96pt   — one per slide (via theme override)
    section_title — 80pt   — section headers (via theme override)
    subtitle      — 48pt   — slide subtitles
    body          — 48pt   — all readable content
    caption       — 32pt   — sources, attributions only
    table text    — 36pt   — grid cells
"""

from streamtex.styles import Container, StxStyles, Style, Text

# Explicit projection-safe sizes (do NOT rely on CSS variable defaults)
_pt48 = Style("font-size: 48pt;", "_pt48")
_pt32 = Style("font-size: 32pt;", "_pt32")


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
        ColorsCustom.highlight + Text.weights.bold_weight + _pt48,
        "subtitle"
    )
    body = Style.create(
        _pt48,
        "body"
    )
    body_accent = Style.create(
        ColorsCustom.accent + Text.weights.bold_weight + _pt48,
        "body_accent"
    )
    caption = Style.create(
        ColorsCustom.muted + _pt32,
        "caption"
    )

    # Factored block styles (used in 2+ blocks — MUST be defined here, not in BlockStyles)
    heading = Style.create(
        ColorsCustom.primary + Text.weights.bold_weight + Text.sizes.Huge_size
        + StxStyles.center_txt,
        "heading"
    )
    keyword = Style.create(
        Text.weights.bold_weight + ColorsCustom.accent + _pt48,
        "keyword"
    )
    label = Style.create(
        Text.weights.bold_weight + ColorsCustom.primary + _pt48,
        "label"
    )
    stat = Style.create(
        Text.weights.bold_weight + ColorsCustom.highlight + _pt48,
        "stat"
    )
    source = Style.create(
        ColorsCustom.muted + _pt32 + StxStyles.center_txt,
        "source"
    )

    # Table-roadmap text styles
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

    # Table-roadmap cell backgrounds
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

    # Grid cell centering
    grid_cell_centered = Style.create(
        Container.layouts.vertical_center_layout + StxStyles.center_txt,
        "grid_cell_centered",
    )

    # Table-roadmap composed cell styles
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

    # Viewport-filling page layouts
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


class Custom:
    """Aggregation class for all presentation-specific styles."""
    colors = ColorsCustom
    backgrounds = BackgroundsCustom
    titles = TextStylesCustom
    containers = ContainerStylesCustom


class Styles(StxStyles):
    """Main Styles class — inherits all StreamTeX styles + presentation overrides."""
    project = Custom
