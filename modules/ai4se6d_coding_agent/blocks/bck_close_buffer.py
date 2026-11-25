"""Slide — Buffer — catch up, questions, tutor window."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_ask_opencode, st_hover_tooltip


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
    ("Or ask opencode",
     "Under « Before leaving », the same checks asked to opencode (build agent): it shows the commands, runs them "
     "and reports."),
    # Command recap: every command and option of the slide, in plain words (NG, 2026-11-24)
    ("Words — issue, nicolasguelfi/gensem, label",
     "An issue is a ticket on a GitHub project: github.com/nicolasguelfi/gensem → tab Issues → New issue "
     "(owner/name = the project's address). A label is a tag on the issue (here ai4se-ed2). Trap: only the "
     "project's members can set labels; a learner who cannot should write « ai4se-ed2 » in the title."),
    ("Command — git status",
     "Read-only: changes nothing. Shows the branch you are on (« On branch mywork ») and what changed since the "
     "last commit: « Changes not staged » (modified, not yet added), « Changes to be committed » (added with git "
     "add), « Untracked files » (new files git does not follow yet). « nothing to commit, working tree clean » = "
     "everything is saved in a commit."),
    ("Command — git tag",
     "Without argument, lists all tags of the project; v0.1 must appear (next to the course tags j2-…)."),
    ("Command — git branch -v",
     "Lists the local branches; -v = with each branch's last commit (short id + message); * = the current branch."
     " main and mywork must show the same short id."),
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
            with h.cell(), st_zoom(80):
                st_write(bs.heading, 'Buffer: Catch Up, Ask, Tutor Window', tag=t.div, toc_lvl='1',
                         label='Buffer (17:00)')
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Buffer", entries=_NOTES,
                                 position="left", width="50vw")
        with st_zoom(92):
            st_write(bs.timer, '17:00 → 17:30', tag=t.div)
        st_space("v", "2vh")

        # one row per item, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
        cols = "5% 90% 5%"
        cells = s.project.containers.rows(len(_ITEMS), cols, filled=(2,))
        with st_zoom(96), st_grid(cols=cols, gap="1.5vh 0.5vw", cell_styles=cells) as g:
            for parts in _ITEMS:
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.body, *parts, tag=t.div)
                with g.cell():
                    pass  # right margin
        st_space("v", "3vh")
        with st_zoom(96), st_block(s.project.containers.callout):
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
        st_space("v", "0.6vh")  # the same checks asked to opencode — build agent (NG, 2026-11-25)
        st_ask_opencode("Give me the git commands to check that the tree is clean, that the tag v0.1 exists, and that "
                        "main and mywork are on the same commit, then run them.", zoom=84, cols="0% 100% 0%")
