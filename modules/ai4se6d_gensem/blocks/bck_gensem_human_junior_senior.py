"""Slide — Junior vs Senior: The Contradictions (3 studies)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Junior/senior comparison styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    stat = s.project.titles.stat
    card_title = s.bold + s.project.colors.primary + s.Large + s.center_txt
    card_sub = s.project.titles.caption + s.center_txt
    source = s.project.citation + s.large + s.center_txt
    takeaway = s.project.titles.body_accent + s.center_txt

bs = BlockStyles


_STUDIES = [
    (
        "Cui et al.",
        "4,867 devs, enterprise",
        s.project.containers.cell_primary_bg,
        "Juniors +27-39%, Seniors +8-13%",
    ),
    (
        "METR",
        "16 devs, OSS",
        s.project.containers.cell_accent_bg,
        "Seniors -19% slower on familiar code",
    ),
    (
        "Daniotti",
        "160K GitHub devs",
        s.project.containers.cell_active_bg,
        "Seniors capture ALL gains, juniors ZERO",
    ),
]


def build():
    st_marker("Junior vs Senior Impact")
    with st_block(s.project.containers.page_fill_top):
        with st_grid(
            cols="95% 5%",
            gap="0px",
            cell_styles=s.project.containers.grid_cell_centered,
        ) as g:
            with g.cell():
                with st_zoom(90):
                    st_write(bs.heading, "Junior vs Senior: The Contradictions", tag=t.div, toc_lvl="+1")
            with g.cell():
                st_hover_tooltip(
                    title="Junior vs Senior in AI-Assisted Development",
                    entries=[
                        ("Cui et al.", "Enterprise study: juniors gain +27-39%, seniors only +8-13%."),
                        ("METR", "OSS study: seniors actually -19% slower on familiar code with AI."),
                        ("Daniotti", "GitHub study: seniors capture ALL gains, juniors zero."),
                        ("GSE-One link", "Structured process helps juniors bridge the gap; without it, experience dominates."),
                    ],
                    scale="2vw", width="70vw", position="left",
                )
        st_space("v", 1)

        with st_zoom(120):
            with st_grid(
                cols="repeat(auto-fit, minmax(280px, 1fr))",
                gap="24px",
                cell_styles=s.project.containers.cell_pad_md,
            ) as g:
                for name, scope, bg, finding in _STUDIES:
                    with g.cell():
                        with st_block(bg + s.project.containers.cell_pad_md):
                            st_write(bs.card_title, name, tag=t.div)
                            st_write(bs.card_sub, scope)
                            st_space("v", 1)
                            st_write(bs.body, finding)

            st_space("v", 1)
            st_write(
                bs.takeaway,
                "The relationship is more nuanced than any single study suggests.",
            )
            st_space("v", 1)
            st_write(bs.source, cite("cui-fieldexperiments2024"))
            st_write(bs.source, cite("metr2025"))
            st_write(bs.source, cite("daniotti-github2025"))
