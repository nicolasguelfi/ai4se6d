"""Slide — Demo 3 then try it: plan with live docs (5 min)."""
# @guideline: minimalist-visual + maximize-viewport
# @pattern: ptn_exercise_flow
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


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
     "Learners do it — on their machine, 5 min, after your 3-min live demo (plan agent, todo list, a Context7 "
     "call). Everyone adds Context7 and gets a plan for /budgets — no build."),
    ("The message",
     "Plan agent, todo list and Context7 together: a plan grounded in current docs, reviewed by you, and no code "
     "yet."),
    ("The demo (3 min)",
     "Plan agent, its todo list, and one Context7 call visible in the conversation."),
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
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(75):
                st_write(bs.heading, "Try It (5 min) — Plan", tag=t.div, toc_lvl="+1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Try It (5 min) — Plan", entries=_NOTES,
                                 position="left", width="50vw")
        st_write(bs.demo, "Demo first (3 min): plan agent, todo list, a Context7 call", tag=t.div)

        # One numbered row per step, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
        steps = [
            ("No context7 yet? ", (bs.keyword, "opencode mcp add context7 --url https://mcp.context7.com/mcp")),
            ("Restart opencode: the sidebar shows context7 ", (bs.keyword, "Connected"), "?"),
            ((bs.keyword, "Shift+Tab → plan"),
             ": “Plan a /budgets page. Use context7 for React Router 7. Tests first.”"),
            ("Read the plan and its todo list, push back once",),
            ((bs.keyword, "Do not build"), ": your real plan comes at 11:00"),
        ]
        cols = "5% 4% 86% 5%"
        cells = s.project.containers.rows(len(steps), cols, filled=(2, 3))
        with st_zoom(85), st_grid(cols=cols, gap="1.2vh 0.5vw", cell_styles=cells) as g:
            for n, parts in enumerate(steps, 1):
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.step + bs.number, f"{n}", tag=t.div)
                with g.cell():
                    st_write(bs.step, *parts, tag=t.div)
                with g.cell():
                    pass  # right margin
        with st_zoom(85), st_grid(cols="5% 90% 5%") as m:
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
