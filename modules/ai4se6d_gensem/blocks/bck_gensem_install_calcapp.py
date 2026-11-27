"""Slide — Install GSE-One v0.93.5 in your CalcApp folder (exercise E11, step 1, edition 2)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Install slide styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.center_txt, "install_calcapp_body")
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "install_calcapp_cmd")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "install_calcapp_foot")
bs = BlockStyles

# First line = the day-3 start command, repeated at the first GSE-One practical (NG, 2026-11-27)
_GSE = (
    "~/ai4se/ai4se-kit/tutor update   # it prints a fix: line for GSE-One? run that line first\n"
    "cd ~/ai4se/calcapp && git switch -c chore/gse-one main\n"
    "curl -fsSL https://raw.githubusercontent.com/nicolasguelfi/gensem/v0.93.5/install.sh \\\n"
    "  | GSE_PLATFORM=opencode GSE_VERSION=v0.93.5 sh\n"
    "git add . && git commit -m \"chore: install GSE-One v0.93.5\"\n"
    "git switch main && git merge --no-ff --no-edit chore/gse-one"
)


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(75):
            st_write(bs.heading, "GSE-One in Your CalcApp", tag=t.div, toc_lvl="+1", label="Install GSE-One in CalcApp")
            st_write(bs.body, "First update the tutor (and run the fix: line if it prints one). Then the same install "
                     "as on day 1, in your project folder this time.", tag=t.div)
            with st_zoom(165):  # readable in the room; longest line still on one line (NG, 2026-11-27)
                st_code(s.none, code=_GSE, language="bash", line_numbers=False)
            st_write(bs.body, "Done when ", (bs.cmd, "cat .gse/registry"), " prints ", (bs.cmd, ".opencode"), tag=t.div)
            st_write(bs.foot, "The new files are part of your project: committed on a branch, merged into main (main only receives merges).", tag=t.div)
