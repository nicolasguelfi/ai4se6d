"""Slide — Compound: The Knowledge Flywheel."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


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
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.heading, "Compound: The Knowledge Flywheel", tag=t.div, toc_lvl="1")
        st_space("v", 1)

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
