"""Slide — Why this matters: the junior developer analogy."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Analogy styles."""
    heading = s.project.titles.heading
    quote = Style.create(s.project.titles.body + s.italic + s.center_txt, "ocwhy_quote")
    body = Style.create(s.project.titles.body + s.center_txt, "ocwhy_body")
    punch = Style.create(s.project.titles.body_accent + s.center_txt, "ocwhy_punch")
bs = BlockStyles

_NOTES = [
    ("The message",
     "The agent is only as good as the context you give it. This slide opens the opencode part: everything after "
     "it is about giving the agent the right context."),
    ("The analogy",
     "A talented junior with no README, no coding standards and no architecture notes writes good code — in the "
     "wrong folder, with the wrong conventions. The agent behaves the same way."),
    ("The trap",
     "Blaming the model when the answer misses the project's conventions. Most of the time the conventions were "
     "never written down where the agent can read them."),
    ("What comes next",
     "Project structure, AGENTS.md, the context window and @file mentions: four ways to hand the agent what the "
     "junior was missing."),
    ("Ask the room",
     "« What would you give a new colleague on their first day so their code fits the project? »"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(75):
                st_write(bs.heading, "Why This Matters", tag=t.div, toc_lvl="+1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Why This Matters", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "8vh")
        with st_zoom(115):
            with st_block(s.project.containers.callout):
                st_write(
                    bs.quote,
                    "You hire a talented junior. No README, no coding standards, no architecture notes. "
                    "How well will they do?", tag=t.div,
                )
            st_space("v", "5vh")
            st_write(bs.body, "Good code — in the wrong folder, with the wrong conventions.", tag=t.div)
            st_space("v", "5vh")
            st_write(bs.punch, "The agent is only as good as the context you give it.", tag=t.div)
