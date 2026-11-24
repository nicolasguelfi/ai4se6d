"""Slide — Commit messages and branch names."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


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
feat/add-history     one task of your plan
fix/rounding         a bug fix
experiment/new-layout  may be thrown away"""


_NOTES = [
    ("Trainer action",
     "Read and comment — nothing to type. Explain the naming rules; learners write their first conventional "
     "message (« docs: say hello ») in the Git exercise."),
    ("The message",
     "Names tell the story: a reader understands the history from the commit messages and branch names alone."),
    ("Commits",
     "type(scope): what changed — e.g. feat(expenses): reject negative amounts. Types: feat, fix, test, refactor, "
     "docs, chore."),
    ("Assisted-by",
     "A trailer Assisted-by: opencode records that the agent took part in the change."),
    ("Branches",
     "mywork is your main line today; feat/add-history for a task of the plan; fix/rounding for a bug fix; "
     "experiment/new-layout may be thrown away."),
    ("Link to GSE-One",
     "GSE-One makes every commit follow one convention, so the history tells the story."),
    ("Ask the room",
     "« Read your git log --oneline from yesterday: does it tell what happened? »"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "Names That Tell the Story", tag=t.div, toc_lvl="+1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Names That Tell the Story", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "2vh")
        # commits above branches: side by side, the code had to stay too small to fit (NG, 2026-11-23)
        with st_zoom(115), st_grid(cols="5% 90% 5%", gap="1vh 0") as g:
            with g.cell():
                pass  # left margin
            with g.cell():
                st_write(bs.col_title, "Commits", tag=t.div)
                st_code(s.none, code=_COMMITS, language="text", line_numbers=False, font_size="22pt")
                st_space("v", "2vh")
                st_write(bs.col_title, "Branches", tag=t.div)
                st_code(s.none, code=_BRANCHES, language="text", line_numbers=False, font_size="22pt")
                st_write(bs.text, "Types: feat, fix, test, refactor, docs, chore.", tag=t.div)
            with g.cell():
                pass  # right margin
