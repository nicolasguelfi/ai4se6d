"""Slide — The FreeSelfApp challenge: a small personal web app, by prompting only."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Challenge slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    label = s.project.titles.label
    keyword = s.bold + s.project.colors.accent
    warn = s.bold + s.project.colors.highlight
    caption = Style.create(s.project.titles.caption + s.center_txt, "setup_challenge_caption")
bs = BlockStyles

_NOTES = [
    ("The message",
     "The FreeSelfApp challenge: a small personal web app that runs in a browser, built by typing prompts, "
     "not code."),
    ("Any stack",
     "Participants choose; HTML + JS is the simplest because it opens in the browser with nothing to install."),
    ("No rules, no plan — on purpose",
     "Today they FEEL vibe coding: no requirements, no tests, no review. The surprises and breakages are the "
     "material of the 16:15 debrief."),
    ("Link to tomorrow",
     "« Today you feel vibe coding. Tomorrow you engineer it. » Day 2 takes the same loop on CalcApp, with git, "
     "a plan and an AI code review."),
    ("Ask the room",
     "« Who already has an idea for their app? »"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "The Challenge", tag=t.div, toc_lvl="1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — The Challenge", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "2vh")

        items = [
            ("It ", (bs.keyword, "runs in a browser")),
            ((bs.keyword, "Any stack"), " — HTML + JS is simplest"),
            ((bs.warn, "No rules, no plan"), " — on purpose"),
            ("You type ", (bs.keyword, "prompts"), ", not code"),
        ]
        # One row per rule of the game, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
        cols = "5% 90% 5%"
        cells = s.project.containers.rows(len(items), cols, filled=(2,))
        with st_zoom(110):
            with st_grid(cols=cols, cell_styles=s.project.containers.row_cell_left) as g:
                with g.cell():
                    pass
                with g.cell():
                    st_write(bs.body, (bs.label, "Goal: "), "a small personal web app.", tag=t.div)
                with g.cell():
                    pass
            st_space("v", "3vh")
            with st_grid(cols=cols, gap="6vh 0.5vw", cell_styles=cells) as g:
                for parts in items:
                    with g.cell():
                        pass  # left margin
                    with g.cell():
                        st_write(bs.body, *parts, tag=t.div)
                    with g.cell():
                        pass  # right margin
            st_space("v", "5vh")
            st_write(bs.caption, "Today you feel vibe coding. Tomorrow you engineer it.", tag=t.div)
