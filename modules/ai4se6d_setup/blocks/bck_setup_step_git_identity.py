"""Slide — Installation step 6b: tell git who you are (global name and email)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Installation step slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    step = Style.create(s.project.titles.caption + s.center_txt, "setup_step_caption")
    body = s.project.titles.body
    label = s.project.titles.label
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "setup_cmd")
    done_box = s.project.containers.callout
    done_label = Style.create(s.bold + s.project.colors.success, "setup_done_label")
bs = BlockStyles

_CODE_ZOOM = 220  # st_code font_size is not applied by Pygments: zoom instead
_GIT = (
    'git config --global user.name  "Your Name"\n'
    'git config --global user.email "you@example.com"\n'
    "git config --global init.defaultBranch main"
)

_NOTES = [
    ("Trainer action",
     "Learners do it — on their machine. Step 6 of the installation, second half: everyone types the three "
     "git config --global commands with their GitHub e-mail."),
    ("The message",
     "Every commit carries a name and an email: tell git who you are, once, for all your repositories (--global)."),
    ("The email",
     "Use the email of your GitHub account, so that your commits are linked to you on GitHub."),
    ("The default branch",
     "init.defaultBranch main: new repositories start on « main », the name used in the course."),
    ("The check",
     "git config --global --list shows the three values."),
    # Command recap: every command and option of the slide, in plain words (NG, 2026-11-24)
    ("Command — git config --global user.name \"Your Name\"",
     "git config changes a git setting. --global = for all your repositories on this machine (saved in ~/.gitconfig), "
     "not just one project. user.name = the author name written in each commit (a commit = one saved snapshot of "
     "the project). The quotes keep first and last name as one value: replace Your Name, keep the quotes."),
    ("Command — git config --global user.email \"you@example.com\"",
     "user.email = the e-mail written in each commit. Use the one of your GitHub account: GitHub links the commits "
     "to your profile."),
    ("Command — git config --global init.defaultBranch main",
     "A branch is a named line of work in a repository. init.defaultBranch = the name of the first branch that git "
     "init creates. main = the name used in the course and on GitHub (older git versions say « master »)."),
    ("Command — git config --global --list",
     "Prints all your global settings, one name=value per line: look for user.name, user.email and "
     "init.defaultbranch (git writes it in small letters)."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.step, "Installation · step 6 of 8 · ~5 min", tag=t.div)
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "6 · Your Git Identity", tag=t.div, toc_lvl="1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — 6 · Your Git Identity", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "2vh")
        with st_zoom(_CODE_ZOOM):
            st_code(s.none, code=_GIT, language="bash", line_numbers=False)
        st_space("v", "6vh")
        with st_zoom(115):
            st_write(bs.body, (bs.label, "Email: "), "the one of your GitHub account.")
            st_space("v", "6vh")
            with st_block(bs.done_box):
                st_write(bs.body, (bs.done_label, "Done when: "), (bs.cmd, "git config --global --list"), " shows them.")
