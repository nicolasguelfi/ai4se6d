"""Slide — Installation step 8: open your tutor window (a second terminal, its own opencode session)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Installation step slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    step = Style.create(s.project.titles.caption + s.center_txt, "setup_step_caption")
    body = s.project.titles.body
    label = s.project.titles.label
    caption = s.project.titles.caption
    done_box = s.project.containers.callout
    done_label = Style.create(s.bold + s.project.colors.success, "setup_done_label")
bs = BlockStyles

_CODE_ZOOM = 160  # st_code font_size is not applied by Pygments: zoom instead


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.step, "Installation · step 8 of 8 · ~5 min", tag=t.div)
        st_write(bs.heading, "8 · Tutor Window", tag=t.div, toc_lvl="1")
        st_write(bs.caption, "Your tutor: an AI prepared by the trainer — not the trainer.", tag=t.div)
        with st_zoom(85):
            st_write(bs.body, (bs.label, "Open a second terminal (on the right), then:"))
        with st_zoom(_CODE_ZOOM):
            st_code(s.none, code="~/ai4se/ai4se-kit/tutor", language="bash", line_numbers=False)
        with st_zoom(85):
            st_write(bs.body, (bs.label, "Then ask it:"))
        with st_zoom(_CODE_ZOOM):
            st_code(s.none, code="what are we doing this afternoon?", language="text", line_numbers=False)
        with st_zoom(85), st_block(bs.done_box):
            st_write(bs.body, (bs.done_label, "Done when: "), "it answers and cites the syllabus.")
