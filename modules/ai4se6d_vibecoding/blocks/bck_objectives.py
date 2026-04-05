"""Slide — Learning objectives for the VibeCoding & VibeEngineering session."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s

class BlockStyles:
    """Learning objectives slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    verb = s.bold + s.project.colors.accent
bs = BlockStyles

def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(bs.heading, "Learning Objectives", tag=t.div, toc_lvl="1")
            st_space("v", 2)

            with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.ordered) as l:
                with l.item():
                    st_write(bs.body, (bs.verb, "Define"), " VibeCoding and its 4 principles")
                with l.item():
                    st_write(bs.body, (bs.verb, "Identify"), " 5 dangers of naive AI-assisted development")
                with l.item():
                    st_write(bs.body, (bs.verb, "Distinguish"), " VibeCoding from VibeEngineering")
                with l.item():
                    st_write(bs.body, (bs.verb, "Apply"), " the 6 VibeEngineering principles to structure AI-assisted work")
