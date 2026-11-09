"""Slide — Take notes as you build (feeds the 16:15 debrief)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Take notes slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    label = s.project.titles.label
    keyword = s.bold + s.project.colors.accent
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "setup_cmd")
    caption = s.project.titles.caption
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.heading, "Take Notes", tag=t.div, toc_lvl="1")
        st_write(bs.body, (bs.label, "In "), (bs.cmd, "notes.md"), (bs.label, " in your folder:"))
        with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
            with l.item():
                st_write(bs.body, "What ", (bs.keyword, "surprised"), " you")
            with l.item():
                st_write(bs.body, "What ", (bs.keyword, "broke"), " — and who fixed it: you or the AI?")
            with l.item():
                st_write(bs.body, (bs.keyword, "How many prompts"), " so far")
            with l.item():
                st_write(bs.body, "One thing you ", (bs.keyword, "would have done by hand"))
        st_write(bs.caption, "We use these notes in the debrief at 16:15.", tag=t.div)
