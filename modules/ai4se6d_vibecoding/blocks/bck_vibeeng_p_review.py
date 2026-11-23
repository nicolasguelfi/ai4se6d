"""Slide — P5: Human Review at Boundaries."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_PORTRAIT as _SUFFIX
from shared_widgets import st_hover_tooltip

class BlockStyles:
    """P5 slide styles."""
    heading = s.project.titles.section_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.primary
    number = Style.create(
        s.Giant + s.bold + s.project.colors.highlight + s.center_txt,
        "ve_p5_number",
    )
bs = BlockStyles

# Text cell: vertically centred, left-aligned (NG, 2026-11-23: same recipes as the intro module)
_text_cell = Style.create(s.container.layouts.vertical_center_layout + Style("text-align:left;", "txt_left"),
                          "ve_p_review_text_cell")

_NOTES = [
    ('The message',
     'Humans review where it matters: architectural decisions, security-critical code, integration points and validation results.'),
    ('The idea explained',
     'Reviewing every generated line does not scale; reviewing nothing is VibeCoding. The boundaries are where a mistake costs most, so that is where the human looks.'),
    ('The analogy',
     'Quality control at critical checkpoints, not on every line.'),
    ('The trap',
     'Approving by habit: a review that always says yes is no review (automation bias).'),
    ('Link to the course',
     'GSE-One makes the risky decisions « Gates »: the agent stops and waits for you.'),
    ('Ask the room',
     '« Which part of your code would you review even if the AI were always right? »'),
]

_PROMPT = (
    f"{_PREFIX} A flow of automated process in electric blue passing through "
    "human-shaped gate checkpoints in amber. Magnifying glass at each gate. "
    f"{_SUFFIX}"
)

def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            # title and « i » on the same line, title smaller (NG, 2026-11-23)
            with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
                with h.cell(), st_zoom(80):
                    st_write(bs.heading, "P5 — Human Review at Boundaries", tag=t.div, toc_lvl="1")
                with h.cell():
                    st_hover_tooltip(title="Trainer notes — P5 — Human Review at Boundaries", entries=_NOTES,
                                     position="left", width="50vw")

            with st_grid(cols="1.5fr 3.5fr", gap="3vw",
                         cell_styles=[s.project.containers.grid_cell_centered, _text_cell]) as g:
                with g.cell():
                    st_image(
                        s.none,
                        width="80%",
                        editable=IS_EDITABLE,
                        name="ve_p5_review",
                        prompt=_PROMPT,
                        provider="openai",
                        ai_size="1024x1536",
                    )

                with g.cell():
                    with st_zoom(70):   # the number smaller: more room for the text
                        st_write(bs.number, "5")
                    with st_zoom(125):
                        st_write(
                            bs.body,
                            "Review ",
                            (bs.keyword, "architectural decisions"),
                            ", ",
                            (bs.keyword, "security-critical code"),
                            ", ",
                            (bs.keyword, "integration points"),
                            ", and ",
                            (bs.keyword, "validation results"),
                            ".",
                        )
                        st_space("v", "2vh")
                        st_write(
                            bs.body,
                            (s.project.colors.muted, "Quality control at critical "
                            "checkpoints, not on every line."),
                        )
