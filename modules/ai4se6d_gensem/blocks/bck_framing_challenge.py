"""Slide — The mini-project challenge, and what "professional" means here (CCSET15, edition 2; adapted from the edition-1 day-5 deck)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Challenge styles."""
    heading = s.project.titles.heading
    callout = Style.create(s.project.titles.body + s.bold + s.center_txt, "challenge_callout")
    label = s.project.titles.label
    body = s.project.titles.body
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "challenge_cmd")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "challenge_foot")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(64):
            st_write(bs.heading, "Your Mini-Project", tag=t.div, toc_lvl="+1", label="The mini-project challenge")
            with st_block(s.project.containers.callout):
                st_write(bs.callout, "Frame a small project of your own and drive it with GSE-One, end to end.", tag=t.div)
            st_write(bs.label, "\"Professional\" does not mean big. It means the method:", tag=t.div)
            with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                with l.item(): st_write(bs.body, "Plan before you build — ", (bs.cmd, "/gse-plan"))
                with l.item(): st_write(bs.body, "Requirements with testable criteria before code — ", (bs.cmd, "/gse-reqs"))
                with l.item(): st_write(bs.body, "Code and tests, on a branch per task — ", (bs.cmd, "/gse-produce"))
                with l.item(): st_write(bs.body, "Deliver with an integrity check — ", (bs.cmd, "/gse-deliver"))
            st_write(bs.foot, "That is the difference between day 1 and today.", tag=t.div)
