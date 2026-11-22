"""Act IV — Other agents you will meet at work: one line each (state checked November 2026).

Sources checked 2026-11-09: GitHub changelog (Copilot cloud agent, renamed 2026-04-01),
github.com/openai/codex, Google developers blog 2026-05-19 ("Transitioning Gemini CLI to
Antigravity CLI": Gemini CLI stops serving individual plans on 2026-06-18, stays available
with paid API keys and enterprise licences), Cursor product pages.
"""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


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

_NOTES = [
    ("The message",
     "At work you will meet other agents than opencode. One line each, to recognise them (state of November 2026)."),
    ("The four",
     "Cursor: an AI-native editor with agent and plan modes. GitHub Copilot: an agent in the IDE, and a cloud agent "
     "that turns an issue into a pull request. Codex CLI: OpenAI's terminal agent, open source, reads AGENTS.md. "
     "Gemini CLI: Google's, succeeded by Antigravity CLI (May 2026)."),
    ("The trap",
     "This landscape changes every few months (Gemini CLI replaced, Copilot's agent renamed): the names age, the "
     "concepts stay."),
    ("Link to the course",
     "Next slide: the same concepts lined up across five agents."),
    ("Ask the room",
     "« Which of these does your company allow? Which data may it see? »"),
]

_ITEMS = [
    # REF: cursor-ainative2025
    ((bs.keyword, "Cursor"), " — AI-native editor, agent and plan modes"),
    # REF: copilot-plans2025
    ((bs.keyword, "GitHub Copilot"), " — IDE agent; cloud agent: issue → pull request"),
    # REF: openai-codex-cli2025
    ((bs.keyword, "Codex CLI"), " — OpenAI, open source, reads AGENTS.md"),
    ((bs.keyword, "Gemini CLI"), " — Google; succeeded by ", (bs.keyword_warn, "Antigravity CLI"), " (May 2026)"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(85):
                st_write(bs.heading, "Other Agents", tag=t.div, toc_lvl="1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Other Agents", entries=_NOTES, position="left", width="50vw")
        st_space("v", "3vh")

        # one row per agent, alternating fills (motif L2 + fonds f1), margins 5 %
        cols = "5% 90% 5%"
        cells = s.project.containers.rows(len(_ITEMS), cols, filled=(2,))
        with st_zoom(100), st_grid(cols=cols, gap="2.5vh 1vw", cell_styles=cells) as g:
            for parts in _ITEMS:
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.body, *parts, tag=t.div)
                with g.cell():
                    pass  # right margin

        st_space("v", "3vh")
        with st_zoom(110):
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
