"""Title slide — Generative Software Engineering Methods."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_LANDSCAPE as _SUFFIX

class BlockStyles:
    """Title slide styles."""
    title = Style.create(
        s.Huge + s.bold + s.center_txt + s.project.colors.primary
        + Style("line-height:1.1;", "gs_title_lh"),
        "gs_title",
    )
    subtitle = Style.create(
        s.project.titles.subtitle + s.center_txt,
        "gs_title_subtitle",
    )
    info = Style.create(
        s.project.titles.caption + s.center_txt,
        "gs_title_info",
    )
bs = BlockStyles

HERO_PROMPT = (
    f"{_PREFIX} A balanced scale with code symbols on one side and a structured process "
    "flowchart on the other, both glowing in electric blue and teal. The scale is perfectly "
    "balanced, symbolizing the equilibrium between AI-assisted coding speed and engineering "
    f"discipline. Geometric, minimal. {_SUFFIX}"
)

def build():
    with st_block(s.project.containers.page_fill_center):
        with st_block(s.center_txt):
            st_write(bs.title, "Generative Software Engineering Methods", tag=t.div, toc_lvl="1")
            st_image(
                s.none,
                width="80%",
                editable=IS_EDITABLE,
                name="hero_gensem_title",
                prompt=HERO_PROMPT,
                provider="openai",
                ai_size="1536x1024",
            )
            st_space("v", 1)
            st_write(bs.subtitle, "GenSEM \u2014 From VibeCoding to Disciplined Generative Engineering", tag=t.div)
            st_write(bs.info, "Session 3 \u00b7 AI for Software Engineering", tag=t.div)
