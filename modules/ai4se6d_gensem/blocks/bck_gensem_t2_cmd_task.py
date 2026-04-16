"""Slide — /gse:task: ad-hoc tasks and spike experiments."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip

_pf = s.project.containers.page_fill_top
_cell = s.project.containers.cell_primary_bg + s.project.containers.cell_pad_md + s.center_txt
_cell_acc = s.project.containers.cell_accent_bg + s.project.containers.cell_pad_md + s.center_txt
_cell_act = s.project.containers.cell_active_bg + s.project.containers.cell_pad_md + s.center_txt


class BlockStyles:
    heading = s.project.titles.slide_title + s.center_txt
    body = Style.create(s.Large + s.center_txt + s.text.wrap.hyphens, "t2ct_body")
    keyword = Style.create(s.Large + s.bold + s.project.colors.primary, "t2ct_kw")
    accent = Style.create(s.Large + s.bold + s.project.colors.accent + s.center_txt, "t2ct_acc")
    highlight = Style.create(s.Large + s.bold + s.project.colors.highlight + s.center_txt, "t2ct_hl")
bs = BlockStyles


def build():
    st_marker("/gse:task")
    with st_block(_pf):
        with st_block(s.center_txt):
            with st_zoom(90):
                st_write(bs.heading, "/gse:task \u2014 Ad-hoc Work & Spikes", tag=t.div, toc_lvl="+1")
            st_hover_tooltip(
                title="/gse:task \u2014 Outside the Standard Lifecycle",
                entries=[
                    ("Ad-hoc task", "Execute a task outside the planned sprint. Creates branch + worktree, adds to backlog, consumes complexity budget. Reviewed during next /gse:review unless trivial (\u2264 1 pt)."),
                    ("--spike option", "Exploratory experiment on any artefact (code, docs, reorg, decision\u2026): produced work is discarded, only the DEC- decision survives. Max 3 pts, non-deliverable (branch deleted after), bypasses REQS/TESTS guardrails. MUST produce a DEC- artifact documenting question, approach, and answer."),
                    ("Spike for beginners", "Gate confirmation: 'This is an experiment \u2014 the code won't be kept. Are you sure?' Prevents confusion between spike and real work."),
                    ("If spike yields reusable code", "A normal TASK must be created to implement it properly with full REQS/TESTS. The spike DEC- artifact traces the origin."),
                    ("Cross-cutting", "Available at any phase. The orchestrator (/gse:go) may suggest a spike when it detects technical uncertainty."),
                ],
                scale="2vw", width="70vw", position="center",
            )
            st_space("v", 1)

        with st_zoom(90):
            with st_grid(cols="1fr 1fr", gap="24px") as g:
                with g.cell():
                    with st_block(_cell):
                        st_write(bs.keyword + s.center_txt, "/gse:task")
                        st_space("v", 1)
                        st_write(bs.body, "Branch + worktree created")
                        st_write(bs.body, "Added to backlog (TASK-)")
                        st_write(bs.body, "Consumes complexity budget")
                        st_write(bs.body, "Reviewed at next /gse:review")
                        st_write(bs.body, "Delivered with sprint \u2014 any artefact (code, docs, rename, \u2026)")
                with g.cell():
                    with st_block(_cell_act):
                        st_write(bs.highlight, "/gse:task --spike")
                        st_space("v", 1)
                        st_write(bs.body, "Max 3 complexity points")
                        st_write(bs.body, "Non-deliverable (branch deleted)")
                        st_write(bs.body, "Bypasses REQS/TESTS")
                        st_write(bs.body, "MUST produce DEC- artifact")
                        st_write(bs.body, "Only the DEC- survives \u2014 whatever the artefact")
