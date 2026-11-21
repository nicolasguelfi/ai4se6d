"""Slide — Day 6 morning: until 11:30, finish rather than start; from 11:00 the last task, empty shells and README (edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Finish line styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "finish_line_cmd")
    label = s.project.titles.label
    lesson = Style.create(s.project.titles.body + s.bold + s.center_txt, "finish_line_lesson")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(68):
            st_write(bs.heading, "Until 11:30: Finish, Do Not Start", tag=t.div, toc_lvl="+1", label="Finish the sprint")
            with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                with l.item(): st_write(bs.body, "Finish the task in progress; start a new one only if it fits")
                with l.item(): st_write(bs.body, (bs.label, "From 11:00, the last task"), ": hunt the empty shells, "
                                        "write the README project card (sheet E22)")
                with l.item(): st_write(bs.body, (bs.cmd, "/gse-status"), ": what is left? Move what will not make it "
                                        "to the backlog")
                with l.item(): st_write(bs.body, "Every task's tests green before the delivery")
                with l.item(): st_write(bs.body, "Note the moments you will show this afternoon: a Gate you changed, "
                                        "a finding, a refusal")
            with st_block(s.project.containers.callout):
                st_write(bs.lesson, "A small thing that works beats a big one that does not run.", tag=t.div)
