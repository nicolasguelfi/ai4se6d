"""Slide — Rescue — restart from tag j2-start."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Rescue — restart from tag j2-start — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "d2_build_rescue_body")
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "d2_build_rescue_cmd")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "d2_build_rescue_foot")
bs = BlockStyles


_RESCUE = """\
git clone https://github.com/nicolasguelfi/calcapp-starter ~/ai4se/calcapp-restart
cd ~/ai4se/calcapp-restart && git checkout -b mywork j2-start && npm ci"""


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(70):
            st_write(bs.heading, 'Lost 15+ Minutes? Rescue', tag=t.div, toc_lvl='+1')
            st_write(bs.body, "Don't fight a broken setup: restart from the course's clean start.", tag=t.div)
            st_code(s.none, code=_RESCUE, language="bash", line_numbers=False, font_size="30pt")
            with st_list(list_type=lt.unordered, l_style=bs.body, li_style=bs.body) as l:
                with l.item():
                    st_write(
                        bs.body,
                        'Copy back ',
                        (bs.cmd, 'docs/plan.md'),
                        ' and ',
                        (bs.cmd, 'AGENTS.md'),
                        ' from ',
                        (bs.cmd, '~/ai4se/calcapp'),
                    )
                with l.item():
                    st_write(bs.body, 'Commit them, then restart at step 1 of the exercise')
            st_write(bs.foot, 'Your old work stays in ~/ai4se/calcapp. From now on, run opencode in calcapp-restart.', tag=t.div)
