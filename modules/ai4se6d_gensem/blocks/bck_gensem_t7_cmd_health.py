"""Slide — /gse:health: 8-dimension project health dashboard."""
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
    body = Style.create(s.Large + s.center_txt + s.text.wrap.hyphens, "t7ch_body")
    keyword = Style.create(s.Large + s.bold + s.project.colors.primary, "t7ch_kw")
    accent = Style.create(s.Large + s.bold + s.project.colors.accent + s.center_txt, "t7ch_acc")
    highlight = Style.create(s.Large + s.bold + s.project.colors.highlight + s.center_txt, "t7ch_hl")
    critical = Style.create(s.Large + s.bold + s.project.colors.critical + s.center_txt, "t7ch_crit")
bs = BlockStyles

_DIMENSIONS = [
    ("\U0001f4cb", "REQ Coverage", "Traced REQ / total REQ"),
    ("\u2705", "Test Pass Rate", "Passing tests / total tests"),
    ("\U0001f4c9", "Design Debt", "f(HIGH\u00d72 + MED\u00d71 + LOW\u00d70.5)"),
    ("\U0001f50d", "Review Findings", "Open vs resolved count"),
    ("\U0001f4b0", "Complexity Budget", "Remaining / total points"),
    ("\U0001f517", "Traceability", "Fully traced / total tasks"),
    ("\U0001f333", "Git Hygiene", "6 sub-factors weighted"),
    ("\U0001f916", "AI Integrity", "Unverified assertions, engagement"),
]


def build():
    st_marker("/gse:health \u2014 8 Dimensions")
    with st_block(_pf):
        with st_block(s.center_txt):
            with st_zoom(90):
                st_write(bs.heading, "/gse:health \u2014 8 Dimensions", tag=t.div, toc_lvl="+1")
            st_hover_tooltip(
                title="/gse:health \u2014 Project Quality Dashboard",
                entries=[
                    ("Composite score", "0\u201310 weighted average across all 8 dimensions. Any dimension below 7/10 triggers a risk alert."),
                    ("Hard guardrail", "Health < 5 triggers a warning before /gse:deliver. You can proceed but must acknowledge the risk."),
                    ("Cross-sprint trends", "Health is tracked across sprints \u2014 you can see if quality improves or degrades over time."),
                    ("Actionable alerts", "Each alert includes a suggestion: 'Requirements coverage below 60% \u2014 consider adding tests for REQ-003 and REQ-005.'"),
                    ("Dashboard view", "Run dashboard.py for a visual view: health radar, Sprint Workflow card (completed \u2705 / active \u25b6 / pending \u25cb / skipped \u2014 with budget bar), and Coherence Alerts card when plan.yaml.coherence.alerts is non-empty."),
                    ("Git hygiene sub-factors", "Uncommitted changes, stale branches (>2 sprints), main branch status, active worktree count, branch naming compliance, backup tag freshness."),
                ],
                scale="2vw", width="70vw", position="center",
            )
            st_space("v", 1)

        with st_zoom(85):
            with st_grid(cols="repeat(auto-fit, minmax(220px, 1fr))", gap="12px") as g:
                for i, (icon, dim, formula) in enumerate(_DIMENSIONS):
                    cell_style = _cell_acc if i % 2 == 0 else _cell
                    with g.cell():
                        with st_block(cell_style):
                            st_write(bs.body, f"{icon} ", (bs.keyword, dim))
                            st_write(bs.body, formula)

            st_space("v", 1)
            st_write(bs.critical, "Any dimension < 7/10 \u2192 risk alert")
            st_write(bs.accent, "Health < 5 \u2192 warning before /gse:deliver")
