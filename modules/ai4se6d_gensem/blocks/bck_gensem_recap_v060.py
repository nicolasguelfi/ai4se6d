"""Postscript — GSE-One evolutions since the session: v0.20.4 → v0.60.1 (2026-04-17 → 2026-04-22)."""
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
    body = Style.create(s.Large + s.center_txt + s.text.wrap.hyphens, "rcp_body")
    body_l = Style.create(s.Large + s.text.wrap.hyphens, "rcp_body_l")
    accent = Style.create(s.Large + s.bold + s.project.colors.accent + s.center_txt, "rcp_acc")
    highlight = Style.create(s.Large + s.bold + s.project.colors.highlight + s.center_txt, "rcp_hl")
    keyword = Style.create(s.Large + s.bold + s.project.colors.primary, "rcp_kw")
    critical = Style.create(s.Large + s.bold + s.project.colors.critical + s.center_txt, "rcp_crit")
    success = Style.create(s.Large + s.bold + s.project.colors.success + s.center_txt, "rcp_ok")
    stat = Style.create(s.Large + s.bold + s.project.colors.highlight, "rcp_stat")
bs = BlockStyles


def _slide_title(title, tooltip_title, entries, position="left"):
    """Shared slide-title pattern: title at 95%, hover tooltip at 5%."""
    with st_grid(
        cols="95% 5%",
        gap="0px",
        cell_styles=s.project.containers.grid_cell_centered,
    ) as g:
        with g.cell():
            with st_zoom(90):
                st_write(bs.heading, title, tag=t.div, toc_lvl="+1")
        with g.cell():
            st_hover_tooltip(
                title=tooltip_title,
                entries=entries,
                scale="2vw", width="70vw", position=position,
            )


def _render_cell_grid(cells, cols="1fr 1fr 1fr", gap="12px", alternating=True):
    """Render a grid of (icon, keyword, description) tuples with alternating cell styles."""
    with st_grid(cols=cols, gap=gap) as g:
        for i, (icon, name, desc) in enumerate(cells):
            if alternating:
                cell_style = _cell if i % 3 == 0 else (_cell_acc if i % 3 == 1 else _cell_act)
            else:
                cell_style = _cell_acc if i % 2 == 0 else _cell
            with g.cell():
                with st_block(cell_style):
                    st_write(bs.body, f"{icon} ", (bs.keyword, name))
                    st_write(bs.body, desc)


def build():
    # ─────────────────────────────────────────────────────────────────
    # Slide 1 — Overview: v0.20.4 → v0.60.1 (2×3 grid)
    # ─────────────────────────────────────────────────────────────────
    st_slide_break(marker_label="Since the Session — v0.20.4 → v0.60.1")
    with st_block(_pf):
        with st_block(s.center_txt):
            _slide_title(
                "Since the Session — v0.20.4 → v0.60.1",
                "Post-session Evolution of GSE-One",
                [
                    ("Period", "2026-04-17 → 2026-04-22 — six days of intensive iteration driven by training feedback."),
                    ("Scope", "End-user oriented summary: what forkers and method users will actually notice."),
                    ("Reading the block", "Themes are grouped logically, not chronologically. Version tags are shown for traceability, not as a roadmap."),
                    ("No breaking changes", "All user-facing APIs preserved. The series is a coherence restoration, not a rewrite."),
                ],
                position="center",
            )
            st_space("v", 1)
            with st_zoom(120):
                st_write(bs.accent, "From GSE-One v0.20.4 to v0.60.1 in six days.")
                st_space("v", 2)
                with st_grid(cols="1fr 1fr 1fr", gap="16px") as g:
                    with g.cell():
                        with st_block(_cell):
                            st_write(bs.stat + s.center_txt, "+40")
                            st_write(bs.body, "releases shipped")
                    with g.cell():
                        with st_block(_cell_acc):
                            st_write(bs.stat + s.center_txt, "2")
                            st_write(bs.body, "new major activities")
                    with g.cell():
                        with st_block(_cell_act):
                            st_write(bs.stat + s.center_txt, "7")
                            st_write(bs.body, "new guardrails")
                    with g.cell():
                        with st_block(_cell):
                            st_write(bs.stat + s.center_txt, "20")
                            st_write(bs.body, "AMÉL from DLH training")
                    with g.cell():
                        with st_block(_cell_acc):
                            st_write(bs.stat + s.center_txt, "~76")
                            st_write(bs.body, "post-audit corrections")
                    with g.cell():
                        with st_block(_cell_act):
                            st_write(bs.stat + s.center_txt, "0")
                            st_write(bs.body, "regressions / 72 tests")

    # ─────────────────────────────────────────────────────────────────
    # Slide 2 — Platforms & Distribution (No-plugin first)
    # ─────────────────────────────────────────────────────────────────
    st_slide_break(marker_label="Platforms & Distribution")
    with st_block(_pf):
        with st_block(s.center_txt):
            _slide_title(
                "Platforms & Distribution",
                "Three Platforms, One Methodology",
                [
                    ("No-plugin Claude", "v0.20.5 — when plugin mode is unavailable, skills install as gse-<name>/ so commands appear as /gse-<name> in the TUI."),
                    ("Native opencode", "v0.21.0 — GSE-One installs on opencode alongside Claude Code and Cursor. Installer accepts --platform opencode and --platform all."),
                    ("Install modes", "Global (~/.config/opencode/) or project-local (.opencode/). Same commands, same artefacts."),
                    ("Install guide", "INSTALL-OPENCODE.md enriched with model recommendations (Ollama, LM Studio, frontier open-weight, OpenRouter) sorted by SWE-bench Verified (April 2026)."),
                ],
                position="center",
            )
            st_space("v", 1)
            with st_zoom(120):
                with st_grid(cols="repeat(auto-fit, minmax(280px, 1fr))", gap="16px") as g:
                    with g.cell():
                        with st_block(_cell):
                            st_write(bs.keyword + s.center_txt, "\U0001f527 No-plugin mode")
                            st_space("v", 0.5)
                            st_write(bs.body, "gse-<name>/ → /gse-<name> in Claude TUI")
                    with g.cell():
                        with st_block(_cell_acc):
                            st_write(bs.keyword + s.center_txt, "\U0001f310 Native opencode")
                            st_space("v", 0.5)
                            st_write(bs.body, "--platform opencode | all — global or project-local")
                    with g.cell():
                        with st_block(_cell_act):
                            st_write(bs.keyword + s.center_txt, "\U0001f4d6 Install guide")
                            st_space("v", 0.5)
                            st_write(bs.body, "Model selection matrices for local + frontier runtimes")

    # ─────────────────────────────────────────────────────────────────
    # Slide 3 — /gse:deploy (own slide, structured grid)
    # ─────────────────────────────────────────────────────────────────
    st_slide_break(marker_label="/gse:deploy")
    with st_block(_pf):
        with st_block(s.center_txt):
            _slide_title(
                "/gse:deploy — Hetzner + Coolify",
                "Auto-piloted Deployment — 6 Phases",
                [
                    ("6 phases", "setup → provision → secure → install-coolify → configure-domain → deploy."),
                    ("3 modes", "solo (single user), training (multi-learners, subdomain format {project}-{user}.{domain}), partial (BYO server — reuse existing infra)."),
                    ("partial / BYO server", "Auto-detected at Step 0 from .env variables. SERVER_IP already set ⇒ skip provisioning. COOLIFY_URL + token set ⇒ skip Coolify install. All set ⇒ app-only (straight to Phase 6). Works with any VPS (Hetzner, OVH, Scaleway, personal server)."),
                    ("4 Dockerfile templates", "Streamlit, Python, Node, static — pre-wired for the common app shapes."),
                    ("18-subcommand CLI", "deploy.py — fine-grained operations (status, redeploy, destroy, training-init, training-reap, registrar…)."),
                    ("10th agent", "deploy-operator — the first Operational archetype agent."),
                    ("Start step — Orientation", "4-option menu: Solo / Instructor / Learner / Skip. The first three persist a role via record-role; Skip is a meta-action (no role stored)."),
                ],
                position="left",
            )
            st_space("v", 1)
            with st_zoom(110):
                _render_cell_grid([
                    ("⚙️", "6 phases", "setup → provision → secure → coolify → DNS/SSL → deploy"),
                    ("\U0001f465", "3 modes", "solo • training (multi-learner) • partial (BYO server)"),
                    ("\U0001f433", "4 Dockerfile templates", "Streamlit • Python • Node • static"),
                    ("\U0001f916", "10th agent", "deploy-operator — first Operational archetype"),
                    ("\U0001f6a9", "Flags", "--status / --redeploy / --destroy / --training-*"),
                    ("\U0001f9ed", "Start step — Orientation", "Solo / Instructor / Learner / Skip"),
                ])

    # ─────────────────────────────────────────────────────────────────
    # Slide 4 — /gse:audit (own slide, structured grid)
    # ─────────────────────────────────────────────────────────────────
    st_slide_break(marker_label="/gse:audit")
    with st_block(_pf):
        with st_block(s.center_txt):
            _slide_title(
                "/gse:audit — Methodology Audit",
                "Detecting Drift in a Live Project",
                [
                    ("24th activity", "Invocable any time — detects methodological drift: stale dashboard, REQs without test evidence, broken artefact formats, sprint freeze violations, intent absence…"),
                    ("Hybrid architecture", "Phase 1 deterministic Python (15 checks, reproducible, no LLM cost). Phase 2 semantic layer (LLM-assisted, placeholder). Phase 3 auto-trigger from conversational signals."),
                    ("15 deterministic checks", "Dashboard freshness, test evidence presence, file format, workflow coherence, git state, sprint freeze, intent artefact, backlog traces, coach observations, OQ resolution…"),
                    ("AUD- prefix", "New artefact scope — meta (about methodology compliance), distinct from RVW- (project-level review findings)."),
                    ("Audit flags", "--auto (silent), --fix (apply safe corrections), --no-fix (report only), --quick (subset), --help."),
                    ("Auto-persistence", "Reports saved in _LOCAL/audits/ (gitignored). latest.md always points to the most recent."),
                ],
                position="left",
            )
            st_space("v", 1)
            with st_zoom(110):
                _render_cell_grid([
                    ("\U0001f3af", "24th activity", "Invocable any time — detects methodological drift"),
                    ("\U0001f9ea", "Phase 1 — deterministic", "15 Python checks, reproducible, no LLM cost"),
                    ("\U0001f9e0", "Phase 2-3", "Semantic layer + auto-trigger from conversation"),
                    ("\U0001f516", "AUD- prefix", "Meta-scope findings (distinct from RVW-)"),
                    ("\U0001f6a9", "Flags", "--auto / --fix / --no-fix / --quick / --help"),
                    ("\U0001f4be", "Auto-persistence", "Saved to _LOCAL/audits/ — latest.md rolling"),
                ])

    # ─────────────────────────────────────────────────────────────────
    # Slide 5 — Guardrails 1/3 (Sprint Freeze, Git Identity, Root-Cause)
    # ─────────────────────────────────────────────────────────────────
    st_slide_break(marker_label="Guardrails (1/3) — Sprint Discipline")
    with st_block(_pf):
        with st_block(s.center_txt):
            _slide_title(
                "Guardrails (1/3) — Sprint Discipline",
                "Before Work Begins",
                [
                    ("Intent", "These three guardrails protect the boundary between sprints, the author identity of commits, and the root-cause discipline of debugging."),
                    ("Activation", "They trigger automatically at the relevant moments — you never have to remember them."),
                    ("Override", "Every guardrail can be overridden with a traced justification in decisions.md."),
                ],
                position="left",
            )
            st_space("v", 1)
            with st_zoom(110):
                with st_grid(cols="1fr 1fr 1fr", gap="16px") as g:
                    with g.cell():
                        with st_block(_cell):
                            st_write(bs.keyword + s.center_txt, "\U0001f9ca Sprint Freeze")
                            st_space("v", 0.5)
                            st_write(bs.body, "Once a sprint is delivered, write activities (task, produce, fix, review) hit a mandatory Gate. Only way forward: open the next sprint.")
                    with g.cell():
                        with st_block(_cell_acc):
                            st_write(bs.keyword + s.center_txt, "\U0001f464 Git Identity")
                            st_space("v", 0.5)
                            st_write(bs.body, "Before the first commit, /gse:hug and /gse:go verify user.name + user.email. 5-option Gate if missing: Global / Local / Placeholder / Auto / Discuss.")
                    with g.cell():
                        with st_block(_cell_act):
                            st_write(bs.keyword + s.center_txt, "\U0001f50e Root-Cause (P16)")
                            st_space("v", 0.5)
                            st_write(bs.body, "On a reported bug: 4-step protocol — Read → Symptom → Hypothesis + Evidence → Patch. After 2–4 failed attempts, a devil-advocate review is spawned.")

    # ─────────────────────────────────────────────────────────────────
    # Slide 6 — Guardrails 2/3 (Scope Reconcile, Config Transparency)
    # ─────────────────────────────────────────────────────────────────
    st_slide_break(marker_label="Guardrails (2/3) — Scope & Config")
    with st_block(_pf):
        with st_block(s.center_txt):
            _slide_title(
                "Guardrails (2/3) — Scope & Config",
                "During Work",
                [
                    ("Intent", "These two guardrails keep what the agent actually does aligned with what it declared — on scope, and on configuration effects."),
                    ("Why it matters", "Silent drift between intent and execution is the single biggest source of audit findings observed during training."),
                ],
                position="left",
            )
            st_space("v", 1)
            with st_zoom(110):
                with st_grid(cols="1fr 1fr", gap="20px") as g:
                    with g.cell():
                        with st_block(_cell_acc):
                            st_write(bs.keyword + s.center_txt, "⚖️ Scope Reconciliation")
                            st_space("v", 0.5)
                            st_write(bs.body, "At the end of /gse:produce and /gse:task, the agent diffs git vs plan. If drift is detected, a 4-option Gate opens: Accept as deliberate / Revert / Amend / Discuss.")
                    with g.cell():
                        with st_block(_cell_act):
                            st_write(bs.keyword + s.center_txt, "\U0001f5e3️ Config Transparency")
                            st_space("v", 0.5)
                            st_write(bs.body, "Any activity that materialises a config.yaml field with visible impact must emit an Inform line — e.g. ‘Config applied: git.strategy = worktree (default — to change: /gse:hug)’.")

    # ─────────────────────────────────────────────────────────────────
    # Slide 7 — Guardrails 3/3 (Test Evidence, Execution Fidelity)
    # ─────────────────────────────────────────────────────────────────
    st_slide_break(marker_label="Guardrails (3/3) — Delivery & Fidelity")
    with st_block(_pf):
        with st_block(s.center_txt):
            _slide_title(
                "Guardrails (3/3) — Delivery & Fidelity",
                "At Delivery Time",
                [
                    ("Intent", "These two guardrails make sure nothing ships without test evidence, and that each activity's internal steps are actually executed (not silently skipped)."),
                    ("Scope coverage", "Test Evidence is invoked at /gse:deliver Step 1.5. Execution Fidelity applies to every activity — intra-activity, not just routing."),
                ],
                position="left",
            )
            st_space("v", 1)
            with st_zoom(110):
                with st_grid(cols="1fr 1fr", gap="20px") as g:
                    with g.cell():
                        with st_block(_cell):
                            st_write(bs.keyword + s.center_txt, "✅ Test Execution Evidence")
                            st_space("v", 0.5)
                            st_write(bs.body, "/gse:deliver Step 1.5 blocks merge when a must-REQ lacks test_evidence.status: pass. Three sub-guardrails: unexecuted tests, unexecuted test strategy, stale evidence.")
                    with g.cell():
                        with st_block(_cell_acc):
                            st_write(bs.keyword + s.center_txt, "\U0001f3af Execution Fidelity")
                            st_space("v", 0.5)
                            st_write(bs.body, "Each activity follows a declared sequence of Steps. The agent must execute them all, in order. Any self-decided skip must be announced with a reason — no silent shortcuts.")

    # ─────────────────────────────────────────────────────────────────
    # Slide 8 — New Methodological Mechanisms (2×3 grid)
    # ─────────────────────────────────────────────────────────────────
    st_slide_break(marker_label="New Methodological Mechanisms")
    with st_block(_pf):
        with st_block(s.center_txt):
            _slide_title(
                "New Methodological Mechanisms",
                "Mechanisms Added — Beyond Guardrails",
                [
                    ("Intent Capture", "v0.28.0 — on greenfield projects, /gse:go elicits INT-001 (verbatim + reformulation + users + boundaries + open questions) before anything else."),
                    ("Open Questions (OQ-)", "v0.29.0 — any ambiguity becomes a first-class artefact with id, question, resolves_in (ASSESS|PLAN|REQS|DESIGN), impact, status. Step 0 Gate resolves them."),
                    ("Scaffold-as-preview", "v0.33.0 — /gse:preview offers 2 variants: static description OR runnable scaffold (Vite+React, Streamlit, Next.js) that becomes the base of /gse:produce."),
                    ("Policy tests", "v0.35.0 — first-class layer in the test pyramid (5% baseline). Checks structural rules (layering, licenses, naming, import boundaries) via static analysis."),
                    ("Complexity point semantics", "v0.34.0 — 1 pt = coupled AI + human effort (≈ 1 hour paired session). S/M/L scale abandoned in favour of integers. Appendix B grid for maintenance activities."),
                    ("Framework isolation", "v0.37.2 — architect agent proposes a framework-free domain module (src/domain/** stdlib only) when heavy UI + non-trivial business logic coexist."),
                ],
                position="left",
            )
            st_space("v", 1)
            with st_zoom(110):
                _render_cell_grid([
                    ("\U0001f9ed", "Intent Capture", "INT-001 on greenfield — verbatim + reformulation + boundaries"),
                    ("❓", "Open Questions", "OQ- artefact, Step 0 Gate resolves pointing questions"),
                    ("\U0001f3d7️", "Scaffold-as-preview", "Runnable scaffold becomes the produce baseline"),
                    ("\U0001f4dc", "Policy tests", "A new kind of test: it checks that the code follows the project's rules, not that the code works."),
                    ("\U0001f9ee", "Complexity points", "1 pt ≈ 1h paired — integers, no S/M/L"),
                    ("\U0001f9f1", "Framework isolation", "Keep the business logic separate from the UI framework, so it can be tested and reused on its own."),
                ], cols="1fr 1fr 1fr")

    # ─────────────────────────────────────────────────────────────────
    # Slide 9 — Coach 1/4 (Pedagogy + Profile calibration)
    # ─────────────────────────────────────────────────────────────────
    st_slide_break(marker_label="Coach (1/4) — Pedagogy & Calibration")
    with st_block(_pf):
        with st_block(s.center_txt):
            _slide_title(
                "Coach (1/4) — Pedagogy & Calibration",
                "Who You Are, What You Learn",
                [
                    ("Coach", "v0.36.0 → v0.37.0 — tutor and proto-coach merged into a single observational agent watching AI + user collaboration on 8 axes."),
                    ("Per-axis toggle", "config.yaml → coach.axes.<axis_name> (snake_case). Each axis is independently on/off."),
                    ("Output tier", "All workflow-axis outputs are Inform-tier — they never block. Proactive by default (opt-out via coach.proactive_gap_detection)."),
                ],
                position="left",
            )
            st_space("v", 1)
            with st_zoom(110):
                with st_grid(cols="1fr 1fr", gap="20px") as g:
                    with g.cell():
                        with st_block(_cell):
                            st_write(bs.keyword + s.center_txt, "\U0001f393 Axis 1 — Pedagogy (P14)")
                            st_space("v", 0.5)
                            st_write(bs.body, "Inserts short explanations during activities and proposes learning sessions at natural breaks (sprint close, tricky task). Each session leaves a persistent LRN- note grounded in your project.")
                    with g.cell():
                        with st_block(_cell_acc):
                            st_write(bs.keyword + s.center_txt, "\U0001f4d0 Axis 2 — Profile Calibration")
                            st_space("v", 0.5)
                            st_write(bs.body, "Watches the gap between your declared HUG profile and how you actually behave. If you keep asking for simpler or longer explanations, it suggests /gse:hug --update on that dimension.")

    # ─────────────────────────────────────────────────────────────────
    # Slide 10 — Coach 2/4 (Sprint velocity + Workflow health)
    # ─────────────────────────────────────────────────────────────────
    st_slide_break(marker_label="Coach (2/4) — Velocity & Health")
    with st_block(_pf):
        with st_block(s.center_txt):
            _slide_title(
                "Coach (2/4) — Velocity & Health",
                "How the Sprint is Going",
                [
                    ("Velocity", "Reads complexity-point estimates (integers, 1 pt ≈ 1 paired hour) across last N sprints."),
                    ("Health", "Reads activity_history in status.yaml — detects skips, re-runs, non-standard sequences."),
                ],
                position="left",
            )
            st_space("v", 1)
            with st_zoom(110):
                with st_grid(cols="1fr 1fr", gap="20px") as g:
                    with g.cell():
                        with st_block(_cell_act):
                            st_write(bs.keyword + s.center_txt, "\U0001f3c3 Axis 3 — Sprint Velocity")
                            st_space("v", 0.5)
                            st_write(bs.body, "Compares planned vs consumed complexity points across recent sprints and flags chronic overcommit — e.g. ‘14 done vs 18 planned three times in a row, target 15 next sprint’.")
                    with g.cell():
                        with st_block(_cell):
                            st_write(bs.keyword + s.center_txt, "\U0001f4ca Axis 4 — Workflow Health")
                            st_space("v", 0.5)
                            st_write(bs.body, "Notices skipped activities, re-runs, or out-of-order sequences (e.g. /gse:produce before /gse:plan). Names the deviation without blocking.")

    # ─────────────────────────────────────────────────────────────────
    # Slide 11 — Coach 3/4 (Quality trends + Engagement pattern)
    # ─────────────────────────────────────────────────────────────────
    st_slide_break(marker_label="Coach (3/4) — Quality & Engagement")
    with st_block(_pf):
        with st_block(s.center_txt):
            _slide_title(
                "Coach (3/4) — Quality & Engagement",
                "Output Quality and Decision Health",
                [
                    ("Quality", "Reads test_evidence outcomes and RVW- findings across sprints. High reviewed/done ratio = clean PRODUCE."),
                    ("Engagement", "Watches P16 consecutive_acceptances counter — an early warning for complaisance or fatigue."),
                ],
                position="left",
            )
            st_space("v", 1)
            with st_zoom(110):
                with st_grid(cols="1fr 1fr", gap="20px") as g:
                    with g.cell():
                        with st_block(_cell_acc):
                            st_write(bs.keyword + s.center_txt, "\U0001f9ea Axis 5 — Quality Trends")
                            st_space("v", 0.5)
                            st_write(bs.body, "Tracks how test pass-rate, HIGH-severity findings, and the reviewed/done ratio evolve sprint after sprint. Points to the quality dimension that needs attention next.")
                    with g.cell():
                        with st_block(_cell_act):
                            st_write(bs.keyword + s.center_txt, "\U0001f91d Axis 6 — Engagement Pattern")
                            st_space("v", 0.5)
                            st_write(bs.body, "Spots long streaks of silent acceptance (complaisance risk) or systematic Gate dismissals (fatigue). Invites you to revisit the most impactful recent choices.")

    # ─────────────────────────────────────────────────────────────────
    # Slide 12 — Coach 4/4 (Process deviation + Sustainability)
    # ─────────────────────────────────────────────────────────────────
    st_slide_break(marker_label="Coach (4/4) — Deviation & Sustainability")
    with st_block(_pf):
        with st_block(s.center_txt):
            _slide_title(
                "Coach (4/4) — Deviation & Sustainability",
                "Method Drift and Pacing",
                [
                    ("Deviation", "Reads DEC- entries tagged type: methodology-deviation."),
                    ("Sustainability", "Reads session cadence (session lengths, gaps) vs spec §8 pacing guidance."),
                ],
                position="left",
            )
            st_space("v", 1)
            with st_zoom(110):
                with st_grid(cols="1fr 1fr", gap="20px") as g:
                    with g.cell():
                        with st_block(_cell):
                            st_write(bs.keyword + s.center_txt, "\U0001f6a6 Axis 7 — Process Deviation")
                            st_space("v", 0.5)
                            st_write(bs.body, "Detects repeated same-shape deviations — e.g. always skipping /gse:reqs, always running preview twice. Suggests either formalising the habit in config or correcting it.")
                    with g.cell():
                        with st_block(_cell_acc):
                            st_write(bs.keyword + s.center_txt, "\U0001f331 Axis 8 — Sustainability")
                            st_space("v", 0.5)
                            st_write(bs.body, "Reads your session cadence and sprint sizes. Warns about marathon sessions, very long gaps, or sprint totals consistently above the sustainable range.")

    # ─────────────────────────────────────────────────────────────────
    # Slide 13 — Data Schemas Stabilised (1 slide, one cell per schema)
    # ─────────────────────────────────────────────────────────────────
    st_slide_break(marker_label="Schemas Stabilised")
    with st_block(_pf):
        with st_block(s.center_txt):
            _slide_title(
                "Schemas Stabilised",
                "Hardening the Data Foundations",
                [
                    ("Why this matters", "Tooling (dashboard, audit, orchestrator) only works when schemas are canonical. These changes unblocked downstream automation."),
                    ("Backward compatibility", "status.yaml.lifecycle_phase → current_phase is aliased during read; new projects write the canonical name only."),
                ],
                position="left",
            )
            st_space("v", 1)
            with st_zoom(110):
                _render_cell_grid([
                    ("\U0001f464", "profile.yaml", "user: {name, git_email} split + 13 dims. 6 aligned enums. project_domain → 9 canonical values."),
                    ("\U0001f4cb", "backlog.yaml", "9-value status enum: open | planned | in-progress | review | reviewed | fixing | done | delivered | deferred."),
                    ("\U0001f9ed", "status.yaml", "lifecycle_phase → current_phase. workflow_observations[] persist cross-sprint (trending)."),
                    ("\U0001f501", "TASK machine", "in-progress → review → {reviewed | fixing} → done → delivered. /gse:deliver accepts reviewed OR done."),
                    ("\U0001f4be", "checkpoint.yaml", "Flat refactor with structured sub-blocks: status_snapshot, backlog_sprint_snapshot, git_state."),
                    ("\U0001f4c1", "30 templates", "+ plan.yaml, decisions.md, checkpoint.yaml, methodology-feedback.md, MANIFEST.yaml (index)."),
                ], cols="1fr 1fr 1fr")

    # ─────────────────────────────────────────────────────────────────
    # Slide 14 — Dashboard & Agents (1 slide, one cell per topic)
    # ─────────────────────────────────────────────────────────────────
    st_slide_break(marker_label="Dashboard & Agents")
    with st_block(_pf):
        with st_block(s.center_txt):
            _slide_title(
                "Dashboard & Agents",
                "Live State and Specialised Agents",
                [
                    ("Dashboard", "docs/dashboard.html — auto-regenerated on every editor write, with failure surfacing on a red banner."),
                    ("Agents", "11 agents now spread across 5 archetypes. Finding formats unified around RVW-NNN + perspective: to eliminate old ad-hoc prefixes."),
                ],
                position="left",
            )
            st_space("v", 1)
            with st_zoom(110):
                _render_cell_grid([
                    ("\U0001f504", "Auto-regen hook", "PostToolUse on Edit/Write/MultiEdit invokes dashboard.py --if-stale. Debounce configurable (default 5s)."),
                    ("\U0001f6a8", "Error banner", "Red banner injected from .gse/.dashboard-error.yaml when regeneration fails."),
                    ("\U0001f4da", "audit_history", "status.yaml rolling log — last 20 runs retained, older runs summarised."),
                    ("\U0001f916", "11 agents", "10 → 11: deploy-operator added (v0.42). coach unified from tutor + proto-coach."),
                    ("\U0001f3db️", "5 archetypes", "Identity (orchestrator) / Reviewer (7) / Operational (deploy-operator) / Observational (coach) / Compliance (guardrail-enforcer)."),
                    ("\U0001f3f7️", "Unified findings", "Severity HIGH/MEDIUM/LOW across reviewers. RVW-NNN + perspective: replaces SEC-, UX-, DEVIL-…"),
                ], cols="1fr 1fr 1fr")

    # ─────────────────────────────────────────────────────────────────
    # Slide 15 — DLH Cycle — 20 AMÉL (1 slide, one cell per fact)
    # ─────────────────────────────────────────────────────────────────
    st_slide_break(marker_label="DLH Cycle — 20 AMÉL")
    with st_block(_pf):
        with st_block(s.center_txt):
            _slide_title(
                "Training Feedback — the DLH Cycle",
                "20 AMÉL Derived from Session Observations",
                [
                    ("DLH cycle", "v0.23.0 → v0.37.4 — improvements extracted directly from 3 training days with 12 learners."),
                    ("Pattern → solution", "Each AMÉL documents one pattern observed in session AND the methodological answer capitalised into GSE-One."),
                    ("Closure", "Officially closed with v0.38.0. All 20 AMÉL are now wired into the methodology and the audit engine."),
                ],
                position="left",
            )
            st_space("v", 1)
            with st_zoom(110):
                _render_cell_grid([
                    ("\U0001f465", "Source signal", "3 training days × 12 learners — dense, firsthand observation."),
                    ("\U0001f501", "Pattern → answer", "Each AMÉL pairs one observed pattern with the exact methodological response."),
                    ("\U0001f3af", "Coverage", "Freeze, root-cause, intent, OQ, scaffold, policy tests, coach, framework isolation…"),
                    ("✅", "Closure", "Official v0.38.0 — the 20 AMÉL are wired into the method and the audit engine."),
                ], cols="1fr 1fr", alternating=False)

    # ─────────────────────────────────────────────────────────────────
    # Slide 16 — Post-audit Remediation (1 slide, one cell per fact)
    # ─────────────────────────────────────────────────────────────────
    st_slide_break(marker_label="Post-audit Remediation Series")
    with st_block(_pf):
        with st_block(s.center_txt):
            _slide_title(
                "Post-audit Remediation — v0.51 → v0.60",
                "Coherence Restoration, No Breaking Change",
                [
                    ("Trigger", "A full methodology audit on v0.50 (then again on v0.57) surfaced 9 clusters of cross-cutting inconsistencies."),
                    ("Approach", "Discipline over novelty: each cluster fixed in a dedicated release, with explicit capitalisation of the fix workflow in CLAUDE.md (v0.56.0)."),
                    ("Result", "Tools (dashboard, audit, orchestrator) now read consistent schemas; user-facing behaviour unchanged."),
                ],
                position="left",
            )
            st_space("v", 1)
            with st_zoom(110):
                _render_cell_grid([
                    ("\U0001f4c5", "Window", "v0.51.0 → v0.60.0 — 10 releases concentrated over a few days."),
                    ("\U0001f9e9", "9 clusters", "Errors, warnings, orphaned schemas, cursor centralisation, upward refinements, contract unification, workflow capitalisation, final propagation."),
                    ("\U0001f4ca", "Scale", "~76 corrections applied • 5 documented false positives • 0 regressions across 72 tests."),
                    ("\U0001f6e1️", "Invariant", "No breaking change — all user-facing APIs preserved. Coherence restored, not rewritten."),
                ], cols="1fr 1fr", alternating=False)

                st_space("v", 1)
                st_write(bs.accent, "Feedback in → Method out. The flywheel you saw — on the method itself.")
