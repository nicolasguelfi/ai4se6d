"""Slide — Enterprise roadmaps 2025-2030: analyst predictions."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip

class BlockStyles:
    """Roadmap slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.accent
    stat = s.bold + s.project.colors.highlight
    source_name = s.bold + s.project.colors.primary
    source = s.project.citation + s.large + s.center_txt
bs = BlockStyles

def build():
    st_marker("Enterprise Roadmap 2025-2030")
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(bs.heading, "Enterprise Roadmaps 2025\u20132030", tag=t.div, toc_lvl="+1")
            st_hover_tooltip(
                title="Industry Analyst Predictions",
                entries=[
                    ("Convergence", "All major analysts agree: AI-assisted SE will become universal by 2028."),
                    ("The failure mode", "Forrester predicts 50% of enterprises will try to replace developers with AI and fail."),
                    ("The success mode", "Bain and McKinsey data shows 25-30% gains only with end-to-end process transformation."),
                ],
                scale="2vw", width="70vw", position="center",
            )

        with st_zoom(90):
            with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                with l.item():
                    st_write(bs.body, (bs.source_name, "Gartner: "), (bs.stat, "90%"), " of enterprise SE will use AI-assisted development by 2028")
                with l.item():
                    st_write(bs.body, (bs.source_name, "Bain: "), (bs.stat, "25\u201330%"), " productivity gains achievable with transformation programs, not just tool adoption")
                with l.item():
                    st_write(bs.body, (bs.source_name, "McKinsey: "), "Organizations must ", (bs.keyword, "redesign processes"), " around AI capabilities, not bolt AI onto existing workflows")
                with l.item():
                    st_write(bs.body, (bs.source_name, "Forrester: "), (bs.stat, "50%"), " of enterprises will attempt to replace developers with AI \u2014 and fail")
                with l.item():
                    st_write(bs.body, (bs.source_name, "GENIUS Project: "), "5-year research program, 30+ academic/industry partners, building foundations for generative SE at scale")

            st_space("v", 2)
