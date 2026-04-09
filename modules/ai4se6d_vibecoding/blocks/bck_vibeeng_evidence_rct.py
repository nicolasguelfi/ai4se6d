"""Slide — The Copilot Effect: what the largest RCT tells us."""
# @guideline: maximize-viewport
# @pattern: stat-hero
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s

class BlockStyles:
    """Copilot RCT stat-hero styles."""
    heading = s.project.titles.slide_title + s.center_txt
    stat = s.project.titles.stat_hero_primary
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.primary
    keyword_accent = s.bold + s.project.colors.accent
    keyword_warn = s.bold + s.project.colors.highlight
    source = s.project.citation + s.large + s.center_txt
    transition = Style.create(
        s.Large + s.italic + s.center_txt + s.project.colors.muted,
        "ve_evidence_rct_transition",
    )
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(bs.heading, "The Copilot Effect", tag=t.div, toc_lvl="1")
            st_space("v", 2)

            with st_grid(
                cols="1fr 1fr",
                gap="32px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    st_write(bs.stat, "+55.8%")
                    st_space("v", 0.5)
                    st_write(
                        bs.body,
                        "faster on ",
                        (bs.keyword, "simple tasks"),
                    )
                    st_space("v", 0.5)
                    # REF: Peng et al. 2023, arXiv 2302.06590
                    st_write(bs.source, cite("peng-copilot2023"))

                with g.cell():
                    st_write(bs.stat, "\u221219%")
                    st_space("v", 0.5)
                    st_write(
                        bs.body,
                        "slower on ",
                        (bs.keyword_warn, "real projects"),
                    )
                    st_space("v", 0.5)
                    # REF: METR 2025
                    st_write(bs.source, cite("metr-aitools2025"))

            st_space("v", 2)
            with st_zoom(150):
                st_write(
                    bs.body,
                    "The difference? ",
                    (bs.keyword_accent, "Complexity"),
                    " and ",
                    (bs.keyword_accent, "discipline"),
                    ".",
                )
            st_space("v", 1)
            st_write(bs.transition, "Who benefits the most? \u2192")
