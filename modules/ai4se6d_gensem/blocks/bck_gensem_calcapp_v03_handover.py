"""Slide — Your Mission: Practice GenSE on CalcApp v0.3."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Handover slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.accent
    time = s.bold + s.project.colors.highlight
    closing = s.project.titles.body + s.project.colors.highlight + s.bold
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(
                bs.heading,
                "Your Mission: Practice GenSE on CalcApp v0.3",
                tag=t.div,
                toc_lvl="1",
            )
            st_space("v", 1)

        st_write(bs.body, (bs.keyword, "Today\u2019s 4 workshop sessions:"))
        st_space("v", 0.5)

        with st_list(li_style=bs.body, list_type=lt.ordered) as l:
            with l.item():
                st_write(
                    bs.body,
                    (bs.keyword, "VibeTesting"),
                    " ",
                    (bs.time, "(10:15\u201311:00)"),
                    ": TDD discipline, Red \u2192 Green \u2192 Refactor",
                )
            with l.item():
                st_write(
                    bs.body,
                    (bs.keyword, "Drafting FRs"),
                    " ",
                    (bs.time, "(12:00\u201312:45)"),
                    ": Write functional requirements, Given/When/Then",
                )
            with l.item():
                st_write(
                    bs.body,
                    (bs.keyword, "VibeNFRs"),
                    " ",
                    (bs.time, "(2:30\u20133:15)"),
                    ": Non-functional requirements implementation",
                )
            with l.item():
                st_write(
                    bs.body,
                    (bs.keyword, "V&V"),
                    " ",
                    (bs.time, "(4:00\u20134:45)"),
                    ": Verification & validation, traceability matrix",
                )

        st_space("v", 1)

        with st_block(s.project.containers.callout):
            st_write(
                bs.closing,
                "You\u2019re practicing CE Phases 1\u20134 manually today. "
                "On Day 6, you\u2019ll see the plugin automate this.",
            )
