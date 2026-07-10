"""Postscript — GSE-One evolutions since the session: v0.20.4 → v0.85.0 (2026-04-17 → 2026-07-10)."""
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
    # Slide 1 — Overview: v0.20.4 → v0.85.0 (2×3 grid)
    # ─────────────────────────────────────────────────────────────────
    st_slide_break(marker_label="Since the Session — v0.20.4 → v0.85.0")
    with st_block(_pf):
        with st_block(s.center_txt):
            _slide_title(
                "Since the Session — v0.20.4 → v0.85.0",
                "Post-session Evolution of GSE-One",
                [
                    ("Period", "2026-04-17 → 2026-07-10 — three months of iteration driven by training feedback, meta-audits and platform expansion."),
                    ("Scope", "End-user oriented summary: what forkers and method users will actually notice."),
                    ("Reading the block", "Themes are grouped logically, not chronologically. Version tags are shown for traceability, not as a roadmap."),
                    ("Principle", "Trainings are always given on the latest version only — this postscript tracks v0.85.0 and will keep moving with the method."),
                    ("No breaking changes", "All user-facing APIs preserved across the whole window. Growth came from audit → fix trains, not rewrites."),
                ],
                position="center",
            )
            st_space("v", 1)
            with st_zoom(120):
                st_write(bs.accent, "From GSE-One v0.20.4 to v0.85.0 in three months.")
                st_space("v", 2)
                with st_grid(cols="1fr 1fr 1fr", gap="16px") as g:
                    with g.cell():
                        with st_block(_cell):
                            st_write(bs.stat + s.center_txt, "24")
                            st_write(bs.body, "commands (activities)")
                    with g.cell():
                        with st_block(_cell_acc):
                            st_write(bs.stat + s.center_txt, "11")
                            st_write(bs.body, "agents across 5 archetypes")
                    with g.cell():
                        with st_block(_cell_act):
                            st_write(bs.stat + s.center_txt, "5")
                            st_write(bs.body, "platforms (3 primary + 2 experimental)")
                    with g.cell():
                        with st_block(_cell):
                            st_write(bs.stat + s.center_txt, "29")
                            st_write(bs.body, "template files (28 + MANIFEST)")
                    with g.cell():
                        with st_block(_cell_acc):
                            st_write(bs.stat + s.center_txt, "125")
                            st_write(bs.body, "unit tests (72 at v0.60)")
                    with g.cell():
                        with st_block(_cell_act):
                            st_write(bs.stat + s.center_txt, "3")
                            st_write(bs.body, "audit → fix trains, 0 regressions")

    # ─────────────────────────────────────────────────────────────────
    # Slide 2 — Platforms & Installation (5 platforms, 4 install modes)
    # ─────────────────────────────────────────────────────────────────
    st_slide_break(marker_label="Platforms & Installation")
    with st_block(_pf):
        with st_block(s.center_txt):
            _slide_title(
                "Platforms & Installation",
                "Five Platforms, One Methodology",
                [
                    ("Primary platforms", "Claude Code, Cursor, opencode — plugin and no-plugin modes (v0.20.5 no-plugin: skills install as gse-<name>/ → /gse-<name>; v0.21.0 native opencode)."),
                    ("Secondary platforms", "v0.72.0 — Codex CLI + Gemini CLI as experimental targets: 24 activities as skills / command TOMLs, sub-agents, hooks. gse-orchestrator-lite (≤ 32 KiB) serves as Codex AGENTS.md."),
                    ("curl | sh bootstrap", "v0.62.7 — install.sh (POSIX sh) resolves a GitHub release tarball and delegates to install.py; env-var overrides (GSE_PLATFORM, GSE_MODE, …), uninstall/upgrade subcommands, release pipeline on v* tags."),
                    ("--mode local", "v0.73.0 — fully project-local install: registry in <project>/.gse/registry, nothing written under $HOME. All 5 platforms."),
                    ("--mode sandbox", "v0.74.0 — HOME-isolated install under <project>/.gse-sandbox/ with a launcher (sh .gse-sandbox/run since v0.79.0) + generic --bypass / --auto flags (v0.80.0). Codex / Gemini / opencode."),
                    ("v0.85.0 installer fixes", "local/sandbox without GSE_PROJECT_DIR no longer installs into the wiped temp dir; relative paths absolutized; uninstall reaches local/sandbox projects; per-platform×mode Next-step hints."),
                ],
                position="center",
            )
            st_space("v", 1)
            with st_zoom(110):
                _render_cell_grid([
                    ("\U0001f310", "5 platforms", "Claude Code • Cursor • opencode + Codex CLI • Gemini CLI (experimental, v0.72.0)"),
                    ("\U0001f9e9", "Orchestrator lite", "Condensed orchestrator ≤ 32 KiB — ships as Codex AGENTS.md"),
                    ("⚡", "curl | sh", "v0.62.7 — one-line bootstrap over GitHub releases, uninstall/upgrade built in"),
                    ("\U0001f4c2", "--mode local", "v0.73.0 — registry in .gse/registry, no $HOME writes, committable"),
                    ("\U0001f512", "--mode sandbox", "v0.74.0 — isolated $HOME, launch any day with sh .gse-sandbox/run"),
                    ("\U0001f527", "v0.85.0 fixes", "Safe local/sandbox paths + per-platform×mode next-step hints"),
                ])

    # ─────────────────────────────────────────────────────────────────
    # Slide 3 — Deploy & Training Infrastructure
    # ─────────────────────────────────────────────────────────────────
    st_slide_break(marker_label="Deploy & Training Infrastructure")
    with st_block(_pf):
        with st_block(s.center_txt):
            _slide_title(
                "/gse:deploy — Hetzner + Coolify + Cohorts",
                "Auto-piloted Deployment, Now Training-grade",
                [
                    ("6 phases, 3 modes", "setup → provision → secure → install-coolify → configure-domain → deploy; solo / training (multi-learner subdomains) / partial (BYO server, auto-detected from .env). 4 Dockerfile templates. deploy-operator = 10th agent, first Operational archetype."),
                    ("20-subcommand CLI", "deploy.py grew to 20 subcommands (deploy-app, app-status, subdomain, env-set/get/delete, record-*, state, detect, training-*…)."),
                    ("Private repos", "v0.62.3 → v0.64.0 — Coolify GitHub App routing: private repos auto-routed when COOLIFY_GITHUB_APP_UUID is set; server_uuid auto-resolution fixes HTTP 422; both keys join the .env.training handout."),
                    ("Role-aware guide", "v0.85.0 — the GitHub App setup guide is now distributed with the plugin as references/private-repo-github-app-setup.md (role-neutral: solo users are their own App owner). /gse:deploy --destroy also cleans SERVER_UUID + COOLIFY_GITHUB_APP_UUID."),
                    ("DAY06 cohort feedback", "v0.62.6 — 5 pedagogical inserts from live training friction: Delivery Map (deliver Step 0.0), OPEN ITEMS synthesis (status Step 6.5), deployed-version check (deploy Phase 6 Step 6), sprint-in-progress pedagogy (backlog), shared-file hint (plan)."),
                    ("Ops knowledge", "deploy-operator carries a 9-row Coolify/build quirks catalog (server_uuid 422, curl-on-slim, healthy-but-stale, Traefik :8080, DNS outage…)."),
                ],
                position="left",
            )
            st_space("v", 1)
            with st_zoom(110):
                _render_cell_grid([
                    ("⚙️", "6 phases · 3 modes", "solo • training (multi-learner) • partial (BYO server) — 20-subcommand deploy.py"),
                    ("\U0001f510", "Private repos", "v0.64.0 — GitHub App routing + server_uuid auto-resolution (no more 422)"),
                    ("\U0001f4d6", "Distributed guide", "v0.85.0 — private-repo-github-app-setup.md ships with the plugin"),
                    ("\U0001f5fa️", "Delivery Map", "v0.62.6 — deliver Step 0.0 previews all 9 steps with their defaults"),
                    ("\U0001f4cb", "OPEN ITEMS", "v0.62.6 — status Step 6.5: findings, in-flight TASKs, OQs, orphan worktrees"),
                    ("\U0001f50e", "Version check", "v0.62.6 — deploy verifies the live app version vs repo HEAD (silent rollbacks)"),
                ])

    # ─────────────────────────────────────────────────────────────────
    # Slide 4 — Audit & Meta-audit
    # ─────────────────────────────────────────────────────────────────
    st_slide_break(marker_label="Audit & Meta-audit")
    with st_block(_pf):
        with st_block(s.center_txt):
            _slide_title(
                "Audit & Meta-audit",
                "The Method Audits Projects — and Itself",
                [
                    ("/gse:audit (project)", "24th activity — detects methodological drift in a live project: hybrid engine (deterministic Python checks + semantic layer + auto-trigger). AUD- findings, distinct from RVW-. Reports go to docs/sprints/sprint-NN/audit-{timestamp}.md when a sprint is active, else .gse/audits/."),
                    ("Meta-audit (corpus)", "/gse-meta-audit (renamed from /gse-audit in v0.84.0) — 28 declarative jobs across 6 categories audit the methodology corpus itself, incl. Category F distribution hygiene (v0.62.0)."),
                    ("Registry contract v2", "v0.75.0 — ONE living artifact _LOCAL/audit/audit.json (stable AUD-<hash> ids, per-finding lifecycle verdict → status → resolution); markdown is a throwaway /tmp render. Replaces the retired multi-file output (audit-<ts>.md, latest.md, latest.json)."),
                    ("Durable backlog", "v0.85.0 — _LOCAL/audit/backlog.json holds decision-ready dossiers + audit.py --backlog-* commands."),
                    ("Three fix trains", "v0.57.0 audit → v0.58–v0.60 9-cluster series; v0.62.8 audit (16 errors, 103 warnings) → v0.63.0 treatment; v0.84.0 full meta-audit → v0.85.0 fix train: 126 verified findings, 0 false positives, 24-agent verification pass."),
                    ("Test suite", "72 tests at v0.60 → 125 tests at v0.85 (audit, counters, dashboard, deploy, hooks)."),
                ],
                position="left",
            )
            st_space("v", 1)
            with st_zoom(110):
                _render_cell_grid([
                    ("\U0001f3af", "/gse:audit", "Project-level drift detection — reports in docs/sprints/sprint-NN/ or .gse/audits/"),
                    ("\U0001f9ea", "Meta-audit", "28 jobs, 6 categories — the methodology audits its own corpus"),
                    ("\U0001f5c3️", "Registry v2", "v0.75.0 — single audit.json, stable AUD-<hash> ids, lifecycle per finding"),
                    ("\U0001f4e6", "Durable backlog", "v0.85.0 — backlog.json with decision-ready dossiers"),
                    ("\U0001f682", "Fix trains", "v0.85.0 — 126 verified findings, 0 false positives, 24-agent verification"),
                    ("✅", "125 tests", "72 → 125 unit tests, green at every release"),
                ])

    # ─────────────────────────────────────────────────────────────────
    # Slide 5 — Guardrails & Hooks
    # ─────────────────────────────────────────────────────────────────
    st_slide_break(marker_label="Guardrails & Hooks")
    with st_block(_pf):
        with st_block(s.center_txt):
            _slide_title(
                "Guardrails & Hooks",
                "Standing Protections — Now Actually Enforced",
                [
                    ("7 guardrails since the session", "Sprint Freeze, Git Identity, Root-Cause (P16), Scope Reconciliation, Config Transparency, Test Execution Evidence, Execution Fidelity."),
                    ("Override taxonomy", "Soft warns (continue on confirm), Hard blocks (override with documented rationale, logged as guardrail_override), Emergency halts and is immutable — never adjusted, for any expertise level. Sprint Freeze offers no 'amend closed sprint' escape hatch."),
                    ("Sprint Freeze — 8 activities", "v0.63.0 — the freeze now also guards /gse:reqs, /gse:design, /gse:preview, /gse:tests (in addition to task, produce, fix, review). LC03 flow restored: compound > integrate > plan --strategic opens the successor sprint."),
                    ("Git Identity Gate", "Before the first commit: 5 options — Set global / Set local (project only) / Quick placeholder / I'll set it myself / Discuss (hug.md Step 4, spec P12.6)."),
                    ("Hooks layer repaired", "v0.63.0 — the guard hooks read a nonexistent CLAUDE_TOOL_INPUT env var and had never fired since creation. Rebuilt on stdin-JSON transport with regex matching (any force-push form) and live config.yaml toggles."),
                    ("Hook hardening", "v0.82.2 — Gemini hooks were silently inert (wrong event names, PreToolUse → BeforeTool); v0.85.0 — the +refspec force-push bypass closed on all platforms, regression-tested."),
                ],
                position="left",
            )
            st_space("v", 1)
            with st_zoom(110):
                _render_cell_grid([
                    ("\U0001f9ca", "Sprint Freeze", "Delivered sprint = frozen. Now guards 8 activities (v0.63.0). No escape hatch — open the next sprint."),
                    ("\U0001f464", "Git Identity", "5-option Gate: Global / Local / Placeholder / Myself / Discuss"),
                    ("\U0001f50e", "Root-Cause (P16)", "Read → Symptom → Hypothesis + Evidence → Patch; devil's advocate after repeated failures"),
                    ("⚖️", "Scope & Config", "Git-vs-plan reconciliation Gate + 'Config applied:' Inform lines"),
                    ("✅", "Evidence & Fidelity", "No merge without test evidence; every declared Step executed, skips announced"),
                    ("\U0001fa9d", "Hooks repaired", "v0.63.0 stdin-JSON (never worked before!) • v0.82.2 Gemini events • v0.85.0 +refspec closed"),
                ])

    # ─────────────────────────────────────────────────────────────────
    # Slide 6 — AI Integrity (P15/P16)
    # ─────────────────────────────────────────────────────────────────
    st_slide_break(marker_label="AI Integrity — P15/P16")
    with st_block(_pf):
        with st_block(s.center_txt):
            _slide_title(
                "AI Integrity — P15 / P16 Hardened",
                "Trusting the Agent, Verifiably",
                [
                    ("Deterministic counters", "v0.66.0 — tools/counters.py: get/incr/reset for the 3 P15/P16 integrity counters + staleness backstop (counters_last_write in status.yaml, checked by /gse:go and /gse:resume)."),
                    ("Devil's advocate isolation", "v0.69.0 — the review pass MUST run in a freshly spawned sub-agent (context brief, no conversation history); execution mode traced (isolated | inline-degraded), inline fallback emits a visible Inform note."),
                    ("Delivery integrity", "v0.70.0 — deliver Step 1.6 (Lightweight mode): devil-advocate 'delivery-integrity' mode before any merge — library/API existence, versions, unverified critical assertions; ≤ 5 findings, HIGH Gates the merge."),
                    ("Confidence escalation", "v0.85.0 spec §P15 — 'Verified but wrong' claims escalate the review finding to CRITICAL at merge time: false certainty is the most dangerous failure mode, and this is the only path to CRITICAL for reviewer findings."),
                    ("State integrity", "v0.82.0 — a failing tool/hook/validation is diagnosed and reported, never worked around by writing invented or out-of-enum values into state files (observed: a run forged current_phase to force a crashing dashboard through)."),
                    ("Anti-framing (P8)", "v0.68.0 — every consequence-analysis choice-Gate must disclose one credible 'Excluded alternative:' with the exclusion reason, recorded in the DEC- entry and audited a posteriori by the devil's advocate."),
                ],
                position="left",
            )
            st_space("v", 1)
            with st_zoom(110):
                _render_cell_grid([
                    ("\U0001f522", "counters.py", "v0.66.0 — P15/P16 counters become deterministic, with a staleness backstop"),
                    ("\U0001f47f", "DA isolation", "v0.69.0 — devil's advocate always in a fresh sub-agent, execution mode traced"),
                    ("\U0001f6c2", "Delivery integrity", "v0.70.0 — integrity pass before merge in Lightweight mode (deliver Step 1.6)"),
                    ("\U0001f6a8", "Verified-but-wrong", "v0.85.0 — false certainty escalates to CRITICAL, the only CRITICAL path"),
                    ("\U0001f9fe", "State integrity", "v0.82.0 — tool failures are reported, never masked with invented state"),
                    ("\U0001f3ad", "P8 anti-framing", "v0.68.0 — Gates disclose the credible alternative that was NOT offered"),
                ])

    # ─────────────────────────────────────────────────────────────────
    # Slide 7 — Requirements & Planning Mechanisms
    # ─────────────────────────────────────────────────────────────────
    st_slide_break(marker_label="Requirements & Planning Mechanisms")
    with st_block(_pf):
        with st_block(s.center_txt):
            _slide_title(
                "Requirements & Planning Mechanisms",
                "From Intent to Sprint — the New Building Blocks",
                [
                    ("Intent Capture", "v0.28.0 — on greenfield projects, /gse:go elicits INT-001 (verbatim + reformulation + users + boundaries + open questions) before anything else; keystroke-minimal flow."),
                    ("Open Questions (OQ-)", "v0.29.0 — any ambiguity becomes a first-class artefact with id, question, resolves_in (ASSESS|PLAN|REQS|DESIGN), impact, status. Step 0 Gates resolve them."),
                    ("Scaffold-as-preview", "v0.33.0 — /gse:preview offers 2 variants: static description OR runnable scaffold (Vite+React, Streamlit, Next.js) that becomes the base of /gse:produce."),
                    ("Policy tests", "v0.35.0 — first-class layer in the test pyramid: checks structural rules (layering, licenses, naming, import boundaries) via static analysis."),
                    ("Complexity points", "v0.34.0 — 1 pt = coupled AI + human effort (≈ 1 hour paired session), integers instead of S/M/L, Cost Assessment Grid for maintenance activities. Complexity assessment refined to a 7-signal + pre-filter model (v0.85.0)."),
                    ("Excluded alternative", "v0.68.0 — the P8 anti-framing line joins the P4 Gate pattern and the DEC- format: decisions record the road not shown, not just the road not taken."),
                ],
                position="left",
            )
            st_space("v", 1)
            with st_zoom(110):
                _render_cell_grid([
                    ("\U0001f9ed", "Intent Capture", "INT-001 on greenfield — verbatim + reformulation + boundaries"),
                    ("❓", "Open Questions", "OQ- artefact — ambiguities tracked to resolution at Step 0 Gates"),
                    ("\U0001f3d7️", "Scaffold-as-preview", "Runnable scaffold becomes the produce baseline"),
                    ("\U0001f4dc", "Policy tests", "Tests that check the code follows the project's rules, not that it works"),
                    ("\U0001f9ee", "Complexity points", "1 pt ≈ 1h paired — integers + Cost Assessment Grid"),
                    ("\U0001f3ad", "Excluded alternative", "Every consequence Gate discloses a credible option it did NOT offer"),
                ])

    # ─────────────────────────────────────────────────────────────────
    # Slide 8 — Coach & Learning
    # ─────────────────────────────────────────────────────────────────
    st_slide_break(marker_label="Coach & Learning")
    with st_block(_pf):
        with st_block(s.center_txt):
            _slide_title(
                "Coach & Learning",
                "One Observational Agent, Eight Axes",
                [
                    ("Coach agent", "v0.36.0 → v0.37.0 — tutor and proto-coach merged into a single observational agent watching AI + user collaboration on 8 axes; per-axis toggle in config.yaml (coach.axes.<axis>), all outputs Inform-tier (never block)."),
                    ("Invocation contract", "v0.62.6 — the orchestrator carries a mandatory coach evaluation table (6 moments × axes) and 4 operational invariants; skipping is itself a recorded observation."),
                    ("Pedagogical ownership", "v0.71.0 — spec §P14 ownership map: coach.md is the runtime authority for proactive triggers and anti-spam; /gse:learn is never blocked."),
                    ("HUG completeness", "v0.81.3 — preference dimensions can no longer be silently defaulted by a preset: all 13 dimensions are explicit numbered choices, and consent-bearing ones (decision involvement, learning goals, contextual tips) are never inferred."),
                    ("Text-fallback discipline", "v0.81.2 — on runtimes without an interactive widget (Codex, Gemini), the HUG interview stays numbered-choice, ≤ 3 dimensions per message — no free-text walls."),
                ],
                position="left",
            )
            st_space("v", 1)
            with st_zoom(105):
                _render_cell_grid([
                    ("\U0001f393", "1 · Pedagogy (P14)", "Explanations in-flow + LRN- learning sessions at natural breaks"),
                    ("\U0001f4d0", "2 · Profile calibration", "Declared HUG profile vs actual behavior — suggests /gse:hug --update"),
                    ("\U0001f3c3", "3 · Sprint velocity", "Planned vs consumed points — flags chronic overcommit"),
                    ("\U0001f4ca", "4 · Workflow health", "Skips, re-runs, out-of-order activity sequences"),
                    ("\U0001f9ea", "5 · Quality trends", "Test pass-rate, HIGH findings, reviewed/done ratio over sprints"),
                    ("\U0001f91d", "6 · Engagement", "Silent-acceptance streaks (complaisance) and Gate fatigue"),
                    ("\U0001f6a6", "7 · Process deviation", "Repeated same-shape deviations — formalise or correct"),
                    ("\U0001f331", "8 · Sustainability", "Session cadence, marathon sessions, sprint-size drift"),
                ], cols="1fr 1fr 1fr 1fr")

    # ─────────────────────────────────────────────────────────────────
    # Slide 9 — State & Data Model
    # ─────────────────────────────────────────────────────────────────
    st_slide_break(marker_label="State & Data Model")
    with st_block(_pf):
        with st_block(s.center_txt):
            _slide_title(
                "State & Data Model",
                "Canonical Schemas — the Base for All Tooling",
                [
                    ("Why this matters", "Dashboard, audit engine and orchestrator only work when schemas are canonical. The rename status.yaml.lifecycle_phase → current_phase is complete — no read-time alias survives."),
                    ("plan.yaml", "The sprint plan is a living artefact (status: active → completed); /gse:plan --tactical pulls pool items in, deliver Step 9.2 freezes it; plan-summary gained 7 Outcome Metrics (v0.67.0)."),
                    ("v0.85.0 polish", "/gse:task final status honors the TASK state machine (review when awaiting review, done when reviewed); /gse:status health display is mode-aware; /gse:backlog legend covers all 9 statuses; /gse:pause gains a commit-failure Gate (rescue branch / override / checkpoint+WARNING); /gse:resume verifies the current branch via the new checkpoint fields git_state.head / clean."),
                    ("Baseline state", "v0.81.0 — template status.yaml starts at current_sprint: 0 + current_phase: LC01 (a fresh project no longer pretends a sprint is active); dashboard handles the pre-first-sprint state instead of crashing."),
                    ("Dashboard", "Auto-regenerated by a PostToolUse hook with an error banner on failure; docs/dashboard.html is now gitignored (v0.82.0) — a regenerable view, not a versioned artefact."),
                ],
                position="left",
            )
            st_space("v", 1)
            with st_zoom(110):
                _render_cell_grid([
                    ("\U0001f464", "profile.yaml", "13 HUG dimensions, aligned enums — completeness invariant since v0.81.3"),
                    ("\U0001f4cb", "backlog.yaml", "9-value status enum: open | planned | in-progress | review | reviewed | fixing | done | delivered | deferred"),
                    ("\U0001f9ed", "status.yaml", "current_phase (rename complete) + task_status_snapshot + counters_last_write"),
                    ("\U0001f501", "TASK machine", "in-progress → review → {reviewed | fixing} → done → delivered — honored by /gse:task since v0.85.0"),
                    ("\U0001f4be", "checkpoint.yaml", "status_snapshot, backlog_sprint_snapshot, git_state (+ head / clean in v0.85.0 for resume verification)"),
                    ("\U0001f4c1", "29 template files", "28 artefact & config templates + MANIFEST.yaml (count corrected in v0.82.1)"),
                ], cols="1fr 1fr 1fr")

    # ─────────────────────────────────────────────────────────────────
    # Slide 10 — Community & Audit Trains — Closing
    # ─────────────────────────────────────────────────────────────────
    st_slide_break(marker_label="Community & the Flywheel")
    with st_block(_pf):
        with st_block(s.center_txt):
            _slide_title(
                "Community & the Flywheel",
                "Feedback In → Method Out",
                [
                    ("DLH cycle — 20 AMÉL", "v0.23.0 → v0.38.0 — 20 improvements extracted from 3 training days × 12 learners, each pairing an observed pattern with the methodological answer. Closed at v0.38.0; internal prefix later renamed ENH (v0.61.1)."),
                    ("DAY06 cohort", "v0.62.6 — a second cohort loop: 5 pedagogical inserts + 2 contract clarifications, no new activity or Gate."),
                    ("Audit trains", "2026-04-22 audit of v0.57.0 → 9-cluster series v0.58–v0.60 (~150 source edits, 72 tests green); v0.62.8 audit → v0.63.0 treatment (16 errors, 103 warnings, repaired hooks); v0.84.0 meta-audit → v0.85.0 fix train (126 verified findings, 0 false positives, 24-agent verification pass)."),
                    ("First external contribution", "v0.62.7 — the curl | sh installer was rebased from PR #8 by Tiago Sousa: the method now takes code from its practitioners."),
                    ("This deck", "Trainings are always given on the latest version — this postscript tracks v0.85.0 and moves with the method."),
                ],
                position="left",
            )
            st_space("v", 1)
            with st_zoom(110):
                _render_cell_grid([
                    ("\U0001f465", "Training cohorts", "DLH: 20 AMÉL closed at v0.38.0 • DAY06: 5 pedagogical inserts at v0.62.6"),
                    ("\U0001f682", "3 audit trains", "v0.57 → v0.58–0.60 • v0.62.8 → v0.63.0 • v0.84.0 → v0.85.0 (126 findings, 0 FP)"),
                    ("\U0001f91d", "Community", "PR #8 (curl installer) rebased in v0.62.7 — first external contribution"),
                    ("\U0001f6e1️", "Invariant", "No breaking change across the whole window — coherence restored, never rewritten"),
                ], cols="1fr 1fr", alternating=False)

                st_space("v", 1)
                st_write(bs.accent, "Feedback in → Method out. The flywheel you saw — on the method itself.")
