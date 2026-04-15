"""Title slide — Generative Software Engineering Methods."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_LANDSCAPE as _SUFFIX
from shared_widgets import st_hover_tooltip

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
    st_marker("GSE-One — Generative SE Methods")
    with st_block(s.project.containers.page_fill_center):
        with st_block(s.center_txt):
            st_write(bs.title, "Generative Software Engineering Methods", tag=t.div, toc_lvl="1")
            st_hover_tooltip(
                title="Generative Software Engineering",
                entries=[
                    ("Generative SE", "Generative Software Engineering is the emerging discipline where AI agents generate artifacts while humans specify, orchestrate, validate, and capitalize."),
                    ("GSE-One", "GSE-One is one methodology for this discipline \u2014 16 principles, 4 lifecycle stages, 23 commands, 9 agents. It illustrates the discipline and equips you to adapt to others."),
                    ("4 Sessions", "This training teaches the discipline through GSE-One across 4 sessions of 3 hours each."),
                ],
                scale="2vw", width="70vw", position="center",
            )
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
            st_write(bs.subtitle, "GSE-One \u2014 From VibeCoding to Disciplined Generative Engineering", tag=t.div)
            st_write(bs.info, "AI for Software Engineering \u2014 4 Sessions \u00d7 3h", tag=t.div)
