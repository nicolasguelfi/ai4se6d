"""Slide — Installation step 7: run check-learner.sh until everything is green."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Installation step slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    step = Style.create(s.project.titles.caption + s.center_txt, "setup_step_caption")
    body = s.project.titles.body
    label = s.project.titles.label
    critical = Style.create(s.bold + s.project.colors.critical, "setup_critical")
    green = Style.create(s.bold + s.project.colors.success, "setup_green")
    done_box = s.project.containers.callout
    done_label = Style.create(s.bold + s.project.colors.success, "setup_done_label")
bs = BlockStyles

_CODE_ZOOM = 190  # st_code font_size is not applied by Pygments: zoom instead
_CHECK = "sh ~/ai4se/ai4se-kit/check-learner.sh"

_NOTES = [
    ("The message",
     "One script checks the whole toolchain: check-learner.sh, shipped with the course kit (step 4)."),
    ("Red line",
     "A red line: redo that step, then run the check again — as many times as needed."),
    ("All green",
     "Show your neighbour: a second pair of eyes, and the neighbour knows you can now help."),
    ("Done when",
     "Every line is green. With the tutor answering (step 8), this is the « Done when » of the whole installation."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.step, "Installation · step 7 of 8 · ~10 min", tag=t.div)
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "7 · Check Everything", tag=t.div, toc_lvl="1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — 7 · Check Everything", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "2vh")
        with st_zoom(_CODE_ZOOM):
            st_code(s.none, code=_CHECK, language="bash", line_numbers=False)
        st_space("v", "4vh")
        with st_zoom(140):
            with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered,
                         text_align="left", item_gap=0.6) as l:
                with l.item():
                    st_write(bs.body, (bs.critical, "Red line? "), "Redo that step, run the check again.")
                with l.item():
                    st_write(bs.body, (bs.green, "All green? "), "Show your neighbour.")
            st_space("v", "4vh")
            with st_block(bs.done_box):
                st_write(bs.body, (bs.done_label, "Done when: "), "every line is green.")
