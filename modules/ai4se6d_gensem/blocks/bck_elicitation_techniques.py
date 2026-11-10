"""Slide — Elicitation techniques: when to use which (Zowghi & Coulin) (CCSET10, edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Elicitation techniques styles."""
    heading = s.project.titles.heading
    hdr = Style.create(s.project.titles.table_header + s.center_txt, "techniques_th")
    lbl = Style.create(s.project.titles.table_label + s.center_txt, "techniques_tl")
    txt = s.project.titles.table_cell
    source = s.project.citation + s.large + s.center_txt
bs = BlockStyles

ROWS = [
    ("Interview", "goals, context, the \"why\"", "people say what they think they do"),
    ("Observation", "the real work, tacit habits", "slow; being watched changes behaviour"),
    ("Workshop", "conflicts between stakeholders", "the loudest voice wins"),
    ("Questionnaire", "many users, simple facts", "no follow-up question"),
    ("Scenarios", "concrete steps, exceptions", "misses the rare cases"),
    ("Prototype", "\"I'll know it when I see it\"", "the mock-up becomes the product"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(62):
            st_write(bs.heading, "Elicitation Techniques", tag=t.div, toc_lvl="+1", label="Elicitation techniques")
            with st_grid(cols="20% 38% 38%", gap="6px", cell_styles=s.project.containers.table_header_cell) as g:
                with g.cell(): st_write(bs.hdr, "Technique")
                with g.cell(): st_write(bs.hdr, "Best for")
                with g.cell(): st_write(bs.hdr, "Watch out")
            for name, best, limit in ROWS:
                with st_grid(cols="20% 38% 38%", gap="6px", cell_styles=s.project.containers.table_normal_cell) as g:
                    with g.cell(): st_write(bs.lbl, name)
                    with g.cell(): st_write(bs.txt, best)
                    with g.cell(): st_write(bs.txt, limit)
            st_write(bs.source, "Combine several techniques — ", cite("zowghi-coulin-elicitation2005"), tag=t.div)
