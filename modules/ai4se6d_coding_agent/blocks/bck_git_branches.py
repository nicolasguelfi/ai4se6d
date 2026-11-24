"""Slide — Pattern 3: one branch per task (diagram)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Branch pattern styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.center_txt, "gitbr_body")
    keyword = s.project.titles.keyword
bs = BlockStyles


_NOTES = [
    ("The message",
     "Third habit: one branch per task. The agent never works directly on your main line."),
    ("How",
     "git switch -c feat/add-history (name it after your task) creates the branch. It works: merge it back. It does not: delete it — nothing is lost."),
    ("Why it matters with an agent",
     "Each task of the plan becomes a branch, so each change of the agent stays isolated and easy to review."),
    ("Link to the day",
     "The build this afternoon uses one branch per task of docs/plan.md."),
    ("Ask the room",
     "« What happens to your main line if the agent's attempt fails on a branch? »"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(70):
                st_write(bs.heading, "3 · One Branch per Task", tag=t.div, toc_lvl="+1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — One Branch per Task", entries=_NOTES,
                                 position="left", width="50vw")
        st_image(uri="images/am/bck_git_branches_image_00.png", width="100%", max_vh=70, align="center")
        st_write(
            bs.body, (bs.keyword, "git switch -c feat/add-history"),
            " — works? merge it back. Doesn’t? delete it: nothing is lost.", tag=t.div,
        )
