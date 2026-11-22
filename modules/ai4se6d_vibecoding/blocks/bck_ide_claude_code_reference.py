"""Act IV — Claude Code: the reference terminal agent, shown through what transfers to opencode."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


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

_NOTES = [
    ("The message",
     "Claude Code is Anthropic's terminal agent, the reference many others copy. It is shown here for what transfers "
     "to opencode, not as the tool of the week."),
    ("The twins",
     "CLAUDE.md plays the role of AGENTS.md (project rules); plan mode plays the role of opencode's plan agent. "
     "Subagents, hooks and skills are ideas other agents have taken up."),
    ("The limit",
     "It runs Claude models only, through a subscription plan or the API: you cannot plug in another provider."),
    ("Link to the course",
     "GSE-One also targets Claude Code: the same method, the same files, another agent."),
    ("Ask the room",
     "« If you change agent tomorrow, what do you keep? » (the rules file, the plan-first habit, the review)"),
]

# (keyword parts, explanation) — one row each
_ITEMS = [
    ((bs.keyword, "Anthropic's agent"), " — terminal, IDE, desktop, web"),
    ((bs.keyword_accent, "CLAUDE.md"), " — twin of AGENTS.md"),
    ((bs.keyword_accent, "Plan mode"), " — twin of the plan agent"),
    ((bs.keyword, "Subagents, hooks, skills"), " — widely copied"),
    ((bs.keyword_warn, "Claude models only"), " — plan or API"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(85):
                st_write(bs.heading, "Claude Code", tag=t.div, toc_lvl="1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Claude Code", entries=_NOTES, position="left", width="50vw")
        st_space("v", "2vh")

        # one row per item, alternating fills (motif L2 + fonds f1), margins 5 %
        cols = "5% 90% 5%"
        cells = s.project.containers.rows(len(_ITEMS), cols, filled=(2,))
        with st_zoom(112), st_grid(cols=cols, gap="3vh 1vw", cell_styles=cells) as g:
            for key, text in _ITEMS:
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.body, key, text, tag=t.div)
                with g.cell():
                    pass  # right margin

        st_space("v", "3vh")
        with st_zoom(110):
            st_write(
                bs.takeaway,
                "Learn the concepts once — recognise them everywhere.",
                tag=t.div,
            )
        st_write(bs.source, cite("anthropic-claude-code2025"))
