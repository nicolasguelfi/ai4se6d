"""Slide — Stuck? 3 before me: the slide, your neighbour, your tutor window, then raise your hand."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Stuck slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    num = Style.create(s.project.titles.section_title + s.project.colors.primary + s.center_txt, "setup_stuck_num")
    num_last = Style.create(s.project.titles.section_title + s.project.colors.highlight + s.center_txt, "setup_stuck_num_last")
    name = Style.create(s.project.titles.body_accent + s.center_txt, "setup_stuck_name")
    name_last = Style.create(s.project.titles.subtitle + s.center_txt, "setup_stuck_name_last")
    hint = Style.create(s.project.titles.table_cell + s.center_txt, "setup_stuck_hint")
    caption = Style.create(s.project.titles.caption + s.center_txt, "setup_stuck_caption")
bs = BlockStyles

_ORDER = [
    ("1", "The slide", "reread the step and its “Done when”"),
    ("2", "Your neighbour", "two pairs of eyes"),
    ("3", "Tutor window", "once step 8 works"),
]

_NOTES = [
    ("The message",
     "« 3 before me »: before raising your hand, try the slide, your neighbour, your tutor window — in that order."),
    ("Why",
     "One trainer for 20 people: the first three solve most problems, and the hand stays free for the problems "
     "only the trainer can solve."),
    ("The slide",
     "Reread the step and its « Done when »: most blockers are a skipped line or a terminal not reopened."),
    ("Raise your hand",
     "Right away for a machine problem, a key problem or lost work — do not wait."),
    ("Ask the room",
     "« Who is already all green? » — they become the neighbours of step 2."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "Stuck? 3 Before Me", tag=t.div, toc_lvl="1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Stuck? 3 Before Me", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "10vh")
        # Four ordered cards between 5 % outer margins (NG, 2026-11-23)
        card = s.project.containers.table_normal_cell
        with st_zoom(112), st_grid(
            cols="5% 1fr 1fr 1fr 1fr 5%",
            gap="16px",
            cell_styles=[s.none, card, card, card, s.project.containers.table_active_cell, s.none],
        ) as g:
            with g.cell():
                pass  # left margin
            for num, name, hint in _ORDER:
                with g.cell():
                    st_write(bs.num, num, tag=t.div)
                    st_write(bs.name, name, tag=t.div)
                    st_write(bs.hint, hint, tag=t.div)
            with g.cell():
                st_write(bs.num_last, "4", tag=t.div)
                st_write(bs.name_last, "Raise your hand", tag=t.div)
                st_write(bs.hint, "machine, key, lost work", tag=t.div)
            with g.cell():
                pass  # right margin
        st_space("v", "12vh")
        with st_zoom(130):
            st_write(bs.caption, "I am alone for 20 people: the first three solve most problems.", tag=t.div)
