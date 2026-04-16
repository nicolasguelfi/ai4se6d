"""Slide — /gse:review: multi-perspective review with devil's advocate."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip

_pf = s.project.containers.page_fill_top
_cell = s.project.containers.cell_primary_bg + s.project.containers.cell_pad_md + s.center_txt
_cell_acc = s.project.containers.cell_accent_bg + s.project.containers.cell_pad_md + s.center_txt
_cell_act = s.project.containers.cell_active_bg + s.project.containers.cell_pad_md + s.center_txt


class BlockStyles:
    heading = s.project.titles.slide_title + s.center_txt
    body = Style.create(s.Large + s.center_txt + s.text.wrap.hyphens, "t6crv_body")
    keyword = Style.create(s.Large + s.bold + s.project.colors.primary, "t6crv_kw")
    accent = Style.create(s.Large + s.bold + s.project.colors.accent + s.center_txt, "t6crv_acc")
    highlight = Style.create(s.Large + s.bold + s.project.colors.highlight + s.center_txt, "t6crv_hl")
bs = BlockStyles

_AGENTS = [
    ("\U0001f50d", "requirements-analyst", "Completeness"),
    ("\U0001f3d7\ufe0f", "architect", "Structure"),
    ("\U0001f4dd", "code-reviewer", "Quality"),
    ("\U0001f6e1\ufe0f", "security-auditor", "Vulnerabilities"),
    ("\U0001f464", "ux-advocate", "Experience"),
    ("\U0001f608", "devil-advocate", "Self-critique (P16)"),
]


def build():
    st_marker("/gse:review")
    with st_block(_pf):
        with st_block(s.center_txt):
            with st_zoom(90):
                st_write(bs.heading, "/gse:review \u2014 Challenge Everything", tag=t.div, toc_lvl="+1")
            st_hover_tooltip(
                title="/gse:review \u2014 6 Perspectives",
                entries=[
                    ("Branch diff", "Review operates on git diff sprint-branch...feature-branch, not just file state. This ensures only sprint changes are reviewed."),
                    ("All artefact types", "Requirements, design, code, tests, docs \u2014 complete review of the current sprint."),
                    ("Devil\u2019s advocate (P16)", "The agent challenges its own productions: hunts hallucinations, verifies libraries/APIs exist, questions assumptions."),
                    ("RVW- findings", "Each finding gets a RVW- ID with severity. Findings auto-populate the backlog for /gse:fix."),
                    ("Cross-sprint regression", "Full test suite runs; tests that passed last sprint but fail now are flagged [REGRESSION] HIGH."),
                    ("Health update", "Health score is recalculated after review."),
                ],
                scale="2vw", width="70vw", position="center",
            )
            st_space("v", 1)

        with st_zoom(85):
            with st_grid(cols="repeat(auto-fit, minmax(200px, 1fr))", gap="12px") as g:
                for i, (icon, agent, focus) in enumerate(_AGENTS):
                    cell_style = _cell_act if agent == "devil-advocate" else (_cell_acc if i % 2 == 0 else _cell)
                    with g.cell():
                        with st_block(cell_style):
                            st_write(bs.body, f"{icon} ", (bs.keyword, agent))
                            st_write(bs.body, focus)

            st_space("v", 1)
            st_write(bs.highlight, "The agent reviews its own work \u2014 and challenges its own assumptions.")
