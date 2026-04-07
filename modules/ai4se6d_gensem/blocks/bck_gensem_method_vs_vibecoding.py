"""Slide — GenSEMOne vs Pure VibeCoding comparison."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Comparison slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    discussion = Style.create(
        s.project.titles.body_accent + s.center_txt,
        "gs_vs_discussion",
    )
bs = BlockStyles

_ROWS = [
    ("Requirements", '"Make me an app..."', "5\u20138 FRs with Given/When/Then"),
    ("Planning", "None", "Architecture + todo list"),
    ("Testing", '"Does it look right?"', "Automated tests per FR"),
    ("Iteration", "Big bang", "One FR per cycle"),
    ("Review", "None", "Systematic gap analysis"),
    ("Knowledge", "None", ".cursor/rules updated"),
    ("Outcome", "Working prototype (maybe)", "Verified, documented app"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.heading, "GenSEMOne vs Pure VibeCoding", tag=t.div, toc_lvl="1")
        st_space("v", 1)

        with st_grid(
            cols="25% 37.5% 37.5%",
            gap="8px",
            cell_styles=s.project.containers.cell_pad_sm,
        ) as g:
            # Header row
            with g.cell():
                with st_block(s.project.containers.table_header_cell):
                    st_write(s.project.titles.table_header, "Aspect")
            with g.cell():
                with st_block(s.project.containers.table_header_cell):
                    st_write(s.project.titles.table_header, "VibeCoding (Day 1)")
            with g.cell():
                with st_block(s.project.containers.table_header_cell):
                    st_write(s.project.titles.table_header, "GenSEMOne (Day 5\u20136)")

            for aspect, vibe, gensem in _ROWS:
                with g.cell():
                    with st_block(s.project.containers.table_normal_cell):
                        st_write(s.project.titles.table_label, aspect)
                with g.cell():
                    with st_block(s.project.containers.table_normal_cell):
                        st_write(s.project.titles.table_cell, vibe)
                with g.cell():
                    with st_block(s.project.containers.table_active_cell):
                        st_write(s.project.titles.table_cell, gensem)

        st_space("v", 2)
        with st_block(s.center_txt):
            st_write(
                bs.discussion,
                "Think back to FreeSelfApp on Day 1. What would have been different?",
            )
