"""T2 Seq 2.3-2.4 — 23 commands, 9 agents, .gse/ storage."""
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
    body = Style.create(s.Large + s.center_txt + s.text.wrap.hyphens, "t2c_body")
    accent = Style.create(s.Large + s.bold + s.project.colors.accent + s.center_txt, "t2c_acc")
    keyword = Style.create(s.Large + s.bold + s.project.colors.primary, "t2c_kw")
    highlight = Style.create(s.Large + s.bold + s.project.colors.highlight, "t2c_hl")
    label = Style.create(s.Large + s.bold + s.project.colors.primary + s.center_txt, "t2c_lbl")
bs = BlockStyles


def build():
    st_slide_break(marker_label="Commands & Agents")

    # ── Slide: 23 commands by category ──────────────────────────────
    with st_block(_pf):
        with st_block(s.center_txt):
            with st_grid(
                cols="95% 5%",
                gap="0px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    st_write(bs.heading, "23 Commands in 12 Categories", tag=t.div, toc_lvl="+1")
                with g.cell():
                    st_hover_tooltip(
                        title="GSE-One Command Map",
                        entries=[
                            ("Orchestration", "/gse:go, /gse:status, /gse:health — manage the overall workflow."),
                            ("Session", "/gse:pause, /gse:resume — save/restore session state."),
                            ("Onboarding", "/gse:hug — create your developer profile (11 dimensions)."),
                            ("Learning", "/gse:learn — guided competency building (reactive + proactive, cross-cutting)."),
                            ("Backlog", "/gse:backlog — unified work item management (pool + sprint), syncs with GitHub Issues."),
                            ("Discovery", "/gse:collect, /gse:assess — inventory sources, gap analysis."),
                            ("Planning", "/gse:plan — sprint planning (cross-cutting, any level, any time)."),
                            ("Engineering", "/gse:reqs, /gse:design, /gse:preview, /gse:tests, /gse:produce, /gse:deliver — the dev cycle."),
                            ("Quality", "/gse:review, /gse:fix — multi-perspective review and fix."),
                            ("Deployment", "/gse:deploy — from zero infrastructure to live app (Hetzner + Coolify)."),
                            ("Capitalization", "/gse:compound, /gse:integrate — codify learnings, route to operational destinations."),
                            ("Ad-hoc", "/gse:task — exploratory spike, complexity-boxed (max 3 pts)."),
                        ],
                        scale="2vw", width="70vw", position="left",
                    )
            st_space("v", 1)
            _cmds_left = [
                ("Orchestration", "/gse:go  /gse:status  /gse:health"),
                ("Session", "/gse:pause  /gse:resume"),
                ("Onboarding", "/gse:hug"),
                ("Learning", "/gse:learn"),
                ("Backlog", "/gse:backlog"),
                ("Discovery", "/gse:collect  /gse:assess"),
            ]
            _cmds_right = [
                ("Planning", "/gse:plan"),
                ("Engineering", "/gse:reqs  /gse:design  /gse:preview  /gse:tests  /gse:produce  /gse:deliver"),
                ("Quality", "/gse:review  /gse:fix"),
                ("Deployment", "/gse:deploy"),
                ("Capitalization", "/gse:compound  /gse:integrate"),
                ("Ad-hoc", "/gse:task"),
            ]
            with st_zoom(80):
                with st_grid(cols="1fr 1fr", gap="16px") as g:
                    with g.cell():
                        with st_grid(cols="1fr", gap="12px", cell_styles=_cell_act) as inner:
                            for cat, cmds in _cmds_left:
                                with inner.cell():
                                    st_write(bs.body, (bs.keyword, f"{cat}  "), (bs.body, cmds))
                    with g.cell():
                        with st_grid(cols="1fr", gap="12px", cell_styles=_cell) as inner:
                            for cat, cmds in _cmds_right:
                                with inner.cell():
                                    st_write(bs.body, (bs.keyword, f"{cat}  "), (bs.body, cmds))

    st_slide_break(marker_label="9 Specialized Agents")

    # ── Slide: 9 agents ─────────────────────────────────────────────
    with st_block(_pf):
        with st_block(s.center_txt):
            with st_grid(
                cols="95% 5%",
                gap="0px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    st_write(bs.heading, "9 Specialized Agents", tag=t.div, toc_lvl="+1")
                with g.cell():
                    st_hover_tooltip(
                        title="The Virtual Team",
                        entries=[
                            ("Why 9 agents?", "Each agent brings a specialized perspective. Together they catch issues that no single reviewer would find."),
                            ("Always-on", "The guardrail-enforcer runs on every action. The devil-advocate activates during review to challenge assumptions."),
                            ("Orchestrator", "The gse-orchestrator coordinates all others, manages the lifecycle, and handles decision classification (Auto/Inform/Gate)."),
                        ],
                        scale="2vw", width="70vw", position="left",
                    )
            st_space("v", 1)
            _agents_left = [
                ("\U0001f3bc", "gse-orchestrator", "Lifecycle management"),
                ("\U0001f50d", "requirements-analyst", "Completeness"),
                ("\U0001f3d7\ufe0f", "architect", "Structural quality"),
                ("\U0001f9ea", "test-strategist", "Coverage"),
                ("\U0001f4dd", "code-reviewer", "Code quality"),
            ]
            _agents_right = [
                ("\U0001f6e1\ufe0f", "security-auditor", "Vulnerabilities"),
                ("\U0001f464", "ux-advocate", "User experience"),
                ("\U0001f6a7", "guardrail-enforcer", "Rules (always-on)"),
                ("\U0001f608", "devil-advocate", "Self-critique (P16)"),
            ]
            with st_zoom(85):
                with st_grid(cols="1fr 1fr", gap="16px") as g:
                    with g.cell():
                        with st_grid(cols="1fr", gap="12px", cell_styles=_cell) as inner:
                            for emoji, name, role in _agents_left:
                                with inner.cell():
                                    st_write(bs.body, (bs.keyword, f"{emoji} {name}  "), (bs.body, role))
                    with g.cell():
                        with st_grid(cols="1fr", gap="12px", cell_styles=_cell) as inner:
                            for emoji, name, role in _agents_right:
                                with inner.cell():
                                    st_write(bs.body, (bs.keyword, f"{emoji} {name}  "), (bs.body, role))

    st_slide_break(marker_label="Project State & Artifacts")

    # ── Slide: .gse/ + docs/ storage structure ──────────────────────
    with st_block(_pf):
        with st_block(s.center_txt):
            with st_grid(
                cols="95% 5%",
                gap="0px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    st_write(bs.heading, "Project State & Artifacts", tag=t.div, toc_lvl="+1")
                with g.cell():
                    st_hover_tooltip(
                        title="Everything Is Stored and Traceable",
                        entries=[
                            (".gse/", "Agent state: config, profile, sprint status, backlog, decisions, sources."),
                            ("docs/sprints/", "Sprint artifacts: plan, reqs, design, test strategy, review, compound."),
                            ("docs/learning/", "Personal learning notes produced by /gse:learn."),
                            ("Key point", ".gse/ is agent state. docs/ is project documentation. Both at project root."),
                        ],
                        scale="2vw", width="70vw", position="left",
                    )
            st_space("v", 1)
            _gse_left = [
                (".gse/config.yaml", "Project settings"),
                (".gse/profile.yaml", "Your profile (HUG output)"),
                (".gse/status.yaml", "Sprint state + health score"),
            ]
            _gse_right = [
                (".gse/backlog.yaml", "All tasks (TASK-)"),
                (".gse/decisions.md", "Decision journal (DEC-)"),
                (".gse/sources.yaml", "External sources (SRC-)"),
            ]
            _docs = [
                ("docs/sprints/", "Sprint artifacts"),
                ("docs/learning/", "Personal learning notes"),
            ]
            with st_grid(cols="1fr 1fr", gap="16px") as g:
                with g.cell():
                    with st_grid(cols="1fr", gap="12px", cell_styles=_cell) as inner:
                        for fname, desc in _gse_left:
                            with inner.cell():
                                st_write(bs.body, (bs.highlight, f"{fname}  "), (bs.body, desc))
                with g.cell():
                    with st_grid(cols="1fr", gap="12px", cell_styles=_cell) as inner:
                        for fname, desc in _gse_right:
                            with inner.cell():
                                st_write(bs.body, (bs.highlight, f"{fname}  "), (bs.body, desc))
            st_space("v", 0.5)
            with st_grid(cols="1fr 1fr", gap="16px") as g:
                for fname, desc in _docs:
                    with g.cell():
                        with st_block(_cell_acc):
                            st_write(bs.body, (bs.highlight, f"{fname}  "), (bs.body, desc))

    st_slide_break(marker_label="Session & Backlog Management")

    # ── Slide: Session management + Backlog ─────────────────────────
    with st_block(_pf):
        with st_block(s.center_txt):
            with st_grid(
                cols="95% 5%",
                gap="0px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    st_write(bs.heading, "Session & Backlog Management", tag=t.div, toc_lvl="+1")
                with g.cell():
                    st_hover_tooltip(
                        title="Pause, Resume, Task, Backlog",
                        entries=[
                            ("/gse:pause", "Auto-commits uncommitted work, saves a checkpoint snapshot, records worktree state. You can safely close your IDE."),
                            ("/gse:resume", "Reloads checkpoint, verifies file integrity, briefs you on where you left off. Seamless session continuity."),
                            ("/gse:task", "Execute an ad-hoc task outside the lifecycle. Spike mode: max 3 complexity points, non-deliverable. For quick experiments."),
                            ("/gse:backlog", "Unified view of all TASK- items: pool (unassigned) and sprint (assigned). Filter, add, sync with GitHub issues."),
                        ],
                        scale="2vw", width="70vw", position="left",
                    )
            st_space("v", 1)
            with st_zoom(120):
                with st_grid(cols="repeat(auto-fit, minmax(280px, 1fr))", gap="16px") as g:
                    with g.cell():
                        with st_block(_cell_acc):
                            st_write(bs.label, "/gse:pause + resume")
                            st_write(bs.body, "Save and restore session state")
                    with g.cell():
                        with st_block(_cell_act):
                            st_write(bs.label, "/gse:task (spike)")
                            st_write(bs.body, "Ad-hoc experiment, max 3pts")
                    with g.cell():
                        with st_block(_cell):
                            st_write(bs.label, "/gse:backlog")
                            st_write(bs.body, "Unified work items, filters, GitHub sync")
                            
    st_space("v", "30vh")