"""Slide — Debrief: this afternoon's experience in this morning's words (cycles 01-03, edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Debrief — link to the morning cycles."""
    heading = s.project.titles.heading
    table_hdr = Style.create(s.project.titles.table_header + s.center_txt, "setup_cycles_th")
    table_txt = Style.create(s.project.titles.table_cell + s.center_txt, "setup_cycles_td")
    table_lbl = Style.create(s.project.titles.table_label + s.center_txt, "setup_cycles_tl")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "setup_cycles_foot")
bs = BlockStyles

ROWS = [
    ("You had to explain your app again", "The model has no memory", "CCSET01"),
    ("The agent did more than you asked", "Autonomy needs a human in the loop", "CCSET02"),
    ("It works — would you ship it?", "VibeCoding is not engineering", "CCSET02"),
    ("Your key, its permissions, what you pasted", "Practical rules, the AI Act", "CCSET03"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(75):
            st_write(bs.heading, "Back to This Morning", tag=t.div, toc_lvl="1", label="Debrief — link to the cycles")
            with st_grid(cols="42% 40% 14%", gap="6px", cell_styles=s.project.containers.table_header_cell) as g:
                with g.cell(): st_write(bs.table_hdr, "This afternoon")
                with g.cell(): st_write(bs.table_hdr, "This morning's idea")
                with g.cell(): st_write(bs.table_hdr, "Cycle")
            for lived, idea, cycle in ROWS:
                with st_grid(cols="42% 40% 14%", gap="6px", cell_styles=s.project.containers.table_normal_cell) as g:
                    with g.cell(): st_write(bs.table_lbl, lived)
                    with g.cell(): st_write(bs.table_txt, idea)
                    with g.cell(): st_write(bs.table_txt, cycle)
            st_write(bs.foot, "Tomorrow: the same app idea, engineered — by hand, on CalcApp.", tag=t.div)
