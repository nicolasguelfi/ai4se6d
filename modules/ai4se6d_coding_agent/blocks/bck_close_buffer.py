"""Slide — Buffer — catch up, questions, tutor window."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Buffer — catch up, questions, tutor window — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "close_buffer_body")
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "close_buffer_cmd")
    timer = Style.create(s.project.titles.stat + s.center_txt, "close_buffer_timer")
bs = BlockStyles

_NOTES = [
    ("Trainer action",
     "Learners do it — on their machine. Buffer 17:00 → 17:30: they finish missed exercises, ask "
     "questions, use the tutor window; before leaving, git status clean and v0.1 tagged."),
    ("The message",
     "The last half hour (17:00 → 17:30) is a buffer: catch up, ask, use the tutor window."),
    ("Catch up",
     "Every exercise sheet is in these slides: anyone who missed an exercise can finish it now."),
    ("Feedback",
     "An issue on nicolasguelfi/gensem with the label ai4se-ed2. It is public: no confidential data."),
    ("Before leaving",
     "git status clean, git tag shows v0.1, and git branch -v shows main and mywork on the same commit — the "
     "state Day 3 starts from."),
    ("Ask the room",
     "« Who does not yet have v0.1 tagged? Let us fix it before you leave. »"),
]

_ITEMS = [
    ('Finish the exercise you missed (its sheet is in these slides)',),
    ('Questions to the trainer',),
    ('Your tutor window', " for anything about today's steps"),
    ('Feedback: an issue on ', (bs.cmd, 'nicolasguelfi/gensem'), ', label ', (bs.cmd, 'ai4se-ed2'),
     ' — public, no confidential data'),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(55):
                st_write(bs.heading, 'Buffer: Catch Up, Ask, Tutor Window', tag=t.div, toc_lvl='1',
                         label='Buffer (17:00)')
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Buffer", entries=_NOTES,
                                 position="left", width="50vw")
        with st_zoom(80):
            st_write(bs.timer, '17:00 → 17:30', tag=t.div)
        st_space("v", "2vh")

        # one row per item, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
        cols = "5% 90% 5%"
        cells = s.project.containers.rows(len(_ITEMS), cols, filled=(2,))
        with st_zoom(95), st_grid(cols=cols, gap="2vh 0.5vw", cell_styles=cells) as g:
            for parts in _ITEMS:
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.body, *parts, tag=t.div)
                with g.cell():
                    pass  # right margin
        st_space("v", "3vh")
        with st_zoom(95), st_block(s.project.containers.callout):
            st_write(
                bs.body,
                'Before leaving: ',
                (bs.cmd, 'git status'),
                ' clean and ',
                (bs.cmd, 'git tag'),
                ' shows ',
                (bs.cmd, 'v0.1'),
                '; ',
                (bs.cmd, 'git branch -v'),
                ': ',
                (bs.cmd, 'main'),
                ' and ',
                (bs.cmd, 'mywork'),
                ' on the same commit.',
            )
