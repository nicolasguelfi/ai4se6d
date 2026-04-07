"""Slide — Three Git Workflow Profiles for Compound Engineering."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s

class BlockStyles:
    """Git profiles slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    profile_name = s.bold + s.project.colors.primary + s.Large
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.accent
    today = s.bold + s.project.colors.highlight + s.Large
bs = BlockStyles

def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(bs.heading, "Three Git Workflow Profiles", tag=t.div, toc_lvl="1")
            st_space("v", 1)

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
                            st_write(bs.body, "CE adds structure without Git overhead")
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
                            st_write(bs.body, "PR workflow with full review")
                        with l.item():
                            st_write(bs.body, "/lfg + /slfg orchestration commands")
                        with l.item():
                            st_write(bs.body, "For production teams with CI/CD")
