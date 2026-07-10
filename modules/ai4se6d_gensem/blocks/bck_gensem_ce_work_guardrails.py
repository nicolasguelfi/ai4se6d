"""Slide — Work: Scope & Quality Guardrails."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Work guardrails slide styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    closing = s.project.titles.body + s.project.colors.highlight + s.bold

bs = BlockStyles


def build():
    st_marker("Work Guardrails: Strategy Before, Reconciliation After")
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(90):
            st_write(bs.heading, "Work: Scope & Quality Guardrails", tag=t.div, toc_lvl="+1")
        st_hover_tooltip(
            title="Scope & Quality Guardrails",
            entries=[
                ("Purpose", "Guardrails keep the AI agent within the planned scope as governance -- no silent scope expansion (P6). There is no file-by-file real-time blocking."),
                ("Rendez-vous", "Strategy is checked before production; scope is reconciled deterministically after, at activity closure -- via git diff against the approved plan."),
                ("Testing", "The test strategy is configurable (auto / tdd / test-after) -- TDD is an option, not a rule. The canonical test run happens after production."),
            ],
            scale="2vw", width="70vw", position="center",
        )
        st_space("v", 1)

        with st_zoom(120):
            with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.ordered) as l:
                with l.item():
                    st_write(
                        bs.body,
                        (bs.keyword, "Before production: "),
                        "Test strategy must exist -- Hard guardrail in Full mode, "
                        "auto-generated Soft in Lightweight; budget watched (Soft 80%, Gate 100%)",
                    )
                with l.item():
                    st_write(
                        bs.body,
                        (bs.keyword, "During: "),
                        "Agent executes within the approved plan, progress visible in plan.yaml -- "
                        "scope cannot expand silently, but no per-file blocking",
                    )
                with l.item():
                    st_write(
                        bs.body,
                        (bs.keyword, "After (the real rendez-vous): "),
                        "Canonical test run, then Scope Reconciliation -- git diff vs plan; "
                        "deltas (ADDED / OMITTED / MODIFIED) hit a Gate: "
                        "Accept as DEC- / Revert / Amend REQ-DES / Discuss",
                    )
                with l.item():
                    st_write(
                        bs.body,
                        (bs.keyword, "Safety nets: "),
                        "Review's requirements-analyst flags scope creep; "
                        "re-planning is proposed on triggers (task > 2x estimate, budget > 80%...) -- never forced",
                    )

            st_space("v", 2)

            with st_block(s.project.containers.callout):
                st_write(
                    bs.closing,
                    "Example: the diff shows a file ADDED out of scope → the closure Gate "
                    "asks you to accept it (DEC-), revert it, amend the requirements, or discuss.",
                )
