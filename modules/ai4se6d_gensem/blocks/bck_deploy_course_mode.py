"""Slide — PLACEHOLDER: how we deploy in this course (operating mode of exercise E19).

To be written once NG has chosen the deployment server and how learners read their logs
(tracker docs/plans/2026-11-20-014-production-days5-6.md, open item). Do not add server names,
domains or tokens here before that decision.
"""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Placeholder styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    warn = Style.create(s.project.titles.body + s.bold + s.project.colors.highlight + s.center_txt, "course_mode_warn")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "course_mode_foot")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(66):
            st_write(bs.heading, "How We Deploy in This Course", tag=t.div, toc_lvl="+1",
                     label="Course deployment set-up (to be written)")
            with st_block(s.project.containers.callout):
                st_write(bs.warn, "To be written once the deployment server is chosen.", tag=t.div)
            st_write(bs.body, "This slide will give:", tag=t.div)
            with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                with l.item(): st_write(bs.body, "your identifier on the server")
                with l.item(): st_write(bs.body, "the configuration file you copy (never committed)")
                with l.item(): st_write(bs.body, "the order of the waves of 5")
                with l.item(): st_write(bs.body, "how you read your logs")
            st_write(bs.foot, "Placeholder — exercise E19.", tag=t.div)
