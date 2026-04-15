"""Slide — SE 3.0: intent-centric, conversation-oriented development."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip

class BlockStyles:
    """SE 3.0 slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.accent
    number = s.bold + s.project.colors.primary
    assessment = Style.create(
        s.project.titles.body_accent + s.center_txt,
        "gs_se30_assessment",
    )
    source = s.project.citation + s.large + s.center_txt
bs = BlockStyles

def build():
    st_marker("SE 3.0 (Hassan)")
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            with st_grid(
                cols="95% 5%",
                gap="0px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    st_write(bs.heading, "SE 3.0", tag=t.div, toc_lvl="+1")
                with g.cell():
                    st_hover_tooltip(
                        title="SE 3.0 — Intent-Centric Development",
                        entries=[
                            ("Key idea", "A paradigm shift where developers express intent and AI determines implementation across 5 characteristics."),
                            ("Limitations", "Remains largely theoretical; no tooling or validated process; high learning curve."),
                            ("GSE-One gap", "GSE-One operationalizes adaptive partnership (P9) and multi-objective quality that SE 3.0 only envisions."),
                        ],
                        scale="2vw", width="70vw", position="left",
                    )

        with st_zoom(90):
            st_write(bs.body, "Hassan et al. propose a paradigm shift with ", (bs.keyword, "5 characteristics"), ":")
            st_space("v", 1)

            with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.ordered) as l:
                with l.item():
                    st_write(bs.body, (bs.keyword, "Intent-centric: "), "Developers express what, AI determines how")
                with l.item():
                    st_write(bs.body, (bs.keyword, "Conversation-oriented: "), "Iterative dialogue replaces specification documents")
                with l.item():
                    st_write(bs.body, (bs.keyword, "Adaptive partnership: "), "AI adapts to developer skill level and style")
                with l.item():
                    st_write(bs.body, (bs.keyword, "Multi-objective: "), "Balances functionality, performance, security, maintainability")
                with l.item():
                    st_write(bs.body, (bs.keyword, "SLA-aware: "), "Generated code meets service-level agreements by design")

            st_space("v", 2)
            st_write(bs.assessment, "Assessment: Most ambitious vision, but remains largely theoretical.")
            st_write(bs.source, cite("hassan-se30-2025"))
