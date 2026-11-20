"""Slide — PLACEHOLDER: final questionnaire, link given in class (open point: DLH questionnaire, edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Questionnaire styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.center_txt, "questionnaire_body")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "questionnaire_foot")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_center):
        with st_zoom(72):
            st_write(bs.heading, "Final Questionnaire", tag=t.div, toc_lvl="1", label="Final questionnaire")
            with st_block(s.project.containers.callout):
                st_write(bs.body, "Link given in class.", tag=t.div)
            st_write(bs.body, "15 minutes, in the room. It is the main way this course improves.", tag=t.div)
            st_write(bs.foot, "Anything else: a GitHub issue on nicolasguelfi/gensem, label ai4se-ed2.", tag=t.div)
