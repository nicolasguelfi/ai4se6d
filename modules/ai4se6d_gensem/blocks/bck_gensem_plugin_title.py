"""Section title slide — Compound Engineering Plugin Live Demo."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s

class BlockStyles:
    """Plugin demo title slide styles."""
    title = Style.create(
        s.Huge + s.bold + s.center_txt + s.project.colors.primary
        + Style("line-height:1.1;", "plugin_title_lh"),
        "plugin_title",
    )
    subtitle = Style.create(
        s.project.titles.subtitle + s.center_txt,
        "plugin_title_subtitle",
    )
    info = Style.create(
        s.project.titles.caption + s.center_txt,
        "plugin_title_info",
    )
bs = BlockStyles

def build():
    with st_block(s.project.containers.page_fill_center):
        with st_block(s.center_txt):
            st_write(bs.title, "Compound Engineering Plugin \u2014 Live Demo", tag=t.div, toc_lvl="1")
            st_space("v", 1)
            st_write(bs.subtitle, "From principles to practice: a complete CE cycle with Claude Code.", tag=t.div)
            st_write(bs.info, "Day 6 \u2014 April 24, 2026", tag=t.div)
