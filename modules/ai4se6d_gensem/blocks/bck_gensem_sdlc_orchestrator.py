"""Slides 11-12 — Implementer to Orchestrator + 3 Pillars."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_LANDSCAPE as _SUFFIX
from shared_widgets import st_hover_tooltip

_page_fill_center = s.project.containers.page_fill_center
_page_fill_top = s.project.containers.page_fill_top


class BlockStyles:
    heading = Style.create(
        s.project.colors.accent + s.bold + s.Huge + s.center_txt,
        "orch_heading",
    )
    slide_title = s.project.titles.slide_title + s.center_txt
    keyword = Style.create(
        s.Large + s.bold + s.project.colors.primary + s.center_txt,
        "orch_kw",
    )
    highlight = Style.create(
        s.Large + s.bold + s.project.colors.highlight + s.center_txt,
        "orch_hl",
    )
    body = Style.create(s.Large + s.center_txt + s.text.wrap.hyphens, "orch_body")
bs = BlockStyles

_PROMPT = (
    f"{_PREFIX} On the left, a single person typing on a keyboard, rendered in "
    "fading blue wireframe. On the right, the same person standing tall with arms "
    "extended, directing 5 glowing orbiting spheres (AI agents) in teal and amber. "
    "A large arrow of light connects left to right. "
    f"{_SUFFIX}"
)


def build():
    # Anti-scroll: invisible marker before first content
    st_slide_break(marker_label="Implementer to Orchestrator")

    # ── Slide 11: Implementer → Orchestrator ────────────────────────
    with st_block(_page_fill_center):
        with st_block(s.center_txt):
            with st_zoom(90):
                st_write(
                bs.heading,
                "Implementer  →  Orchestrator",
                tag=t.div, toc_lvl="+1",
                )
            st_hover_tooltip(
                title="Implementer to Orchestrator",
                entries=[
                    ("What changed", "Developers used to spend 80% of their time writing code. With GenAI agents, the ratio inverts: 80% is now specifying intent, orchestrating agents, and validating results."),
                    ("Evidence", "Gartner predicts 80% of the developer workforce will need to reskill by 2027 to adapt to AI-augmented workflows."),
                    ("GSE-One link", "GSE-One structures this transition by providing a lifecycle that covers all 3 new roles: Specify (/gse:reqs), Orchestrate (/gse:produce), Validate (/gse:review)."),
                ],
                scale="2vw", width="70vw", position="center",
            )
            st_space("v", 1)
            st_image(
                s.none, width="60%",
                editable=IS_EDITABLE,
                name="gse_implementer_orchestrator",
                prompt=_PROMPT,
                provider="openai",
                ai_size="1536x1024",
            )

    st_slide_break(marker_label="What This Changes For You")

    # ── Slide 12: 3 Pillars ─────────────────────────────────────────
    with st_block(_page_fill_top):
        with st_block(s.center_txt):
            with st_zoom(90):
                st_write(
                bs.slide_title,
                "What This Changes For You",
                tag=t.div, toc_lvl="+1",
                )
            st_space("v", 2)

            with st_grid(
                cols="repeat(auto-fit, minmax(280px, 1fr))",
                gap="24px",
            ) as g:
                with g.cell():
                    with st_block(s.project.containers.callout):
                        st_write(bs.keyword, "Specify")
                        st_space("v", 0.5)
                        st_write(bs.body, "Formulate intent with precision")

                with g.cell():
                    with st_block(s.project.containers.callout):
                        st_write(bs.highlight, "Orchestrate")
                        st_space("v", 0.5)
                        st_write(bs.body, "Coordinate agents, tools and processes")

                with g.cell():
                    with st_block(s.project.containers.callout):
                        st_write(bs.keyword, "Validate")
                        st_space("v", 0.5)
                        st_write(bs.body, "Verify, review, capitalize")
