"""Slide — The comparison grid of exercise E21: two models, the same /gse-reqs (edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Model grid styles."""
    heading = s.project.titles.heading
    hdr = Style.create(s.project.titles.table_header + s.center_txt, "model_grid_th")
    lbl = s.project.titles.table_label
    txt = Style.create(s.project.titles.table_cell + s.center_txt, "model_grid_td")
    lesson = Style.create(s.project.titles.body + s.bold + s.center_txt, "model_grid_lesson")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "model_grid_foot")
bs = BlockStyles

CRITERIA = [
    "Number of requirements",
    "Testable ones (Given / When / Then)",
    "Non-functional requirement forgotten",
    "Questions it asked you",
    "Cost (tokens, $ spent)",
]


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(64):
            st_write(bs.heading, "Two Models, One Grid", tag=t.div, toc_lvl="+1", label="E21 comparison grid")
            with st_grid(cols="44% 26% 26%", gap="6px", cell_styles=s.project.containers.table_header_cell) as g:
                with g.cell(): st_write(bs.hdr, "Criterion")
                with g.cell(): st_write(bs.hdr, "Model A (course)")
                with g.cell(): st_write(bs.hdr, "Model B (backup)")
            for criterion in CRITERIA:
                with st_grid(cols="44% 26% 26%", gap="6px", cell_styles=s.project.containers.table_normal_cell) as g:
                    with g.cell(): st_write(bs.lbl, criterion)
                    with g.cell(): st_write(bs.txt, "…")
                    with g.cell(): st_write(bs.txt, "…")
            with st_block(s.project.containers.callout):
                st_write(bs.lesson, "Compare the structure, not the words.", tag=t.div)
            st_write(bs.foot, "A: openrouter/deepseek/deepseek-v4.1-flash · B: openrouter/minimax/minimax-m3.1-flash "
                     "(switch with /models)", tag=t.div)
