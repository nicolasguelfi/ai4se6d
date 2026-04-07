"""Slide — Specialization: making Compound Engineering your own."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s

class BlockStyles:
    """CE specialization slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.accent
    teaser = s.project.titles.body + s.project.colors.highlight + s.bold
bs = BlockStyles

def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(bs.heading, "Specialization \u2014 Making CE Your Own", tag=t.div, toc_lvl="1")
            st_space("v", 1)

        st_write(bs.body, "CE is a process experimentation platform. Four steps to create your variant:")
        st_space("v", 1)

        with st_list(li_style=bs.body, list_type=lt.ordered) as l:
            with l.item():
                st_write(bs.body, (bs.keyword, "Define process model"), " \u2014 choose which phases, which artifacts, what granularity")
            with l.item():
                st_write(bs.body, (bs.keyword, "Create variant skill files"), " \u2014 custom prompts, templates, and phase definitions")
            with l.item():
                st_write(bs.body, (bs.keyword, "Configure activation"), " \u2014 set up rules so your variant is invoked by default")
            with l.item():
                st_write(bs.body, (bs.keyword, "Synchronize across tools"), " \u2014 plugin architecture ensures consistency (Cursor, Claude Code, etc.)")

        st_space("v", 2)

        with st_block(s.project.containers.callout):
            st_write(
                bs.teaser,
                "We'll create GenSEMOne (Part 5) \u2014 a lightweight CE variant "
                "using only Cursor native features.",
            )
