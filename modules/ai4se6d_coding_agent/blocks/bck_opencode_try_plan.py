"""Slide — Demo 3 then try it: plan with live docs (5 min)."""
# @guideline: minimalist-visual + maximize-viewport
# @pattern: ptn_exercise_flow
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_ask_opencode, st_hover_tooltip


class BlockStyles:
    """Try-it sheet styles."""
    heading = s.project.titles.heading
    step = s.project.titles.table_cell
    keyword = s.project.titles.table_label
    label = s.project.titles.table_label
    text = s.project.titles.table_cell
    demo = Style.create(s.project.titles.table_cell + s.project.colors.muted, "try_demo")
    number = s.bold + s.project.colors.highlight
bs = BlockStyles

_SHEET = [
    ("Goal", "a reviewed plan, no code"),
    ("Done when", "the plan names files and tests; a Context7 call appears"),
    ("Mid-point (2 min)", "context7 shows as connected"),
    ("If stuck", "your tutor window, then raise your hand"),
]

_NOTES = [
    ("Trainer action",
     "Learners do it — on their machine, 5 min, after your 3-min live demo (plan agent, a Context7 "
     "call). Everyone adds Context7 and gets a plan for /budgets — no build."),
    ("The message",
     "Plan agent and Context7 together: a plan grounded in current docs, reviewed by you, and no code "
     "yet."),
    ("The demo (3 min)",
     "Plan agent and one Context7 call visible in the conversation."),
    ("The steps",
     "Add context7 if it is not there yet; restart opencode and check « Connected » in the sidebar; switch to plan "
     "with Shift+Tab and ask for a /budgets page using context7 for React Router 7, tests first; read the plan and "
     "push back once."),
    ("Do not build",
     "This is a rehearsal: the real plan of CalcApp v0.1 is written in the planning workshop at 11:00."),
    ("Done when",
     "The plan names files and tests and a Context7 call appears. Mid-point at 2 min: context7 shows as connected."),
    ("If stuck",
     "Tutor window first, then raise your hand."),
    # Command recap: every command and option of the slide, in plain words (NG, 2026-11-24)
    ("Command — opencode mcp add context7 --url https://mcp.context7.com/mcp",
     "Typed in the terminal (not in opencode), in the project folder. mcp add = register an MCP server; context7 ="
     " the name you give it; --url = the address of the remote server. It writes the entry under mcp.servers in "
     "the project's opencode.json. Add --global to have it in every project instead. Check with opencode mcp list."),
    ("Or ask opencode",
     "Needs the build agent (plan may not edit the project). It still needs a restart: servers load at start. "
     "Read the server address before you allow it — an agent that gives itself new tools is a real risk."),
    ("Restart opencode",
     "Quit (/exit or Ctrl+C) and run opencode again: new servers are loaded at start."),
    ("Key — Shift+Tab",
     "In opencode, hold Shift and press Tab: it switches to the next primary agent (plan → build → plan). The "
     "active agent's name is shown near the prompt box. « Shift+Tab → plan » = press it until plan is shown."),
    ("Prompt — « Plan a /budgets page. Use context7 for React Router 7. Tests first. »",
     "/budgets is the web address of the new page (http://localhost:5173/budgets), not an opencode command. « Use "
     "context7 » asks for the live React Router 7 docs; « Tests first » = tests planned before code."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "Try It (5 min) — Plan", tag=t.div, toc_lvl="+1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Try It (5 min) — Plan", entries=_NOTES,
                                 position="left", width="50vw")
        st_write(bs.demo, "Demo first (3 min): plan agent, a Context7 call", tag=t.div)

        # One numbered row per step, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23); under step 1, the same
        # thing asked to opencode — build agent; the terminal command stays the main way (NG, 2026-11-25)
        steps = [
            (("No context7 yet? ", (bs.keyword, "opencode mcp add context7 --url https://mcp.context7.com/mcp")),
             "Give me the command to add the Context7 MCP server (https://mcp.context7.com/mcp) to this project, "
             "then run it."),
            (("Restart opencode: the sidebar shows context7 ", (bs.keyword, "Connected"), "?"), None),
            (((bs.keyword, "Shift+Tab → plan"),
              ": “Plan a /budgets page. Use context7 for React Router 7. Tests first.”"), None),
            (("Read the plan, push back once",), None),
            (((bs.keyword, "Do not build"), ": your real plan comes at 11:00"), None),
        ]
        cols = "5% 4% 86% 5%"
        for i, (parts, prompt) in enumerate(steps):
            if i:
                st_space("v", "0.8vh")
            cells = s.project.containers.rows(i + 1, cols, filled=(2, 3))[-4:]  # keeps the alternation
            with st_zoom(90), st_grid(cols=cols, gap="0 0.5vw", cell_styles=cells) as g:
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.step + bs.number, f"{i + 1}", tag=t.div)
                with g.cell():
                    st_write(bs.step, *parts, tag=t.div)
                with g.cell():
                    pass  # right margin
            if prompt:
                st_space("v", "0.4vh")
                st_ask_opencode(prompt, zoom=76, cols="5% 90% 5%", agent="build")
        st_space("v", "1.2vh")
        with st_zoom(90), st_grid(cols="5% 90% 5%") as m:
            with m.cell():
                pass  # left margin
            with m.cell():
                with st_block(s.project.containers.callout):
                    with st_grid(cols="auto 1fr", gap="4px 24px") as g:
                        for label, text in _SHEET:
                            with g.cell():
                                st_write(bs.label, label)
                            with g.cell():
                                st_write(bs.text, text)
            with m.cell():
                pass  # right margin
