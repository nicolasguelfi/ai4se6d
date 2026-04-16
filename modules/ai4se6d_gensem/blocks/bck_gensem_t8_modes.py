"""Slide — 3 Project Modes comparison table for professional project choice."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip

_pf = s.project.containers.page_fill_top
_hdr_cell = s.project.containers.table_header_cell
_normal_cell = s.project.containers.table_normal_cell
_active_cell = s.project.containers.table_active_cell


class BlockStyles:
    heading = s.project.titles.slide_title + s.center_txt
    body = Style.create(s.Large + s.center_txt + s.text.wrap.hyphens, "t8m_body")
    accent = Style.create(s.Large + s.bold + s.project.colors.accent + s.center_txt, "t8m_acc")
    table_hdr = s.project.titles.table_header
    table_txt = s.project.titles.table_cell
    table_lbl = s.project.titles.table_label
    table_lbl_act = s.project.titles.table_label_active
bs = BlockStyles

_HEADERS = ("Aspect", "Micro", "Lightweight", "Full")

_ROWS = [
    ("Lifecycle", "PRODUCE \u2192 DELIVER", "PLAN \u2192 PRODUCE \u2192 DELIVER", "LC01 \u2192 LC02 \u2192 LC03"),
    ("Git strategy", "Direct commit", "Branch-only", "Worktree per task"),
    ("State files", "status.yaml only", "4 files", "4 files + sprint docs"),
    ("Sprint artifacts", "None", "Plan only", "Full set (plan, reqs, design, review, compound)"),
    ("Health dimensions", "None", "3 dimensions", "8 dimensions"),
    ("Decisions", "Gate-only", "Auto + Gate", "Auto / Inform / Gate"),
    ("Guardrails", "Not enforced", "Hard (mandatory)", "Hard + Soft + Emergency"),
    ("Complexity budget", "Not tracked", "Not tracked", "Tracked (8\u201315 pts)"),
]


def build():
    st_marker("Choose Your Mode")
    with st_block(_pf):
        with st_block(s.center_txt):
            with st_zoom(90):
                st_write(bs.heading, "Choose Your Mode", tag=t.div, toc_lvl="+1")
            st_hover_tooltip(
                title="3 Modes \u2014 Choose Based on Project Scope",
                entries=[
                    ("Micro", "For <3 files: prototypes, quick experiments, learning exercises. Minimal overhead."),
                    ("Lightweight", "For 3-4 files: internal tools, small features. Adds planning and branch isolation."),
                    ("Full", "For \u22655 files: production systems, team projects. Complete lifecycle with all guardrails and traceability."),
                    ("How to choose", "Start Lightweight for your professional project. Escalate to Full when you need requirements, review, or full traceability. The agent proposes the mode during /gse:go."),
                    ("Adopt mode", "For existing projects: /gse:go --adopt performs a non-destructive scan and creates a sprint-0 baseline without modifying any files."),
                ],
                scale="2vw", width="70vw", position="center",
            )

        with st_zoom(80):
            st_space("v", 1)

            # Header row
            with st_grid(cols="20% 22% 26% 32%", gap="6px", cell_styles=_hdr_cell) as g:
                for header in _HEADERS:
                    with g.cell():
                        st_write(bs.table_hdr, header)

            # Data rows
            for aspect, micro, light, full in _ROWS:
                with st_grid(cols="20% 22% 26% 32%", gap="6px", cell_styles=_normal_cell) as g:
                    with g.cell():
                        st_write(bs.table_lbl, aspect)
                    with g.cell():
                        st_write(bs.table_txt, micro)
                    with g.cell():
                        st_write(bs.table_txt, light)
                    with g.cell():
                        st_write(bs.table_lbl_act, full)

            st_space("v", 1)
            st_write(bs.accent, "Start Lightweight. Escalate to Full when complexity demands it.")
