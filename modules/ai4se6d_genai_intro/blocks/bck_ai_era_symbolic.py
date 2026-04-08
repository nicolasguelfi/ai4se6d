"""Slide — 1956 Symbolic AI: balanced image + key points."""
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
    "ai_era_symbolic_cell",
)


class BlockStyles:
    """Slide: Symbolic AI — maximize-viewport archetype: balanced."""
    heading = s.project.titles.slide_title + s.center_txt
    body = Style.create(
        s.Large + s.text.wrap.hyphens,
        "ai_era_symbolic_body",
    )
    keyword = Style.create(
        s.Large + s.bold + s.project.colors.primary + s.text.wrap.hyphens,
        "ai_era_symbolic_keyword",
    )
bs = BlockStyles


# Master prompt components

_PROMPT = (
    f"{_PREFIX} A vintage-styled terminal screen outline with rigid if-then decision tree "
    "branches inside, drawn in geometric electric blue lines. Small amber nodes at each "
    "decision point. Represents rule-based expert systems of early AI. "
    f"{_SUFFIX}"
)


def build():
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.heading, "1956 — Symbolic AI", tag=t.div, toc_lvl="1")

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
                        name="ai_era_symbolic",
                        prompt=_PROMPT,
                        provider="openai",
                        ai_size="1024x1536",
                    )

                with g.cell():
                    with st_zoom(120):
                        with st_list(
                            list_type=lt.unordered,
                            li_style=bs.body,
                        ) as l:
                            with l.item():
                                st_write(
                                    bs.body,
                                    (bs.keyword, "Rules"),
                                    (bs.body, " — Hand-crafted if-then logic programming"),
                                )
                            with l.item():
                                st_write(
                                    bs.body,
                                    (bs.keyword, "Expert systems"),
                                    (bs.body, " — Encoded human knowledge explicitly"),
                                )
                            with l.item():
                                st_write(
                                    bs.body,
                                    (bs.keyword, "Narrow domains"),
                                    (bs.body, " — Medical diagnosis, chess"),
                                )
                            with l.item():
                                st_write(
                                    bs.body,
                                    (bs.keyword, "Rigid"),
                                    (bs.body, " — Handled exceptions and complex cases poorly"),
                                )
