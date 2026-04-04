"""Title slide — Discovering VibeCoding & VibeEngineering."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.styles import Style as ns
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_LANDSCAPE as _SUFFIX


# Viewport-filling container: billboard centered
_page_fill = s.project.containers.page_fill_center


class BlockStyles:
    """Title slide styles."""
    title = Style.create(
        s.Huge + s.bold + s.center_txt + s.project.colors.primary
        + ns("line-height:1.1;", "vc_title_lh"),
        "vc_title",
    )
    subtitle = Style.create(
        s.project.titles.subtitle + s.center_txt,
        "vc_title_subtitle",
    )
    info = Style.create(
        s.project.titles.caption + s.center_txt,
        "vc_title_info",
    )
bs = BlockStyles


HERO_PROMPT = (
    f"{_PREFIX} A split-screen composition: left side shows a human hand casually waving "
    "at a glowing code editor, right side shows the same code editor with structured "
    "blueprints and test tubes. Electric blue and teal energy flows connect both sides "
    f"through an amber bridge. Symbolizes the spectrum from casual to disciplined AI coding. {_SUFFIX}"
)


def build():
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.title, "Discovering VibeCoding & VibeEngineering", tag=t.div, toc_lvl="1")

            st_image(
                s.none,
                width="80%",
                editable=IS_EDITABLE,
                name="hero_title",
                prompt=HERO_PROMPT,
                provider="openai",
                ai_size="1536x1024",
            )

            st_write(
                bs.subtitle,
                "Session 1 \u2014 Part 2 \u00b7 AI for Software Engineering",
                tag=t.div,
            )
