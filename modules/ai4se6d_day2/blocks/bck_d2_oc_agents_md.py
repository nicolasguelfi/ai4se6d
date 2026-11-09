"""Slide — Project rules = AGENTS.md (opencode)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """AGENTS.md styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    closing = Style.create(s.project.titles.body_accent + s.center_txt, "d2_ocagents_closing")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(75):
            st_write(bs.heading, "Project Rules = AGENTS.md", tag=t.div, toc_lvl="+1")
        st_space("v", 1)
        with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
            with l.item(): st_write(bs.body, "Markdown at the project root, read at every start")
            with l.item(): st_write(bs.body, (bs.keyword, "/init"), " drafts one from your project")
            with l.item(): st_write(bs.body, (bs.keyword, "Commit it"), ": same rules for everyone")
            with l.item(): st_write(bs.body, "Personal: ", (bs.keyword, "~/.config/opencode/AGENTS.md"))
            with l.item(): st_write(bs.body, "Extra files: ", (bs.keyword, "instructions"), " in opencode.json")
        st_space("v", 1)
        st_write(bs.closing, "Plain Markdown. No special syntax.", tag=t.div)
