"""Slide — Ambiguity: words that hide decisions (CCSET10, edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Ambiguity styles."""
    heading = s.project.titles.heading
    hdr = Style.create(s.project.titles.table_header + s.center_txt, "ambiguity_th")
    word = Style.create(s.project.titles.table_label + s.center_txt, "ambiguity_word")
    txt = s.project.titles.table_cell
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "ambiguity_foot")
bs = BlockStyles

ROWS = [
    ("\"monthly\"", "calendar month, or the last 30 days?"),
    ("\"category\"", "a fixed list, or free text the user types?"),
    ("\"amount\"", "which currency? negative for refunds? how many decimals?"),
    ("\"delete\"", "gone for ever, or recoverable?"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(72):
            st_write(bs.heading, "Ambiguity Hides Decisions", tag=t.div, toc_lvl="+1", label="Ambiguity")
            with st_grid(cols="26% 70%", gap="6px", cell_styles=s.project.containers.table_header_cell) as g:
                with g.cell(): st_write(bs.hdr, "The word")
                with g.cell(): st_write(bs.hdr, "The decision it hides")
            for word, decision in ROWS:
                with st_grid(cols="26% 70%", gap="6px", cell_styles=s.project.containers.table_normal_cell) as g:
                    with g.cell(): st_write(bs.word, word)
                    with g.cell(): st_write(bs.txt, decision)
            st_write(bs.foot, "If you do not decide, the agent decides — silently.", tag=t.div)
