"""Slide — AgileGen: Gherkin-bridge approach to agile + GenAI."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip

class BlockStyles:
    """AgileGen detail slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.accent
    callout_title = Style.create(
        s.Large + s.bold + s.project.colors.highlight,
        "gs_ag_callout_title",
    )
    callout_body = s.project.titles.body
    verdict = Style.create(
        s.project.titles.body_accent + s.center_txt,
        "gs_ag_verdict",
    )
bs = BlockStyles

def build():
    st_marker("AgileGen (Zhang 2025)")
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            with st_grid(
                cols="95% 5%",
                gap="0px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    with st_zoom(90):
                        st_write(bs.heading, "AgileGen", tag=t.div, toc_lvl="+1")
                with g.cell():
                    st_hover_tooltip(
                        title="AgileGen — Gherkin-Bridge Approach",
                        entries=[
                            ("Key idea", "Translates user stories into Gherkin scenarios as a formal bridge between intent and generated code."),
                            ("Limitations", "Requires BDD literacy; narrow applicability; no knowledge capitalization across sprints."),
                            ("GSE-One gap", "GSE-One adds compound phases and cross-tool portability that AgileGen lacks."),
                        ],
                        scale="2vw", width="70vw", position="left",
                    )

        with st_zoom(90):
            with st_grid(
                cols=s.project.containers.responsive_2col,
                gap="24px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                # Left — Gherkin bridge callout
                with g.cell():
                    with st_block(s.project.containers.callout):
                        st_write(bs.callout_title, "The Gherkin Bridge", tag=t.div)
                        st_space("v", 1)
                        st_write(bs.callout_body, "Natural-language user stories are translated into Gherkin scenarios (Given/When/Then) that serve as both specification and acceptance test.")
                        st_space("v", 1)
                        st_write(bs.callout_body, "This creates a ", (bs.keyword, "formal bridge"), " between stakeholder intent and generated code.")

                # Right — bullet list
                with g.cell():
                    with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                        with l.item():
                            st_write(bs.body, (bs.keyword, "Origin: "), "Zhang et al. \u2014 agile adapted for LLM code generation")
                        with l.item():
                            st_write(bs.body, (bs.keyword, "Memory pool: "), "Stores successful patterns for reuse across sprints")
                        with l.item():
                            st_write(bs.body, (bs.keyword, "XP2025 frustrations: "), "Teams report mismatch between agile ceremonies and AI speed")
                        with l.item():
                            st_write(bs.body, (bs.keyword, "Limitation: "), "Requires Gherkin literacy; not all teams adopt BDD")

            st_space("v", 2)
            st_write(bs.verdict, "Verdict: Practical for BDD teams, but narrow applicability.")
