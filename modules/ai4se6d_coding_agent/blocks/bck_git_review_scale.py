"""Slide — Too big to read every line? Reading every line does not scale; how the check grows with the change (NG, 2026-11-24).

Placed at the end of the Git section: today's tasks are small, so learners read the whole diff, but the course says
upfront how the check changes when an agent changes hundreds or thousands of files.
"""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Review-at-scale styles."""
    heading = s.project.titles.heading
    pitch = Style.create(s.project.titles.body_accent + s.center_txt, "revscale_pitch")
    th = s.project.titles.table_header
    td = s.project.titles.table_cell
    tl = s.project.titles.table_label
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "revscale_cmd")
    note = Style.create(s.project.titles.caption + s.center_txt, "revscale_note")
bs = BlockStyles

_TABLE_ZOOM = 88    # tuned by measure: content bottom <= 1000 px at 1920x1080

# (size of the change, how you check it, where in the course)
_ROWS = [
    ("A few lines, one task", ("read the whole ", (bs.cmd, "git diff")), "Today, CalcApp tasks"),
    ("Tens of files", ("scope with ", (bs.cmd, "git diff --stat"), ", tests green, test files untouched, "
                       "read the risky parts"), "Day 2 — tasks with tests (11:30)"),
    ("Hundreds of files", ("AI review against the plan, triage HIGH / MEDIUM / LOW, read and fix the HIGH ones",),
     "Day 2 — review (14:30)"),
    ("Thousands of files", ("automatic checks (tests, lint, types), several agents review, you review the plan, the "
                            "tests and the risky zones",), "Days 3-6 — GSE-One"),
]

_NOTES = [
    ("Trainer action",
     "Read and comment — nothing to type. Say it clearly: today you read everything because the tasks are small; "
     "that is training, not the rule for real projects."),
    ("The message",
     "You never stop being responsible for what the agent wrote. What changes with the size of the change is how you "
     "check it: reading, then scope + tests, then AI review, then automatic checks and several reviewers."),
    ("Why not read everything",
     "A coding agent can change thousands of files in minutes: nobody reads that line by line, and a tired reader "
     "misses bugs anyway. Reading is kept for what is small or risky."),
    ("Risky parts — what to read even in a big change",
     "Security (authentication, secrets, input that reaches storage or a query), data (formats, migrations, "
     "deletion), money and business rules, configuration and dependencies (package.json, lock file, CI), and any "
     "change to the tests themselves."),
    ("Prevention — keep changes reviewable",
     "One small task per prompt, one branch per task (the plan of 11:00). A rule in AGENTS.md can ask the agent to "
     "stop and ask when a task needs more than a few files."),
    ("Words",
     "Scope = which files and how many lines changed. Triage = sort the problems by severity. Lint = a tool that "
     "flags suspicious code. Types = TypeScript's checks (npm run build). N-version review = several agents "
     "review the same change independently."),
    ("Command — git diff --stat",
     "One line per changed file with the number of lines added (+) and removed (-), then a total; no content. "
     "--stat = statistics only. The first thing to read on any change, big or small."),
    ("Ask the room",
     "« The agent changed 300 files for a 1-line request. What do you do before reading a single line? » "
     "(stop: the scope is wrong — undo with git restore, make the task smaller)."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "Too Big to Read Every Line?", tag=t.div, toc_lvl="+1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Too Big to Read Every Line?", entries=_NOTES,
                                 position="left", width="50vw")
        with st_zoom(105):
            st_write(bs.pitch, "You own every change — how you check it grows with its size.", tag=t.div)
        st_space("v", "3vh")

        # Header row, then one row per size, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
        cols = "2% 22% 50% 24% 2%"
        base = s.project.containers.row_cell_left
        hc = s.project.containers.table_header_cell
        head = [base, hc, hc, hc, base]
        cells = head + s.project.containers.rows(len(_ROWS), cols, filled=(2, 3, 4))
        with st_zoom(_TABLE_ZOOM), st_grid(cols=cols, gap="1.5vh 0.5vw", cell_styles=cells) as g:
            for h in ("", "The change", "How you check it", "In this course", ""):
                with g.cell():
                    if h:
                        st_write(bs.th, h)
            for size, how, when in _ROWS:
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.tl, size)
                with g.cell():
                    st_write(bs.td, *how)
                with g.cell():
                    st_write(bs.td, when)
                with g.cell():
                    pass  # right margin
        st_space("v", "3vh")
        with st_zoom(105):
            st_write(bs.note, "Keep changes small: one task, one branch — then reading stays possible.", tag=t.div)
