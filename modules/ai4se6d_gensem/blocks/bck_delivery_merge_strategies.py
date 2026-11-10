"""Slide — Delivering: three merge strategies and their trade-offs (CCSET14, edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Merge strategy styles."""
    heading = s.project.titles.heading
    hdr = Style.create(s.project.titles.table_header + s.center_txt, "merge_th")
    lbl = Style.create(s.project.titles.table_label + s.center_txt, "merge_tl")
    txt = s.project.titles.table_cell
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "merge_foot")
bs = BlockStyles

ROWS = [
    ("Merge commit", "every commit kept, plus a merge point", "full history, but noisy"),
    ("Squash", "the branch becomes one commit", "clean main line, details lost"),
    ("Rebase", "commits replayed on top of main", "linear history, rewritten commits"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(68):
            st_write(bs.heading, "Bringing Work to Main", tag=t.div, toc_lvl="+1", label="Merge strategies")
            with st_grid(cols="22% 40% 34%", gap="6px", cell_styles=s.project.containers.table_header_cell) as g:
                with g.cell(): st_write(bs.hdr, "Strategy")
                with g.cell(): st_write(bs.hdr, "What happens")
                with g.cell(): st_write(bs.hdr, "Trade-off")
            for name, what, trade in ROWS:
                with st_grid(cols="22% 40% 34%", gap="6px", cell_styles=s.project.containers.table_normal_cell) as g:
                    with g.cell(): st_write(bs.lbl, name)
                    with g.cell(): st_write(bs.txt, what)
                    with g.cell(): st_write(bs.txt, trade)
            st_write(bs.foot, "No right answer: choose, and say why.", tag=t.div)
