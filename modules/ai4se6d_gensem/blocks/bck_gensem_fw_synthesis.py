"""Slide — Synthesis: which framework? Comparison table."""
# @guideline: minimalist-visual + maximize-viewport
# @pattern: table-roadmap
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip

class BlockStyles:
    """Framework synthesis table styles."""
    heading = s.project.titles.slide_title + s.center_txt
    header_text = s.project.titles.table_header
    cell_text = s.project.titles.table_cell
    label = s.project.titles.table_label
    label_active = s.project.titles.table_label_active
    weak = Style.create(
        s.project.titles.table_cell + s.project.colors.critical,
        "gs_synth_weak",
    )
    discussion = Style.create(
        s.project.titles.body_accent + s.center_txt,
        "gs_synth_discussion",
    )
bs = BlockStyles

_WEAK = "\u2717"  # ✗

_HEADERS = ("Framework", "Practical", "Agile", "Tool Support", "Enterprise", "Learning")

_ROWS = [
    ("AgileGen", "\u2713", "\u2713\u2713", "\u2717", "\u2717", "Medium", False),
    ("Agentic DevOps", "\u2717", "\u2713", "\u2713\u2713", "\u2713\u2713", "High", False),
    ("SE 3.0", "\u2717", "\u2717", "\u2717", "\u2713", "High", False),
    ("V-Bounce", "\u2713", "\u2713", "\u2717", "\u2717", "Medium", False),
    ("Promptware Eng.", "\u2713\u2713", "\u2713", "\u2713", "\u2713", "Low", False),
    ("GSE-One", "\u2713\u2713", "\u2713\u2713", "\u2713\u2713", "\u2713\u2713", "Low", True),
]

def build():
    st_marker("Framework Comparison Table")
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            with st_grid(
                cols="95% 5%",
                gap="0px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    with st_zoom(75):
                        st_write(bs.heading, "Generative SE Methodologies: A Panorama", tag=t.div, toc_lvl="+1")
                with g.cell():
                    st_hover_tooltip(
                        title="Generative SE Methodologies Compared",
                        entries=[
                            ("Reading the table", "Columns rate each methodology on practicality, agility, tool support, enterprise readiness, and learning curve."),
                            ("Symbols", "\u2713\u2713 = strong, \u2713 = partial, \u2717 (red) = weak or theoretical."),
                            ("Discipline view", "These are all responses to the same emerging discipline: Generative Software Engineering. Each addresses different facets \u2014 none is complete in isolation."),
                            ("GSE-One in this training", "GSE-One is the methodology we practice here because it covers the widest scope. The principles you learn transfer to any of these frameworks."),
                        ],
                        scale="2vw", width="70vw", position="left",
                    )
            with st_zoom(95):
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
                        for val in (practical, agile, tool, enterprise, learning):
                            with g.cell():
                                _st = bs.weak if _WEAK in val else bs.cell_text
                                st_write(_st, val)

                st_space("v", 2)
                st_write(bs.discussion, "Discussion: Which methodology best fits your context? What principles are shared across all of them?")
