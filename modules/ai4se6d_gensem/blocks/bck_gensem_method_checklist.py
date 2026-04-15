"""Slide — GSE-One Quick Reference Checklist."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


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
    st_marker("GSE-One Quick Reference")
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.heading, "GSE-One Quick Reference Checklist", tag=t.div, toc_lvl="+1")
        st_hover_tooltip(
            title="Quick Reference Checklist",
            entries=[
                ("Purpose", "A step-by-step checklist to follow the GSE-One workflow in practice."),
                ("Key discipline", "Each step builds on the previous -- skip one and the downstream quality drops."),
                ("Carry forward", "This checklist is your companion for the hands-on practice sessions."),
            ],
            scale="2vw", width="70vw", position="center",
        )
        st_space("v", 1)

        with st_zoom(120):
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
