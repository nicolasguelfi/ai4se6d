"""Slide — Living Plan: coherence monitoring & non-blocking alerts."""
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
    body = Style.create(s.Large + s.center_txt + s.text.wrap.hyphens, "cpl_body")
    keyword = Style.create(s.Large + s.bold + s.project.colors.primary, "cpl_kw")
    accent = Style.create(s.Large + s.bold + s.project.colors.accent + s.center_txt, "cpl_acc")
    label = Style.create(s.Large + s.bold + s.project.colors.primary + s.center_txt, "cpl_lbl")

bs = BlockStyles

_ALERTS = [
    ("\u26a0\ufe0f", "budget_pressure", ">80% consumed with tasks remaining"),
    ("\U0001f3af", "scope_drift", ">50% of original tasks changed"),
    ("\u23f1\ufe0f", "velocity_risk", "Pace suggests sprint won't complete"),
]


def build():
    st_marker("Living Plan \u2014 Coherence Monitoring")
    with st_block(_pf):
        with st_block(s.center_txt):
            with st_grid(
                cols="95% 5%",
                gap="0px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    with st_zoom(90):
                        st_write(bs.heading, "Living Plan \u2014 Coherence Monitoring", tag=t.div, toc_lvl="+1")
                with g.cell():
                    st_hover_tooltip(
                        title="Coherence Monitoring \u2014 Inform, Never Block",
                        entries=[
                            ("Living update", "After every activity transition, the orchestrator updates .gse/plan.yaml: workflow state, budget consumed, and coherence checks."),
                            ("3 alerts", "budget_pressure (>80% consumed), significant_scope_drift (>50% tasks changed since PLAN), velocity_risk (current pace won't complete the sprint)."),
                            ("Scope changes log", "coherence.scope_changes[] records every mutation with timestamp, trigger, description, and budget impact \u2014 auditable history."),
                            ("Inform-tier only", "Alerts never block the workflow. They surface as 1-line informations (Full mode) or silent (Micro mode). Quality guardrails remain Hard tier."),
                            ("Tactical replan", "When an alert fires, the orchestrator may suggest /gse:plan --tactical to realign scope \u2014 user decides."),
                        ],
                        scale="2vw", width="70vw", position="left",
                    )
            st_space("v", 1)

            with st_zoom(110):
                cell_styles = [_cell_act, _cell_acc, _cell]
                with st_grid(cols="repeat(auto-fit, minmax(260px, 1fr))", gap="16px") as g:
                    for (icon, name, desc), cell_s in zip(_ALERTS, cell_styles):
                        with g.cell():
                            with st_block(cell_s):
                                st_write(bs.label, f"{icon} {name}")
                                st_space("v", 0.3)
                                st_write(bs.body, desc)

                st_space("v", 1)
                st_write(bs.accent, "Inform-tier only \u2014 observes, never blocks.")
