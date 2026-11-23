"""Slide — Installation in the room: the exercise sheet (goal, steps, done when)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Installation exercise sheet styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    label = s.project.titles.label
    step_num = Style.create(s.project.titles.stat + s.center_txt, "setup_sheet_step_num")
    step_name = Style.create(s.project.titles.table_cell, "setup_sheet_step_name_left")
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "setup_cmd")
    done_box = s.project.containers.callout
    done_label = Style.create(s.bold + s.project.colors.success, "setup_done_label")
bs = BlockStyles

_STEPS = [
    ("0", "Terminal"), ("1", "opencode 2"), ("2", "Node.js"),
    ("3", "Model key"), ("4", "Course kit"), ("5", "GSE-One"),
    ("6", "GitHub"), ("7", "Check"), ("8", "Tutor window"),
]

# Text cell: vertically centred, left-aligned (NG, 2026-11-23: same recipes as the intro module)
_text_cell = Style.create(s.container.layouts.vertical_center_layout + Style("text-align:left;", "txt_left"),
                          "setup_sheet_text_cell")

_NOTES = [
    ("Trainer action",
     "Read and comment — 2 min, nothing to type yet. Present the nine steps and the 13:50 mid-point; "
     "learners start typing at step 0, on the next slide."),
    ("The message",
     "Nine steps, 0 to 8, one slide each: follow them in order, each one ends with a « Done when » check."),
    ("The goal",
     "Your toolchain: a terminal, opencode 2, Node.js, your model key, the course kit, GSE-One, GitHub, a final "
     "check, and your tutor window."),
    ("Done when",
     "The check (step 7) is all green and your tutor (step 8) answers."),
    ("Pace",
     "Mid-point at 13:50: step 4 or beyond. Behind? Say it early."),
    ("If stuck",
     "The slide, then your neighbour, then the tutor window (step 8), then raise your hand — « 3 before me »."),
    ("Ask the room",
     "« Raise your hand at each step you finish » — the trainer sees who needs help."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "Installation — 75 min", tag=t.div, toc_lvl="1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Installation — 75 min", entries=_NOTES,
                                 position="left", width="50vw")

        # Left: the 9 ordered steps as alternating rows (number | name); right: goal, done when, pace, if stuck.
        with st_grid(cols="5% 36% 4% 50% 5%", cell_styles=[s.none, s.none, s.none, _text_cell, s.none]) as g:
            with g.cell():
                pass  # left margin
            with g.cell():
                cols = "20% 80%"
                cells = s.project.containers.rows(len(_STEPS), cols, filled=(1, 2))
                with st_zoom(110), st_grid(cols=cols, gap="0.8vh 0.3vw", cell_styles=cells) as steps:
                    for num, name in _STEPS:
                        with steps.cell():
                            st_write(bs.step_num, num, tag=t.div)
                        with steps.cell():
                            st_write(bs.step_name, name, tag=t.div)
            with g.cell():
                pass
            with g.cell(), st_zoom(105):
                st_write(bs.body, (bs.label, "Goal: "), "your toolchain, one step per slide.")
                st_space("v", "4vh")
                with st_block(bs.done_box):
                    st_write(bs.body, (bs.done_label, "Done when: "),
                             "the check is all green and your tutor answers.")
                st_space("v", "4vh")
                st_write(bs.body, (bs.label, "Mid-point (13:50): "), "step 4 or beyond.")
                st_space("v", "4vh")
                st_write(bs.body, (bs.label, "If stuck: "), "slide → neighbour → tutor window (step 8) → hand.")
            with g.cell():
                pass  # right margin
