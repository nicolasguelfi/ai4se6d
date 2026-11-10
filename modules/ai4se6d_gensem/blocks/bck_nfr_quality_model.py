"""Slide — The ISO/IEC 25010:2023 product quality model, nine characteristics (CCSET11, edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Quality model styles."""
    heading = s.project.titles.heading
    name = Style.create(s.project.titles.table_label + s.center_txt, "quality_model_name")
    hint = Style.create(s.project.titles.table_cell + s.center_txt, "quality_model_hint")
    source = s.project.citation + s.large + s.center_txt
bs = BlockStyles

CHARACTERISTICS = [
    ("Functional suitability", "complete, correct"),
    ("Performance efficiency", "time, resources"),
    ("Compatibility", "coexists, exchanges"),
    ("Interaction capability", "learnable, accessible"),
    ("Reliability", "available, recovers"),
    ("Security", "confidential, accountable"),
    ("Maintainability", "modular, testable"),
    ("Flexibility", "adaptable, installable"),
    ("Safety", "no harm to people"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(62):
            st_write(bs.heading, "A Checklist of Qualities", tag=t.div, toc_lvl="+1", label="ISO/IEC 25010 quality model")
            with st_grid(cols="repeat(auto-fit, minmax(330px, 1fr))", gap="12px",
                         cell_styles=s.project.containers.table_normal_cell) as g:
                for name, hint in CHARACTERISTICS:
                    with g.cell():
                        st_write(bs.name, name, tag=t.div)
                        st_write(bs.hint, hint, tag=t.div)
            st_write(bs.source, "Nine product quality characteristics — ", cite("iso25010-2023"), tag=t.div)
