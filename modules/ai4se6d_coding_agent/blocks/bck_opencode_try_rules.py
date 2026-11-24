"""Slide — Demo 1 then try it: project rules (5 min)."""
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
    ("Goal", "a rule of yours changes the agent’s answer"),
    ("Done when", "the proposal shows 25.5 as €25.50; git log shows your AGENTS.md commit"),
    ("Mid-point (2 min)", "the agent named the test command"),
    ("If stuck", "your tutor window, then raise your hand"),
]

_NOTES = [
    ("Trainer action",
     "Learners do it — on their machine, 5 min, after your 3-min live demo (/init on a copy vs the starter's "
     "AGENTS.md). Everyone adds the euro rule, runs /new and commits AGENTS.md."),
    ("The message",
     "One rule written in AGENTS.md visibly changes what the agent proposes. Participants see it on their own "
     "project in five minutes."),
    ("The demo (3 min)",
     "Run /init on a copy of the project and compare its draft with the starter's AGENTS.md: what did /init "
     "find on its own, what did it miss?"),
    ("The steps",
     "Work on the mywork branch; ask which test command and folders the agent must use; add the euro rule; start "
     "a clean session with /new and ask for formatAmount, code only; check git diff AGENTS.md and commit."),
    ("Why /new",
     "Without a new session the rule is only « in the chat »: /new proves the agent picks it up from AGENTS.md."),
    ("Done when",
     "The proposal shows 25.5 as €25.50 and git log shows the AGENTS.md commit. Mid-point at 2 min: the agent "
     "named the test command."),
    ("If stuck",
     "Tutor window first, then raise your hand."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "Try It (5 min) — Rules", tag=t.div, toc_lvl="+1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Try It (5 min) — Rules", entries=_NOTES,
                                 position="left", width="50vw")
        st_write(bs.demo, "Demo first (3 min): /init on a copy vs the starter’s AGENTS.md", tag=t.div)

        # One numbered row per step, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
        steps = [
            ((bs.keyword, "git switch mywork"), ", then ", (bs.keyword, "opencode")),
            ("Ask: “Which test command and folders must you use?”",),
            ("Add to AGENTS.md: ", (bs.keyword, "Amounts are in euros, 2 decimals: €25.50.")),
            ((bs.keyword, "/new"), ", then: “Propose formatAmount. Code only, no file.”"),
            ((bs.keyword, "git diff AGENTS.md"), ", then commit it"),
        ]
        cols = "5% 4% 86% 5%"
        cells = s.project.containers.rows(len(steps), cols, filled=(2, 3))
        with st_zoom(98), st_grid(cols=cols, gap="1.2vh 0.5vw", cell_styles=cells) as g:
            for n, parts in enumerate(steps, 1):
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.step + bs.number, f"{n}", tag=t.div)
                with g.cell():
                    st_write(bs.step, *parts, tag=t.div)
                with g.cell():
                    pass  # right margin
        with st_zoom(98), st_grid(cols="5% 90% 5%") as m:
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
