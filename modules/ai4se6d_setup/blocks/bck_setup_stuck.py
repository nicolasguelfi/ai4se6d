"""Slide — Stuck? 3 before me: the slide, your neighbour, @tutor, then raise your hand."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


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
    ("3", "@tutor", "once step 7 works"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.heading, "Stuck? 3 Before Me", tag=t.div, toc_lvl="1")
        st_space("v", 1)
        with st_grid(
            cols="repeat(auto-fit, minmax(260px, 1fr))",
            gap="16px",
            cell_styles=[s.project.containers.table_normal_cell] * 3 + [s.project.containers.table_active_cell],
        ) as g:
            for num, name, hint in _ORDER:
                with g.cell():
                    st_write(bs.num, num, tag=t.div)
                    st_write(bs.name, name, tag=t.div)
                    st_write(bs.hint, hint, tag=t.div)
            with g.cell():
                st_write(bs.num_last, "4", tag=t.div)
                st_write(bs.name_last, "Raise your hand", tag=t.div)
                st_write(bs.hint, "machine, key, lost work", tag=t.div)
        st_space("v", 1)
        st_write(bs.caption, "I am alone for 20 people: the first three solve most problems.", tag=t.div)
