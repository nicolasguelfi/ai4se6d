"""Slide — Evidence: why process matters (Tool alone vs Tool + Process)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip

class BlockStyles:
    """Evidence comparison slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    col_title_warn = Style.create(
        s.Large + s.bold + s.project.colors.highlight + s.center_txt,
        "gs_ev_col_warn",
    )
    col_title_ok = Style.create(
        s.Large + s.bold + s.project.colors.success + s.center_txt,
        "gs_ev_col_ok",
    )
    body = s.project.titles.body
    stat_warn = s.bold + s.project.colors.highlight
    stat_ok = s.bold + s.project.colors.success
    takeaway = Style.create(
        s.project.titles.body_accent + s.center_txt,
        "gs_ev_takeaway",
    )
    source = s.project.citation + s.large + s.center_txt
bs = BlockStyles

def build():
    st_marker("Tool Alone vs Tool + Process")
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            with st_grid(
                cols="95% 5%",
                gap="0px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    with st_zoom(90):
                        st_write(bs.heading, "Evidence: Why Process Matters", tag=t.div, toc_lvl="+1")
                with g.cell():
                    st_hover_tooltip(
                        title="Evidence: Tool Alone vs Tool + Process",
                        entries=[
                            ("Tool alone", "+55.8% on simple tasks but -19% on real projects and 7h/week lost to AI-generated tech debt."),
                            ("Tool + process", "25-30% gains with transformation program. FlowGen: 15% fewer code smells when design + code review are part of the process; FlowGenScrum achieves 75.2% Pass@1 on HumanEval."),
                            ("Pass@1", "The percentage of AI-generated code that passes all tests on the first attempt, without retries. A higher Pass@1 means the AI produces correct code more often."),
                            ("HumanEval", "A benchmark of 164 programming problems created by OpenAI, used as the standard reference to compare code-generation models. 75.2% means FlowGenScrum solves 3 out of 4 problems correctly on the first try."),
                            ("Key takeaway", "The methodology is the multiplier, not the tool \u2014 process discipline determines whether AI helps or hinders."),
                        ],
                        scale="2vw", width="70vw", position="left",
                    )
            st_space("v", 1)

        with st_zoom(90):
            with st_grid(
                cols=s.project.containers.responsive_2col,
                gap="32px",
                cell_styles=s.project.containers.cell_primary_bg + s.project.containers.cell_pad_md,
            ) as g:
                # Left column — Tool alone (amber)
                with g.cell():
                    st_write(bs.col_title_warn, "Tool Alone", tag=t.div)
                    st_space("v", 1)
                    with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                        with l.item():
                            st_write(bs.body, (bs.stat_warn, "+55.8%"), " productivity on simple tasks")
                        with l.item():
                            st_write(bs.body, (bs.stat_warn, "\u221219%"), " slower for experienced devs on real projects")
                        with l.item():
                            st_write(bs.body, (bs.stat_warn, "7h/week"), " lost to AI-generated technical debt")
                    st_space("v", 1)
                    st_write(bs.source, cite("peng-copilot2023"))
                    st_write(bs.source, cite("metr2025"))
                    st_write(bs.source, cite("gitlab-devsecops2025"))

                # Right column — Tool + Process (teal)
                with g.cell():
                    st_write(bs.col_title_ok, "Tool + Process", tag=t.div)
                    st_space("v", 1)
                    with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                        with l.item():
                            st_write(bs.body, (bs.stat_ok, "25\u201330%"), " gains with transformation program")
                        with l.item():
                            st_write(bs.body, (bs.stat_ok, "15%"), " fewer code smells with FlowGen structured process")
                        with l.item():
                            st_write(bs.body, (bs.stat_ok, "75.2%"), " genCode Pass@1 on HumanEval (FlowGenScrum)")
                    st_space("v", 1)
                    st_write(bs.source, cite("soen101-2024"))

            st_space("v", 2)
            st_write(bs.takeaway, "The methodology is the multiplier, not the tool.")
