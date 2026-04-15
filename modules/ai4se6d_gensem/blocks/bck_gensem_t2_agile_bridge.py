"""Slide — Agile → GSE-One: how GSE-One adapts agile concepts."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip

_pf = s.project.containers.page_fill_top
_hdr_cell = s.project.containers.table_header_cell
_normal_cell = s.project.containers.table_normal_cell


class BlockStyles:
    heading = s.project.titles.slide_title + s.center_txt
    body = Style.create(s.Large + s.center_txt + s.text.wrap.hyphens, "t2ab_body")
    table_hdr = s.project.titles.table_header
    table_txt = s.project.titles.table_cell
    table_lbl = s.project.titles.table_label
bs = BlockStyles

_ROWS = [
    ("Sprint", "Time-boxed (2 weeks)", "Complexity-budgeted (8\u201315 pts)"),
    ("Story Points", "Effort estimation", "Complexity Points (dependency cost model)"),
    ("User Story", "As a [role], I want\u2026", "REQ- with Given/When/Then"),
    ("Retrospective", "Team reflection on process", "/gse:compound (3 axes)"),
    ("Definition of Done", "Checklist for completion", "Artifact completion + health score"),
    ("Velocity", "Points delivered per sprint", "Budget consumption rate"),
    ("Product Backlog", "Ordered wish list", "/gse:backlog (pool + sprint)"),
]


def build():
    st_marker("Agile \u2192 GSE-One")
    with st_block(_pf):
        with st_block(s.center_txt):
            st_write(bs.heading, "From Agile to GSE-One", tag=t.div, toc_lvl="+1")

            # Two tooltips side by side
            with st_grid(cols="1fr 1fr", gap="16px") as g:
                with g.cell():
                    st_hover_tooltip(
                        title="Agile Concepts \u2014 Definitions",
                        entries=[
                            ("Sprint", "A fixed-duration iteration (typically 2 weeks) during which a team delivers a potentially shippable product increment."),
                            ("Story Points", "A relative measure of effort and complexity used to estimate how much work a user story requires."),
                            ("User Story", "A short requirement written from the user\u2019s perspective: 'As a [role], I want [goal], so that [benefit].'"),
                            ("Retrospective", "A meeting at the end of each sprint where the team reflects on what went well, what didn\u2019t, and what to improve."),
                            ("Definition of Done", "A shared checklist of criteria that every work item must satisfy before it is considered complete."),
                            ("Velocity", "The average number of story points a team completes per sprint \u2014 used for capacity planning."),
                            ("Product Backlog", "An ordered list of everything the product needs \u2014 features, fixes, improvements \u2014 maintained by the Product Owner."),
                        ],
                        scale="2vw", width="70vw", position="center",
                    )
                with g.cell():
                    st_hover_tooltip(
                        title="GSE-One Adaptations \u2014 Definitions",
                        entries=[
                            ("Complexity-budgeted sprint", "Not time-boxed: the sprint ends when the complexity budget is consumed. Typical budget: 8\u201315 points. Utility dependency = 1pt, framework = 2\u20133pts, architectural change = 3\u20135pts."),
                            ("Complexity Points", "Cost model based on dependency type and risk, not relative effort. Tests, docs, and renames cost 0. Simplification earns credits (\u22121 to \u22122)."),
                            ("REQ- with Given/When/Then", "Formal requirement with unique ID (REQ-001), user story, and testable acceptance criteria in BDD format: Given [context], When [action], Then [outcome]."),
                            ("/gse:compound", "Replaces the retrospective with 3 systematic axes: Axe 1 (project patterns), Axe 2 (methodology feedback), Axe 3 (competency growth). Produces compound.md."),
                            ("Artifact completion + health", "Definition of Done becomes an 8-dimension health dashboard score. Each artifact must satisfy its type-specific checklist AND contribute to overall health > 6/10."),
                            ("Budget consumption rate", "Replaces velocity: tracks how fast the complexity budget is consumed. Warning at 80%, Gate at 100%. Overrun = debt carried to next sprint."),
                            ("/gse:backlog", "Unified backlog with pool (unplanned items, sprint: null) and sprint-assigned items. Managed as TASK- artifacts with git state tracking."),
                        ],
                        scale="2vw", width="70vw", position="center",
                    )

        with st_zoom(100):
            st_space("v", 1)

            # Header row
            with st_grid(
                cols="22% 34% 44%",
                gap="8px",
                cell_styles=_hdr_cell,
            ) as g:
                for header in ("Concept", "Agile", "GSE-One"):
                    with g.cell():
                        st_write(bs.table_hdr, header)

            # Data rows
            for concept, agile, gse in _ROWS:
                with st_grid(
                    cols="22% 34% 44%",
                    gap="8px",
                    cell_styles=_normal_cell,
                ) as g:
                    with g.cell():
                        st_write(bs.table_lbl, concept)
                    with g.cell():
                        st_write(bs.table_txt, agile)
                    with g.cell():
                        st_write(bs.table_txt, gse)
