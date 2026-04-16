"""Slide — /gse:pause + /gse:resume: session continuity."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip

_pf = s.project.containers.page_fill_top
_cell = s.project.containers.cell_primary_bg + s.project.containers.cell_pad_md + s.center_txt
_cell_acc = s.project.containers.cell_accent_bg + s.project.containers.cell_pad_md + s.center_txt


class BlockStyles:
    heading = s.project.titles.slide_title + s.center_txt
    body = Style.create(s.Large + s.center_txt + s.text.wrap.hyphens, "t2cpr_body")
    keyword = Style.create(s.Large + s.bold + s.project.colors.primary, "t2cpr_kw")
    accent = Style.create(s.Large + s.bold + s.project.colors.accent + s.center_txt, "t2cpr_acc")
bs = BlockStyles


def build():
    st_marker("/gse:pause + /gse:resume")
    with st_block(_pf):
        with st_block(s.center_txt):
            with st_zoom(90):
                st_write(bs.heading, "/gse:pause + /gse:resume", tag=t.div, toc_lvl="+1")
            st_hover_tooltip(
                title="Session Continuity \u2014 Never Lose Work",
                entries=[
                    ("/gse:pause", "Auto-commits all uncommitted work (WIP), saves a comprehensive checkpoint: context, sprint state, pending tasks, review findings, decision log, worktree map."),
                    ("/gse:resume", "Reloads the checkpoint, verifies worktree integrity, briefs you on where work stopped, and proposes next actions."),
                    ("Checkpoint contents", "Context state, sprint artifacts, pending task list, review findings, decision log snapshot, worktree map \u2014 everything needed to continue seamlessly."),
                    ("Living plan aware", "/gse:resume reads .gse/plan.yaml to show the workflow trajectory: active activity, pending items, completed count, and coherence alerts. workflow.active is the primary signal for the next-action proposal."),
                    ("Cross-cutting", "Available at any phase. Use /gse:pause before closing your session, /gse:resume when you return."),
                ],
                scale="2vw", width="70vw", position="center",
            )
            st_space("v", 1)

        with st_zoom(90):
            with st_grid(cols="1fr 1fr", gap="24px") as g:
                with g.cell():
                    with st_block(_cell_acc):
                        st_write(bs.keyword + s.center_txt, "/gse:pause")
                        st_space("v", 1)
                        st_write(bs.body, "\u2705 Auto-commit all WIP")
                        st_write(bs.body, "\U0001f4be Save full checkpoint")
                        st_write(bs.body, "\U0001f5c2\ufe0f Snapshot worktree map")
                        st_write(bs.body, "\U0001f4cb Capture decision log")
                with g.cell():
                    with st_block(_cell):
                        st_write(bs.keyword + s.center_txt, "/gse:resume")
                        st_space("v", 1)
                        st_write(bs.body, "\U0001f504 Reload checkpoint")
                        st_write(bs.body, "\U0001f50d Verify worktree integrity")
                        st_write(bs.body, "\U0001f4dd Brief: where you stopped")
                        st_write(bs.body, "\U0001f5fa\ufe0f Show workflow trajectory")
                        st_write(bs.body, "\U0001f449 Propose next actions")
