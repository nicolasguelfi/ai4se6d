"""Slide — Commit messages and branch names."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Naming conventions styles."""
    heading = s.project.titles.heading
    col_title = s.project.titles.subtitle
    text = s.project.titles.table_cell
bs = BlockStyles

_COMMITS = """\
type(scope): what changed

feat(expenses): reject negative amounts
fix(list): round the monthly total
test(form): cover the empty category

Assisted-by: opencode"""

_BRANCHES = """\
mywork               your main line today
feat/<task>          one task of your plan
fix/<bug>            a bug fix
experiment/<idea>    may be thrown away"""


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(75):
            st_write(bs.heading, "Names That Tell the Story", tag=t.div, toc_lvl="+1")
        st_space("v", 0.5)
        with st_grid(cols=s.project.containers.responsive_2col, grid_style=s.project.containers.gap_24) as g:
            with g.cell():
                st_write(bs.col_title, "Commits", tag=t.div)
                st_code(s.none, code=_COMMITS, language="text", line_numbers=False, font_size="22pt")
            with g.cell():
                st_write(bs.col_title, "Branches", tag=t.div)
                st_code(s.none, code=_BRANCHES, language="text", line_numbers=False, font_size="22pt")
                st_write(bs.text, "Types: feat, fix, test, refactor, docs, chore.", tag=t.div)
