"""Slides — P1: Free discovery of GSE-One (briefing + debrief)."""
# @guideline: minimalist-visual + maximize-viewport
# @pattern: exercise-flow
from pathlib import Path
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip

_page_fill = s.project.containers.page_fill_top
_page_fill_center = s.project.containers.page_fill_center

_MODULE_DIR = Path(__file__).resolve().parent.parent
_VIDEO_SHORT = str(
    _MODULE_DIR / "static" / "images" / "managed" / "GSE" / "videos"
    / "GSE-One-promo-V02-SHORT-24s.mp4"
)


class BlockStyles:
    heading = s.project.titles.slide_title + s.center_txt
    section = s.project.titles.section_title + s.center_txt
    body = Style.create(s.Large + s.center_txt + s.text.wrap.hyphens, "p1_body")
    accent = Style.create(
        s.Large + s.bold + s.project.colors.accent + s.center_txt, "p1_acc",
    )
    highlight = Style.create(
        s.Large + s.bold + s.project.colors.highlight + s.center_txt, "p1_hl",
    )
    keyword = Style.create(
        s.Large + s.bold + s.project.colors.primary, "p1_kw",
    )
    instruction = Style.create(
        s.huge + s.bold + s.project.colors.accent + s.center_txt, "p1_instr",
    )
    timer = Style.create(
        s.Huge + s.bold + s.project.colors.highlight + s.center_txt, "p1_timer",
    )
bs = BlockStyles

_cell = (
    s.project.containers.cell_primary_bg
    + s.project.containers.cell_pad_md + s.center_txt
)
_cell_accent = (
    s.project.containers.cell_accent_bg
    + s.project.containers.cell_pad_md + s.center_txt
)


def build():
    st_slide_break(marker_label="Practice: Discover GSE-One")

    # ── Slide 1: Briefing — what you'll do ──────────────────────────
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(
                bs.heading, "Practice: Discover GSE-One",
                tag=t.div, toc_lvl="+1",
            )
            st_hover_tooltip(
                title="Why free discovery?",
                entries=[
                    ("Pedagogy", "You'll experience the full GSE-One lifecycle BEFORE having the theory explained. This creates concrete reference points for the concepts that follow."),
                    ("What to expect", "The GSE-One agent will guide you through onboarding (HUG), discovery (COLLECT/ASSESS), planning (PLAN), and the beginning of production (PRODUCE)."),
                    ("Your role", "Follow the agent's lead. Don't try to understand everything — just observe and note what surprises you."),
                ],
                scale="2vw", width="70vw", position="center",
            )
            st_space("v", 1)

            _left = Style("text-align: left;", "p1_left")
            with st_grid(cols="3fr 7fr", gap="24px") as g:
                with g.cell():
                    st_image(
                        s.center_txt, width="90%",
                        uri="images/managed/GSE/images/logo-gse-geni-with-shield.webp",
                    )
                with g.cell():
                    with st_grid(
                        cols="1fr 1fr",
                        gap="16px",
                        cell_styles=s.project.containers.cell_pad_sm,
                    ) as g2:
                        with g2.cell():
                            with st_block(_cell + _left):
                                with st_list(l_style=bs.body + _left, li_style=bs.body + _left, list_type=lt.unordered) as l:
                                    with l.item():
                                        st_write(bs.body + _left, (bs.keyword, "1. "), (bs.keyword, "Install GSE-One"), " from GitHub: ", (bs.accent, "github.com/nicolasguelfi/gensem"))
                                    with l.item():
                                        st_write(bs.body + _left, (bs.keyword, "2. "), (bs.keyword, "Open Cursor"), " on your empty CalcApp folder with ", (bs.accent, ".cursor"))
                                    with l.item():
                                        st_write(bs.body + _left, (bs.keyword, "3. "), "Type ", (bs.accent, "/gse:go"))
                        with g2.cell():
                            with st_block(_cell + _left):
                                with st_list(l_style=bs.body + _left, li_style=bs.body + _left, list_type=lt.unordered) as l:
                                    with l.item():
                                        st_write(bs.body + _left, (bs.keyword, "4. "), (bs.keyword, "Follow the process"), " without external help")
                                    with l.item():
                                        st_write(bs.body + _left, (bs.keyword, "5. "), (bs.keyword, "Note your observations"))

    st_slide_break(marker_label="Open CalcApp. Type /gse:go.")


    # ── Slide 2: Debrief questions ──────────────────────────────────
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(
                bs.heading, "Debrief: What Did You Experience?",
                tag=t.div, toc_lvl="+1",
            )
            st_hover_tooltip(
                title="Debrief — Mapping to GSE-One Concepts",
                entries=[
                    ("Questions → HUG", "The agent asked about your profile — that's Principle P4 (Human-in-the-Loop) and P9 (Adaptive Communication)."),
                    ("Choices → Gate", "When the agent presented options with consequences — that's P7 (Risk-Based Decision Classification)."),
                    ("Refusals → Guardrails", "When the agent refused an action — that's P11 (Guardrails) protecting you from risky operations."),
                    ("Branches → Worktrees", "The agent created branches/worktrees — that's P12 (Version Control Isolation)."),
                ],
                scale="2vw", width="70vw", position="center",
            )
            st_space("v", 1)

            _cell_alt = (
                s.project.containers.cell_active_bg
                + s.project.containers.cell_pad_md + s.center_txt
            )
            with st_zoom(90):
                with st_grid(
                    cols="1fr 1fr 1fr",
                    gap="16px",
                ) as g:
                    with g.cell():
                        with st_block(_cell_accent):
                            st_write(bs.body, "Did the agent ask you questions?")
                    with g.cell():
                        with st_block(_cell_alt):
                            st_write(bs.body, "Did it propose choices with consequences?")
                    with g.cell():
                        with st_block(_cell_accent):
                            st_write(bs.body, "Did it refuse to do something?")
                with st_grid(
                    cols="1fr 1fr 1fr",
                    gap="16px",
                ) as g:
                    with g.cell():
                        with st_block(_cell_alt):
                            st_write(bs.body, "Did it create branches or worktrees?")
                    with g.cell():
                        with st_block(_cell_accent):
                            st_write(bs.body, "Did it explain its confidence level?")
                    with g.cell():
                        with st_block(_cell_alt):
                            st_write(bs.body, "Did you feel in control?")

        st_space("v", "30vh")
