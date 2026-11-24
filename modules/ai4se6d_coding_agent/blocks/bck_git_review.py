"""Slide — Pattern 1: review before stage."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Review-before-stage styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    number = Style.create(s.project.titles.body + s.bold + s.project.colors.highlight, "gitrev_number")
    closing = Style.create(s.project.titles.body_accent + s.center_txt, "gitrev_closing")
bs = BlockStyles

_STEPS = [
    ((bs.keyword, "git status"), " — which files did the agent touch?"),
    ((bs.keyword, "git diff"), " — read every change"),
    ((bs.keyword, "git add src/App.tsx"), " — only what you approve"),
    ((bs.keyword, "git diff --staged"), " — last look"),
    ((bs.keyword, "git commit"), " — a message that says what and why"),
]

_NOTES = [
    ("The message",
     "First habit of the day: nothing the agent wrote goes into a commit before you have read it."),
    ("The five steps",
     "git status (which files), git diff (every change), git add src/App.tsx (one file, e.g.: only what you approve), "
     "git diff --staged (last look), git commit (what and why)."),
    ("The key step",
     "Step 2: the diff IS your review. Skipping it means committing code nobody has read."),
    ("The trap",
     "git add . after the agent worked: it stages everything, including changes you never saw."),
    ("Link to the afternoon",
     "The code review session (14:30) builds on the same reflex, with the AI helping to read the diff."),
    ("Ask the room",
     "« What would you do if git status shows a file you did not expect? »"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "1 · Review Before Stage", tag=t.div, toc_lvl="+1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Review Before Stage", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "3vh")

        # one numbered row per step, alternating fills — motif L2 + fonds f1 (margins 5 %, numbering column)
        cols = "5% 5% 85% 5%"
        cells = s.project.containers.rows(len(_STEPS), cols, filled=(2, 3))
        with st_zoom(114), st_grid(cols=cols, gap="4.5vh 0.5vw", cell_styles=cells) as g:
            for n, step in enumerate(_STEPS, 1):
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.number, f"{n}", tag=t.div)
                with g.cell():
                    st_write(bs.body, *step, tag=t.div)
                with g.cell():
                    pass  # right margin
        st_space("v", "5vh")
        with st_zoom(126):
            st_write(bs.closing, "Never skip step 2: the diff is your review.", tag=t.div)
