"""Slide — Exercise sheet — review: done when, mid-point, if stuck."""
# @guideline: minimalist-visual + maximize-viewport
# @pattern: ptn_exercise_flow
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_ask_opencode, st_hover_tooltip


class BlockStyles:
    """Exercise sheet — review: done when, mid-point, if stuck — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "review_ex_check_body")
    label = s.project.titles.label
    keyword = s.bold + s.project.colors.highlight
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "review_ex_check_cmd")
    done_box = s.project.containers.callout
    done_label = Style.create(s.bold + s.project.colors.success, "review_ex_check_done")
bs = BlockStyles

_NOTES = [
    ("Trainer action",
     "Learners do it — on their machine. Same exercise: they check themselves against « Done when »; walk "
     "around at the 15:35 mid-point and ask who has no triage yet."),
    ("The message",
     "When the review exercise is finished, and what to do when it is not."),
    ("Done when",
     "docs/review.md lists the findings with severities; at least two are fixed with a test; at least one is "
     "refused with a reason; npm run test:run is green on fix/review."),
    ("Mid-point check (15:35)",
     "The triage should be written by then. If not, narrow the scope: review the diff of one task only."),
    ("If stuck",
     "First your tutor window, then the recovery tag j2-v0.1, then raise your hand — you then review the "
     "reference code instead of your own."),
    ("Next",
     "15:50: README 80/20 — the agent writes the what, you write the why."),
    ("Or ask opencode",
     "Under « Done when », the test check asked to opencode (build agent). docs/review.md is read by you. No "
     "prompt for the j2-v0.1 recovery: it starts from a new clone."),
    # Command recap: every command and option of the slide, in plain words (NG, 2026-11-24)
    ("Command — npm run test:run",
     "Runs all the tests once with Vitest (script « vitest run » of package.json) and gives the prompt back; "
     "green = all pass, red = at least one fails. npm test would stay in watch mode in your terminal (q quits)."),
    ("Branch — fix/review",
     "Check you are on it: git status (first line « On branch fix/review ») or git branch (the current branch has"
     " a *)."),
    ("Tag — j2-v0.1",
     "A tag is a fixed label on one commit — here a checkpoint of the course: j2-start (start of day 2), j2-part1"
     " (end of Part 1), j2-v0.1 (v0.1 reference). Same rescue commands with this tag name (git checkout -b mywork"
     " j2-v0.1): you get the reference v0.1 and review it instead of your code."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, 'Review — Am I Done?', tag=t.div, toc_lvl='+1')
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Review — Am I Done?", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "2vh")
        with st_zoom(100), st_block(bs.done_box):
            st_write(
                bs.body,
                (bs.done_label, 'Done when: '),
                (bs.cmd, 'docs/review.md'),
                ' lists your findings with their severity; at least two are ',
                (bs.keyword, 'fixed'),
                ', each with a test; at least one is ',
                (bs.keyword, 'refused'),
                ', with a reason; and ',
                (bs.cmd, 'npm run test:run'),
                ' passes on the branch ',
                (bs.cmd, 'fix/review'),
                '.',
            )
        st_space("v", "0.6vh")  # the test check asked to opencode — build agent (NG, 2026-11-25)
        st_ask_opencode("Give me the commands to switch to fix/review and run the tests, then run them.", zoom=80,
                        cols="0% 100% 0%")
        st_space("v", "2vh")

        # one row per checkpoint, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
        rows = [
            ('Mid-point (15:35): ', ("your triage is written. Not yet? Review the diff of one task only.",)),
            ('If stuck: ', ('1. ', 'your tutor window', '  2. recovery tag ', (bs.cmd, 'j2-v0.1'),
                            '  3. raise your hand (review the reference code)')),
            ('Next (15:50): ', ('the README exercise (80/20).',)),
        ]
        cols = "5% 26% 64% 5%"
        cells = s.project.containers.rows(len(rows), cols, filled=(2, 3))
        with st_zoom(96), st_grid(cols=cols, gap="2.5vh 0.5vw", cell_styles=cells) as g:
            for label, parts in rows:
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.body, (bs.label, label), tag=t.div)
                with g.cell():
                    st_write(bs.body, *parts, tag=t.div)
                with g.cell():
                    pass  # right margin
