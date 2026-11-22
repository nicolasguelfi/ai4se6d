"""Slide 32 — The Autonomy Spectrum + The Agentic Turn."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_PORTRAIT as _SUFFIX
from shared_widgets import st_hover_tooltip

class BlockStyles:
    """Autonomy spectrum slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    subheading = s.project.titles.section_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.primary
    keyword_accent = s.bold + s.project.colors.accent
    keyword_warn = s.bold + s.project.colors.highlight
    number = s.project.titles.body + s.bold + s.project.colors.highlight
    takeaway = s.project.titles.body + s.center_txt
    source = s.project.citation + s.large + s.center_txt
bs = BlockStyles

_PROMPT = (
    f"{_PREFIX} A steep upward curve in electric blue with inflection point in amber burst. "
    "Below: small tool icons. Above: larger autonomous agent icons rising. "
    f"{_SUFFIX}"
)

# Image + list slide: text cell vertically centred, left-aligned (NG, 2026-11-23)
_text_cell = Style.create(s.container.layouts.vertical_center_layout + Style("text-align:left;", "txt_left"),
                          "ide_autonomy_text_cell")

# One screen per slide: the box is a full screen (the book zoom is 90 %), so the next slide's title does not show
# at the bottom (NG, 2026-11-23)
_one_screen = Style("min-height:104vh;", "ide_autonomy_one_screen")

# (number, keyword, style, explanation)
_LEVELS = [
    ("1", "Passive assistance", bs.keyword, " — responds only when invoked"),
    ("2", "Proactive copiloting", bs.keyword, " — suggests unprompted, you decide"),
    ("3", "Task-level delegation", bs.keyword_accent, " — you describe, AI executes"),
    ("4", "Autonomous agents", bs.keyword_warn, " — AI plans, executes, tests, iterates"),
    ("5", "Multi-agent orchestration", bs.keyword_warn, " — specialized AI teams collaborate"),
]

_NOTES_SPECTRUM = [
    ("The message",
     "AI coding tools differ less by their model than by how much they decide alone: from answering when asked (1) "
     "to teams of agents working together (5)."),
    ("Reading the levels",
     "1–2: the developer writes, the AI helps (answers, suggestions). 3: the developer describes a task, the AI "
     "carries it out. 4–5: the AI plans, executes, tests and iterates, alone or as a team."),
    ("The trap",
     "The higher the level, the more is done between two looks from you: autonomy moves the work from writing to "
     "reviewing, it does not remove it."),
    ("Link to the course",
     "This week you work at the agent levels with opencode (plan / build agents, @subagents): next slide."),
    ("Ask the room",
     "« At which level is the tool you use at work? Who reviews what it does? »"),
]

_NOTES_AGENTIC = [
    ("The message",
     "The turn: the tool no longer completes your line, it plans, edits files and runs commands. Your job becomes "
     "framing the task and reviewing the result."),
    ("The examples",
     "opencode (plan, build, @subagents), Claude Code (subagents, background tasks), GitHub Copilot (from an issue "
     "to a pull request), Cursor (IDE, CLI and cloud agents)."),
    ("The trap",
     "An agent that « runs » can also break: read the plan before letting it build, and the diff before you commit."),
    ("Link to the course",
     "VibeEngineering P5, human review at boundaries, is the answer to this turn."),
    ("Ask the room",
     "« What would you let an agent run on your machine without asking you first? »"),
]


def _header(style, title, lvl, notes, zoom):
    """Title and « i » on the same line (header grid 95% / 5%), title smaller (NG, 2026-11-23)."""
    with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
        with h.cell(), st_zoom(zoom):
            st_write(style, title, tag=t.div, toc_lvl=lvl)
        with h.cell():
            st_hover_tooltip(title=f"Trainer notes — {title}", entries=notes, position="left", width="50vw")


def build():
    # Slide 1 — The Autonomy Spectrum (Lines 455-461)
    with st_block(s.project.containers.page_fill_top + _one_screen):
        _header(bs.heading, "The Autonomy Spectrum", "1", _NOTES_SPECTRUM, 85)
        st_space("v", "2vh")
        # one row per level, alternating fills, a narrow numbering column (motif L2 + fonds f1)
        cols = "5% 6% 84% 5%"
        cells = s.project.containers.rows(len(_LEVELS), cols, filled=(2, 3))
        cells = [c + s.center_txt if k % 4 == 1 else c for k, c in enumerate(cells)]
        with st_zoom(100), st_grid(cols=cols, gap="2.5vh 0.5vw", cell_styles=cells) as g:
            for num, key, style, text in _LEVELS:
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.number, num, tag=t.div)
                with g.cell():
                    st_write(bs.body, (style, key), text, tag=t.div)
                with g.cell():
                    pass  # right margin

    st_slide_break()

    # Slide 2 — The Agentic Turn
    with st_block(s.project.containers.page_fill_top):
        _header(bs.subheading, "The Agentic Turn", "2", _NOTES_AGENTIC, 85)

        with st_grid(
            cols="1.5fr 3.5fr",
            gap="3vw",
            cell_styles=[s.project.containers.grid_cell_centered, _text_cell],
        ) as g:
            with g.cell():
                st_image(
                    s.none,
                    width="80%",
                    editable=IS_EDITABLE,
                    name="ide_autonomy_agentic",
                    prompt=_PROMPT,
                    provider="openai",
                    ai_size="1024x1536",
                )

            with g.cell(), st_zoom(105):
                with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered,
                             text_align="left", item_gap=0.6) as l:
                    # REF: opencode-sst2024
                    with l.item():
                        st_write(bs.body, (bs.keyword_warn, "opencode"), " — plan, build, @subagents")
                    # REF: anthropic-claude-code2025
                    with l.item():
                        st_write(bs.body, (bs.keyword_accent, "Claude Code"), " — subagents, background tasks")
                    with l.item():
                        st_write(bs.body, (bs.keyword, "GitHub Copilot"), " — issue → pull request")
                    with l.item():
                        st_write(bs.body, (bs.keyword, "Cursor"), " — IDE, CLI and cloud agents")
                st_space("v", 1)
                st_write(
                    bs.body,
                    "It ", (bs.keyword_warn, "plans, edits, runs"),
                    ". You ", (bs.keyword_accent, "frame and review"), ".",
                )

        st_write(bs.source, cite("opencode-sst2024"), " · ", cite("anthropic-claude-code2025"))
