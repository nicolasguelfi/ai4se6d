"""Slides 13-15 — RE transformed, Testing, 3 Paradigms + transition to GSE-One."""
# @guideline: minimalist-visual + maximize-viewport
# @pattern: evidence-insight, transition-gse
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip

_page_fill = s.project.containers.page_fill_top
_page_fill_center = s.project.containers.page_fill_center

_hdr_cell = s.project.containers.table_header_cell
_normal_cell = s.project.containers.table_normal_cell
_active_cell = s.project.containers.table_active_cell

cell_center = Style(                                                                         
    "display:flex; flex-direction:column; "                                                  
    "justify-content:center; align-items:center; text-align:center;",                        
    "cell_center",                                                                           
) 

class BlockStyles:
    heading = s.project.titles.slide_title + s.center_txt
    body = Style.create(s.Large + s.center_txt + s.text.wrap.hyphens, "para_body")
    accent = Style.create(
        s.Large + s.bold + s.project.colors.accent + s.center_txt,
        "para_acc",
    )
    keyword = Style.create(
        s.Large + s.bold + s.project.colors.primary,
        "para_kw",
    )
    highlight = Style.create(
        s.Large + s.bold + s.project.colors.highlight + s.center_txt,
        "para_hl",
    )
    table_hdr = s.project.titles.table_header
    table_txt = s.project.titles.table_cell
    table_lbl = s.project.titles.table_label
    table_lbl_active = s.project.titles.table_label_active
bs = BlockStyles


def build():
    # Anti-scroll: invisible marker before first content
    st_slide_break(marker_label="SDLC Impact and Paradigms")

    # ── Slide 13: RE Transformed ────────────────────────────────────
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(
                bs.heading,
                "Requirements Engineering: Transformed",
                tag=t.div, toc_lvl="+1",
            )
            st_hover_tooltip(
                title="Requirements Engineering Transformed — Explained",
                entries=[
                    ("What the research shows", "Cheng et al. analyzed 238 papers on GenAI in requirements engineering. Most work focuses on elicitation (22%) and analysis (30%), but management is underexplored (6.8%)."),
                    ("What changed", "AI agents can now conduct conversational requirements elicitation — asking clarifying questions, proposing acceptance criteria, and detecting ambiguities automatically."),
                    ("The challenges", "Reproducibility (66.8%), hallucinations (63.4%), and interpretability (57.1%) remain significant concerns — requirements must still be validated by humans."),
                    ("GSE-One link", "/gse:reqs implements this conversational elicitation with built-in quality checks (completeness, testability, consistency)."),
                ],
                scale="2vw", width="70vw", position="center",
            )
            with st_zoom(120):
                st_space("v", 2)
                st_write(
                    bs.accent,
                    "The AI asks the questions. You validate the answers.",
                )
                st_space("v", 2)
                st_write(
                    bs.body,
                    (bs.keyword, "Conversational elicitation"),
                    (bs.body, " replaces static requirement forms. "
                     "The agent clarifies ambiguity, proposes acceptance criteria, "
                     "and traces every requirement to tests."),
                )

    st_slide_break(marker_label="Testing and Reviewing: Structured Process Matters")

    # ── Slide 14: Testing and Reviewing ─────────────────────────────
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(
                bs.heading,
                "Testing and Reviewing: Structured Process Matters",
                tag=t.div, toc_lvl="+1",
            )
            st_hover_tooltip(
                title="Testing & Process — Explained",
                entries=[
                    ("What Wang et al. found", "A survey of 102 studies on AI-assisted testing shows that AI generates tests faster, but the quality depends heavily on the surrounding process."),
                    ("FlowGen experiment", "When code generation follows a structured SE process (design review + code review), code smells decrease by 15%. FlowGenScrum achieves 75.2% Pass@1 on HumanEval."),
                    ("The warning", "Haque et al. showed that LLM-refactored code is not always reliable — tests that pass don't guarantee correctness."),
                    ("GSE-One link", "/gse:tests calibrates a test pyramid by project domain (web, API, CLI) and tracks 3 coverage dimensions: code, requirements, and risk."),
                ],
                scale="2vw", width="70vw", position="center",
            )
            with st_zoom(120):
                st_space("v", 2)
                st_write(
                    bs.accent,
                    "Design review + code review = 15% fewer code smells.",
                )
                st_space("v", 2)
                st_write(
                    bs.body,
                    "AI generates tests faster, but ",
                    (bs.keyword, "the test strategy requires human judgment"),
                    (bs.body, ". A structured SE process consistently improves "
                     "the quality of AI-generated code."),
                )

    st_slide_break(marker_label="3 Paradigms of Code Generation")

    # ── Slide 15: 3 Paradigms + transition ──────────────────────────
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(
                bs.heading,
                "3 Paradigms of Code Generation",
                tag=t.div, toc_lvl="+1",
            )
            st_hover_tooltip(
                title="3 Paradigms — What you practiced in Days 1-2",
                entries=[
                    ("CHOP", "Chat-Oriented Programming: 33-37% of developer time is now spent in multi-turn conversations with AI. You did this every time you chatted in Cursor."),
                    ("VibeCoding", "Coined by Karpathy (Feb 2025): describe what you want, accept the code without deep review. You experienced this on FreeSelfApp Day 1 — fast but fragile."),
                    ("VibeEngineering", "Kent Beck's response: reintroduce requirements, TDD, and architecture discipline. You applied this on CalcApp Day 2 — structured and reliable."),
                    ("Beyond VibeEngineering", "Generative Software Engineering is the emerging discipline that adds lifecycle, risk governance, and knowledge capitalization. GSE-One is one methodology for this discipline \u2014 AgileGen, SE 3.0, V-Bounce are others."),
                ],
                scale="2vw", width="70vw", position="center",
            )
            st_space("v", 1)


            # Responsive table
            with st_grid(
                cols="repeat(auto-fit, minmax(250px, 1fr))",
                gap="12px", cell_styles=_hdr_cell,
            ) as g:
                with g.cell():
                    st_write(bs.table_hdr + s.center_txt, "Paradigm")
                with g.cell():
                    st_write(bs.table_hdr + s.center_txt, "Principle")
                with g.cell():
                    st_write(bs.table_hdr + s.center_txt, "You lived it...")

            with st_grid(
                cols="repeat(auto-fit, minmax(250px, 1fr))",
                gap="12px", cell_styles=_normal_cell,
            ) as g:
                with g.cell():
                    st_write(bs.table_lbl + s.center_txt, "CHOP")
                with g.cell():
                    st_write(bs.table_txt + s.center_txt, "Multi-turn conversations")
                with g.cell():
                    st_write(bs.table_txt + s.center_txt, "Every chat in Cursor")

            with st_grid(
                cols="repeat(auto-fit, minmax(250px, 1fr))",
                gap="12px", cell_styles=_normal_cell,
            ) as g:
                with g.cell():
                    st_write(bs.table_lbl + s.center_txt, "VibeCoding")
                with g.cell():
                    st_write(bs.table_txt + s.center_txt, "Intent first, accept as-is")
                with g.cell():
                    st_write(bs.table_txt + s.center_txt, "FreeSelfApp Day 1")

            with st_grid(
                cols="repeat(auto-fit, minmax(250px, 1fr))",
                gap="12px", cell_styles=_active_cell,
            ) as g:
                with g.cell():
                    st_write(bs.table_lbl_active + s.center_txt, "VibeEngineering")
                with g.cell():
                    st_write(bs.table_txt + s.center_txt, "REQ, TDD, architecture")
                with g.cell():
                    st_write(bs.table_txt + s.center_txt, "CalcApp Day 2")

            st_space("v", 2)
            with st_grid(cols="1fr 2fr", gap="24px",cell_styles=cell_center) as g:
                with g.cell():
                    st_image(
                        s.center_txt, width="50%",
                        uri="images/managed/GSE/images/logo-gse-geni-with-shield.webp",
                    )
                with g.cell():
                    st_write(bs.highlight, "Today: beyond VibeEngineering \u2192 Generative SE as a discipline, practiced through GSE-One")
