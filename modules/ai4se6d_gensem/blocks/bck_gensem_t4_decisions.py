"""T4 — Risk classification (P7), consequence horizons (P8), guardrails (P11), AI integrity (P15-P16)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip

_pf = s.project.containers.page_fill_top
_pfc = s.project.containers.page_fill_center
_cell = s.project.containers.cell_primary_bg + s.project.containers.cell_pad_md + s.center_txt
_cell_acc = s.project.containers.cell_accent_bg + s.project.containers.cell_pad_md + s.center_txt
_cell_act = s.project.containers.cell_active_bg + s.project.containers.cell_pad_md + s.center_txt


class BlockStyles:
    heading = s.project.titles.slide_title + s.center_txt
    body = Style.create(s.Large + s.center_txt + s.text.wrap.hyphens, "t4_body")
    accent = Style.create(s.Large + s.bold + s.project.colors.accent + s.center_txt, "t4_acc")
    highlight = Style.create(s.Large + s.bold + s.project.colors.highlight + s.center_txt, "t4_hl")
    keyword = Style.create(s.Large + s.bold + s.project.colors.primary, "t4_kw")
    critical = Style.create(s.Large + s.bold + s.project.colors.critical + s.center_txt, "t4_crit")
    success = Style.create(s.Large + s.bold + s.project.colors.success + s.center_txt, "t4_ok")
bs = BlockStyles


def build():
    st_slide_break(marker_label="Decisions, Risks & AI Integrity")

    # ── Slide: 3 Decision Tiers (P7) ────────────────────────────────
    with st_block(_pf):
        with st_block(s.center_txt):
            with st_grid(
                cols="95% 5%",
                gap="0px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    with st_zoom(90):
                        st_write(bs.heading, "P7: 3 Decision Tiers", tag=t.div, toc_lvl="+1")
                with g.cell():
                    st_hover_tooltip(
                        title="Risk-Based Decision Classification",
                        entries=[
                            ("Auto (green)", "Low risk — agent decides silently. Example: rename a variable, format code."),
                            ("Inform (amber)", "Moderate risk — agent decides but explains in 1 line. Example: add a utility dependency."),
                            ("Gate (red)", "High risk — full analysis presented, human validates. Example: change CSS framework, add external API."),
                            ("Calibration", "Beginners get more Gates; experts get more Auto. The agent adapts to your profile from /gse:hug."),
                            ("Composite rule", "3+ moderate risks on different dimensions automatically escalate to a Gate — even if no single risk is high."),
                        ],
                        scale="2vw", width="70vw", position="left",
                    )
            st_space("v", 1)
            with st_zoom(120):
                with st_grid(cols="repeat(auto-fit, minmax(280px, 1fr))", gap="16px") as g:
                    with g.cell():
                        with st_block(_cell_acc):
                            st_write(bs.success, "\U0001f7e2 Auto")
                            st_space("v", 0.5)
                            st_write(bs.body, "Agent decides, logs silently")
                    with g.cell():
                        with st_block(_cell_act):
                            st_write(bs.highlight, "\U0001f7e1 Inform")
                            st_space("v", 0.5)
                            st_write(bs.body, "Agent decides, explains in 1 line")
                    with g.cell():
                        with st_block(_cell):
                            st_write(bs.critical, "\U0001f534 Gate")
                            st_space("v", 0.5)
                            st_write(bs.body, "Full analysis, human validates")

    st_slide_break(marker_label="P8: Consequence Horizons")

    # ── Slide: Consequence Horizons (P8) ────────────────────────────
    with st_block(_pf):
        with st_block(s.center_txt):
            with st_grid(
                cols="95% 5%",
                gap="0px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    with st_zoom(90):
                        st_write(bs.heading, "P8: Consequence Horizons", tag=t.div, toc_lvl="+1")
                with g.cell():
                    st_hover_tooltip(
                        title="3 Time Horizons for Every Gate Decision",
                        entries=[
                            ("Now", "What is the immediate impact on the current sprint? Quick to assess."),
                            ("3 months", "What are the maintenance, scalability, and cost implications? Requires experience."),
                            ("1 year", "What are the architectural consequences? Migration paths, vendor lock-in, team growth."),
                            ("CalcApp example", "localStorage: Now=fast. 3 months=no sync. 1 year=painful migration."),
                        ],
                        scale="2vw", width="70vw", position="left",
                    )
            st_space("v", 1)
            with st_zoom(120):
                with st_grid(cols="repeat(auto-fit, minmax(280px, 1fr))", gap="16px") as g:
                    with g.cell():
                        with st_block(s.project.containers.callout):
                            st_write(bs.success, "\U0001f50d Now")
                            st_write(bs.body, "Sprint impact")
                    with g.cell():
                        with st_block(s.project.containers.callout):
                            st_write(bs.highlight, "\U0001f52d 3 months")
                            st_write(bs.body, "Scalability, cost")
                    with g.cell():
                        with st_block(s.project.containers.callout):
                            st_write(bs.critical, "\U0001f52d 1 year")
                            st_write(bs.body, "Architecture")

    st_slide_break(marker_label="P11: 3 Guardrail Levels")

    # ── Slide: Guardrails (P11) ─────────────────────────────────────
    with st_block(_pf):
        with st_block(s.center_txt):
            with st_grid(
                cols="95% 5%",
                gap="0px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    with st_zoom(90):
                        st_write(bs.heading, "P11: 3 Guardrail Levels", tag=t.div, toc_lvl="+1")
                with g.cell():
                    st_hover_tooltip(
                        title="Guardrails — Safety Net, Not Punishment",
                        entries=[
                            ("Soft", "Warning without blocking. Example: >5 active branches → 'Consider cleaning up'."),
                            ("Hard", "Blocked until override with justification. Example: commit on main → 'Create a branch first'."),
                            ("Emergency", "Full stop, explicit acknowledgment required. Example: force push → 'This will destroy history'."),
                            ("Override", "Every guardrail can be overridden with a traced justification in decisions.md."),
                        ],
                        scale="2vw", width="70vw", position="left",
                    )
            st_space("v", 1)
            with st_zoom(120):
                with st_grid(cols="repeat(auto-fit, minmax(280px, 1fr))", gap="16px") as g:
                    with g.cell():
                        with st_block(s.project.containers.callout):
                            st_write(bs.highlight, "\u26a0\ufe0f Soft")
                            st_write(bs.body, "Warn, don't block")
                    with g.cell():
                        with st_block(s.project.containers.callout):
                            st_write(bs.critical, "\U0001f6d1 Hard")
                            st_write(bs.body, "Block until override")
                    with g.cell():
                        with st_block(s.project.containers.callout):
                            st_write(bs.critical, "\U0001f6a8 Emergency")
                            st_write(bs.body, "Full stop required")

    st_slide_break(marker_label="P15-P16: AI Integrity")

    # ── Slide: AI Integrity (P15-P16) ───────────────────────────────
    with st_block(_pf):
        with st_block(s.center_txt):
            with st_grid(
                cols="95% 5%",
                gap="0px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    with st_zoom(90):
                        st_write(bs.heading, "P15-P16: AI Integrity", tag=t.div, toc_lvl="+1")
                with g.cell():
                    st_hover_tooltip(
                        title="The Agent Admits Its Limits and Challenges Itself",
                        entries=[
                            ("P15 Confidence levels", "Every recommendation carries a confidence level: Verified, High, Moderate, or Low. The agent says when it's unsure."),
                            ("P16 Devil's Advocate", "During review, the agent activates self-critique: Does this library exist? Did I test edge cases? Am I being complaisant?"),
                            ("Pushback trigger", "Consecutive acceptances without discussion trigger a review. Thresholds: Beginner = 3, Intermediate = 5, Expert = 8. The agent says: 'Are you sure? Let\u2019s revisit the most impactful choices.'"),
                            ("Why it matters", "An AI that doubts is more reliable than an AI that affirms. P15-P16 counter hallucinations and automation bias."),
                        ],
                        scale="2vw", width="70vw", position="left",
                    )
            with st_zoom(120):
                st_space("v", 2)
                st_write(bs.accent, "An AI that doubts is more reliable than an AI that affirms.")
                st_space("v", 2)
                with st_grid(cols="repeat(auto-fit, minmax(300px, 1fr))", gap="24px") as g:
                    with g.cell():
                        with st_block(s.project.containers.callout):
                            st_write(bs.keyword + s.center_txt, "P15: Confidence")
                            st_write(bs.body, "Verified → High → Moderate → Low")
                    with g.cell():
                        with st_block(s.project.containers.callout):
                            st_write(bs.keyword + s.center_txt, "P16: Devil's Advocate")
                            st_write(bs.body, "Challenges assumptions, hunts hallucinations")

    st_slide_break(marker_label="P4: Human-in-the-Loop Pattern")

    # ── Slide: P4 Human-in-the-Loop interaction pattern ─────────────
    with st_block(_pf):
        with st_block(s.center_txt):
            with st_grid(
                cols="95% 5%",
                gap="0px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    with st_zoom(90):
                        st_write(bs.heading, "P4: Human-in-the-Loop Pattern", tag=t.div, toc_lvl="+1")
                with g.cell():
                    st_hover_tooltip(
                        title="The Structured Interaction Pattern",
                        entries=[
                            ("Question", "The agent presents the situation: what decision needs to be made?"),
                            ("Context", "Background information: what led here, what are the constraints?"),
                            ("Options", "Concrete alternatives with trade-offs for each (consequence horizons apply for Gate)."),
                            ("Discuss", "Escape hatch: at any tier, the human can say 'let's discuss' to open a dialogue before deciding."),
                        ],
                        scale="2vw", width="70vw", position="left",
                    )
            with st_zoom(120):
                st_space("v", 2)
                st_write(bs.accent, "Every Gate interaction follows: Question → Context → Options → Decide")
                st_space("v", 1)
                with st_grid(cols="repeat(auto-fit, minmax(200px, 1fr))", gap="12px") as g:
                    with g.cell():
                        with st_block(_cell):
                            st_write(bs.body, "\u2753 Question")
                    with g.cell():
                        with st_block(_cell):
                            st_write(bs.body, "\U0001f4cb Context")
                    with g.cell():
                        with st_block(_cell_acc):
                            st_write(bs.body, "\U0001f500 Options")
                    with g.cell():
                        with st_block(_cell_act):
                            st_write(bs.body, "\U0001f4ac Discuss")

    st_slide_break(marker_label="P13: Event-Driven Hooks")

    # ── Slide: P13 Event-Driven Hooks ───────────────────────────────
    with st_block(_pf):
        with st_block(s.center_txt):
            with st_grid(
                cols="95% 5%",
                gap="0px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    with st_zoom(90):
                        st_write(bs.heading, "P13: Event-Driven Hooks", tag=t.div, toc_lvl="+1")
                with g.cell():
                    st_hover_tooltip(
                        title="Hooks — Deterministic Enforcement",
                        entries=[
                            ("System hooks", "Deterministic rules that fire on specific events: protect main branch, block force-push, warn on unreviewed merges."),
                            ("Agent behaviors", "Adaptive actions: warn about stale branches, suggest cleanup, detect framework drift."),
                            ("Claude Code", "hooks.claude.json with PascalCase event names (PreToolUse, PostToolUse)."),
                            ("Cursor", "hooks.cursor.json with camelCase event names (preToolUse, postToolUse)."),
                        ],
                        scale="2vw", width="70vw", position="left",
                    )
            with st_zoom(120):
                st_space("v", 2)
                with st_grid(cols="repeat(auto-fit, minmax(300px, 1fr))", gap="16px") as g:
                    with g.cell():
                        with st_block(s.project.containers.callout):
                            st_write(bs.keyword + s.center_txt, "System Hooks")
                            st_write(bs.body, "Protect main, block force-push, warn unreviewed")
                    with g.cell():
                        with st_block(s.project.containers.callout):
                            st_write(bs.keyword + s.center_txt, "Agent Behaviors")
                            st_write(bs.body, "Warn stale branches, suggest cleanup, detect drift")
