"""Slide — Three Git Workflow Profiles for GSE-One."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip

class BlockStyles:
    """Git profiles slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    profile_name = s.bold + s.project.colors.primary + s.Large
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.accent
    future = s.italic + s.project.colors.accent
    today = s.bold + s.project.colors.highlight + s.Large
bs = BlockStyles

def build():
    st_marker("3 Git Workflow Profiles")
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            with st_grid(
                cols="95% 5%",
                gap="0px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    with st_zoom(90):
                        st_write(bs.heading, "Three Git Workflow Profiles", tag=t.div, toc_lvl="+1")
                with g.cell():
                    st_hover_tooltip(
                        title="Git Profiles in GSE-One",
                        entries=[
                            ("Profile A", "Solo/small projects. Direct commits on main. GSE-One adds structure without Git overhead."),
                            ("Profile B", "Solo/large projects. Feature branches + worktrees for parallel work."),
                            ("Profile C", "Team/large projects. Future commands: /gse:sync, /gse:pr, /gse:review --pr, /gse:merge, /gse:status --team, /gse:handoff."),
                            ("Conventional commits", "GSE-One uses a structured format: gse(sprint-NN/activity): description. Example: gse(sprint-01/feat/budget): add category budget component. The agent generates these automatically."),
                            ("Today", "Training uses Profile A -- direct commits, GSE-One phases map to commit messages."),
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
                    with st_block(s.project.containers.cell_active_bg + s.project.containers.cell_pad_md):
                        st_write(bs.profile_name, "Profile A \u2014 Solo, Small", tag=t.div)
                        st_write(bs.today, "Today's profile", tag=t.div)
                        st_space("v", 0.5)
                        with st_list(li_style=bs.body, list_type=lt.unordered) as l:
                            with l.item():
                                st_write(bs.body, "Direct commits on main")
                            with l.item():
                                st_write(bs.body, "GSE-One adds structure without Git overhead")
                            with l.item():
                                st_write(bs.body, "Ideal for learning and small projects")

                with g.cell():
                    with st_block(s.project.containers.cell_primary_bg + s.project.containers.cell_pad_md):
                        st_write(bs.profile_name, "Profile B \u2014 Solo, Large", tag=t.div)
                        st_space("v", 0.5)
                        with st_list(li_style=bs.body, list_type=lt.unordered) as l:
                            with l.item():
                                st_write(bs.body, "Feature branches + worktrees")
                            with l.item():
                                st_write(bs.body, "Parallel work on multiple features")
                            with l.item():
                                st_write(bs.body, "For larger personal projects")

                with g.cell():
                    with st_block(s.project.containers.cell_primary_bg + s.project.containers.cell_pad_md):
                        st_write(bs.profile_name, "Profile C \u2014 Team, Large", tag=t.div)
                        st_space("v", 0.5)
                        with st_list(li_style=bs.body, list_type=lt.unordered) as l:
                            with l.item():
                                st_write(bs.future, "/gse:sync")
                            with l.item():
                                st_write(bs.future, "/gse:pr")
                            with l.item():
                                st_write(bs.future, "/gse:review --pr")
                            with l.item():
                                st_write(bs.future, "/gse:merge")
                            with l.item():
                                st_write(bs.future, "/gse:status --team")
                            with l.item():
                                st_write(bs.future, "/gse:handoff")
