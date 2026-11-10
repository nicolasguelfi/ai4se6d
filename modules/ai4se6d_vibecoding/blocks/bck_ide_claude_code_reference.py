"""Act IV — Claude Code: the reference terminal agent, shown through what transfers to opencode."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Claude Code slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.primary
    keyword_accent = s.bold + s.project.colors.accent
    keyword_warn = s.bold + s.project.colors.highlight
    takeaway = Style.create(
        s.Large + s.italic + s.project.colors.accent + s.center_txt,
        "ide_claude_code_takeaway",
    )
    source = s.project.citation + s.large + s.center_txt
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(bs.heading, "Claude Code", tag=t.div, toc_lvl="1")
            st_space("v", 1)

            with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                with l.item():
                    st_write(bs.body, (bs.keyword, "Anthropic's agent"), " — terminal, IDE, desktop, web")
                with l.item():
                    st_write(bs.body, (bs.keyword_accent, "CLAUDE.md"), " — twin of AGENTS.md")
                with l.item():
                    st_write(bs.body, (bs.keyword_accent, "Plan mode"), " — twin of the plan agent")
                with l.item():
                    st_write(bs.body, (bs.keyword, "Subagents, hooks, skills"), " — widely copied")
                with l.item():
                    st_write(bs.body, (bs.keyword_warn, "Claude models only"), " — plan or API")

            st_space("v", 1)
            st_write(
                bs.takeaway,
                "Learn the concepts once — recognise them everywhere.",
                tag=t.div,
            )
            st_write(bs.source, cite("anthropic-claude-code2025"))
