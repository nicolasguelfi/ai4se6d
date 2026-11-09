# Adapted from streamtex-all-trainings@7707c1c5:content/genai_landscape/bck_genai_model_alone_concept.py
# Adapted from streamtex-all-trainings@7707c1c5:content/genai_landscape/bck_genai_tools_concept.py
# Adapted from streamtex-all-trainings@7707c1c5:content/genai_landscape/bck_genai_ai_agent_concept.py
# Adapted from streamtex-all-trainings@7707c1c5:content/genai_landscape/bck_genai_on_computer_concept.py
"""Slide — From LLM to Agent: model alone → + documents → + tools → agent loop in an authorised folder.

Edition 2, day-1 notion 1 (board peda1, P10). Four concept slides of all-trainings condensed into one ladder;
the example is opencode, the course tool (permissions allow / ask / deny, project folder).
"""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from streamtex.styles import StyleGrid as sg
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


_page_fill = s.project.containers.page_fill_top

_step = Style.create(
    s.project.containers.cell_primary_bg + s.project.containers.cell_pad_md,
    "l2a_step",
)
_step_last = Style.create(
    s.project.containers.cell_active_bg + s.project.containers.cell_pad_md,
    "l2a_step_last",
)
_example = Style.create(s.project.containers.callout, "l2a_example")


class BlockStyles:
    """Slide: LLM → agent — four-step ladder + opencode example."""
    heading = s.project.titles.section_title + s.center_txt
    num = Style.create(s.project.colors.highlight + s.bold + s.text.sizes.pt28, "l2a_num")
    name = Style.create(
        s.project.colors.accent + s.bold + s.text.sizes.pt32 + s.text.wrap.hyphens, "l2a_name",
    )
    what = Style.create(s.text.sizes.pt24, "l2a_what")
    trap = Style.create(
        s.project.colors.muted + s.italic + s.text.sizes.pt22 + s.text.wrap.hyphens, "l2a_trap",
    )
    ex = Style.create(s.text.sizes.pt24, "l2a_ex")
    ex_key = Style.create(s.text.sizes.pt24 + s.bold + s.project.colors.primary, "l2a_ex_key")
    duo = Style.create(s.text.sizes.pt24 + s.center_txt, "l2a_duo")
    duo_key = Style.create(s.text.sizes.pt24 + s.bold + s.project.colors.highlight, "l2a_duo_key")


bs = BlockStyles

# (step, name, what it does, the trap)
_STEPS = [
    ("1", "The model alone",
     "Writes the most likely continuation of a text. Looks nothing up, checks nothing.",
     "Trap: plausible is not checked."),
    ("2", "+ documents",
     "Sees only what is put in its context: your question, the conversation, the files given.",
     "Trap: the right passage is missing or outdated."),
    ("3", "+ tools",
     "The model asks, a program executes (read a file, run a test); the result comes back.",
     "Trap: \"I checked\" with no trace of a tool call."),
    ("4", "AI agent",
     "Chooses its next action itself, in a loop — act, check, choose — until the goal, "
     "inside a folder you authorise.",
     "Trap: too wide a folder; not reading its plan."),
]

_NOTES = [
    ("Message", "An AI agent = a model + context + tools + a loop. It decides the next step; "
                "nobody wrote the list of steps in advance."),
    ("Vocabulary", "Say \"AI agent\", never \"agent\" alone for a person."),
    ("Sources", "Zaharia et al. 2024 (compound AI systems); Anthropic 2024 (building effective agents); "
                "Willison 2025 (\"runs tools in a loop to achieve a goal\")."),
]


def build():
    with st_block(_page_fill):
        with st_grid(cols="92% 8%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell():
                st_write(bs.heading, "From LLM to AI Agent", tag=t.div, toc_lvl="1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — LLM to agent", entries=_NOTES, position="left", width="45vw")

        cells = sg.create("A1:C1", _step) + sg.create("D1", _step_last)
        with st_grid(cols="1fr 1fr 1fr 1fr", gap="14px", cell_styles=cells) as g:
            for num, name, what, trap in _STEPS:
                with g.cell():
                    st_write(bs.num, f"Step {num}", tag=t.div)
                    st_write(bs.name, name, tag=t.div)
                    st_space("v", 1)
                    st_write(bs.what, what, tag=t.div)
                    st_space("v", 1)
                    st_write(bs.trap, trap, tag=t.div)

        with st_block(_example):
            st_write(
                bs.ex,
                (bs.ex_key, "opencode is step 4, in your terminal: "),
                "it reads files, runs commands (e.g. the tests), edits code — and asks your permission "
                "(allow / ask / deny) before acting, inside the project folder.",
            )

        st_write(
            bs.duo,
            (bs.duo_key, "The AI does "), "the long work, action after action.   ",
            (bs.duo_key, "You keep "), "the instruction, the plan review, the move that matters.",
            tag=t.div,
        )
