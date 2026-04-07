"""Section title — GenSEMOne: Your Lightweight GenSE Method."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_LANDSCAPE as _SUFFIX


class BlockStyles:
    """Method title slide styles."""
    title = Style.create(
        s.Huge + s.bold + s.center_txt + s.project.colors.primary
        + Style("line-height:1.1;", "gs_method_title_lh"),
        "gs_method_title",
    )
    subtitle = Style.create(
        s.project.titles.subtitle + s.center_txt,
        "gs_method_subtitle",
    )
bs = BlockStyles

HERO_PROMPT = (
    f"{_PREFIX} A winding teal path with six amber glowing waypoint nodes, "
    "starting from a small human silhouette on the left and ending at a "
    "glowing diamond shape on the right. The path curves gently upward "
    "like a roadmap. Each waypoint is a circle with a subtle glow. "
    f"Landscape orientation, sense of journey and progression. {_SUFFIX}"
)


def build():
    with st_block(s.project.containers.page_fill_center):
        with st_block(s.center_txt):
            st_write(bs.title, "GenSEMOne \u2014 Your Lightweight GenSE Method", tag=t.div, toc_lvl="1")
            st_image(
                s.none,
                width="80%",
                editable=IS_EDITABLE,
                name="hero_gensem_method",
                prompt=HERO_PROMPT,
                provider="openai",
                ai_size="1536x1024",
            )
            st_space("v", 1)
            st_write(
                bs.subtitle,
                "A practical, Cursor-native method for your professional mini-project. "
                "No plugins required \u2014 just discipline.",
                tag=t.div,
            )
