"""Slide — Eliciting requirements with the plan agent (starter prompt)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Elicitation styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.center_txt, "elicit_body")
    keyword = s.project.titles.keyword
bs = BlockStyles

_PROMPT = """\
I'm building CalcApp v0.1, a personal budget tracker (see @AGENTS.md).
v0.1: add an expense (amount, category, date), list expenses with a
monthly total, two pages with navigation, data kept in localStorage.
My extra ideas: <yours>.
Ask me 3 clarifying questions first. Then propose 4-6 user stories:
title, "As a user, I want...", testable acceptance criteria."""

_NOTES = [
    ("Trainer action",
     "Read and comment — nothing to type yet. Explain the elicitation prompt; learners paste it into the plan "
     "agent in the plan exercise (step 2, about 11:05)."),
    ("The message",
     "Requirements come from a conversation, not from one shot: switch to the plan agent (Shift+Tab → plan), "
     "adapt the prompt with your own ideas, paste it."),
    ("How the prompt works",
     "It gives the context (@AGENTS.md, the v0.1 scope), asks for 3 clarifying questions FIRST, then for 4-6 "
     "user stories with a title, « As a user, I want... » and testable acceptance criteria."),
    ("The trap",
     "Accepting the stories as they come. Read critically and ask back: what happens on errors? fixed or free "
     "categories? which currency?"),
    ("Link to what follows",
     "The stories are split into atomic tasks, then written to docs/plan.md."),
    ("Ask the room",
     "« Which question did the agent ask you that you had not thought of? »"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "Elicit with the Plan Agent", tag=t.div, toc_lvl="+1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Elicit with the Plan Agent", entries=_NOTES,
                                 position="left", width="50vw")
        with st_zoom(169):
            st_write(bs.body, (bs.keyword, "Shift+Tab → plan"), ", then adapt and paste:", tag=t.div)
        st_space("v", "3vh")
        st_code(s.none, code=_PROMPT, language="text", line_numbers=False, font_size="30pt")
        st_space("v", "2vh")
        with st_zoom(169):
            st_write(bs.body, "Read critically. Ask back: errors? fixed or free categories? currency?", tag=t.div)
