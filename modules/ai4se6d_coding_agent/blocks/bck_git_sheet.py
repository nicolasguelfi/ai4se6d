"""Slide — Git exercise sheet: done when, mid-point, if stuck."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Exercise sheet styles."""
    heading = s.project.titles.heading
    label = s.project.titles.table_label
    text = s.project.titles.table_cell
    done = Style.create(s.project.titles.table_label + s.project.colors.success, "sheet_done")
bs = BlockStyles

_SHEET = [
    ("Done when", "git log --oneline shows your commit on feat/hello, and git status is clean"),
    ("Mid-point (7 min)", "npm run test:run is green and git branch shows * feat/hello"),
    ("If stuck", "1. your tutor window  2. re-clone at j2-start in a new folder  3. raise your hand"),
    ("Git asks who you are?", "git config --global user.name \"Your Name\"  then  user.email"),
]

_NOTES = [
    ("Trainer action",
     "Learners do it — on their machine. Leave this sheet on screen during the Git exercise; check the 7-min mid-"
     "point (tests green, * feat/hello) by walking around."),
    ("The message",
     "Participants check themselves: a clear « done when », a mid-point at 7 minutes, and what to do if stuck."),
    ("Done when",
     "git log --oneline shows the commit on feat/hello and git status is clean — nothing left unstaged."),
    ("Mid-point",
     "At 7 minutes, npm run test:run is green and git branch shows * feat/hello. Walk around: who is not there yet?"),
    ("If stuck",
     "Tutor window first, then a fresh clone at j2-start in a new folder, then a raised hand."),
    ("Frequent snag",
     "Git asks who you are on the first commit: git config --global user.name \"Your Name\", then user.email."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "Git — Check Yourself", tag=t.div, toc_lvl="+1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Git — Check Yourself", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "4vh")

        # one row per check, alternating fills — motif L2 + fonds f1 (margins 5 %)
        cols = "5% 26% 64% 5%"
        cells = s.project.containers.rows(len(_SHEET), cols, filled=(2, 3))
        with st_zoom(110), st_grid(cols=cols, gap="5vh 0.4vw", cell_styles=cells) as g:
            for label, text in _SHEET:
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.done if label == "Done when" else bs.label, label)
                with g.cell():
                    st_write(bs.text, text)
                with g.cell():
                    pass  # right margin
