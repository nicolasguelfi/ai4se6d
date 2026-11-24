"""Slide — Exercise sheet — review: done when, mid-point, if stuck."""
# @guideline: minimalist-visual + maximize-viewport
# @pattern: ptn_exercise_flow
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


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
                ' lists your findings with severities; 2+ are ',
                (bs.keyword, 'fixed'),
                ' with a test; 1+ is ',
                (bs.keyword, 'refused'),
                ' with a reason; ',
                (bs.cmd, 'npm run test:run'),
                ' green on ',
                (bs.cmd, 'fix/review'),
                '.',
            )
        st_space("v", "5vh")

        # one row per checkpoint, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
        rows = [
            ('Mid-point (15:35): ', ("triage written. Not yet? Review one task's diff only.",)),
            ('If stuck: ', ('1. ', 'your tutor window', '  2. recovery tag ', (bs.cmd, 'j2-v0.1'),
                            '  3. raise your hand (review the reference code)')),
            ('Next (15:50): ', ('README 80/20.',)),
        ]
        cols = "5% 26% 64% 5%"
        cells = s.project.containers.rows(len(rows), cols, filled=(2, 3))
        with st_zoom(100), st_grid(cols=cols, gap="4vh 0.5vw", cell_styles=cells) as g:
            for label, parts in rows:
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.body, (bs.label, label), tag=t.div)
                with g.cell():
                    st_write(bs.body, *parts, tag=t.div)
                with g.cell():
                    pass  # right margin
