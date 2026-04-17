"""T2 Seq 2.1-2.2 — GSE-One philosophy: 80/20, principles P1-P6, lifecycle LC00-LC03."""
# @guideline: minimalist-visual + maximize-viewport
# @reuse: bck_gensem_ce_philosophy, _8020_example, _five_phases (v01)
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_LANDSCAPE as _SUFFIX
from shared_widgets import st_hover_tooltip

_pf = s.project.containers.page_fill_top
_pfc = s.project.containers.page_fill_center
_cell = s.project.containers.cell_primary_bg + s.project.containers.cell_pad_md + s.center_txt
_cell_acc = s.project.containers.cell_accent_bg + s.project.containers.cell_pad_md + s.center_txt
_cell_act = s.project.containers.cell_active_bg + s.project.containers.cell_pad_md + s.center_txt


class BlockStyles:
    heading = s.project.titles.slide_title + s.center_txt
    body = Style.create(s.Large + s.center_txt + s.text.wrap.hyphens, "t2p_body")
    accent = Style.create(s.Large + s.bold + s.project.colors.accent + s.center_txt, "t2p_acc")
    highlight = Style.create(s.Large + s.bold + s.project.colors.highlight + s.center_txt, "t2p_hl")
    keyword = Style.create(s.Large + s.bold + s.project.colors.primary, "t2p_kw")
    label = Style.create(s.Large + s.bold + s.project.colors.primary + s.center_txt, "t2p_lbl")
bs = BlockStyles

_PROMPT_LIFECYCLE = (
    f"{_PREFIX} A circular flow diagram with 4 connected stages arranged clockwise. "
    "Stage 1 (top, teal): a handshake icon. Stage 2 (right, blue): a magnifying glass + map. "
    "Stage 3 (bottom, amber): gears + code + magnifying glass. Stage 4 (left, teal): a growing tree. "
    "Arrows connect each stage to the next, forming a continuous loop. "
    f"{_SUFFIX}"
)


def build():
    st_slide_break(marker_label="GSE-One Philosophy")

    # ── Slide: P1 recall + 80/20 ────────────────────────────────────
    with st_block(_pfc):
        with st_block(s.center_txt):
            with st_grid(
                cols="95% 5%",
                gap="0px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    with st_zoom(90):
                        st_write(bs.heading, "GSE-One: The 80/20 Rule", tag=t.div, toc_lvl="+1")
                with g.cell():
                    st_hover_tooltip(
                        title="The 80/20 Rule — Explained",
                        entries=[
                            ("What it means", "In GSE-One, 80% of the quality comes from planning and review. Only 20% comes from the actual code generation."),
                            ("Contrast with VibeCoding", "VibeCoding inverts this: 90% coding, 10% thinking. FreeSelfApp Day 1 demonstrated the result \u2014 fast but fragile."),
                            ("In practice", "Before writing any code, GSE-One requires: requirements, design, preview. After code: review, fix, compound."),
                            ("Discipline principle", "The 80/20 rule is not specific to GSE-One \u2014 it is a foundational principle of Generative SE as a discipline, shared by all mature methodologies."),
                        ],
                        scale="2vw", width="70vw", position="left",
                    )
            with st_zoom(120):
                st_space("v", 2)
                st_write(bs.accent, "80% planning & review = quality")
                st_space("v", 1)
                st_write(bs.body, "20% execution = code generation")
                st_space("v", 2)
                st_write(bs.body, "Remember FreeSelfApp Day 1? That was the 20/80 — fast but fragile.")

    st_slide_break(marker_label="6 Foundation Principles")

    # ── Slide: 6 Foundation principles ──────────────────────────────
    with st_block(_pf):
        with st_block(s.center_txt):
            with st_grid(
                cols="95% 5%",
                gap="0px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    with st_zoom(90):
                        st_write(bs.heading, "6 Foundation Principles", tag=t.div, toc_lvl="+1")
                with g.cell():
                    st_hover_tooltip(
                        title="Principles P1-P6 — The Foundation",
                        entries=[
                            ("P1 Iterative", "All work is organized in sprints with modular file structure and incremental delivery."),
                            ("P3 Artifacts", "Every deliverable (code, requirements, tests, decisions) is tracked with a unique ID (REQ-, DES-, TST-, etc.)."),
                            ("P5 Planning", "Planning happens at 4 levels: project, sprint, task, and micro (within a single agent interaction)."),
                            ("P6 Traceability", "Every artifact is linked to its origin (derives_from, implements, decided_by, related_to)."),
                        ],
                        scale="2vw", width="70vw", position="left",
                    )
            st_space("v", 1)
            with st_zoom(120):
                with st_grid(cols="1fr 1fr 1fr", gap="16px", cell_styles=_cell) as g:
                    with g.cell():
                        st_write(bs.body, (bs.keyword, "P1 "), (bs.body, "Iterative & Incremental"))
                    with g.cell():
                        st_write(bs.body, (bs.keyword, "P2 "), (bs.body, "Agile Vocabulary"))
                    with g.cell():
                        st_write(bs.body, (bs.keyword, "P3 "), (bs.body, "Artifacts Are Everything"))
                    with g.cell():
                        st_write(bs.body, (bs.keyword, "P5 "), (bs.body, "Planning at Every Level"))
                    with g.cell():
                        st_write(bs.body, (bs.keyword, "P6 "), (bs.body, "Full Traceability"))
                    with g.cell():
                        st_write(bs.body, (bs.keyword, "3 Modes "), (bs.body, "Micro / Lightweight / Full"))

    st_slide_break(marker_label="The GSE-One Lifecycle")

    # ── Slide: The 4-stage lifecycle ────────────────────────────────
    with st_block(_pf):
        with st_block(s.center_txt):
            with st_grid(
                cols="95% 5%",
                gap="0px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    with st_zoom(90):
                        st_write(bs.heading, "The GSE-One Lifecycle", tag=t.div, toc_lvl="+1")
                with g.cell():
                    st_hover_tooltip(
                        title="4 Lifecycle Stages",
                        entries=[
                            ("LC00 Onboarding", "/gse:hug captures your profile (11 dimensions) to adapt the agent's behavior to your experience level."),
                            ("LC01 Discovery", "/gse:collect + /gse:assess + /gse:plan — inventory sources, analyze gaps, create a sprint plan with complexity budget."),
                            ("LC02 Engineering", "REQS → DESIGN → PREVIEW → TESTS → PRODUCE → REVIEW → [FIX] → DELIVER — the full development cycle. [FIX] is conditional: the orchestrator inserts it only if REVIEW produces HIGH/MEDIUM findings."),
                            ("LC03 Capitalization", "/gse:compound + /gse:integrate — capture learnings, route them to operational destinations."),
                        ],
                        scale="2vw", width="70vw", position="left",
                    )
            st_space("v", 1)
            with st_block(s.center_txt):
                st_image(
                    s.none, width="50%",
                    editable=IS_EDITABLE,
                    name="gse_lifecycle_4stages",
                    prompt=_PROMPT_LIFECYCLE,
                    provider="openai",
                    ai_size="1536x1024",
                )
            st_space("v", 1)
            with st_grid(cols="repeat(auto-fit, minmax(200px, 1fr))", gap="12px") as g:
                with g.cell():
                    with st_block(_cell_acc):
                        st_write(bs.label, "LC00")
                        st_write(bs.body, "Onboarding")
                with g.cell():
                    with st_block(_cell):
                        st_write(bs.label, "LC01")
                        st_write(bs.body, "Discovery")
                with g.cell():
                    with st_block(_cell_act):
                        st_write(bs.label, "LC02")
                        st_write(bs.body, "Engineering")
                with g.cell():
                    with st_block(_cell_acc):
                        st_write(bs.label, "LC03")
                        st_write(bs.body, "Capitalization")

    st_slide_break(marker_label="/gse:hug — Your Profile")

    # ── Slide: HUG — 11 profile dimensions + P9 adaptive comm ──────
    with st_block(_pf):
        with st_block(s.center_txt):
            with st_grid(
                cols="95% 5%",
                gap="0px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    with st_zoom(90):
                        st_write(bs.heading, "/gse:hug — Your Profile", tag=t.div, toc_lvl="+1")
                with g.cell():
                    st_hover_tooltip(
                        title="P9: Adaptive Communication + HUG Profile",
                        entries=[
                            ("Why a profile?", "The agent adapts its communication to your level. A beginner gets more Gates and explanations. An expert gets a streamlined flow."),
                            ("11 dimensions", "IT expertise, scientific expertise, abstraction capability, language, verbosity, domain background, decision involvement, project domain, team context, learning goals, contextual tips."),
                            ("Teacher context", "If your domain is Teaching, the agent uses pedagogical language and progressive disclosure."),
                            ("Business context", "If your domain is Business, the agent focuses on ROI, deadlines, and risk impact."),
                        ],
                        scale="2vw", width="70vw", position="left",
                    )
            st_space("v", 1)
            _dims_left = [
                ("IT expertise", "Beginner → Expert"),
                ("Scientific expertise", "None → Researcher"),
                ("Abstraction", "Concrete-first → Abstract-first"),
                ("Language", "Chat + artifact languages"),
                ("Verbosity", "Terse / Normal / Detailed"),
                ("Domain", "Teaching / Business / Science / Engineering"),
            ]
            _dims_right = [
                ("Decision involvement", "Autonomous → Supervised"),
                ("Project domain", "Web / Embedded / CLI / Mobile"),
                ("Team context", "Solo / Small / Large"),
                ("Learning goals", "Your competency targets"),
                ("Contextual tips", "Enable / Disable micro-explanations"),
            ]
            with st_zoom(85):
                with st_grid(cols="1fr 1fr", gap="16px") as g:
                    with g.cell():
                        with st_grid(cols="1fr", gap="10px", cell_styles=_cell_act) as inner:
                            for dim, val in _dims_left:
                                with inner.cell():
                                    st_write(bs.body, (bs.keyword, f"{dim}  "), (bs.body, val))
                    with g.cell():
                        with st_grid(cols="1fr", gap="10px", cell_styles=_cell) as inner:
                            for dim, val in _dims_right:
                                with inner.cell():
                                    st_write(bs.body, (bs.keyword, f"{dim}  "), (bs.body, val))

    st_slide_break(marker_label="Phases vs Activities")

    # ── Slide: Phases × Activities mapping ──────────────────────────
    with st_block(_pf):
        with st_block(s.center_txt):
            with st_grid(
                cols="95% 5%",
                gap="0px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    with st_zoom(90):
                        st_write(bs.heading, "Phases vs Activities", tag=t.div, toc_lvl="+1")
                with g.cell():
                    st_hover_tooltip(
                        title="Two Levels of Abstraction",
                        entries=[
                            ("Phases (LC)", "High-level containers grouping activities by purpose."),
                            ("Activities", "Concrete work units, each mapped to a /gse: command."),
                            ("Why it matters", "Project modes (Micro/Lightweight/Full) select a subset of activities, not phases."),
                        ],
                        scale="2vw", width="70vw", position="left",
                    )
            st_space("v", 1)

            with st_zoom(100):
                _hdr = s.project.containers.table_header_cell
                _nrm = s.project.containers.table_normal_cell
                _act = s.project.containers.table_active_cell

                with st_grid(
                    cols="15% 25% 60%",
                    gap="4px",
                    cell_styles=s.project.containers.cell_pad_sm,
                ) as g:
                    # Header row
                    with g.cell():
                        with st_block(_hdr):
                            st_write(s.project.titles.table_header, "Phase")
                    with g.cell():
                        with st_block(_hdr):
                            st_write(s.project.titles.table_header, "Purpose")
                    with g.cell():
                        with st_block(_hdr):
                            st_write(s.project.titles.table_header, "Activities (/gse: commands)")

                    # LC00
                    with g.cell():
                        with st_block(_nrm):
                            st_write(s.project.titles.table_label, "LC00")
                    with g.cell():
                        with st_block(_nrm):
                            st_write(s.project.titles.table_cell, "Onboarding")
                    with g.cell():
                        with st_block(_act):
                            st_write(s.project.titles.table_cell, "HUG")

                    # LC01
                    with g.cell():
                        with st_block(_nrm):
                            st_write(s.project.titles.table_label, "LC01")
                    with g.cell():
                        with st_block(_nrm):
                            st_write(s.project.titles.table_cell, "Discovery & Planning")
                    with g.cell():
                        with st_block(_act):
                            st_write(s.project.titles.table_cell, "COLLECT \u2192 ASSESS \u2192 PLAN")

                    # LC02
                    with g.cell():
                        with st_block(_nrm):
                            st_write(s.project.titles.table_label, "LC02")
                    with g.cell():
                        with st_block(_nrm):
                            st_write(s.project.titles.table_cell, "Development")
                    with g.cell():
                        with st_block(_act):
                            st_write(
                                s.project.titles.table_cell,
                                "REQS \u2192 DESIGN \u2192 PREVIEW \u2192 TESTS \u2192 PRODUCE \u2192 REVIEW \u2192 [FIX] \u2192 DELIVER",
                            )

                    # LC03
                    with g.cell():
                        with st_block(_nrm):
                            st_write(s.project.titles.table_label, "LC03")
                    with g.cell():
                        with st_block(_nrm):
                            st_write(s.project.titles.table_cell, "Capitalization")
                    with g.cell():
                        with st_block(_act):
                            st_write(s.project.titles.table_cell, "COMPOUND \u2192 INTEGRATE")

                    # Cross-cutting
                    with g.cell():
                        with st_block(_cell_acc):
                            st_write(s.project.titles.table_label, "\u2014")
                    with g.cell():
                        with st_block(_cell_acc):
                            st_write(s.project.titles.table_cell, "Cross-cutting")
                    with g.cell():
                        with st_block(_cell_acc):
                            st_write(
                                s.project.titles.table_cell,
                                "PLAN \u00b7 LEARN \u00b7 HEALTH \u00b7 STATUS \u00b7 PAUSE \u00b7 RESUME \u00b7 TASK",
                            )

            st_space("v", 1)
            with st_block(s.project.containers.callout + s.center_txt):
                st_write(
                    bs.body,
                    (bs.keyword, "PLAN"),
                    " is cross-cutting \u2014 invocable at ",
                    (bs.keyword, "4 levels"),
                    " (project, sprint, task, micro) at ",
                    (bs.keyword, "any point"),
                    " in the lifecycle.",
                )
                st_write(
                    bs.body,
                    (bs.keyword, "[FIX]"),
                    " is conditional \u2014 inserted by the orchestrator only when REVIEW reports ",
                    (bs.keyword, "HIGH/MEDIUM findings"),
                    "; a clean review moves FIX to ",
                    (bs.keyword, "workflow.skipped"),
                    ".",
                )

    st_slide_break(marker_label="3 Project Modes")

    # ── Slide: 3 Project Modes ──────────────────────────────────────
    with st_block(_pf):
        with st_block(s.center_txt):
            with st_grid(
                cols="95% 5%",
                gap="0px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    with st_zoom(90):
                        st_write(bs.heading, "3 Project Modes", tag=t.div, toc_lvl="+1")
                with g.cell():
                    st_hover_tooltip(
                        title="When to Use Each Mode",
                        entries=[
                            ("Triviality pre-filter", "File count is a pre-filter for Micro. Beyond <3 files, mode selection uses 7 structural signals (coupling, surface, cross-cutting, data-flow, integrations, risk domains, test breadth)."),
                            ("Micro", "Pre-filter: <3 project files. PRODUCE \u2192 DELIVER only. Direct commits (no branches). Gate-only decisions. No guardrails enforced. No health score. State: .gse/status.yaml only."),
                            ("Lightweight", "Small scope on the 7 signals. PLAN \u2192 REQS \u2192 PRODUCE \u2192 DELIVER. Branch-only (no worktrees). Auto+Gate decisions. Hard guardrails. 3 health dimensions. Plan artifact only."),
                            ("Full", "Rich scope on the 7 signals. Complete lifecycle LC01\u2192LC02\u2192LC03. Worktree isolation (1 task = 1 worktree). Full Auto/Inform/Gate decisions. All guardrails. All 8 health dimensions. Full sprint artifacts."),
                            ("Git strategy", "Micro = direct commit. Lightweight = branch-only. Full = worktree per task + sprint integration branch."),
                            ("Recommendation", "Start Lightweight. Escalate to Full when the 7 structural signals indicate real complexity."),
                        ],
                        scale="2vw", width="70vw", position="left",
                    )
            st_space("v", 1)
            with st_zoom(120):
                with st_grid(cols="repeat(auto-fit, minmax(280px, 1fr))", gap="16px") as g:
                    with g.cell():
                        with st_block(_cell):
                            st_write(bs.label, "Micro")
                            st_write(bs.body, "Quick prototype")
                            st_write(bs.body, "PRODUCE → DELIVER only")
                    with g.cell():
                        with st_block(_cell_acc):
                            st_write(bs.label, "Lightweight")
                            st_write(bs.body, "Small projects")
                            st_write(bs.body, "PLAN → REQS → PRODUCE → DELIVER")
                    with g.cell():
                        with st_block(_cell_act):
                            st_write(bs.label, "Full")
                            st_write(bs.body, "Production systems")
                            st_write(bs.body, "Complete lifecycle")

    st_slide_break(marker_label="/gse:go vs Individual Commands")

    # ── Slide: GPS vs Map metaphor ──────────────────────────────────
    with st_block(_pfc):
        with st_block(s.center_txt):
            with st_grid(
                cols="95% 5%",
                gap="0px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    with st_zoom(90):
                        st_write(bs.heading, "/gse:go vs Individual Commands", tag=t.div, toc_lvl="+1")
                with g.cell():
                    st_hover_tooltip(
                        title="Two Ways to Use GSE-One",
                        entries=[
                            ("/gse:go", "Like a GPS: the agent guides you through the entire lifecycle automatically. Best for beginners and standard workflows."),
                            ("Individual commands", "Like a map: you choose which command to run and when. Best for experienced users who want fine control."),
                            ("--adopt option", "/gse:go --adopt for existing projects: non-destructive scan, sprint-0 baseline, optional frontmatter annotation. No files modified without approval."),
                            ("Orchestrator behavior", "The orchestrator detects project state and proposes the next activity. It can launch commands with options based on the conversation (e.g., /gse:plan --interactive)."),
                            ("You experienced this", "In P1, you used /gse:go. From now on, you'll learn the individual commands."),
                        ],
                        scale="2vw", width="70vw", position="left",
                    )
            with st_zoom(120):
                st_space("v", 2)
                with st_grid(cols="repeat(auto-fit, minmax(300px, 1fr))", gap="24px") as g:
                    with g.cell():
                        with st_block(s.project.containers.callout):
                            st_write(bs.accent, "/gse:go = GPS")
                            st_space("v", 0.5)
                            st_write(bs.body, "Agent guides you through the full lifecycle")
                    with g.cell():
                        with st_block(s.project.containers.callout):
                            st_write(bs.highlight, "Commands = Map")
                            st_space("v", 0.5)
                            st_write(bs.body, "You choose what to run and when")

    st_space("v", "30vh")