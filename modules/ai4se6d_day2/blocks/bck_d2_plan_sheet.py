"""Slide — Planning exercise sheet: done when, mid-point, if stuck."""
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
    ("Done when", "git log --oneline on mywork shows “docs: v0.1 plan”; docs/plan.md has 5-8 tasks, one [next]"),
    ("Mid-point (11:15)", "your user stories have testable acceptance criteria; you are splitting them"),
    ("If stuck", "1. your tutor window  2. cp docs/plan-example.md docs/plan.md, adapt it  3. raise your hand"),
    ("New file?", "git diff ignores untracked files: git add first, then git diff --staged"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(75):
            st_write(bs.heading, "Your Plan — Check Yourself", tag=t.div, toc_lvl="+1")
        st_space("v", 1)
        with st_grid(cols="28% 72%", gap="10px") as g:
            for label, text in _SHEET:
                with g.cell():
                    with st_block(s.project.containers.table_header_cell):
                        st_write(bs.done if label == "Done when" else bs.label, label)
                with g.cell():
                    with st_block(s.project.containers.table_normal_cell):
                        st_write(bs.text, text)
