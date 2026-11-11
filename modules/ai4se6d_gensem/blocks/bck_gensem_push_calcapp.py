"""Slide — Push your CalcApp to your own GitHub repository (day 3 welcome, edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Push CalcApp styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.center_txt, "push_calcapp_body")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "push_calcapp_foot")
bs = BlockStyles

_CMD = (
    "cd ~/ai4se/calcapp && git switch main\n"
    "gh repo create calcapp --public --source=. --remote=mine\n"
    "git push mine --all && git push mine --tags\n"
    "gh repo view --web"
)


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(75):
            st_write(bs.heading, "Your CalcApp on GitHub", tag=t.div, toc_lvl="+1", label="Push CalcApp to GitHub")
            st_write(bs.body, "Your work goes to your own repository, pushed every evening.", tag=t.div)
            with st_zoom(140):
                st_code(s.none, code=_CMD, language="bash", line_numbers=False)
            st_write(bs.body, "Write the repository address in the tracking sheet.", tag=t.div)
            st_write(bs.foot, "No secret in the repository: it is public.", tag=t.div)
