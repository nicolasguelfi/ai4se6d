"""Slide — Plan: The Living Artifact (.gse/plan.yaml)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Plan artifact slide styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    label = s.project.titles.label
    closing = s.project.titles.body + s.project.colors.highlight + s.bold

bs = BlockStyles

_PLAN_YAML = """\
id: PLN-001
sprint: 2
mode: full
status: active
goal: "Budget Alerts feature"

tasks:
  - { id: TASK-010, complexity: M, branch: "gse/sprint-02/feat/alerts" }
  - { id: TASK-011, complexity: S, branch: "gse/sprint-02/feat/banner" }

budget: { total: 8, consumed: 5, remaining: 3 }

workflow:
  completed: [collect, assess, plan, reqs]
  active: design
  pending: [tests, produce, review, deliver]

coherence:
  alerts: [budget_pressure]"""


def build():
    st_marker(".gse/plan.yaml — Living Sprint Plan")
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(90):
            st_write(bs.heading, "Plan: The Living Artifact", tag=t.div, toc_lvl="+1")
        st_hover_tooltip(
            title=".gse/plan.yaml — Living Sprint Plan",
            entries=[
                ("Phase", "CE Plan = /gse:plan in GSE-One. Writes .gse/plan.yaml."),
                ("Living", "The orchestrator updates plan.yaml after every activity transition (workflow state, budget, coherence)."),
                ("Content", "Goal, tasks with branches, complexity budget, workflow tracking, coherence alerts."),
                ("Purpose", "Executable contract + live workflow state — constrains the AI during /gse:produce."),
                ("Archive", "At sprint end, DELIVER generates a read-only snapshot: docs/sprints/sprint-NN/plan-summary.md."),
            ],
            scale="2vw", width="70vw", position="center",
        )
        st_space("v", 0.5)

        with st_zoom(120):
            st_write(bs.body, (bs.label, "Example"), " — .gse/plan.yaml mid-sprint:")
            st_space("v", 0.5)

            st_code(s.none, code=_PLAN_YAML, language="yaml")

            st_space("v", 0.5)
            with st_block(s.project.containers.callout):
                st_write(
                    bs.closing,
                    "Living during the sprint — archived as plan-summary.md at delivery.",
                )
