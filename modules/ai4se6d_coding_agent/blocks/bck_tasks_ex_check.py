"""Slide — Exercise sheet — Part 2: done when, mid-point, if stuck."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_ask_opencode, st_hover_tooltip


class BlockStyles:
    """Exercise sheet — Part 2: done when, mid-point, if stuck — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "tasks_ex_check_body")
    label = s.project.titles.label
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "tasks_ex_check_cmd")
    done_box = s.project.containers.callout
    done_label = Style.create(s.bold + s.project.colors.success, "tasks_ex_check_done")
bs = BlockStyles


_NOTES = [
    ("Trainer action",
     "Learners do it — on their machine. Same exercise: they check themselves against « Done when »; walk "
     "around at 13:55 and ask who has not merged routing yet."),
    ("The message",
     "How a participant knows Part 2 is finished, where they should be at mid-time, and what to do when stuck."),
    ("Done when",
     "Three observable facts: npm run test:run shows at least 4 passing tests; the app has two pages; an added expense "
     "survives a browser refresh."),
    ("Mid-point 13:55",
     "Routing merged into mywork. Walk around at 13:55 and ask who is not there yet — now, not at 14:20."),
    ("If stuck — in this order",
     "The tutor window first, then the recovery tag j2-part1, then a raised hand."),
    ("Ahead?",
     "Delete an expense (onDelete) with the same loop: test first, then code, then review."),
    ("Or ask opencode",
     "Under « Done when », the test check asked to opencode (build agent). The two pages and the refresh test stay "
     "in the browser. No prompt for the j2-part1 recovery: it starts from a new clone."),
    # Command recap: every command and option of the slide, in plain words (NG, 2026-11-24)
    ("Command — npm run test:run",
     "Runs all the tests once with Vitest (script « vitest run » of package.json) and gives the prompt back; "
     "green = all pass, red = at least one fails. npm test would stay in watch mode in your terminal (q quits)."),
    ("Check — « routing merged into mywork »",
     "git switch mywork then git log --oneline: the routing commits (test: …, feat: …) appear in the list. git "
     "branch --merged lists the branches already merged into the current one."),
    ("Tag — j2-part1",
     "A tag is a fixed label on one commit — here a checkpoint of the course: j2-start (start of day 2), j2-part1"
     " (end of Part 1), j2-v0.1 (v0.1 reference). Restart from it with the catch-up commands (clone into a new "
     "folder, git checkout -b mywork j2-part1, npm ci)."),
    ("Words — onDelete",
     "The function ExpenseItem calls when its delete button is clicked; the « ahead » task wires it so that an "
     "expense can be removed (and removed from localStorage)."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, 'Part 2 — Am I Done?', tag=t.div, toc_lvl='+1')
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Part 2, Am I Done?", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "2vh")
        with st_zoom(98), st_block(bs.done_box):
            st_write(
                bs.body,
                (bs.done_label, 'Done when: '),
                (bs.cmd, 'npm run test:run'),
                ' shows at least 4 passing tests; the app has two pages; an added expense survives a browser refresh.',
            )
        st_space("v", "0.6vh")  # the test check asked to opencode — build agent (NG, 2026-11-25)
        st_ask_opencode("Give me the command to run the tests and count the passing ones, then run it.", zoom=80,
                        cols="0% 100% 0%")
        st_space("v", "3vh")

        # One row per situation (label | what to do), alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
        items = [
            ('Mid-point (13:55): ', ('your routing task is merged into ', (bs.cmd, 'mywork'), '. Not yet? Ask now.')),
            ('If stuck: ', ('1. ', 'your tutor window', '  2. recovery tag ', (bs.cmd, 'j2-part1'),
                            '  3. raise your hand')),
            ('Finished early? ', ('add one more task — delete an expense (the ', (bs.cmd, 'onDelete'),
                                  ' handler) — with the same steps.')),
        ]
        cols = "5% 22% 68% 5%"
        cells = s.project.containers.rows(len(items), cols, filled=(2, 3))
        with st_zoom(104), st_grid(cols=cols, gap="2.2vh 0.5vw", cell_styles=cells) as g:
            for label, parts in items:
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.body, (bs.label, label), tag=t.div)
                with g.cell():
                    st_write(bs.body, *parts, tag=t.div)
                with g.cell():
                    pass  # right margin
