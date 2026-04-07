"""Slide — V-Bounce Model: humans validate, AI implements."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_PORTRAIT as _SUFFIX

class BlockStyles:
    """V-Bounce slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.accent
    assessment = Style.create(
        s.project.titles.body_accent + s.center_txt,
        "gs_vb_assessment",
    )
    source = s.project.titles.caption + s.center_txt
bs = BlockStyles

_PROMPT = (
    f"{_PREFIX} A V-shape diagram with downward arrows on the left side (requirements, "
    "design, implementation) and upward arrows on the right side (unit test, integration "
    "test, acceptance). Bounce arrows in amber connect each level, showing AI bouncing "
    "between implementation and validation. Human figures stand at each validation "
    f"checkpoint. Geometric, minimal. {_SUFFIX}"
)

def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(bs.heading, "V-Bounce Model", tag=t.div, toc_lvl="1")
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
                    name="gs_fw_vbounce",
                    prompt=_PROMPT,
                    provider="openai",
                    ai_size="1024x1536",
                )

            with g.cell():
                with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                    with l.item():
                        st_write(bs.body, (bs.keyword, "Author: "), "Hymel \u2014 first formal AI-native SDLC model")
                    with l.item():
                        st_write(bs.body, (bs.keyword, "Core principle: "), "Humans = validators, AI = implementation engine")
                    with l.item():
                        st_write(bs.body, (bs.keyword, "Multi-agent roles: "), "Architect, Coder, Tester, Reviewer \u2014 each an AI agent")
                    with l.item():
                        st_write(bs.body, (bs.keyword, "Bounce pattern: "), "AI iterates between V-model phases until human approves")
                    with l.item():
                        st_write(bs.body, (bs.keyword, "Key insight: "), "Validation gates prevent AI drift; humans stay in control")

        st_space("v", 1)
        st_write(bs.assessment, "First formal AI-native SDLC \u2014 promising but early-stage.")
        st_write(bs.source, "Hymel \u2014 V-Bounce Model, 2024")
