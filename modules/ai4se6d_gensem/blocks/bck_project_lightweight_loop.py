"""Slide — The mini-project sprint in Lightweight mode: PLAN → REQS → PRODUCE → DELIVER, milestones (edition 2).

Spec gensem §13.2 — Lightweight Mode: no TESTS / REVIEW / FIX / COMPOUND activity; a minimal test
strategy is generated at PRODUCE; DELIVER Step 1.6 runs a minimal integrity pass (devil's advocate,
at most 5 findings, HIGH findings gate the merge).
"""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Lightweight loop styles."""
    heading = s.project.titles.heading
    step = Style.create(s.project.titles.table_label + s.center_txt, "lw_loop_step")
    cmd = Style.create(s.project.titles.table_cell + s.text.fonts.font_monospace + s.project.colors.accent + s.center_txt,
                       "lw_loop_cmd")
    body = s.project.titles.body
    label = s.project.titles.label
    inline = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "lw_loop_inline")
bs = BlockStyles

STEPS = [("Plan", "/gse-plan"), ("Requirements", "/gse-reqs"), ("Production", "/gse-produce"), ("Delivery", "/gse-deliver")]


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(62):
            st_write(bs.heading, "Your Sprint, in Lightweight Mode", tag=t.div, toc_lvl="+1",
                     label="The Lightweight sprint")
            with st_grid(cols="repeat(4, 1fr)", gap="10px", cell_styles=s.project.containers.table_normal_cell) as g:
                for i, (step, cmd) in enumerate(STEPS):
                    with g.cell():
                        st_write(bs.step, step + ("  →" if i < len(STEPS) - 1 else ""), tag=t.div)
                        st_write(bs.cmd, cmd, tag=t.div)
            with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                with l.item(): st_write(bs.body, "No tests, review, fix or capitalisation step: a small test strategy "
                                        "is generated at production, and delivery runs a ", (bs.label, "minimal integrity check"),
                                        " (at most 5 findings; a HIGH one stops the merge until you decide)")
                with l.item(): st_write(bs.body, "8 to 10 complexity points; every extra idea goes to ",
                                        (bs.inline, "/gse-backlog"))
                with l.item(): st_write(bs.body, "The 3-question grid at every Gate; push before each break")
                with l.item(): st_write(bs.body, (bs.label, "Milestones"), ": day 5 16:30 plan and requirements validated · "
                                        "day 6 11:30 first delivery · 12:00 freeze")
