"""References — Bibliography of all cited sources."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.bib import st_bibliography
from custom.styles import Styles as s


class BlockStyles:
    """References slide styles."""
    heading = s.project.titles.section_title + s.center_txt
bs = BlockStyles


def build():
    st_marker("References")
    st_bibliography(
        title="References",
        title_style=bs.heading,
        entry_style=s.large,
        toc_lvl="1",
        only_cited=True,
    )
