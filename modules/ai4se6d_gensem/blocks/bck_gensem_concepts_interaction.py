"""Slide — Layer 1: Interaction (C1-C3)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Interaction layer styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    card_title = s.bold + s.project.colors.primary + s.Large + s.center_txt
    takeaway = s.project.titles.body_accent + s.center_txt

bs = BlockStyles


_CONCEPTS = [
    ("C1 \u2014 Inline Completion", "Autocomplete on steroids: real-time suggestions as you type."),
    ("C2 \u2014 Chat", "Multi-turn dialogue: ask, refine, iterate with the model."),
    ("C3 \u2014 Agent Mode", "Autonomous multi-step execution: plan, execute, verify."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.heading, "Layer 1: Interaction (C1-C3)", tag=t.div, toc_lvl="1")
        st_space("v", 1)

        with st_grid(
            cols="repeat(auto-fit, minmax(280px, 1fr))",
            gap="24px",
            cell_styles=s.project.containers.cell_primary_bg
            + s.project.containers.cell_pad_md,
        ) as g:
            for title, desc in _CONCEPTS:
                with g.cell():
                    st_write(bs.card_title, title, tag=t.div)
                    st_space("v", 1)
                    st_write(bs.body, desc)

        st_space("v", 2)
        st_write(
            bs.takeaway,
            "The continuum of autonomy: suggestion \u2192 conversation \u2192 delegation.",
        )
