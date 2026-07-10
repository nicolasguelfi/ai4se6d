"""Slide — Three Git Strategies for GSE-One."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip

class BlockStyles:
    """Git strategies slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    profile_name = s.bold + s.project.colors.primary + s.Large
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.accent
    future = s.italic + s.project.colors.accent
    today = s.bold + s.project.colors.highlight + s.Large
bs = BlockStyles

def build():
    st_marker("3 Git Strategies")
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            with st_grid(
                cols="95% 5%",
                gap="0px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    with st_zoom(90):
                        st_write(bs.heading, "Three Git Strategies", tag=t.div, toc_lvl="+1")
                with g.cell():
                    st_hover_tooltip(
                        title="Git Strategies in GSE-One",
                        entries=[
                            ("Configuration", "Set in .gse/config.yaml: git.strategy = worktree | branch-only | none. Calibrated by the lifecycle mode and the HUG profile; change via /gse:hug --update or by editing the config."),
                            ("none", "Direct commits on main. Default for Micro mode (trivial scripts) and legitimate ONLY there: in the other modes the protect-main hook blocks any git commit on main (Hard guardrail)."),
                            ("branch-only", "Feature branches without worktrees — the agent switches branches in the main checkout. Lightweight default: a single feature branch off main, no sprint branch."),
                            ("worktree", "One git worktree per task under .worktrees/ + a sprint integration branch gse/sprint-NN/integration. Full-mode default and the GSE-One flagship (P12 — Version Control Isolation)."),
                            ("Conventional commits", "GSE-One uses a structured format: gse(sprint-NN/type): description, with Sprint / Task / Traces trailers. Example: gse(sprint-03/feat): implement user authentication flow. The agent generates these automatically."),
                            ("Today", "Training uses the worktree strategy -- practices run Full mode."),
                        ],
                        scale="2vw", width="70vw", position="left",
                    )
            st_space("v", 1)

        with st_zoom(90):
            with st_grid(
                cols="repeat(auto-fit, minmax(280px, 1fr))",
                gap="16px",
                cell_styles=s.project.containers.cell_pad_md,
            ) as g:
                with g.cell():
                    with st_block(s.project.containers.cell_primary_bg + s.project.containers.cell_pad_md):
                        st_write(bs.profile_name, "none — Micro mode", tag=t.div)
                        st_space("v", 0.5)
                        with st_list(li_style=bs.body, list_type=lt.unordered) as l:
                            with l.item():
                                st_write(bs.body, "Direct commits on main, no branch creation")
                            with l.item():
                                st_write(bs.body, "Default for Micro mode (trivial scripts, one-offs)")
                            with l.item():
                                st_write(bs.body, "Legitimate ", (bs.keyword, "only"), " there — elsewhere the protect-main hook blocks commits on main")

                with g.cell():
                    with st_block(s.project.containers.cell_primary_bg + s.project.containers.cell_pad_md):
                        st_write(bs.profile_name, "branch-only — Lightweight", tag=t.div)
                        st_space("v", 0.5)
                        with st_list(li_style=bs.body, list_type=lt.unordered) as l:
                            with l.item():
                                st_write(bs.body, "Feature branches, no worktrees")
                            with l.item():
                                st_write(bs.body, "Agent switches branches in the main checkout")
                            with l.item():
                                st_write(bs.body, "Lightweight default: single feature branch off main, no sprint branch")

                with g.cell():
                    with st_block(s.project.containers.cell_active_bg + s.project.containers.cell_pad_md):
                        st_write(bs.profile_name, "worktree — Full mode", tag=t.div)
                        st_write(bs.today, "Today's strategy", tag=t.div)
                        st_space("v", 0.5)
                        with st_list(li_style=bs.body, list_type=lt.unordered) as l:
                            with l.item():
                                st_write(bs.body, "One worktree per task in ", (bs.keyword, ".worktrees/"))
                            with l.item():
                                st_write(bs.body, "Sprint integration branch ", (bs.keyword, "gse/sprint-NN/integration"))
                            with l.item():
                                st_write(bs.body, "GSE-One flagship — ", (bs.keyword, "P12"), " isolation: main always stable")

                with g.cell():
                    with st_block(s.project.containers.cell_primary_bg + s.project.containers.cell_pad_md):
                        st_write(bs.profile_name, "Team support", tag=t.div)
                        st_space("v", 0.5)
                        with st_list(li_style=bs.body, list_type=lt.unordered) as l:
                            with l.item():
                                st_write(bs.body, "Per-member HUG profiles in ", (bs.keyword, ".gse/profiles/"))
                            with l.item():
                                st_write(bs.body, "Enabled via ", (bs.keyword, "/gse:hug --team"), " or auto-detected from git contributors")
                            with l.item():
                                st_write(bs.body, "Plan tasks carry ", (bs.keyword, "assignee"), " / ", (bs.keyword, "reviewer"), " fields")
                            with l.item():
                                st_write(bs.body, "Each member works in their own worktree/branch — no file-level conflicts")

        st_space("v", 0.5)
        with st_block(s.center_txt):
            st_write(bs.body, "Strategy is set in ", (bs.keyword, ".gse/config.yaml"), " (", (bs.keyword, "git.strategy"), ") and calibrated by the lifecycle mode and HUG profile.", tag=t.div)
