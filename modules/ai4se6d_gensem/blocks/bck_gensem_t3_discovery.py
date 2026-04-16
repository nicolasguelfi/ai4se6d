"""T3 — LC01: COLLECT, ASSESS, PLAN + complexity budget + worktrees."""
# @guideline: minimalist-visual + maximize-viewport
# @reuse: bck_gensem_ce_git_profiles, _git_mapping, _plan_antipattern (v01)
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_PORTRAIT as _SUFFIX
from shared_widgets import st_hover_tooltip

_pf = s.project.containers.page_fill_top
_pfc = s.project.containers.page_fill_center
_cell = s.project.containers.cell_primary_bg + s.project.containers.cell_pad_md + s.center_txt
_cell_acc = s.project.containers.cell_accent_bg + s.project.containers.cell_pad_md + s.center_txt
_cell_act = s.project.containers.cell_active_bg + s.project.containers.cell_pad_md + s.center_txt

_hdr_cell = s.project.containers.table_header_cell
_normal_cell = s.project.containers.table_normal_cell


class BlockStyles:
    heading = s.project.titles.slide_title + s.center_txt
    body = Style.create(s.Large + s.center_txt + s.text.wrap.hyphens, "t3_body")
    accent = Style.create(s.Large + s.bold + s.project.colors.accent + s.center_txt, "t3_acc")
    highlight = Style.create(s.Large + s.bold + s.project.colors.highlight + s.center_txt, "t3_hl")
    keyword = Style.create(s.Large + s.bold + s.project.colors.primary, "t3_kw")
    stat = Style.create(s.Large + s.bold + s.project.colors.highlight, "t3_stat")
    critical = Style.create(s.Large + s.bold + s.project.colors.critical + s.center_txt, "t3_crit")
    label = Style.create(s.Large + s.bold + s.project.colors.primary + s.center_txt, "t3_lbl")
    table_hdr = s.project.titles.table_header
    table_txt = s.project.titles.table_cell
    table_lbl = s.project.titles.table_label
bs = BlockStyles

_PROMPT_COLLECT = (
    f"{_PREFIX} A radar dish scanning a landscape of code files, documents, and API icons. "
    "Beams of blue light sweep across the scene, highlighting reusable assets in teal. "
    f"{_SUFFIX}"
)


def build():
    st_slide_break(marker_label="LC01: Discovery & Planning")

    # ── Slide: COLLECT ──────────────────────────────────────────────
    with st_block(_pf):
        with st_block(s.center_txt):
            with st_grid(
                cols="95% 5%",
                gap="0px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    with st_zoom(90):
                        st_write(bs.heading, "/gse:collect — Inventory Sources", tag=t.div, toc_lvl="+1")
                with g.cell():
                    st_hover_tooltip(
                        title="COLLECT — What it does",
                        entries=[
                            ("Purpose", "Before building anything, scan all available sources: existing code, docs, tests, external repos, APIs."),
                            ("Output", "sources.yaml with provenance tracking \u2014 each source gets an SRC- ID with reusability assessment."),
                            ("Reusability levels", "as-is (use directly), adaptable (modify), reference (learn from), incompatible (skip)."),
                            ("CalcApp example", "v1-skeleton code = as-is, requirements docs = adaptable, currency API = to evaluate."),
                            ("Discipline principle", "Structured upstream work (COLLECT-ASSESS-PLAN) is what every Generative SE methodology must provide \u2014 this is what VibeEngineering lacks."),
                        ],
                        scale="2vw", width="70vw", position="left",
                    )
            with st_zoom(120):
                st_space("v", 2)
                st_write(bs.accent, "Before building, understand what you have.")
                st_space("v", 1)
                with st_grid(cols="1fr 1fr", gap="16px") as g:
                    with g.cell():
                        with st_grid(cols="1fr", gap="12px") as inner:
                            with inner.cell():
                                with st_block(_cell):
                                    st_write(bs.body, "\u2705 as-is")
                            with inner.cell():
                                with st_block(_cell_acc):
                                    st_write(bs.body, "\U0001f504 adaptable")
                    with g.cell():
                        with st_grid(cols="1fr", gap="12px") as inner:
                            with inner.cell():
                                with st_block(_cell):
                                    st_write(bs.body, "\U0001f4d6 reference")
                            with inner.cell():
                                with st_block(_cell_act):
                                    st_write(bs.body, "\u274c incompatible")

    st_slide_break(marker_label="/gse:assess — Gap Analysis")

    # ── Slide: ASSESS ───────────────────────────────────────────────
    with st_block(_pf):
        with st_block(s.center_txt):
            with st_grid(
                cols="95% 5%",
                gap="0px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    with st_zoom(90):
                        st_write(bs.heading, "/gse:assess — Gap Analysis", tag=t.div, toc_lvl="+1")
                with g.cell():
                    st_hover_tooltip(
                        title="ASSESS — What it does",
                        entries=[
                            ("Purpose", "Compare current state vs project goals. Identify what's covered, partial, missing, or risky."),
                            ("4 categories", "✓ covered, ◐ partial, ✗ missing, ⚠ risk — produces a clear gap map."),
                            ("CalcApp example", "✓ CRUD expenses, ◐ monthly filter, ✗ budgets per category, ⚠ performance with large datasets."),
                            ("Output", "The gap feeds directly into /gse:plan as candidate backlog items."),
                        ],
                        scale="2vw", width="70vw", position="left",
                    )
            with st_zoom(120):
                st_space("v", 2)
                with st_grid(cols="1fr 1fr", gap="16px") as g:
                    with g.cell():
                        with st_grid(cols="1fr", gap="12px") as inner:
                            with inner.cell():
                                with st_block(_cell_acc):
                                    st_write(bs.body, "\u2713 Covered")
                            with inner.cell():
                                with st_block(_cell):
                                    st_write(bs.body, "\u25d0 Partial")
                    with g.cell():
                        with st_grid(cols="1fr", gap="12px") as inner:
                            with inner.cell():
                                with st_block(_cell_act):
                                    st_write(bs.body, "\u2717 Missing")
                            with inner.cell():
                                with st_block(s.project.containers.cell_primary_bg + s.project.containers.cell_pad_md + s.center_txt + Style("border: 2px solid #E74C3C;", "_risk_border")):
                                    st_write(bs.body, "\u26a0 Risk")

    st_slide_break(marker_label="/gse:plan — Sprint Planning")

    # ── Slide: PLAN + Complexity Budget ─────────────────────────────
    with st_block(_pf):
        with st_block(s.center_txt):
            with st_grid(
                cols="95% 5%",
                gap="0px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    with st_zoom(90):
                        st_write(bs.heading, "/gse:plan — Sprint Planning", tag=t.div, toc_lvl="+1")
                with g.cell():
                    st_hover_tooltip(
                        title="PLAN + Complexity Budget (P10)",
                        entries=[
                            ("Purpose", "Transform the gap into an actionable sprint: decompose into TASK- items with branches, dependencies, and complexity costs."),
                            ("Complexity budget", "Each sprint has 8-15 complexity points. Tests/docs/renames = free. Simplification earns credits (\u22121 to \u22122)."),
                            ("Cost examples", "Utility dependency = 1pt, UI component = 1-2pts, framework = 2-3pts, external service = 2-4pts, security surface = 2-3pts, architectural pattern = 3-5pts, new language/framework = 4-6pts."),
                            ("The plan as contract", "The plan constrains the AI agent — it cannot deviate without plan revision. This prevents scope creep."),
                            ("Gate", "The user MUST validate the plan before production starts. No auto-approval."),
                            ("Spike tasks", "For unknowns, create a spike (max 3 pts, no REQS/TESTS required). Must produce a DEC- decision artifact. Use /gse:task --spike to explore before committing."),
                        ],
                        scale="2vw", width="70vw", position="left",
                    )
            with st_zoom(120):
                st_space("v", 2)
                st_write(bs.accent, "The plan is a CONTRACT between you and the agent.")
                st_space("v", 1)
                with st_grid(cols="repeat(auto-fit, minmax(280px, 1fr))", gap="16px") as g:
                    with g.cell():
                        with st_block(s.project.containers.callout):
                            st_write(bs.body, (bs.stat, "8-15 pts"), (bs.body, " per sprint"))
                    with g.cell():
                        with st_block(s.project.containers.callout):
                            st_write(bs.body, (bs.stat, "Warn 80%"), (bs.body, " Gate 100%"))
                    with g.cell():
                        with st_block(s.project.containers.callout):
                            st_write(bs.body, (bs.keyword, "Tests = 0pt"), (bs.body, " always free"))

    st_slide_break(marker_label="Version Control: Worktree Isolation")

    # ── Slide: Version Control & Worktrees ──────────────────────────
    with st_block(_pf):
        with st_block(s.center_txt):
            with st_grid(
                cols="95% 5%",
                gap="0px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    with st_zoom(90):
                        st_write(bs.heading, "Version Control: Worktree Isolation", tag=t.div, toc_lvl="+1")
                with g.cell():
                    st_hover_tooltip(
                        title="P12 — Why Worktrees?",
                        entries=[
                            ("Main always stable", "Direct commits to main are blocked. Every task works on its own branch + worktree."),
                            ("No git skills needed", "The agent handles all git operations. Beginners never need to learn git commands."),
                            ("Parallel work", "Each task has its own folder (.worktrees/). No stash, no checkout conflicts."),
                            ("Merge adapted to level", "Beginners see 'Clean summary' vs 'Full history'. Advanced users see squash/merge/rebase."),
                        ],
                        scale="2vw", width="70vw", position="left",
                    )
            with st_zoom(120):
                st_space("v", 2)
                with st_grid(cols="repeat(auto-fit, minmax(280px, 1fr))", gap="16px") as g:
                    with g.cell():
                        with st_block(s.project.containers.callout):
                            st_write(bs.accent, "main = always stable")
                    with g.cell():
                        with st_block(s.project.containers.callout):
                            st_write(bs.accent, "1 task = 1 worktree")
                    with g.cell():
                        with st_block(s.project.containers.callout):
                            st_write(bs.accent, "Agent handles git")
