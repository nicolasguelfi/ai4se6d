"""Act IV — Other agents you will meet at work: one line each (state checked November 2026).

Sources checked 2026-11-09: GitHub changelog (Copilot cloud agent, renamed 2026-04-01),
github.com/openai/codex, Google developers blog 2026-05-19 ("Transitioning Gemini CLI to
Antigravity CLI": Gemini CLI stops serving individual plans on 2026-06-18, stays available
with paid API keys and enterprise licences), Cursor product pages.
"""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Other agents slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.primary
    keyword_accent = s.bold + s.project.colors.accent
    keyword_warn = s.bold + s.project.colors.highlight
    takeaway = Style.create(
        s.Large + s.italic + s.project.colors.accent + s.center_txt,
        "ide_others_takeaway",
    )
    source = s.project.citation + s.large + s.center_txt
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(bs.heading, "Other Agents", tag=t.div, toc_lvl="1")
            st_space("v", 1)

            with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                # REF: cursor-ainative2025
                with l.item():
                    st_write(bs.body, (bs.keyword, "Cursor"), " — AI-native editor, agent and plan modes")
                # REF: copilot-plans2025
                with l.item():
                    st_write(bs.body, (bs.keyword, "GitHub Copilot"), " — IDE agent; cloud agent: issue → pull request")
                # REF: openai-codex-cli2025
                with l.item():
                    st_write(bs.body, (bs.keyword, "Codex CLI"), " — OpenAI, open source, reads AGENTS.md")
                with l.item():
                    st_write(
                        bs.body,
                        (bs.keyword, "Gemini CLI"), " — Google; succeeded by ",
                        (bs.keyword_warn, "Antigravity CLI"), " (May 2026)",
                    )

            st_space("v", 1)
            st_write(
                bs.takeaway,
                "Not exclusive: know which one to reach for.",
                tag=t.div,
            )
            st_write(
                bs.source,
                cite("cursor-ainative2025"), " · ", cite("copilot-plans2025"),
                " · ", cite("openai-codex-cli2025"),
                " · developers.googleblog.com, 19 May 2026",
            )
