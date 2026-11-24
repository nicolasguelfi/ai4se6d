"""Slide — Git debrief (5 min)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Debrief styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    number = Style.create(s.project.titles.body + s.bold + s.project.colors.highlight, "gitdeb_number")
    pair = Style.create(s.project.titles.body_accent + s.center_txt, "gitdeb_pair")
bs = BlockStyles

_QUESTIONS = [
    ("What did ", (bs.keyword, "git diff"), " show when you broke the file — and after ",
     (bs.keyword, "git restore"), "?"),
    ("The agent just edited 5 files. Which command do you run first, and why?",),
]

_NOTES = [
    ("Trainer action",
     "Learners do it — in pairs, on their machine. Ask the two questions, then neighbours compare their git log "
     "--oneline."),
    ("The message",
     "Five minutes to fix the reflex: see the change, then decide to keep it or throw it away."),
    ("Question 1",
     "Expected: git diff showed the broken lines; after git restore the diff is empty and the tests are green "
     "again."),
    ("Question 2",
     "Expected: git status first (which files), then git diff (which lines) — before any git add."),
    ("Pair check",
     "Comparing git log --oneline with a neighbour shows whether both made the same commit on feat/hello."),
    ("Link to what follows",
     "Next session: driving opencode — every change the agent makes will now go through this review."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "Debrief — 5 min", tag=t.div, toc_lvl="+1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Git debrief", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "8vh")

        # one numbered row per question, alternating fills — motif L2 + fonds f1 (margins 5 %, numbering column)
        cols = "5% 5% 85% 5%"
        cells = s.project.containers.rows(len(_QUESTIONS), cols, filled=(2, 3))
        with st_zoom(128), st_grid(cols=cols, gap="6vh 0.5vw", cell_styles=cells) as g:
            for n, question in enumerate(_QUESTIONS, 1):
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.number, f"{n}", tag=t.div)
                with g.cell():
                    st_write(bs.body, *question, tag=t.div)
                with g.cell():
                    pass  # right margin
        st_space("v", "10vh")
        with st_zoom(123):
            st_write(bs.pair, "Compare git log --oneline with your neighbour: same history?", tag=t.div)
