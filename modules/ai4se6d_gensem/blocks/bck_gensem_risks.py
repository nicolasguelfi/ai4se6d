"""Slides — 6 risks that motivate the need for methodology + methodological gap."""
# @guideline: minimalist-visual + maximize-viewport
# @pattern: task-card, transition-gse
# @reuse: bck_gensem_risks_overview (v01) — data points reused
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_PORTRAIT as _SUFFIX
from shared_widgets import st_hover_tooltip

_page_fill = s.project.containers.page_fill_top
_page_fill_center = s.project.containers.page_fill_center

# Card styles: 2-row (header + description) like task-card pattern
_cell = s.project.containers.cell_primary_bg + s.center_txt
_hdr = Style.create(
    s.project.containers.cell_primary_bg + s.project.containers.cell_pad_sm
    + s.center_txt + Style("background-color: rgba(231,76,60,0.20);", "_risk_hdr_bg"),
    "risk_hdr",
)
_desc = s.project.containers.cell_pad_sm + s.center_txt


class BlockStyles:
    heading = s.project.titles.slide_title + s.center_txt
    body = Style.create(s.Large + s.center_txt + s.text.wrap.hyphens, "risk_body")
    accent = Style.create(
        s.Large + s.bold + s.project.colors.accent + s.center_txt, "risk_acc",
    )
    highlight = Style.create(
        s.Large + s.bold + s.project.colors.highlight + s.center_txt, "risk_hl",
    )
    critical = Style.create(
        s.Large + s.bold + s.project.colors.critical, "risk_crit",
    )
    label = Style.create(
        s.Large + s.bold + s.project.colors.critical, "risk_lbl",
    )
    source = s.project.citation + s.large + s.center_txt
bs = BlockStyles

_RISKS = [
    ("\u26a0\ufe0f", "Security", "12-65% vulnerability rate",
     "Generated code inherits training-data weaknesses across all languages and models."),
    ("\U0001f47b", "Hallucinations", "5.2-21.7% package hallucinations",
     "LLMs invent plausible but nonexistent dependencies — supply chain attack vectors."),
    ("\U0001f4c9", "Technical Debt", "Homogenization reduces diversity",
     "AI-generated code converges toward similar patterns, creating uniform fragile codebases."),
    ("\U0001f916", "Automation Bias", "Uncritical acceptance of AI output",
     "Developers trust AI suggestions without verification, especially novices."),
    ("\u2696\ufe0f", "IP & Legal", "Unsettled legal status",
     "Ongoing litigation on training data consent. Who owns AI-generated code?"),
    ("\U0001f9ed", "Ethics", "Bias and skill erosion",
     "AI reproduces training biases. Junior developers may miss foundational learning."),
]

_PROMPT_GAP = (
    f"{_PREFIX} A wide canyon or chasm viewed from above. "
    "On the left cliff: a glowing blue toolbox (representing AI tools). "
    "On the right cliff: a teal blueprint scroll (representing methodology). "
    "The gap between them is dark and deep. "
    "A fragile bridge of amber light is forming across the gap. "
    f"{_SUFFIX}"
)


def build():
    st_slide_break(marker_label="Risks & Methodological Gap")

    _tt_entries = [
        ("Security", "Studies show 12-65% of AI-generated code contains vulnerabilities (Basic et al., 2025). The rate varies by language and model."),
        ("Hallucinations", "Spracklen et al. found 5.2-21.7% of AI-suggested packages don't exist \u2014 creating supply chain attack vectors."),
        ("Why it matters", "These risks don't disappear with better models. They require structured processes: review, testing, and verification at every step."),
        ("GSE-One link", "Principles P15 (Agent Fallibility) and P16 (Devil's Advocate) directly address these risks."),
    ]

    # ── Slide 1a: Risks 1-3 ────────────────────────────────────────
    with st_block(_page_fill):
        with st_block(s.center_txt):
            with st_zoom(90):
                st_write(
                bs.heading, "The Risks Are Real (1/2)",
                tag=t.div, toc_lvl="+1",
                )
            st_hover_tooltip(
                title="6 Risks of AI-Assisted Development",
                entries=_tt_entries,
                scale="2vw", width="70vw", position="center",
            )
            st_space("v", 1)

            with st_zoom(80):
                with st_grid(
                    cols="repeat(auto-fit, minmax(350px, 1fr))",
                    gap="16px", cell_styles=_cell,
                ) as g:
                    for emoji, title, stat, desc in _RISKS[:3]:
                        with g.cell():
                            with st_block(_hdr):
                                st_write(bs.body, (bs.label, f"{emoji} {title}  "), (bs.critical, stat))
                            with st_block(_desc):
                                st_write(bs.body, desc)

                st_space("v", 1)
                st_write(
                    bs.source,
                    cite("basic-codesecurity-slr2025"), " | ",
                    cite("spracklen-packages2025"),
                )

    st_slide_break(marker_label="The Risks Are Real (2/2)")

    # ── Slide 1b: Risks 4-6 ────────────────────────────────────────
    with st_block(_page_fill):
        with st_block(s.center_txt):
            with st_zoom(90):
                st_write(
                bs.heading, "The Risks Are Real (2/2)",
                tag=t.div, toc_lvl="+1",
                )
            st_hover_tooltip(
                title="6 Risks of AI-Assisted Development",
                entries=_tt_entries,
                scale="2vw", width="70vw", position="center",
            )
            st_space("v", 1)

            with st_zoom(80):
                with st_grid(
                    cols="repeat(auto-fit, minmax(350px, 1fr))",
                    gap="16px", cell_styles=_cell,
                ) as g:
                    for emoji, title, stat, desc in _RISKS[3:]:
                        with g.cell():
                            with st_block(_hdr):
                                st_write(bs.body, (bs.label, f"{emoji} {title}  "), (bs.critical, stat))
                            with st_block(_desc):
                                st_write(bs.body, desc)

    st_slide_break(marker_label="More AI Does Not Fix These Risks")

    # ── Slide 2: These risks don't disappear ────────────────────────
    with st_block(_page_fill_center):
        with st_block(s.center_txt):
            with st_zoom(90):
                st_write(
                bs.heading, "More AI Does Not Fix These Risks",
                tag=t.div, toc_lvl="+1",
                )
            st_hover_tooltip(
                title="Why more AI doesn't help",
                entries=[
                    ("The trap", "Organizations assume the next model version will fix security and hallucination issues. But these are structural problems, not model limitations."),
                    ("The pattern", "Faster code generation with the same lack of review = more vulnerabilities, faster. Speed amplifies both good and bad practices."),
                    ("The solution", "Structured review, testing, and verification processes — applied consistently at every AI generation, not just at merge time."),
                ],
                scale="2vw", width="70vw", position="center",
            )
            with st_zoom(120):
                st_space("v", 2)
                st_write(
                    bs.accent,
                    "Faster coding with the same lack of review = more bugs, faster.",
                )
                st_space("v", 2)
                st_write(
                    bs.body,
                    "These risks require structured processes: review, testing, "
                    "and verification at every step — not better models.",
                )

    st_slide_break(marker_label="The Methodological Gap")

    # ── Slide 3: The Methodological Gap ─────────────────────────────
    with st_block(_page_fill):
        with st_block(s.center_txt):
            with st_zoom(90):
                st_write(
                bs.heading, "The Methodological Gap",
                tag=t.div, toc_lvl="+1",
                )
            st_hover_tooltip(
                title="The Gap Between Tools and Methods",
                entries=[
                    ("The situation", "AI coding tools are adopted at 84-85% rates. But a structured engineering discipline for AI-assisted development barely exists."),
                    ("VibeCoding", "Fast prototyping, but 12-65% vulnerabilities, no requirements, no review \u2014 a house of cards."),
                    ("VibeEngineering", "Reintroduces RE + TDD + CI/CD, but lacks lifecycle management, risk governance, and knowledge capitalization."),
                    ("The answer", "Methodologies are emerging (GSE-One, AgileGen, SE 3.0\u2026), but the discipline that unifies them is not \u2014 yet. This training contributes to building it."),
                ],
                scale="2vw", width="70vw", position="center",
            )

            with st_grid(cols="2fr 3fr", gap="24px") as g:
                with g.cell():
                    with st_block(s.center_txt):
                        st_image(
                            s.none, width="80%",
                            editable=IS_EDITABLE,
                            name="gse_methodological_gap",
                            prompt=_PROMPT_GAP,
                            provider="openai",
                            ai_size="1024x1536",
                        )
                with g.cell():
                    with st_zoom(120):
                        st_space("v", 2)
                        st_write(
                            bs.body,
                            (bs.critical, "VibeCoding"),
                            (bs.body, " — fast but fragile"),
                        )
                        st_space("v", 1)
                        st_write(
                            bs.body,
                            (bs.accent, "VibeEngineering"),
                            (bs.body, " \u2014 rigorous but incomplete"),
                        )
                        st_space("v", 1)
                        st_write(
                            bs.highlight,
                            "Methodologies are emerging. The discipline that unifies them is not \u2014 yet.",
                        )
