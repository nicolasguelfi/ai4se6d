"""Section title — CalcApp v0.3: Practicing GenSE Principles."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """CalcApp section title styles."""
    title = Style.create(
        s.Huge + s.bold + s.center_txt + s.project.colors.primary
        + Style("line-height:1.1;", "calcapp_title_lh"),
        "calcapp_title",
    )
    subtitle = Style.create(
        s.project.titles.subtitle + s.center_txt,
        "calcapp_subtitle",
    )
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_center):
        with st_block(s.center_txt):
            st_write(
                bs.title,
                "CalcApp v0.3 \u2014 Practicing GenSE Principles",
                tag=t.div,
                toc_lvl="1",
            )
            st_space("v", 1)
            st_write(
                bs.subtitle,
                "From theory to practice: applying Compound Engineering "
                "principles on a real application.",
                tag=t.div,
            )
