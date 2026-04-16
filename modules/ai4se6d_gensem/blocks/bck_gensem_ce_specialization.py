"""Slide — Specialization: making GSE-One your own."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip

class BlockStyles:
    """GSE-One specialization slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.accent
    teaser = s.project.titles.body + s.project.colors.highlight + s.bold
bs = BlockStyles

def build():
    st_marker("Making GSE-One Your Own")
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            with st_grid(
                cols="95% 5%",
                gap="0px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    with st_zoom(90):
                        st_write(bs.heading, "Specialization \u2014 Making GSE-One Your Own", tag=t.div, toc_lvl="+1")
                with g.cell():
                    st_hover_tooltip(
                        title="GSE-One Specialization",
                        entries=[
                            ("Platform, not framework", "GSE-One is a process experimentation platform -- you customize phases, artifacts, and quality gates."),
                            ("Four steps", "Define process model, create variant skills, configure activation, synchronize across tools."),
                            ("Cross-tool", "Plugin architecture ensures your variant works consistently in Cursor, Claude Code, etc."),
                        ],
                        scale="2vw", width="70vw", position="left",
                    )
            st_space("v", 1)

        with st_zoom(120):
            st_write(bs.body, "GSE-One is a process experimentation platform. Four steps to create your variant:")
            st_space("v", 1)

            with st_list(li_style=bs.body, list_type=lt.ordered) as l:
                with l.item():
                    st_write(bs.body, (bs.keyword, "Define process model"), " \u2014 choose which phases, which artifacts, what granularity")
                with l.item():
                    st_write(bs.body, (bs.keyword, "Create variant skill files"), " \u2014 custom prompts, templates, and phase definitions")
                with l.item():
                    st_write(bs.body, (bs.keyword, "Configure activation"), " \u2014 set up rules so your variant is invoked by default")
                with l.item():
                    st_write(bs.body, (bs.keyword, "Synchronize across tools"), " \u2014 plugin architecture ensures consistency (Cursor, Claude Code, etc.)")

            st_space("v", 2)

            with st_block(s.project.containers.callout):
                st_write(
                    bs.teaser,
                    "We'll create a lightweight GSE-One variant (Part 5) \u2014 "
                    "using only Cursor native features.",
                )
