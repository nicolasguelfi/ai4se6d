"""Slide — Closing: certificates and what you keep after the course (edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Resources styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "resources_cmd")
    thanks = Style.create(s.project.titles.subtitle + s.center_txt, "resources_thanks")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(66):
            st_write(bs.heading, "What You Keep", tag=t.div, toc_lvl="+1", label="Certificates and resources")
            with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                with l.item(): st_write(bs.body, "Your work in ", (bs.cmd, "~/ai4se"), ": FreeSelfApp, CalcApp with "
                                        "its tags, and your mini-project on GitHub")
                with l.item(): st_write(bs.body, "The course kit: syllabus of the 12 half-days, glossary, FAQ "
                                        "(CC BY 4.0) — ", (bs.cmd, "~/ai4se/ai4se-kit/syllabus"))
                with l.item(): st_write(bs.body, "GSE-One, open source, for opencode, Claude Code, Cursor, Codex CLI "
                                        "and Gemini CLI — ", (bs.cmd, "github.com/nicolasguelfi/gensem"))
                with l.item(): st_write(bs.body, "After the course you only need your own model key")
                with l.item(): st_write(bs.body, "Your certificate of attendance: handed out now")
            st_write(bs.thanks, "Thank you — build with discipline.", tag=t.div)
