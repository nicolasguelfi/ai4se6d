"""Slide — Catch-up — restart from tag j2-part1."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Catch-up — restart from tag j2-part1 — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "tasks_catchup_body")
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "tasks_catchup_cmd")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "tasks_catchup_foot")
bs = BlockStyles

_CODE_ZOOM = 82  # code readable in the room; tuned by measure so the slide fills one screen (NG, 2026-11-24)


_CATCHUP = """\
cd ~/ai4se
git clone https://github.com/nicolasguelfi/calcapp-starter calcapp-restart
cd calcapp-restart && git checkout -b mywork j2-part1 && npm ci"""

_NOTES = [
    ("Trainer action",
     "Learners do it — on their machine. Only those who failed a re-orientation check: they restart from "
     "the tag j2-part1 now."),
    ("The message",
     "For whoever failed a re-orientation check: restart from the tag j2-part1, the end of Part 1 (task T1 "
     "done, tests green; its plan already marks T1 [done] and T2 [next])."),
    ("What the commands do",
     "Clone the starter into a new folder (calcapp-restart), create mywork from j2-part1, install the exact "
     "dependencies with npm ci. The old folder stays as it was."),
    ("What to carry over",
     "docs/plan.md and AGENTS.md from ~/ai4se/calcapp — the participant's own plan and rules — then skip the "
     "tasks the tag already contains."),
    ("The tone",
     "A recovery tag is a safety net, not a failure: the goal of the afternoon is the loop and the review, "
     "not finishing at all costs."),
    ("Or ask opencode — not here",
     "No prompt on this slide: the catch-up starts from a new clone in a new folder, and opencode works in the "
     "folder where it was started. Once opencode runs in the new folder, it can copy back and commit: « Give me "
     "the commands to copy docs/plan.md and AGENTS.md from ~/ai4se/calcapp into this project and commit them as "
     "'docs: my plan and rules', then run them. »"),
    # Command recap: every command and option of the slide, in plain words (NG, 2026-11-24)
    ("Command — cd ~/ai4se",
     "cd = change directory: the terminal now works inside ~/ai4se, the course folder (~ = your home folder, "
     "/home/student in the course VM). Every course project is cloned here, so the tutor window can read it."),
    ("Command — git clone (address) calcapp-restart",
     "git clone copies a project from GitHub onto your machine, with its whole history and its tags. First argument: "
     "the project's address (the CalcApp starter). Second argument: the name of the folder to create inside the "
     "current folder (~/ai4se, thanks to the cd just before); it must not exist yet — if it does, git refuses: pick "
     "another name such as calcapp-restart2 and use it in the next line."),
    ("Command — cd calcapp-restart",
     "cd = change directory: the terminal now works inside the new folder, so the next commands act on it."),
    ("Symbol — &&",
     "Runs the next command only if the previous one succeeded: if cd fails, nothing else runs."),
    ("Command — git checkout -b mywork j2-part1",
     "A tag is a fixed label on one commit — here a checkpoint of the course: j2-start (start of day 2), j2-part1"
     " (end of Part 1), j2-v0.1 (v0.1 reference). -b = create a new branch, mywork = its name, j2-part1 = the "
     "commit it starts from; git then switches to it. Newer equivalent: git switch -c mywork j2-part1."),
    ("Command — npm ci",
     "Installs the project's libraries (into node_modules/) exactly at the versions of package-lock.json. ci = « "
     "clean install »: it deletes any old node_modules first. Needed once per fresh clone, before npm run "
     "test:run or npm run dev."),
    ("Command — copy back plan and rules",
     "From inside calcapp-restart: cp ~/ai4se/calcapp/docs/plan.md docs/ then cp ~/ai4se/calcapp/AGENTS.md . — cp"
     " (source) (destination) copies a file; . = the current folder; an existing file of the same name is "
     "replaced without warning. Then git add docs/plan.md AGENTS.md && git commit -m \"docs: my plan and rules\"."),
    ("Command — opencode (in the new folder)",
     "Quit the old opencode (Ctrl+C or /exit), then cd ~/ai4se/calcapp-restart and type opencode: the agent works"
     " in the folder where it is started."),
    ("Trap — the tag's own plan",
     "j2-part1 already contains a docs/plan.md (the reference plan): copying yours back replaces it. Check which "
     "of your tasks the tag already covers (git log --oneline shows its commits), mark them [done] in your "
     "docs/plan.md and the first one left [next]."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, 'Catch-up: Tag j2-part1', tag=t.div, toc_lvl='+1')
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Catch-up: Tag j2-part1", entries=_NOTES,
                                 position="left", width="50vw")
        with st_zoom(106):
            st_write(bs.body, 'Restart from the end of Part 1 (task T1 done, tests green):', tag=t.div)
            st_space("v", "2vh")
            with st_zoom(_CODE_ZOOM):
                st_code(s.none, code=_CATCHUP, language="bash", line_numbers=False, font_size="26pt")   # one line per command at this zoom
            st_space("v", "2vh")
            with st_list(list_type=lt.unordered, l_style=bs.body, li_style=bs.body,
                         text_align="left", item_gap=0.6) as l:
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
                    st_write(bs.body, 'In your docs/plan.md, mark [done] the tasks ', (bs.cmd, 'git log --oneline'),
                             ' already shows, mark the first one left [next], continue with it')
            st_space("v", "2vh")
            st_write(bs.foot, 'A recovery tag is a safety net, not a failure.', tag=t.div)
