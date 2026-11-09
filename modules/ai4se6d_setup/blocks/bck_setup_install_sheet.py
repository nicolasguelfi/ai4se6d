"""Slide — Installation in the room: the exercise sheet (goal, steps, done when)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Installation exercise sheet styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    label = s.project.titles.label
    step_num = s.project.titles.stat
    step_name = Style.create(s.project.titles.table_cell + s.center_txt, "setup_sheet_step_name")
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "setup_cmd")
    done_box = s.project.containers.callout
    done_label = Style.create(s.bold + s.project.colors.success, "setup_done_label")
bs = BlockStyles

_STEPS = [
    ("0", "Terminal"), ("1", "opencode 2"), ("2", "Node.js"),
    ("3", "Model key"), ("4", "Course kit"), ("5", "GSE-One"),
    ("6", "GitHub"), ("7", "Check"), ("8", "@tutor"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.heading, "Installation — 75 min", tag=t.div, toc_lvl="1")
        st_write(bs.body, (bs.label, "Goal: "), "your toolchain, one step per slide.")
        with st_zoom(85), st_grid(
            cols="repeat(auto-fit, minmax(380px, 1fr))",
            gap="12px",
            cell_styles=s.project.containers.table_normal_cell,
        ) as g:
            for num, name in _STEPS:
                with g.cell():
                    st_write(bs.step_name, (bs.step_num, f"{num} · "), name, tag=t.div)
        with st_zoom(85):
            with st_block(bs.done_box):
                st_write(bs.body, (bs.done_label, "Done when: "), "the check is all green and @tutor answers you.")
            st_write(bs.body, (bs.label, "Mid-point (13:50): "), "step 4 or beyond.")
            st_write(bs.body, (bs.label, "If stuck: "), "slide → neighbour → @tutor → hand.")
