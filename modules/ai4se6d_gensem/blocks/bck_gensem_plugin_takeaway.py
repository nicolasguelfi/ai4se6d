"""Slide — Plugin takeaways and closing."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s

class BlockStyles:
    """Takeaway slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.accent
    closing = Style.create(
        s.project.titles.section_title + s.center_txt,
        "plugin_takeaway_closing",
    )
bs = BlockStyles

def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(90):
            st_write(bs.heading, "Plugin Takeaways", tag=t.div, toc_lvl="1")
        st_space("v", 2)

        with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.ordered) as l:
            with l.item():
                st_write(bs.body, (bs.keyword, "CE is not a tool \u2014 it's a discipline."), " The plugin enforces it, but the value comes from the methodology itself.")
            with l.item():
                st_write(bs.body, (bs.keyword, "Start with individual phases,"), " graduate to /gse:go orchestration as you build confidence in each step.")
            with l.item():
                st_write(bs.body, (bs.keyword, "The compound phase is what creates exponential improvement."), " Without it, you get linear productivity; with it, each cycle amplifies the next.")

        st_space("v", 4)
        st_write(bs.closing, "Questions?", tag=t.div)
