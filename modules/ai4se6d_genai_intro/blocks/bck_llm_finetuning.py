"""Slide — Phase 2: Fine-tuning: balanced image + key points."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_PORTRAIT as _SUFFIX


_page_fill = s.project.containers.page_fill_top

# Cell centering for grid
_cell = Style.create(
    s.container.layouts.vertical_center_layout + s.center_txt,
    "llm_finetuning_cell",
)


class BlockStyles:
    """Slide: Fine-tuning — maximize-viewport archetype: balanced."""
    heading = s.project.titles.slide_title + s.center_txt
    body = Style.create(
        s.Large + s.text.wrap.hyphens,
        "llm_finetuning_body",
    )
    keyword = Style.create(
        s.Large + s.bold + s.project.colors.primary + s.text.wrap.hyphens,
        "llm_finetuning_keyword",
    )
bs = BlockStyles


# Master prompt components

_PROMPT = (
    f"{_PREFIX} A large electric blue sphere (base model) with a smaller teal beam of "
    "light refining a specific region, turning it amber. The rest remains unchanged. "
    f"Represents targeted fine-tuning on specific tasks. {_SUFFIX}"
)


def build():
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.heading, "Phase 2: Fine-tuning", tag=t.div, toc_lvl="1")
            st_space("v","3vh")
            with st_grid(
                cols="1.5fr 3.5fr",
                gap="24px",
                cell_styles=_cell,
            ) as g:
                with g.cell():
                    st_image(
                        s.none,
                        width="80%",
                        editable=IS_EDITABLE,
                        name="llm_finetuning",
                        prompt=_PROMPT,
                        provider="openai",
                        ai_size="1024x1536",
                    )

                with g.cell():
                    with st_zoom(120):
                        with st_list(
                            list_type=lt.unordered,
                            li_style=bs.body,
                            text_align="left",  # bullets and wrapped lines start at the left edge (NG, 2026-11-22)
                            item_gap=0.6,  # 0.6 em between items — streamtex st_list(item_gap=), 0.7.85 (NG, 2026-11-22)
                        ) as l:
                            with l.item():
                                st_write(
                                    bs.body,
                                    (bs.keyword, "Curated data"),
                                    (bs.body, " — High-quality instruction-response pairs"),
                                )
                            with l.item():
                                st_write(
                                    bs.body,
                                    (bs.keyword, "Specialization"),
                                    (bs.body, " — Adapt base model to specific tasks"),
                                )
                            with l.item():
                                st_write(
                                    bs.body,
                                    (bs.keyword, "Efficient"),
                                    (bs.body, " — Smaller dataset, targeted improvement"),
                                )
