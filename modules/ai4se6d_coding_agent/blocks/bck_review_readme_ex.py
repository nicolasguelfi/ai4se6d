"""Slide — Exercise — README 80/20."""
# @guideline: minimalist-visual + maximize-viewport
# @pattern: ptn_exercise_flow
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Exercise — README 80/20 — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "review_readme_ex_body")
    keyword = s.bold + s.project.colors.highlight
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "review_readme_ex_cmd")
    timer = Style.create(s.project.titles.stat + s.center_txt, "review_readme_ex_timer")
    done_box = s.project.containers.callout
    done_label = Style.create(s.bold + s.project.colors.success, "review_readme_ex_done")
    number = Style.create(s.bold + s.project.colors.highlight + s.center_txt, "review_readme_ex_num")
bs = BlockStyles

_CODE_ZOOM = 97  # code readable in the room; tuned by measure so the slide fills one screen (NG, 2026-11-24)

_NOTES = [
    ("Trainer action",
     "Learners do it — on their machine. Exercise 15:50 → 16:05: the agent drafts the README, they run "
     "every command in it and add their own Why section."),
    ("The message",
     "15 minutes to apply the 80/20 rule: the agent drafts the README, you check it and add the Why."),
    ("The prompt",
     "It lists what the README must contain and restricts the sources to the code and @docs/plan.md: "
     "« Invent nothing ». A README is a promise to its reader."),
    ("Check it",
     "Run every command it gives. A README whose install or run command fails is worse than no README."),
    ("Your part",
     "A Why section of three sentences that only you could write: design choices, known limits, accepted "
     "trade-offs. Then commit on fix/review as « docs: README »."),
    ("Ask the room",
     "« Did any command in your generated README fail? »"),
]

_README = """\
Write README.md for CalcApp: what it does and for whom, tech stack,
install and run, scripts, project structure, features. Use only the
code and @docs/plan.md as sources. Invent nothing."""


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, 'Exercise — README 80/20', tag=t.div, toc_lvl='+1')
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Exercise — README 80/20", entries=_NOTES,
                                 position="left", width="50vw")
        with st_zoom(98):
            st_write(bs.timer, '15:50 → 16:05 · 15 min', tag=t.div)
        with st_zoom(105):
            with st_zoom(_CODE_ZOOM):
                st_code(s.none, code=_README, language='text', line_numbers=False, font_size="36pt")
        st_space("v", "1vh")

        # One numbered row per step, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
        steps = [
            ('Run every command in it: do they all work?',),
            ('Add a ', (bs.keyword, 'Why'), ' section: 3 sentences only you could write'),
            ('Commit on ', (bs.cmd, 'fix/review'), ': ', (bs.cmd, 'docs: README')),
        ]
        cols = "5% 5% 85% 5%"
        cells = s.project.containers.rows(len(steps), cols, filled=(2, 3))
        with st_zoom(111), st_grid(cols=cols, gap="1.5vh 0.5vw", cell_styles=cells) as g:
            for n, parts in enumerate(steps, 1):
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.body + bs.number, f"{n}", tag=t.div)
                with g.cell():
                    st_write(bs.body, *parts, tag=t.div)
                with g.cell():
                    pass  # right margin
        st_space("v", "1vh")
        with st_zoom(111), st_block(bs.done_box):
            st_write(
                bs.body,
                (bs.done_label, 'Done when: '),
                'the README works as written and ends with a Why section of your own.',
            )
