"""Slide — Git exercise sheet: done when, mid-point, if stuck."""
# @guideline: minimalist-visual + maximize-viewport
# @pattern: ptn_exercise_flow
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Exercise sheet styles."""
    heading = s.project.titles.heading
    label = s.project.titles.table_label
    text = s.project.titles.table_cell
    done = Style.create(s.project.titles.table_label + s.project.colors.success, "d2_sheet_done")
bs = BlockStyles

_SHEET = [
    ("Done when", "git log --oneline shows your commit on feat/hello, and git status is clean"),
    ("Mid-point (7 min)", "npm run test:run is green and git branch shows * feat/hello"),
    ("If stuck", "1. your tutor window  2. re-clone at j2-start in a new folder  3. raise your hand"),
    ("Git asks who you are?", "git config --global user.name \"Your Name\"  then  user.email"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(75):
            st_write(bs.heading, "Git — Check Yourself", tag=t.div, toc_lvl="+1")
        st_space("v", 1)
        with st_grid(cols="28% 72%", gap="10px") as g:
            for label, text in _SHEET:
                with g.cell():
                    with st_block(s.project.containers.table_header_cell):
                        st_write(bs.done if label == "Done when" else bs.label, label)
                with g.cell():
                    with st_block(s.project.containers.table_normal_cell):
                        st_write(bs.text, text)
