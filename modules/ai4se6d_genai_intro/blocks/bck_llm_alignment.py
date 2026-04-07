"""Slide — Phase 3: Alignment (RLHF): balanced image + key points."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_PORTRAIT as _SUFFIX


_page_fill = s.project.containers.page_fill_top

# Cell centering for grid
_cell = Style.create(
    s.container.layouts.vertical_center_layout + s.center_txt,
    "llm_alignment_cell",
)


class BlockStyles:
    """Slide: Alignment (RLHF) — maximize-viewport archetype: balanced."""
    heading = s.project.titles.slide_title + s.center_txt
    body = Style.create(
        s.Large + s.text.wrap.hyphens,
        "llm_alignment_body",
    )
    keyword = Style.create(
        s.Large + s.bold + s.project.colors.primary + s.text.wrap.hyphens,
        "llm_alignment_keyword",
    )
    source = s.project.citation + s.large + s.center_txt
bs = BlockStyles


# Master prompt components

_PROMPT = (
    f"{_PREFIX} Two paths diverging from a central point: one path curves upward "
    "(preferred, in amber with a subtle thumbs-up shape), the other curves down "
    "(rejected, fading teal). An electric blue compass icon at the center. Represents "
    f"RLHF steering model toward human preferences. {_SUFFIX}"
)


def build():
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.heading, "Phase 3: Alignment (RLHF/RLAIF)", tag=t.div, toc_lvl="1")

            with st_grid(
                cols="2fr 3fr",
                gap="24px",
                cell_styles=_cell,
            ) as g:
                with g.cell():
                    st_image(
                        s.none,
                        width="80%",
                        editable=IS_EDITABLE,
                        name="llm_alignment",
                        prompt=_PROMPT,
                        provider="openai",
                        ai_size="1024x1536",
                    )

                with g.cell():
                    with st_zoom(140):
                        with st_list(
                            list_type=lt.unordered,
                            li_style=bs.body,
                        ) as l:
                            with l.item():
                                st_write(
                                    bs.body,
                                    (bs.keyword, "HHH"),
                                    (bs.body, " — Helpful, Harmless, Honest"),
                                )
                            with l.item():
                                st_write(
                                    bs.body,
                                    (bs.keyword, "Reward model"),
                                    (bs.body, " — Guides LLM toward preferred responses"),
                                )
                            with l.item():
                                st_write(
                                    bs.body,
                                    (bs.keyword, "Human feedback"),
                                    (bs.body, " — Evaluators rank model outputs (RLHF)"),
                                )
                            with l.item():
                                st_write(
                                    bs.body,
                                    (bs.keyword, "Constitutional AI"),
                                    (bs.body, " — Anthropic's principle-based self-critique (RLAIF)"),
                                )
                        # REF: https://arxiv.org/abs/2212.08073
                        st_write(bs.source, cite("bai2022constitutional"))
