"""Slide — Key takeaways from SOTA review."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s

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
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(bs.heading, "Key Takeaways", tag=t.div, toc_lvl="1")
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
            st_write(bs.transition, "Let\u2019s deep-dive into Compound Engineering.")
