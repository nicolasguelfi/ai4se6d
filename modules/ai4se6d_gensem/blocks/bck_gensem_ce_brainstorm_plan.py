"""Slide — Phases 1-2: Brainstorm & Plan details."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip

class BlockStyles:
    """Brainstorm & Plan slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    phase_title = s.bold + s.project.colors.primary + s.Large
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.accent
    key_point = s.project.titles.body + s.project.colors.highlight + s.bold
bs = BlockStyles

def build():
    st_marker("Assess & Plan Phases")
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            with st_zoom(100):
                with st_grid(
                    cols="95% 5%",
                    gap="0px",
                    cell_styles=s.project.containers.grid_cell_centered,
                ) as g:
                    with g.cell():
                        with st_zoom(90):
                            st_write(bs.heading, "Phases 1-2: Brainstorm & Plan", tag=t.div, toc_lvl="+1")
                    with g.cell():
                        st_hover_tooltip(
                            title="Brainstorm & Plan in GSE-One",
                            entries=[
                                ("Brainstorm", "CE Brainstorm = /gse:assess in GSE-One. Clarify requirements, surface risks."),
                                ("Plan", "CE Plan = /gse:plan in GSE-One. Task decomposition, file mapping, verification."),
                                ("Key insight", "These two phases represent the bulk of the 80% planning investment."),
                                ("Anti-pattern", "Skipping these leads to premature implementation and scope creep."),
                            ],
                            scale="2vw", width="70vw", position="left",
                        )
            st_space("v", 1)

        with st_zoom(80):
            with st_grid(
                cols=s.project.containers.responsive_2col,
                gap="24px",
                cell_styles=s.project.containers.cell_pad_md,
            ) as g:
                with g.cell():
                    with st_block(s.project.containers.cell_primary_bg + s.project.containers.cell_pad_md):
                        st_write(bs.phase_title, "Brainstorm", tag=t.div)
                        st_space("v", 0.5)
                        with st_list(li_style=bs.body, list_type=lt.unordered) as l:
                            with l.item():
                                st_write(bs.body, (bs.keyword, "Clarify"), " requirements with structured questions")
                            with l.item():
                                st_write(bs.body, (bs.keyword, "Identify"), " edge cases and boundary conditions")
                            with l.item():
                                st_write(bs.body, (bs.keyword, "Compare"), " architectures with explicit trade-offs")
                            with l.item():
                                st_write(bs.body, (bs.keyword, "Surface"), " risks before any code is written")
                        st_space("v", 0.5)
                        st_write(bs.key_point, "Addresses the premature implementation problem")

                with g.cell():
                    with st_block(s.project.containers.cell_accent_bg + s.project.containers.cell_pad_md):
                        st_write(bs.phase_title, "Plan", tag=t.div)
                        st_space("v", 0.5)
                        with st_list(li_style=bs.body, list_type=lt.unordered) as l:
                            with l.item():
                                st_write(bs.body, (bs.keyword, "Task decomposition"), " with dependencies")
                            with l.item():
                                st_write(bs.body, (bs.keyword, "File-level changes"), " mapped out in advance")
                            with l.item():
                                st_write(bs.body, (bs.keyword, "Interface contracts"), " specified before implementation")
                            with l.item():
                                st_write(bs.body, (bs.keyword, "Verification strategy"), " defined per task")
                            with l.item():
                                st_write(bs.body, (bs.keyword, "Risk mitigation"), " steps for each identified risk")
                        st_space("v", 0.5)
                        st_write(bs.key_point, "Acts as a contract preventing scope creep")
