"""Slide — What you clone: the CalcApp starter at the tag j2-start (NG, 2026-11-24).

Shown just before « Try it: Git on CalcApp »: what the app will do, and what the clone contains on day 2 at 09:15.
Facts checked in the calcapp-starter repo at j2-start (src/App.tsx, src/pages/Home.tsx, tests/App.test.tsx,
AGENTS.md, docs/plan-example.md, package.json).
"""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Starter slide styles."""
    heading = s.project.titles.heading
    pitch = Style.create(s.project.titles.body_accent + s.center_txt, "starter_pitch")
    th = s.project.titles.table_header
    td = s.project.titles.table_cell
    tl = s.project.titles.table_label
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "starter_cmd")
    note = Style.create(s.project.titles.caption + s.center_txt, "starter_note")
bs = BlockStyles

_TABLE_ZOOM = 80   # tuned by measure: content bottom <= 1000 px at 1920x1080

# (what, what you get at j2-start)
_ROWS = [
    ("The screen", ("one page that shows only the title ", (bs.cmd, "CalcApp"), " — no feature yet")),
    ("The code", ((bs.cmd, "src/App.tsx"), " = the route ", (bs.cmd, "/"), " · ",
                  (bs.cmd, "src/pages/Home.tsx"), " = that page")),
    ("The test", ("one test, green: « the home page shows the CalcApp title » (", (bs.cmd, "tests/App.test.tsx"),
                  ")")),
    ("For the agent", ((bs.cmd, "AGENTS.md"), ": stack, commands and rules a coding agent must follow")),
    ("A fallback plan", ((bs.cmd, "docs/plan-example.md"), ": 7 tasks to v0.1, only if your own plan is not ready")),
    ("The stack", ("React 19 + TypeScript, Vite (dev server), Vitest (tests) — locked by ",
                   (bs.cmd, "package-lock.json"))),
]

_NOTES = [
    ("Trainer action",
     "Read and comment — nothing to type yet. Then the next slide: learners clone it themselves (Git exercise)."),
    ("The message",
     "CalcApp is the app of the day: a budget tracker in the browser. What they clone is an empty but working "
     "shell: everything they will see built today, they build with the agent, test first."),
    ("What CalcApp will do",
     "Add an expense (amount, category, date); list expenses with filters; set a monthly budget per category; see "
     "what is left, with a warning near or over budget (slide « CalcApp: Budget Tracker », Planning section). "
     "Tonight's target is v0.1 (16:15), tag j2-v0.1 = the reference solution."),
    ("What j2-start contains — exactly",
     "src/App.tsx (React Router with one route « / »), src/pages/Home.tsx (a heading « CalcApp »), src/main.tsx, "
     "src/App.css; tests/App.test.tsx (1 test) and tests/setup.ts; AGENTS.md; docs/plan-example.md; README.md; "
     "package.json + package-lock.json; Vite, TypeScript and ESLint config; a Dockerfile (used on day 6)."),
    ("Why start from a shell",
     "Everyone starts from the same, known-good state: npm ci installs the exact same libraries, the test is "
     "green, so any later red test comes from today's changes — not from the setup."),
    ("Words",
     "Route = a web address of the app (« / » = home page). Stack = the set of tools the app is built with. "
     "Vite = serves the app while you work (npm run dev). Vitest = runs the tests (npm run test:run). "
     "Lock file = the exact versions of every library."),
    ("Ask the room",
     "« The test is green and the app does nothing: what does that green really prove? » (only that the title shows)."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "What You Clone: CalcApp at j2-start", tag=t.div, toc_lvl="+1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — What You Clone: CalcApp at j2-start", entries=_NOTES,
                                 position="left", width="50vw")
        with st_zoom(100):
            st_write(bs.pitch, "The budget tracker you build today — you start from an empty shell.",
                     tag=t.div)
        st_space("v", "3vh")

        # Header row, then one row per item, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
        cols = "2% 20% 76% 2%"
        base = s.project.containers.row_cell_left
        head = [base, s.project.containers.table_header_cell, s.project.containers.table_header_cell, base]
        cells = head + s.project.containers.rows(len(_ROWS), cols, filled=(2, 3))
        with st_zoom(_TABLE_ZOOM), st_grid(cols=cols, gap="1.6vh 0.5vw", cell_styles=cells) as g:
            for h in ("", "At j2-start", "What you get", ""):
                with g.cell():
                    if h:
                        st_write(bs.th, h)
            for what, parts in _ROWS:
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.tl, what)
                with g.cell():
                    st_write(bs.td, *parts)
                with g.cell():
                    pass  # right margin
        st_space("v", "3vh")
        with st_zoom(100):
            st_write(bs.note, "Tonight (16:15): CalcApp v0.1 — add, list and total your expenses.", tag=t.div)
