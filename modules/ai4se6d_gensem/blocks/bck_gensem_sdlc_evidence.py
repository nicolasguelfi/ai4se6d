"""Slide — Evidence: why process matters (Tool alone vs Tool + Process)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s

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
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(bs.heading, "Evidence: Why Process Matters", tag=t.div, toc_lvl="1")
            st_space("v", 1)

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
                        st_write(bs.body, (bs.stat_ok, "15%"), " Pass@1 improvement with FlowGen structured process")
                st_space("v", 1)
                st_write(bs.source, cite("soen101-2024"))

        st_space("v", 2)
        st_write(bs.takeaway, "The methodology is the multiplier, not the tool.")
