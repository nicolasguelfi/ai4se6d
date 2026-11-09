"""Slide — Why Git matters more with AI tools."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Why-Git styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    closing = Style.create(s.project.titles.body_accent + s.center_txt, "d2_gitwhy_closing")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(75):
            st_write(bs.heading, "Why Git Matters More with AI", tag=t.div, toc_lvl="+1")
        st_space("v", 1)
        with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.ordered) as l:
            with l.item(): st_write(bs.body, (bs.keyword, "Fast, broad changes"), " — the agent edits 10 files in seconds; Git shows which")
            with l.item(): st_write(bs.body, (bs.keyword, "You review"), " — the agent proposes, ", (bs.keyword, "git diff"), " is how you check")
            with l.item(): st_write(bs.body, (bs.keyword, "Cheap experiments"), " — try on a branch, delete it if it fails")
        st_space("v", 2)
        st_write(bs.closing, "Even opencode’s /undo relies on Git: no repo, no undo.", tag=t.div)
