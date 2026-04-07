"""Slide — Junior vs Senior: The Contradictions (3 studies)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Junior/senior comparison styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    stat = s.project.titles.stat
    card_title = s.bold + s.project.colors.primary + s.Large + s.center_txt
    card_sub = s.project.titles.caption + s.center_txt
    source = s.project.citation + s.large + s.center_txt
    takeaway = s.project.titles.body_accent + s.center_txt

bs = BlockStyles


_STUDIES = [
    (
        "Cui et al.",
        "4,867 devs, enterprise",
        s.project.containers.cell_primary_bg,
        "Juniors +27-39%, Seniors +8-13%",
    ),
    (
        "METR",
        "16 devs, OSS",
        s.project.containers.cell_accent_bg,
        "Seniors -19% slower on familiar code",
    ),
    (
        "Daniotti",
        "160K GitHub devs",
        s.project.containers.cell_active_bg,
        "Seniors capture ALL gains, juniors ZERO",
    ),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.heading, "Junior vs Senior: The Contradictions", tag=t.div, toc_lvl="1")
        st_space("v", 1)

        with st_grid(
            cols="repeat(auto-fit, minmax(280px, 1fr))",
            gap="24px",
            cell_styles=s.project.containers.cell_pad_md,
        ) as g:
            for name, scope, bg, finding in _STUDIES:
                with g.cell():
                    with st_block(bg + s.project.containers.cell_pad_md):
                        st_write(bs.card_title, name, tag=t.div)
                        st_write(bs.card_sub, scope)
                        st_space("v", 1)
                        st_write(bs.body, finding)

        st_space("v", 1)
        st_write(
            bs.takeaway,
            "The relationship is more nuanced than any single study suggests.",
        )
        st_space("v", 1)
        st_write(bs.source, cite("cui-fieldexperiments2024"))
        st_write(bs.source, cite("metr2025"))
        st_write(bs.source, cite("daniotti-github2025"))
