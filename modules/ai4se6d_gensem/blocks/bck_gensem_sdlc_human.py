"""Slide — Human factor: role evolution in AI-augmented SE."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_PORTRAIT as _SUFFIX

class BlockStyles:
    """Human factor slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.accent
    stat = s.bold + s.project.colors.highlight
    source = s.project.titles.caption + s.center_txt
bs = BlockStyles

_PROMPT = (
    f"{_PREFIX} A human silhouette transitioning from typing on a keyboard (left, fading) "
    "to conducting an orchestra of floating code blocks and process diagrams (right, vivid). "
    "The transition represents the shift from implementer to orchestrator. Electric blue "
    f"and teal tones. {_SUFFIX}"
)

def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(bs.heading, "The Human Factor", tag=t.div, toc_lvl="1")
            st_space("v", 1)

        with st_grid(
            cols="2fr 3fr",
            gap="24px",
            cell_styles=s.project.containers.grid_cell_centered,
        ) as g:
            with g.cell():
                st_image(
                    s.none,
                    width="80%",
                    editable=IS_EDITABLE,
                    name="gs_sdlc_human",
                    prompt=_PROMPT,
                    provider="openai",
                    ai_size="1024x1536",
                )

            with g.cell():
                with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                    with l.item():
                        st_write(bs.body, (bs.keyword, "Role evolution: "), "Implementer \u2192 Orchestrator")
                    with l.item():
                        st_write(bs.body, (bs.stat, "80%"), " of workforce needs upskilling by 2027 (Gartner)")
                    with l.item():
                        st_write(bs.body, (bs.keyword, "Differential impact: "), "Juniors ", (bs.stat, "+27\u201339%"), " / Seniors ", (bs.stat, "+8\u201313%"), " or ", (bs.stat, "\u221219%"))
                    with l.item():
                        st_write(bs.body, (bs.keyword, "Creativity risk: "), "Homogenization effect on generated code")
                    with l.item():
                        st_write(bs.body, (bs.keyword, "Knowledge transfer: "), "AI replaces colleagues; pair programming needs adaptation")
