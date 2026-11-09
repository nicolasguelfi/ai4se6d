"""Act IV — Why opencode for this course (replaces the former "You Will Master Cursor" slide)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Course-tool rationale slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.primary
    keyword_accent = s.bold + s.project.colors.accent
    keyword_warn = s.bold + s.project.colors.highlight
    note = Style.create(
        s.large + s.italic + s.project.colors.muted + s.center_txt,
        "ide_opencode_choice_note",
    )
    source = s.project.citation + s.large + s.center_txt
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_center_wide):
        with st_block(s.center_txt):
            st_write(bs.heading, "Why opencode?", tag=t.div, toc_lvl="1")
            st_space("v", 1)

            with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.ordered) as l:
                with l.item():
                    st_write(bs.body, (bs.keyword_warn, "Open source"), " — no seat licence, readable")
                with l.item():
                    st_write(bs.body, (bs.keyword, "Any provider"), " — one capped key for the course")
                with l.item():
                    st_write(bs.body, (bs.keyword_accent, "Concepts transfer"), " — to Cursor, Claude Code…")
                with l.item():
                    st_write(bs.body, (bs.keyword, "Terminal-first"), " — files, git, npm, tests")
                with l.item():
                    st_write(
                        bs.body,
                        (bs.keyword_warn, "GSE-One"), " — runs on 5 agents: the method goes with you",
                    )

            st_space("v", 1)
            st_write(
                bs.note,
                "The programme says Cursor: keep it (or any editor) open next to opencode to read code.",
                tag=t.div,
            )
            st_write(bs.source, cite("opencode-sst2024"))
