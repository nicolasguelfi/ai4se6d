"""Slide — What You Will Be Able to Do: six observable objectives of the 6-day course.

Edition 2 (board peda1, P20): real objectives shown on day 1, each tied to the days that build it,
plus the framing line (the published programme mentions Cursor; this edition uses opencode).
"""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


_page_fill = s.project.containers.page_fill_top

_card = Style.create(
    s.project.containers.cell_primary_bg + s.project.containers.cell_pad_md,
    "obj_card",
)
_frame = Style.create(
    s.project.containers.callout + s.center_txt,
    "obj_frame",
)


class BlockStyles:
    """Slide: objectives — 3x2 grid of cards + framing callout."""
    heading = s.project.titles.section_title + s.center_txt
    days = Style.create(
        s.project.colors.highlight + s.bold + s.text.sizes.pt22,
        "obj_days",
    )
    verb = Style.create(
        s.project.colors.accent + s.bold + s.text.sizes.pt24,
        "obj_verb",
    )
    detail = Style.create(
        s.text.sizes.pt22,
        "obj_detail",
    )
    frame = Style.create(s.text.sizes.pt24, "obj_frame_text")
    frame_key = Style.create(
        s.text.sizes.pt24 + s.bold + s.project.colors.primary, "obj_frame_key",
    )


bs = BlockStyles

# (days, objective, how you will show it)
_OBJECTIVES = [
    ("Days 1-2", "Drive a coding agent with discipline",
     "give a precise task, read its plan, approve or refuse each action"),
    ("Day 2", "Plan, build, test and review a small app with an AI agent",
     "CalcApp v0.1: your plan, your tests, an AI review you triage"),
    ("Day 2 →", "Use git as your safety net",
     "commit, branch, compare, go back to a known-good tag"),
    ("Days 3-4", "Run a structured AI-assisted lifecycle with GSE-One",
     "requirements → plan → build → review → deliver, on CalcApp"),
    ("Day 4", "Measure quality instead of trusting the agent's word",
     "lint, tests and CI give a green/red signal you can check"),
    ("Days 5-6", "Ship and present a mini-project",
     "scope, milestones, deployment, gallery demo"),
]

_NOTES = [
    ("Message", "These are the six things you can check at the end of day 6 — not topics, abilities."),
    ("Cursor vs opencode", "Say it once: the concepts (agent loop, plan, permissions, context files) "
                           "are the same in every coding agent."),
]


def build():
    with st_block(_page_fill):
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell():
                st_write(bs.heading, "What You Will Be Able to Do", tag=t.div, toc_lvl="1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — objectives", entries=_NOTES, position="left", width="45vw")

        with st_grid(cols="1fr 1fr 1fr", gap="16px", cell_styles=_card) as g:
            for days, verb, detail in _OBJECTIVES:
                with g.cell():
                    st_write(bs.days, days, tag=t.div)
                    st_write(bs.verb, verb, tag=t.div)
                    st_write(bs.detail, detail, tag=t.div)

        with st_block(_frame):
            st_write(
                bs.frame,
                "The published programme mentions Cursor. This edition uses ",
                (bs.frame_key, "opencode"),
                ": open-source, provider-agnostic, in the terminal. "
                "Same concepts — the skills transfer to any coding agent.",
            )
