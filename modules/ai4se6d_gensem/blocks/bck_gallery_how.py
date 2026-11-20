"""Slide — How the gallery works: two rotations, half presents, half visits (open point 10, edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Gallery styles."""
    heading = s.project.titles.heading
    hdr = Style.create(s.project.titles.table_header + s.center_txt, "gallery_th")
    lbl = Style.create(s.project.titles.table_label + s.center_txt, "gallery_tl")
    txt = Style.create(s.project.titles.table_cell + s.center_txt, "gallery_td")
    body = Style.create(s.project.titles.body + s.center_txt, "gallery_body")
    label = s.project.titles.label
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "gallery_foot")
bs = BlockStyles

ROWS = [
    ("13:45", "prepare", "prepare"),
    ("14:00 — rotation 1", "present", "visit"),
    ("14:45 — rotation 2", "visit", "present"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(66):
            st_write(bs.heading, "The Gallery", tag=t.div, toc_lvl="1", label="Gallery demos")
            with st_grid(cols="36% 30% 30%", gap="6px", cell_styles=s.project.containers.table_header_cell) as g:
                with g.cell(): st_write(bs.hdr, "When")
                with g.cell(): st_write(bs.hdr, "Half A")
                with g.cell(): st_write(bs.hdr, "Half B")
            for when, a, b in ROWS:
                with st_grid(cols="36% 30% 30%", gap="6px", cell_styles=s.project.containers.table_normal_cell) as g:
                    with g.cell(): st_write(bs.lbl, when)
                    with g.cell(): st_write(bs.txt, a)
                    with g.cell(): st_write(bs.txt, b)
            with st_block(s.project.containers.callout):
                st_write(bs.body, (bs.label, "5-7 minutes, at your laptop: "),
                         "the problem · the product, live · one GSE moment · one lesson · questions", tag=t.div)
            st_write(bs.foot, "You give your demo again to each new group of visitors.", tag=t.div)
