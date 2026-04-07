"""Slide — Section title: SDLC transformed by GenAI."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s

class BlockStyles:
    heading = s.project.titles.section_title + s.center_txt
    body = s.project.titles.body + s.center_txt
bs = BlockStyles

def build():
    with st_block(s.project.containers.page_fill_center):
        st_write(bs.heading, "The SDLC is Being Transformed", tag=t.div, toc_lvl="1")
        st_space("v", 2)
        st_write(bs.body, "Every phase of the software development lifecycle is impacted by generative AI \u2014 but not equally.")
