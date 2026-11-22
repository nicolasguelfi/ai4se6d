"""Title slide — Discovering VibeCoding & VibeEngineering."""
# @guideline: maximize-viewport
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
        + Style("line-height:1.1;", "vc_title_lh"),
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

_NOTES = [
    ("The session",
     "Second part of session 1. After the introduction to generative AI, this part looks at how developers "
     "actually code with it: VibeCoding, its dangers, and VibeEngineering as the disciplined answer."),
    ("The image",
     "Left, a hand waving at a code editor: casual coding by conversation. Right, the same editor with blueprints "
     "and test tubes: structure and verification. The bridge between them is what the session builds."),
    ("The thread",
     "Definition and principles of VibeCoding → this afternoon you try it (FreeSelfApp) → the dangers, with "
     "figures → VibeEngineering and its six principles → the tools, with opencode as the course agent."),
    ("Ask the room",
     "« Has anyone already built something just by talking to an AI? Did it work? »"),
]


def build():
    with st_block(s.project.containers.page_fill_center):
        # title on one line with the « i » (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(55):
                st_write(bs.title, "Discovering VibeCoding & VibeEngineering", tag=t.div, toc_lvl="1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Discovering VibeCoding & VibeEngineering",
                                 entries=_NOTES, position="left", width="50vw")
        st_space("v", "3vh")
        with st_block(s.center_txt):
            st_image(
                s.none,
                width="85%",
                editable=IS_EDITABLE,
                name="hero_title",
                prompt=HERO_PROMPT,
                provider="openai",
                ai_size="1536x1024",
            )
            st_space("v", "3vh")

            with st_zoom(170):
                st_write(
                    bs.subtitle,
                    "Session 1 \u2014 Part 2 \u00b7 \n AI for Software Engineering",
                    tag=t.div,
                )
