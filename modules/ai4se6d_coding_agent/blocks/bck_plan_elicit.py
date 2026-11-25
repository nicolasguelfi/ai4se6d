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

_CODE_ZOOM = 104  # code readable in the room; tuned by measure so the slide fills one screen (NG, 2026-11-24)

_PROMPT = """\
I'm building CalcApp v0.1, a personal budget tracker.
v0.1: add an expense (amount, category, date), list expenses with a
monthly total, two pages with navigation, data kept in the browser
after closing it (localStorage, no server).
My extra ideas: a monthly budget limit, CSV export.
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
     "It gives the context (the v0.1 scope; AGENTS.md is already loaded by opencode, no @ needed), asks for 3 clarifying questions FIRST, then for 4-6 "
     "user stories with a title, « As a user, I want... » and testable acceptance criteria."),
    ("User story",
     "Agile origin (XP, then Scrum): one need seen by the user, « As a user, I want … », plus acceptance criteria "
     "= how we check it is done. Used lightly today (no backlog, no estimates); the full notion (INVEST, backlog) "
     "comes on day 3, GenSem."),
    ("The trap",
     "Accepting the stories as they come. Read critically and ask back: what happens on errors? fixed or free "
     "categories? which currency?"),
    ("Link to what follows",
     "The stories are split into atomic tasks, then written to docs/plan.md."),
    ("Ask the room",
     "« Which question did the agent ask you that you had not thought of? »"),
    # Command recap: every command and option of the slide, in plain words (NG, 2026-11-24)
    ("Key — Shift+Tab",
     "In opencode, hold Shift and press Tab: it switches to the next primary agent (plan → build → plan). The "
     "active agent's name is shown near the prompt box. « Shift+Tab → plan » = press it until plan is shown."),
    ("Prompt — the elicitation prompt",
     "Lines 1-4 give the context: the v0.1 scope, the need in user words, the technique in brackets. No "
     "@AGENTS.md: opencode loads AGENTS.md on its own at the start and again whenever it changes. « My extra "
     "ideas: » — replace the two examples with your own 2-3 ideas. « Ask me 3 clarifying questions first » = no answer "
     "before your replies. Then 4-6 user stories, each with a title, « As a user, I want… » and testable "
     "acceptance criteria."),
    ("Word — localStorage",
     "Storage inside the browser, on this computer: the data survives a reload or closing the browser, with no "
     "server. Not cookies: cookies travel to a server with every request."),
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
        with st_zoom(120):
            st_write(bs.body, (bs.keyword, "Shift+Tab → plan"), ", then adapt and paste:", tag=t.div)
        st_space("v", "2vh")
        with st_zoom(_CODE_ZOOM):
            st_code(s.none, code=_PROMPT, language="text", line_numbers=False, font_size="30pt")
        st_space("v", "1.5vh")
        with st_zoom(100):  # first time the word appears in the course: define it (NG, 2026-11-25)
            st_write(bs.body, (bs.keyword, "User story"), " = one need seen by the user: “As a user, I want …” + "
                     "acceptance criteria (how we check it is done).", tag=t.div)
        st_space("v", "1.5vh")
        with st_zoom(105):
            st_write(bs.body, "Read critically. Ask back: errors? fixed or free categories? currency?", tag=t.div)
