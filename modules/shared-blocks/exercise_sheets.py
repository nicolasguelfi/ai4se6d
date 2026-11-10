"""Exercise sheets of edition 2 (days 3-4) — single source for the slides and the syllabus.

One entry per sheet (keys are keywords, never numbers). Text in English (slides language).
Backticks mark commands and file names. Fields: cycle, time, title, goal, steps (list),
done_when, midpoint (optional), if_stuck, debrief. Timetable: docs/plans/2026-11-10-012-six-days-cycles-plan.html.
"""

SHEETS = {
    # ── Day 3 afternoon ─────────────────────────────────────────────────────
    "discover": {
        "cycle": "CCSET09 · Exercise E11 (P1)",
        "time": "13:30 · 50 min",
        "title": "Discover GSE-One on Your CalcApp",
        "goal": "Bring your CalcApp under GSE-One and pass your first Gate.",
        "steps": [
            "`cd ~/ai4se/calcapp`, `git switch mywork`; install GSE-One in this folder "
            "(same command as day 1, installation step 5).",
            "Start `opencode`, type `/gse-go`, answer the profile questions in plain language.",
            "At the mode Gate choose Full; apply the 3-question grid and write your answers in the tracking sheet.",
            "Open `.gse/profile.yaml` (do you recognise yourself?) and `.gse/status.yaml`, then run `/gse-status`.",
            "Ask the agent to commit straight on `main`. Watch the guardrail refuse, and note it.",
        ],
        "done_when": "`/gse-status` shows the project in Full mode, and one guardrail refusal is noted in the tracking sheet.",
        "midpoint": "14:00 — the profile questions are done.",
        "if_stuck": "Your tutor window → restart from the tag `p3-start` → raise your hand.",
        "debrief": "Which principles from this morning did you see: a Gate, a guardrail, the memory in files?",
    },
    "plan": {
        "cycle": "CCSET06 again, now with GSE-One · Exercise E12 (P3)",
        "time": "14:35 · 35 min",
        "title": "Plan the Sprint with GSE-One",
        "goal": "A sprint plan you validated, with at least one change of your own.",
        "steps": [
            "Let `/gse-go` chain collect → assess → plan (or run `/gse-plan`).",
            "Open `.gse/plan.yaml`: count the tasks and the complexity points.",
            "At the plan Gate, apply the grid and change at least one thing: split, reorder or remove a task.",
            "Compare with the `docs/plan.md` you wrote by hand on day 2.",
        ],
        "done_when": "`/gse-status` shows a validated plan, and your change is noted in the tracking sheet.",
        "midpoint": None,
        "if_stuck": "Your tutor window → restart from the tag `p3-start` → raise your hand.",
        "debrief": "What did GSE-One's plan see that your `docs/plan.md` missed — and the other way round?",
    },
    "requirements": {
        "cycle": "CCSET10 and CCSET11 · Exercise E13 (P5)",
        "time": "15:30 · 65 min",
        "title": "Requirements and Design",
        "goal": "The functional and non-functional requirements of CalcApp's next version, then a validated design.",
        "steps": [
            "`/gse-reqs`: answer in plain language; check that every functional requirement has testable "
            "acceptance criteria (Given / When / Then).",
            "Add yourself at least one measurable non-functional requirement, for example "
            "\"1,000 expenses are listed in less than 200 ms\".",
            "`/gse-design`: a Gate — apply the grid.",
            "`/gse-preview`: compare with what you had in mind.",
            "`/gse-status`: check the chain requirement → design → task.",
        ],
        "done_when": "`reqs.md` holds at least 3 functional requirements and 1 measurable non-functional one; "
                     "the design is validated; the links show in `/gse-status`.",
        "midpoint": "16:00 — the requirements are validated.",
        "if_stuck": "Your tutor window → restart from the tag `p5-start` → raise your hand.",
        "debrief": "Which elicitation technique did the agent use? Which non-functional requirement was missing?",
    },
    # ── Day 4 ───────────────────────────────────────────────────────────────
    "testing": {
        "cycle": "CCSET12 · Exercise E14 (P6)",
        "time": "09:25 · 80 min + 11:00 · 30 min",
        "title": "Test Strategy, Production, Review",
        "goal": "The next feature, tested according to your strategy, then reviewed.",
        "steps": [
            "On paper, 5 lines: your test strategy for the next requirement — which levels, which edge cases.",
            "`/gse-tests`: compare with your strategy; accept or refuse at least one point.",
            "`/gse-produce`: the tests run; how many pass?",
            "Part 2 (11:00): `/gse-review`; read the 3 most severe findings in `review.md`.",
            "Do you agree with the triage? Refuse at least one finding, with a written reason.",
        ],
        "done_when": "The feature is produced, its tests are green, `review.md` exists, and your triage is noted "
                     "with at least one reasoned refusal.",
        "midpoint": "10:05 — your test strategy is validated.",
        "if_stuck": "Your tutor window → restart from the tag `p6-start` → raise your hand.",
        "debrief": "What did the review find that you missed by hand on day 2? What do you fix first, what do you refuse?",
    },
    "quality": {
        "cycle": "CCSET13 · Exercise E15",
        "time": "11:58 · 12 min",
        "title": "Measure Your CalcApp",
        "goal": "Three measures of the quality of your code.",
        "steps": [
            "`npm run lint`: how many warnings?",
            "`npm run test:coverage`: which percentage, and which file is the least covered?",
            "Open the last CI run of your repository on GitHub: what does it check?",
            "`/gse-health`: compare with your three numbers.",
        ],
        "done_when": "The three numbers are written in the tracking sheet.",
        "midpoint": None,
        "if_stuck": "Your tutor window → raise your hand.",
        "debrief": "What does coverage not tell you?",
    },
    "delivery": {
        "cycle": "CCSET14 · Exercise E16 (P7)",
        "time": "13:30 · 60 min",
        "title": "Full Cycle and Continuity",
        "goal": "Close the sprint loop, and know how to pick your work up again.",
        "steps": [
            "`/gse-fix` on 2 findings, test first.",
            "`/gse-deliver`: choose the merge strategy at the Gate and justify it.",
            "`/gse-compound`: read the lessons captured, add your own.",
            "`/gse-health`: compare with this morning.",
            "Continuity: note an idea with `/gse-backlog`; `/gse-pause`, close opencode, reopen it, `/gse-resume`.",
        ],
        "done_when": "The feature is on `main`; your lesson is in the capitalisation file; `/gse-resume` tells you where you were.",
        "midpoint": "14:00 — the delivery is done.",
        "if_stuck": "Your tutor window → restart from the tag `p7-start` → raise your hand.",
        "debrief": "What did the agent keep as a lesson, and what would you have written? Did the health improve since this morning?",
    },
    "project_card": {
        "cycle": "CCSET15 · Exercise E17",
        "time": "15:20 · 25 min",
        "title": "Your Project Card",
        "goal": "A mini-project you can finish in a day and a half.",
        "steps": [
            "Pick a subject: professional or personal. An existing project is allowed if reduced to one small change.",
            "Fill one page: the user, the problem, 2 to 4 essential requirements, what is out of scope (backlog).",
            "Add the technology (deployable, or with your own Dockerfile) and the 5-7 minute demo you will give.",
            "Check it against the mini-project rules on the slide.",
        ],
        "done_when": "The card is written in the project repository (`docs/project.md`).",
        "midpoint": None,
        "if_stuck": "Your tutor window → ask your neighbour to read your card → raise your hand.",
        "debrief": "The trainer reads each card in one minute: \"green\" or \"reduce\".",
    },
    "project_start": {
        "cycle": "CCSET15 · Exercise E18",
        "time": "15:45 · 45 min",
        "title": "Start Your Mini-Project in Lightweight Mode",
        "goal": "Your mini-project started under GSE-One and validated by the trainer.",
        "steps": [
            "Create the project folder, `git init`, and its GitHub repository (private allowed).",
            "Install GSE-One in the folder; run `/gse-go` and choose Lightweight mode.",
            "Put every extra idea in the backlog, not in the plan.",
            "Folder outside `~/ai4se`? Run `~/ai4se/ai4se-kit/tutor add <path>`.",
            "Show your card to the trainer: \"green\" or \"reduce\".",
        ],
        "done_when": "`/gse-status` shows Lightweight mode, the card is \"green\", the repository is pushed.",
        "midpoint": None,
        "if_stuck": "Your tutor window → raise your hand.",
        "debrief": "Push both repositories (CalcApp and your project); hands-up quiz.",
    },
}
