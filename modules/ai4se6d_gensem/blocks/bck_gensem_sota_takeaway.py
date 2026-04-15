"""Slide — Key takeaways from SOTA review."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip

class BlockStyles:
    """Takeaway slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.accent
    stat = s.bold + s.project.colors.highlight
    transition = Style.create(
        s.project.titles.body_accent + s.center_txt,
        "gs_takeaway_transition",
    )
bs = BlockStyles

def build():
    st_marker("3 Takeaways → GSE-One")
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(bs.heading, "Key Takeaways", tag=t.div, toc_lvl="+1")
            st_hover_tooltip(
                title="SOTA Review Takeaways",
                entries=[
                    ("Disciplinary foundation", "Structured processes consistently outperform ad-hoc approaches \u2014 this is a principle of the discipline, not of any single methodology."),
                    ("Methodology multiplier", "Tool alone yields ~10% gains; tool + process yields 25-30%. Generative SE methodologies operationalize this multiplier."),
                    ("80/20 rule", "Planning and review account for 80% of quality; execution is only 20%. This principle is shared by all mature GenSE methodologies."),
                ],
                scale="2vw", width="70vw", position="center",
            )

        with st_zoom(120):
            st_space("v", 2)
            with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.ordered) as l:
                with l.item():
                    st_write(bs.body, (bs.keyword, "Process discipline persists"), " across all paradigms \u2014 from waterfall to agentic, structured processes consistently outperform ad-hoc approaches")
                with l.item():
                    st_write(bs.body, (bs.keyword, "The methodology is the multiplier: "), "tool alone yields ", (bs.stat, "~10%"), " gains; tool + process yields ", (bs.stat, "25\u201330%"))
                with l.item():
                    st_write(bs.body, (bs.keyword, "The 80/20 rule: "), "planning and review account for ", (bs.stat, "80%"), " of quality; execution is only ", (bs.stat, "20%"))

            st_space("v", 3)
            with st_block(s.center_txt):
                st_write(bs.transition, "These takeaways define a discipline: Generative Software Engineering. Let\u2019s practice it through GSE-One.")
