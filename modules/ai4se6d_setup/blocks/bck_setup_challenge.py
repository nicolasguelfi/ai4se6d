"""Slide — The FreeSelfApp challenge: a small personal web app, by prompting only."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Challenge slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    label = s.project.titles.label
    keyword = s.bold + s.project.colors.accent
    warn = s.bold + s.project.colors.highlight
    caption = Style.create(s.project.titles.caption + s.center_txt, "setup_challenge_caption")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.heading, "The Challenge", tag=t.div, toc_lvl="1")
        st_write(bs.body, (bs.label, "Goal: "), "a small personal web app.")
        with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
            with l.item():
                st_write(bs.body, "It ", (bs.keyword, "runs in a browser"))
            with l.item():
                st_write(bs.body, (bs.keyword, "Any stack"), " — HTML + JS is simplest")
            with l.item():
                st_write(bs.body, (bs.warn, "No rules, no plan"), " — on purpose")
            with l.item():
                st_write(bs.body, "You type ", (bs.keyword, "prompts"), ", not code")
        st_space("v", 1)
        st_write(bs.caption, "Today you feel vibe coding. Tomorrow you engineer it.", tag=t.div)
