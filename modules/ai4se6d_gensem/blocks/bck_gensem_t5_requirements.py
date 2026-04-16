"""T5 — LC02a: REQS (FR/NFR, Given/When/Then), DESIGN (decisions), PREVIEW, traceability."""
# @guideline: minimalist-visual + maximize-viewport
# @reuse: bck_gensem_calcapp_fr_example, _nfr_example, _traceability (v01)
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip

_pf = s.project.containers.page_fill_top
_pfc = s.project.containers.page_fill_center
_cell = s.project.containers.cell_primary_bg + s.project.containers.cell_pad_md + s.center_txt
_cell_acc = s.project.containers.cell_accent_bg + s.project.containers.cell_pad_md + s.center_txt


class BlockStyles:
    heading = s.project.titles.slide_title + s.center_txt
    body = Style.create(s.Large + s.center_txt + s.text.wrap.hyphens, "t5_body")
    accent = Style.create(s.Large + s.bold + s.project.colors.accent + s.center_txt, "t5_acc")
    highlight = Style.create(s.Large + s.bold + s.project.colors.highlight + s.center_txt, "t5_hl")
    keyword = Style.create(s.Large + s.bold + s.project.colors.primary, "t5_kw")
    critical = Style.create(s.Large + s.bold + s.project.colors.critical + s.center_txt, "t5_crit")
bs = BlockStyles


def build():
    st_slide_break(marker_label="LC02a: Requirements, Design, Preview")

    # ── Slide: REQS — conversational elicitation ────────────────────
    with st_block(_pf):
        with st_block(s.center_txt):
            with st_grid(
                cols="95% 5%",
                gap="0px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    with st_zoom(90):
                        st_write(bs.heading, "/gse:reqs — Specify Before Coding", tag=t.div, toc_lvl="+1")
                with g.cell():
                    st_hover_tooltip(
                        title="Requirements Engineering in GSE-One",
                        entries=[
                            ("Step 0", "Conversational elicitation — the agent asks clarifying questions, not you."),
                            ("FR structure", "Each functional requirement has: ID, user story, acceptance criteria (Given/When/Then), priority, test file."),
                            ("NFR structure", "Each non-functional requirement has: standard (ISO 25010), measurement method, verification approach."),
                            ("Quality check", "The agent verifies: Complete? Consistent? Testable? Non-ambiguous?"),
                        ],
                        scale="2vw", width="70vw", position="left",
                    )
            with st_zoom(120):
                st_space("v", 2)
                st_write(bs.accent, "The agent asks the questions. You validate the answers.")
                st_space("v", 1)
                with st_grid(cols="repeat(auto-fit, minmax(300px, 1fr))", gap="16px") as g:
                    with g.cell():
                        with st_block(s.project.containers.callout):
                            st_write(bs.keyword + s.center_txt, "FR — What the system DOES")
                            st_write(bs.body, "Given / When / Then → directly testable")
                    with g.cell():
                        with st_block(s.project.containers.callout):
                            st_write(bs.keyword + s.center_txt, "NFR — HOW it does it")
                            st_write(bs.body, "Performance, security, accessibility")

    st_slide_break(marker_label="/gse:design — Architecture Decisions")

    # ── Slide: DESIGN — decisions traced ────────────────────────────
    with st_block(_pf):
        with st_block(s.center_txt):
            with st_grid(
                cols="95% 5%",
                gap="0px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    with st_zoom(90):
                        st_write(bs.heading, "/gse:design — Architecture Decisions", tag=t.div, toc_lvl="+1")
                with g.cell():
                    st_hover_tooltip(
                        title="Design in GSE-One",
                        entries=[
                            ("Purpose", "Transform requirements into architecture: component decomposition, interface contracts, technical choices."),
                            ("Decision journal", "Every significant choice gets a DEC- ID and is logged in decisions.md with 4 fields: Context (why this decision arose), Options (alternatives considered with trade-offs), Choice (what was decided), Consequences (impact at Now / 3 months / 1 year)."),
                            ("Gate decisions", "Architectural choices (framework, state management, persistence) always trigger a Gate — the human decides."),
                            ("Anti-pattern", "Over-engineering at sprint 1. YAGNI + complexity budget = lean design for now, extensible for later."),
                        ],
                        scale="2vw", width="70vw", position="left",
                    )
            with st_zoom(120):
                st_space("v", 2)
                st_write(bs.accent, "AI proposes. You decide. Every decision is traced.")
                st_space("v", 1)
                st_write(bs.body, "Output: design.md + decisions.md with DEC- IDs")

    st_slide_break(marker_label="Preview & Traceability")

    # ── Slide: PREVIEW + Traceability ───────────────────────────────
    with st_block(_pf):
        with st_block(s.center_txt):
            with st_grid(
                cols="95% 5%",
                gap="0px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    with st_zoom(90):
                        st_write(bs.heading, "Preview & Traceability", tag=t.div, toc_lvl="+1")
                with g.cell():
                    st_hover_tooltip(
                        title="Preview and Full Traceability",
                        entries=[
                            ("/gse:preview", "Wireframes, API contracts, user story walkthroughs — validate before any code is written."),
                            ("Cost of change", "Fixing a design flaw costs 10x less than fixing the same flaw in code. Preview closes the 80% of the 80/20 rule."),
                            ("Traceability web", "TASK → derives_from REQ → implements DES → decided_by DEC → validates TST. Every artifact is linked."),
                            ("Impact analysis", "Change REQ-007? The agent shows all impacted tests, designs, and tasks automatically."),
                        ],
                        scale="2vw", width="70vw", position="left",
                    )
            with st_zoom(120):
                st_space("v", 2)
                st_write(bs.accent, "Everything is linked. Change one, see all impacts.")
                st_space("v", 1)
                st_write(
                    bs.body,
                    (bs.keyword, "REQ-"),
                    (bs.body, " → "),
                    (bs.keyword, "DES-"),
                    (bs.body, " → "),
                    (bs.keyword, "TST-"),
                    (bs.body, " → "),
                    (bs.keyword, "TASK-"),
                    (bs.body, " → "),
                    (bs.keyword, "RVW-"),
                )
