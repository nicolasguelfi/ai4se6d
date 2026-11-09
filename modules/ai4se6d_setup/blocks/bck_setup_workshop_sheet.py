"""Slide — FreeSelfApp exercise sheet: done when, mid-point, if stuck, debrief."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Workshop exercise sheet styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    label = s.project.titles.label
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "setup_cmd")
    done_box = s.project.containers.callout
    done_label = Style.create(s.bold + s.project.colors.success, "setup_done_label")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.heading, "Exercise Sheet", tag=t.div, toc_lvl="1")
        with st_zoom(85):
            st_write(bs.body, (bs.label, "Goal: "), "your small web app, by prompting only.", tag=t.div)
            with st_block(bs.done_box):
                st_write(
                    bs.body,
                    (bs.done_label, "Done when: "),
                    "it opens in the browser, does one thing you wanted, and ",
                    (bs.cmd, "git log"), " shows 2+ commits.",
                )
            st_write(bs.body, (bs.label, "Mid-point (15:15): "), "it opens + 1 commit.", tag=t.div)
            st_write(bs.body, (bs.label, "If stuck: "), "rephrase → paste the error → @tutor → hand.", tag=t.div)
            st_write(bs.body, (bs.label, "Debrief (16:15): "), "your notes + one example.", tag=t.div)
