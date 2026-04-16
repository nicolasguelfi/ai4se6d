"""Slide — Artifact frontmatter: how traceability is implemented in practice."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip

_pf = s.project.containers.page_fill_top
_cell = s.project.containers.cell_primary_bg + s.project.containers.cell_pad_md


class BlockStyles:
    heading = s.project.titles.slide_title + s.center_txt
    body = Style.create(s.Large + s.text.wrap.hyphens, "t3fm_body")
    keyword = Style.create(s.Large + s.bold + s.project.colors.primary, "t3fm_kw")
    accent = Style.create(s.Large + s.bold + s.project.colors.accent, "t3fm_acc")
bs = BlockStyles

_FRONTMATTER = """\
---
gse:
  type: requirement
  sprint: 1
  branch: gse/sprint-01/feat/budget
  status: draft
  complexity_cost: 2
  traces:
    derives_from: [REQ-001]
    implements: [DES-002]
    tested_by: [TST-001]
    decided_by: [DEC-003]
---"""


def build():
    st_marker("Artifact Frontmatter")
    with st_block(_pf):
        with st_block(s.center_txt):
            with st_zoom(80):
                with st_zoom(90):
                    st_write(bs.heading, "Artifact Frontmatter: Traceability", tag=t.div, toc_lvl="+1")
            st_hover_tooltip(
                title="YAML Frontmatter \u2014 Why it matters",
                entries=[
                    ("What it is", "A YAML header at the top of every artifact file (requirements, design, tests, reviews, plans). The agent generates and maintains it automatically."),
                    ("P3 \u2014 Artifacts Are Everything", "Every deliverable is tracked: code, requirements, design, tests, decisions, learning notes. The frontmatter is how P3 is implemented."),
                    ("P6 \u2014 Traceability", "The traces section links each artifact to its origin, implementation, tests, and decisions. This enables automatic impact analysis."),
                    ("You don\u2019t write it", "The agent creates and updates frontmatter. You read it to understand the traceability web and verify links."),
                ],
                scale="2vw", width="70vw", position="center",
            )
            st_space("v", 1)

        with st_grid(cols="1.5fr 2fr 2fr", gap="24px") as g:
            # Left — code block with frontmatter example
            with g.cell():
                st_code(s.none, code=_FRONTMATTER, language="yaml")

            # Center — first 5 fields
            with st_zoom(75):
                with g.cell():
                    with st_block(_cell):
                        with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                            with l.item():
                                st_write(bs.body, (bs.keyword, "type"), " \u2014 artifact kind: requirement, design, test, review, plan, compound, decision, code")
                            with l.item():
                                st_write(bs.body, (bs.keyword, "sprint"), " \u2014 which sprint produced this artifact")
                            with l.item():
                                st_write(bs.body, (bs.keyword, "branch"), " \u2014 git branch where the work happens")
                            with l.item():
                                st_write(bs.body, (bs.keyword, "status"), " \u2014 lifecycle: draft \u2192 reviewed \u2192 approved \u2192 implemented")
                            with l.item():
                                st_write(bs.body, (bs.keyword, "complexity_cost"), " \u2014 points consumed from the sprint budget")

            # Right — traces (5 fields)
            with st_zoom(80):
                with g.cell():
                    with st_block(_cell):
                        with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                            with l.item():
                                st_write(bs.body, (bs.accent, "traces"), " \u2014 the traceability web:")
                            with l.item():
                                st_write(bs.body, (bs.keyword, "derives_from"), " \u2014 origin (what requirement?)")
                            with l.item():
                                st_write(bs.body, (bs.keyword, "implements"), " \u2014 what design does it satisfy?")
                            with l.item():
                                st_write(bs.body, (bs.keyword, "tested_by"), " \u2014 which tests verify it?")
                            with l.item():
                                st_write(bs.body, (bs.keyword, "decided_by"), " \u2014 which decision shaped it?")
