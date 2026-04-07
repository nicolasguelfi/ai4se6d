"""Slide — Synthesis: which framework? Comparison table."""
# @guideline: maximize-viewport
# @pattern: table-roadmap
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s

class BlockStyles:
    """Framework synthesis table styles."""
    heading = s.project.titles.slide_title + s.center_txt
    header_text = s.project.titles.table_header
    cell_text = s.project.titles.table_cell
    label = s.project.titles.table_label
    label_active = s.project.titles.table_label_active
    discussion = Style.create(
        s.project.titles.body_accent + s.center_txt,
        "gs_synth_discussion",
    )
bs = BlockStyles

_HEADERS = ("Framework", "Practical", "Agile", "Tool Support", "Enterprise", "Learning")

_ROWS = [
    ("AgileGen", "\u2713", "\u2713\u2713", "\u2605", "\u2605", "Medium", False),
    ("Agentic DevOps", "\u2605", "\u2713", "\u2713\u2713", "\u2713\u2713", "High", False),
    ("SE 3.0", "\u2605", "\u2605", "\u2605", "\u2713", "High", False),
    ("V-Bounce", "\u2713", "\u2713", "\u2605", "\u2605", "Medium", False),
    ("Promptware Eng.", "\u2713\u2713", "\u2713", "\u2713", "\u2713", "Low", False),
    ("Compound Eng.", "\u2713\u2713", "\u2713\u2713", "\u2713\u2713", "\u2713\u2713", "Low", True),
]

def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(bs.heading, "Synthesis: Which Framework?", tag=t.div, toc_lvl="1")
            st_space("v", 1)

            # Header row
            with st_grid(
                cols="20% 14% 14% 14% 14% 14%",
                gap="6px",
                cell_styles=s.project.containers.table_header_cell,
            ) as g:
                for header in _HEADERS:
                    with g.cell():
                        st_write(bs.header_text, header)

            # Data rows
            for framework, practical, agile, tool, enterprise, learning, is_active in _ROWS:
                cell = s.project.containers.table_active_cell if is_active else s.project.containers.table_normal_cell
                name_style = bs.label_active if is_active else bs.label
                with st_grid(
                    cols="20% 14% 14% 14% 14% 14%",
                    gap="6px",
                    cell_styles=cell,
                ) as g:
                    with g.cell():
                        st_write(name_style, framework)
                    with g.cell():
                        st_write(bs.cell_text, practical)
                    with g.cell():
                        st_write(bs.cell_text, agile)
                    with g.cell():
                        st_write(bs.cell_text, tool)
                    with g.cell():
                        st_write(bs.cell_text, enterprise)
                    with g.cell():
                        st_write(bs.cell_text, learning)

            st_space("v", 2)
            st_write(bs.discussion, "Discussion: What matters most for your context \u2014 tool support, agility, or learning curve?")
