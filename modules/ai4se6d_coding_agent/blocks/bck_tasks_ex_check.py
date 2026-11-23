"""Slide — Exercise sheet — Part 2: done when, mid-point, if stuck."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


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
    ("The message",
     "How a participant knows Part 2 is finished, where they should be at mid-time, and what to do when stuck."),
    ("Done when",
     "Three observable facts: npm run test:run shows 4+ passing tests; the app has two pages; an added expense "
     "survives a browser refresh."),
    ("Mid-point 13:55",
     "Routing merged into mywork. Walk around at 13:55 and ask who is not there yet — now, not at 14:20."),
    ("If stuck — in this order",
     "The tutor window first, then the recovery tag j2-part1, then a raised hand."),
    ("Ahead?",
     "Delete an expense (onDelete) with the same loop: test first, then code, then review."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(65):
                st_write(bs.heading, 'Part 2 — Am I Done?', tag=t.div, toc_lvl='+1')
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Part 2, Am I Done?", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "2vh")
        with st_zoom(105), st_block(bs.done_box):
            st_write(
                bs.body,
                (bs.done_label, 'Done when: '),
                (bs.cmd, 'npm run test:run'),
                ' shows 4+ passing tests; the app has two pages; an added expense survives a browser refresh.',
            )
        st_space("v", "3vh")

        # One row per situation (label | what to do), alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
        items = [
            ('Mid-point (13:55): ', ('routing merged into ', (bs.cmd, 'mywork'), '. Not there? Ask now.')),
            ('If stuck: ', ('1. ', 'your tutor window', '  2. recovery tag ', (bs.cmd, 'j2-part1'),
                            '  3. raise your hand')),
            ('Ahead? ', ('delete an expense (', (bs.cmd, 'onDelete'), ') — same loop.')),
        ]
        cols = "5% 22% 68% 5%"
        cells = s.project.containers.rows(len(items), cols, filled=(2, 3))
        with st_zoom(102), st_grid(cols=cols, gap="3vh 0.5vw", cell_styles=cells) as g:
            for label, parts in items:
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.body, (bs.label, label), tag=t.div)
                with g.cell():
                    st_write(bs.body, *parts, tag=t.div)
                with g.cell():
                    pass  # right margin
