"""Section title slide — Compound Engineering: A Practical GenSE Approach."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_LANDSCAPE as _SUFFIX

class BlockStyles:
    """CE title slide styles."""
    title = Style.create(
        s.Huge + s.bold + s.center_txt + s.project.colors.primary
        + Style("line-height:1.1;", "ce_title_lh"),
        "ce_title",
    )
    subtitle = Style.create(
        s.project.titles.subtitle + s.center_txt,
        "ce_title_subtitle",
    )
bs = BlockStyles

HERO_PROMPT = (
    f"{_PREFIX} A spiral staircase viewed from directly above, each step progressively "
    "larger than the last, radiating outward. Steps transition from electric blue at the "
    "center through teal to amber at the outermost ring. Clean geometric lines, glowing "
    f"edges, sense of upward growth and compounding progress. {_SUFFIX}"
)

def build():
    with st_block(s.project.containers.page_fill_center):
        with st_block(s.center_txt):
            with st_zoom(90):
                st_write(bs.title, "Compound Engineering", tag=t.div, toc_lvl="1")
            st_write(bs.subtitle, "A Practical GenSE Approach", tag=t.div)
            st_image(
                s.none,
                width="70%",
                editable=IS_EDITABLE,
                name="hero_ce_title",
                prompt=HERO_PROMPT,
                provider="openai",
                ai_size="1536x1024",
            )
            st_space("v", 1)
            st_write(
                s.project.titles.body + s.center_txt + s.project.colors.muted,
                "Named after compound interest: each development cycle makes "
                "subsequent cycles easier, not harder.",
                tag=t.div,
            )
