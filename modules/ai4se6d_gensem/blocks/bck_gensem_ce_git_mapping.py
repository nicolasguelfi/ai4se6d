"""Slide — GSE-One Activity-to-Git Mapping."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Git mapping table slide styles."""
    heading = s.project.titles.heading
    th = s.project.titles.table_header
    td = s.project.titles.table_cell
    tl = s.project.titles.table_label

bs = BlockStyles

_HEADER = ("Activity", "Git Operation", "worktree (Full)", "branch-only / none")

_ROWS = [
    (
        "PLAN (strategic)",
        "create sprint integration branch gse/sprint-NN/integration from main; assign branch names to tasks",
        "sprint branch created",
        "no sprint branch (feature branch off main / no branching)",
    ),
    (
        "PRODUCE",
        "feature branch gse/sprint-NN/{type}/{name}; commits gse(sprint-NN/{type}): ... + Sprint/Traces trailers",
        "branch + worktree in .worktrees/",
        "branch in main checkout / direct commits",
    ),
    (
        "REVIEW",
        "branch diff: git diff integration...feature",
        "diff-based review",
        "no REVIEW activity",
    ),
    (
        "DELIVER",
        "merge features → sprint → main; semver tag; release notes; branch + worktree cleanup (backup tags)",
        "full merge chain",
        "merge single branch / nothing to merge",
    ),
    (
        "COMPOUND",
        "no release git ops — capitalization on main after delivery",
        "learnings → compound.md",
        "no COMPOUND activity",
    ),
]


def build():
    st_marker("Activity → Git Mapping")
    with st_block(s.project.containers.page_fill_top):
        with st_grid(
            cols="95% 5%",
            gap="0px",
            cell_styles=s.project.containers.grid_cell_centered,
        ) as g:
            with g.cell():
                with st_zoom(90):
                    st_write(bs.heading, "GSE-One Activity-to-Git Mapping", tag=t.div, toc_lvl="+1")
            with g.cell():
                st_hover_tooltip(
                    title="GSE-One Activity-to-Git Mapping",
                    entries=[
                        ("CE genealogy", "The CE phases map pedagogically onto GSE-One activities: CE Brainstorm ~ /gse:assess, CE Plan = /gse:plan, CE Work = /gse:produce, CE Review = /gse:review, CE Compound = /gse:compound. GSE-One extends CE with a full version-control strategy (spec section 10)."),
                        ("Branch model", "main -> gse/sprint-NN/integration -> gse/sprint-NN/{type}/{name} with type in feat/fix/refactor/docs/test/chore. With the worktree strategy each active branch lives in its own .worktrees/ directory."),
                        ("Columns", "Third column = worktree strategy (Full-mode default). Fourth column = branch-only (Lightweight: single feature branch off main, no worktree) and none (Micro: direct commits, no branches). REVIEW and COMPOUND exist in Full mode only."),
                        ("Safety", "Before every destructive operation (merge, branch delete, worktree remove) DELIVER creates gse-backup/ safety tags, retained 30 days by default."),
                    ],
                    scale="2vw", width="70vw", position="left",
                )
        st_space("v", 1)

        with st_zoom(100):
            with st_grid(
                cols="15% 40% 22% 23%",
                gap="4px",
                cell_styles=s.project.containers.cell_pad_sm,
            ) as g:
                # Header row
                for h in _HEADER:
                    with g.cell():
                        with st_block(s.project.containers.table_header_cell + s.project.containers.cell_pad_sm):
                            st_write(bs.th, h)

                # Data rows
                for activity, git_op, full_col, light_col in _ROWS:
                    with g.cell():
                        with st_block(s.project.containers.table_normal_cell + s.project.containers.cell_pad_sm):
                            st_write(bs.tl, activity)
                    with g.cell():
                        with st_block(s.project.containers.table_normal_cell + s.project.containers.cell_pad_sm):
                            st_write(bs.td, git_op)
                    with g.cell():
                        with st_block(s.project.containers.table_normal_cell + s.project.containers.cell_pad_sm):
                            st_write(bs.td, full_col)
                    with g.cell():
                        with st_block(s.project.containers.table_normal_cell + s.project.containers.cell_pad_sm):
                            st_write(bs.td, light_col)
