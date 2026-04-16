"""Slide — /gse:go: orchestrate the full lifecycle automatically."""
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
    body = Style.create(s.Large + s.center_txt + s.text.wrap.hyphens, "t2cgo_body")
    keyword = Style.create(s.Large + s.bold + s.project.colors.primary, "t2cgo_kw")
    accent = Style.create(s.Large + s.bold + s.project.colors.accent + s.center_txt, "t2cgo_acc")
    highlight = Style.create(s.Large + s.bold + s.project.colors.highlight + s.center_txt, "t2cgo_hl")
bs = BlockStyles


def build():
    st_marker("/gse:go")
    with st_block(_pf):
        with st_block(s.center_txt):
            with st_zoom(90):
                st_write(bs.heading, "/gse:go \u2014 The Single Entry Point", tag=t.div, toc_lvl="+1")
            st_hover_tooltip(
                title="/gse:go \u2014 Orchestrate Everything",
                entries=[
                    ("Purpose", "Detect current project state (including git branch and worktree state), propose the next logical activity group (LC00\u2013LC03), and orchestrate it with validation gates between activities."),
                    ("--adopt", "Onboard an existing project: scan, infer sprint state, initialize .gse/, offer to annotate existing artefacts. Auto-detected when .gse/ is absent but the project has existing code."),
                    ("Smart detection", "The orchestrator checks: is .gse/ present? Is a sprint active? What phase are we in? Are there uncommitted changes? Then proposes the right next step."),
                    ("Cross-cutting", "Available at any time. This is the command beginners use \u2014 the agent figures out what to do next."),
                ],
                scale="2vw", width="70vw", position="center",
            )
            st_space("v", 1)

        with st_zoom(90):
            with st_grid(cols="1fr 1fr 1fr 1fr", gap="8px") as g:
                for icon, phase, label in [
                    ("\U0001f464", "LC00", "Onboarding"),
                    ("\U0001f50d", "LC01", "Discovery"),
                    ("\u2699\ufe0f", "LC02", "Development"),
                    ("\U0001f4da", "LC03", "Capitalization"),
                ]:
                    with g.cell():
                        with st_block(_cell):
                            st_write(bs.body, f"{icon} ", (bs.keyword, phase))
                            st_write(bs.body, label)

            st_space("v", 1)

            with st_grid(cols="1fr 1fr", gap="16px") as g:
                with g.cell():
                    with st_block(_cell_acc):
                        st_write(bs.keyword + s.center_txt, "/gse:go")
                        st_space("v", 0.5)
                        st_write(bs.body, "Detects project state")
                        st_write(bs.body, "Proposes next activity")
                        st_write(bs.body, "Orchestrates with gates")
                with g.cell():
                    with st_block(_cell_act):
                        st_write(bs.highlight, "/gse:go --adopt")
                        st_space("v", 0.5)
                        st_write(bs.body, "Scans existing project")
                        st_write(bs.body, "Infers sprint state")
                        st_write(bs.body, "Initializes .gse/")
