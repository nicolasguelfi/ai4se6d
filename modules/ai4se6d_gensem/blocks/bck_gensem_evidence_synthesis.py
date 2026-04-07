"""Slide — Evidence Synthesis: 3 numbered takeaways."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    label = s.project.titles.label
    keyword = s.project.titles.keyword
    takeaway = Style.create(
        s.project.titles.body_accent + s.center_txt,
        "gs_ev_synth_takeaway",
    )
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(bs.heading, "Evidence Synthesis", tag=t.div, toc_lvl="1")
            st_space("v", 1)

        with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.ordered) as l:
            with l.item():
                st_write(
                    bs.body,
                    (bs.label, "Gains are real but highly variable"),
                    " \u2014 depends on experience, context, task complexity.",
                )
            with l.item():
                st_write(
                    bs.body,
                    (bs.label, "The methodology is the multiplier"),
                    " \u2014 10% with tools \u2192 25\u201330% with process transformation.",
                )
            with l.item():
                st_write(
                    bs.body,
                    (bs.label, "Senior expertise + structured process"),
                    " = where the real value is captured.",
                )

        st_space("v", 2)
        st_write(
            bs.takeaway,
            "This is why we need GenSEM \u2014 Generative Software Engineering Methods.",
        )
