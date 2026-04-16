"""Slide — Compound: The Knowledge Flywheel."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Compound flywheel slide styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    stat = s.project.titles.stat
    label = s.project.titles.label
    closing = s.project.titles.body + s.project.colors.highlight + s.bold

bs = BlockStyles

_CYCLES = [
    ("Cycle 1:", " 0 rules", " \u2192 brainstorm produces first patterns"),
    ("Cycle 3:", " 10 rules", " \u2192 AI follows project conventions, fewer corrections"),
    ("Cycle 5:", " 25 rules", " \u2192 AI generates correct code 80%+ on first attempt"),
    ("Cycle 10:", " 50+ rules", " \u2192 project is self-documenting, onboarding takes hours not weeks"),
]


def build():
    st_marker("Knowledge Flywheel (0→50+ rules)")
    with st_block(s.project.containers.page_fill_top):
        with st_grid(
            cols="95% 5%",
            gap="0px",
            cell_styles=s.project.containers.grid_cell_centered,
        ) as g:
            with g.cell():
                with st_zoom(90):
                    st_write(bs.heading, "Compound: The Knowledge Flywheel", tag=t.div, toc_lvl="+1")
            with g.cell():
                st_hover_tooltip(
                    title="The Knowledge Flywheel",
                    entries=[
                        ("Flywheel effect", "Each cycle adds rules that make the next cycle faster -- 0 to 50+ rules over 10 cycles."),
                        ("Why GSE-One is different", "Most AI workflows are stateless. GSE-One accumulates project intelligence across sessions."),
                        ("Compound interest", "Like financial compounding: small consistent improvements yield exponential long-term gains."),
                    ],
                    scale="2vw", width="70vw", position="left",
                )
        st_space("v", 1)

        with st_zoom(120):
            with st_grid(
                cols="1fr",
                gap="12px",
                cell_styles=s.project.containers.cell_primary_bg
                + s.project.containers.cell_pad_md,
            ) as g:
                for cycle, rules, outcome in _CYCLES:
                    with g.cell():
                        st_write(
                            bs.body,
                            (bs.label, cycle),
                            (bs.stat, rules),
                            outcome,
                        )

            st_space("v", 1)

            with st_block(s.project.containers.callout):
                st_write(
                    bs.closing,
                    "Each cycle makes the next one faster. "
                    "This is the compound interest of engineering.",
                )
