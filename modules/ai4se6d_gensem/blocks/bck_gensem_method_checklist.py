"""Slide — GenSEMOne Quick Reference Checklist."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Checklist slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.accent
    step = s.bold + s.project.colors.primary
    closing = Style.create(
        s.project.titles.body_accent + s.center_txt,
        "gs_checklist_closing",
    )
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.heading, "GenSEMOne Quick Reference Checklist", tag=t.div, toc_lvl="1")
        st_space("v", 1)

        with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.ordered) as l:
            with l.item():
                st_write(bs.body, (bs.step, "Step 0: "), ".cursor/rules/project.mdc created")
            with l.item():
                st_write(bs.body, (bs.step, "Step 1: "), "docs/requirements.md with FRs + NFRs")
            with l.item():
                st_write(bs.body, (bs.step, "Step 2: "), "docs/plan.md with structure + todos")
            with l.item():
                st_write(
                    bs.body,
                    (bs.step, "Step 3: "),
                    "For each FR: ",
                    (bs.keyword, "Tests"),
                    " \u2192 ",
                    (bs.keyword, "Implementation"),
                    " \u2192 ",
                    (bs.keyword, "Pass"),
                    " \u2192 ",
                    (bs.keyword, "Commit"),
                    " \u2192 ",
                    (bs.keyword, "Todo"),
                )
            with l.item():
                st_write(bs.body, (bs.step, "Step 4: "), "Review against requirements. Top 5 fixes done.")
            with l.item():
                st_write(bs.body, (bs.step, "Step 5: "), ".cursor/rules updated with 3\u20135 new rules.")

        st_space("v", 2)
        with st_block(s.center_txt):
            st_write(bs.closing, "Carry this checklist for Day 5\u20136!")
