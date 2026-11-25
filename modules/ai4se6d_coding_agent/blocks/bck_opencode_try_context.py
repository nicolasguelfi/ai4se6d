"""Slide — Demo 2 then try it: context and @file (5 min)."""
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
    ("Goal", "compare a vague prompt with a precise one"),
    ("Done when", "it quotes the test command and folder from the files"),
    ("Mid-point (2 min)", "the vague answer is noted"),
    ("If stuck", "your tutor window, then raise your hand"),
]

_NOTES = [
    ("Trainer action",
     "Learners do it — on their machine, 5 min, after your 3-min live demo (the same question, vague then with "
     "@files). Everyone compares the two answers and runs !npm run test:run."),
    ("The message",
     "The same question gets a guess without context and a grounded answer with @files. Participants measure the "
     "difference themselves."),
    ("The demo (3 min)",
     "Ask the same question twice: vague, then with @files. Point at what changes in the answer."),
    ("The steps",
     "/new and a vague question about tests, noted; /new and the same question from @package.json; "
     "!npm run test:run so the real output joins the conversation; a two-line summary of the results."),
    ("Why the « ! »",
     "A command run with ! puts its output in the context: the agent then reasons on the real test results, not "
     "on what it imagines."),
    ("Done when",
     "The answer quotes the test command and folder from the files. Mid-point at 2 min: the vague answer is noted."),
    ("If stuck",
     "Tutor window first, then raise your hand."),
    # Command recap: every command and option of the slide, in plain words (NG, 2026-11-24)
    ("Command — /new",
     "Typed in the opencode prompt box: starts a new, empty session (conversation). AGENTS.md is read again, the "
     "previous chat is forgotten, your files are unchanged. Shortcut: Ctrl+X then N."),
    ("Prompt — « How are tests organised here? »",
     "Deliberately vague: no file given, so the agent explores or guesses. Note its answer to compare."),
    ("Prompt — « How are tests organised here? Answer from @package.json. »",
     "The same question, grounded: @ attaches the file. package.json holds the scripts (test:run = vitest run)."),
    ("Why not @AGENTS.md",
     "opencode loads AGENTS.md on its own at the start of every session (and again when it changes): it is in both "
     "runs, so the layout rules (tests/ mirrors src/) are known either way. Only @package.json makes the "
     "difference. opencode never writes AGENTS.md itself: /init, you, or the agent when you ask."),
    ("Symbol — ! (shell mode)",
     "Typing ! at the start of an empty prompt switches opencode to shell mode: what follows runs in the terminal,"
     " in the project folder, and its output stays in the session for the agent. Esc leaves shell mode without "
     "running anything."),
    ("Command — !npm run test:run",
     "Runs the tests (vitest run, once) from inside opencode; the real results join the conversation."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "Try It (5 min) — Context", tag=t.div, toc_lvl="+1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Try It (5 min) — Context", entries=_NOTES,
                                 position="left", width="50vw")
        st_write(bs.demo, "Demo first (3 min): the same question, vague then with @files", tag=t.div)

        # One numbered row per step, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
        steps = [
            ((bs.keyword, "/new"), " “How are tests organised here?” Note the answer"),
            ((bs.keyword, "/new"), " “How are tests organised here? Answer from ", (bs.keyword, "@package.json"), ".”"),
            ((bs.keyword, "!npm run test:run"), " — the output joins the conversation"),
            ("“Summarise the test results in two lines.”",),
        ]
        cols = "5% 4% 86% 5%"
        cells = s.project.containers.rows(len(steps), cols, filled=(2, 3))
        with st_zoom(100), st_grid(cols=cols, gap="2vh 0.5vw", cell_styles=cells) as g:
            for n, parts in enumerate(steps, 1):
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.step + bs.number, f"{n}", tag=t.div)
                with g.cell():
                    st_write(bs.step, *parts, tag=t.div)
                with g.cell():
                    pass  # right margin
        with st_zoom(100), st_grid(cols="5% 90% 5%") as m:
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
