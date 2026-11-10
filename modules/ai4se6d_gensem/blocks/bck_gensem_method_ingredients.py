"""Slide — What a generative software engineering method (GenSEM) must define (CCSET09, edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Method ingredients styles."""
    heading = s.project.titles.heading
    hdr = Style.create(s.project.titles.table_header + s.center_txt, "ingredients_th")
    lbl = Style.create(s.project.titles.table_label + s.center_txt, "ingredients_tl")
    txt = s.project.titles.table_cell
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "ingredients_foot")
bs = BlockStyles

ROWS = [
    ("Lifecycle", "the activities and their order: from the idea to delivery, then learning"),
    ("Artefacts", "what is written down: requirements, plan, design, tests, decisions"),
    ("Roles", "what the human decides, what the agent may do alone"),
    ("Decision rules", "which decisions need a human, with which information"),
    ("Quality gates", "the checks before moving on: tests, review, evidence"),
    ("Learning", "how lessons of one cycle improve the next"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(70):
            st_write(bs.heading, "What a GenSEM Must Define", tag=t.div, toc_lvl="+1", label="Ingredients of a GenSEM")
            with st_grid(cols="26% 70%", gap="6px", cell_styles=s.project.containers.table_header_cell) as g:
                with g.cell(): st_write(bs.hdr, "Ingredient")
                with g.cell(): st_write(bs.hdr, "The question it answers")
            for name, question in ROWS:
                with st_grid(cols="26% 70%", gap="6px", cell_styles=s.project.containers.table_normal_cell) as g:
                    with g.cell(): st_write(bs.lbl, name)
                    with g.cell(): st_write(bs.txt, question)
            st_write(bs.foot, "Your own GenSEM can be small. It cannot be implicit.", tag=t.div)
