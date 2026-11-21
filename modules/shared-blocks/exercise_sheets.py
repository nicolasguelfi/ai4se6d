"""Exercise sheets of edition 2 (days 3-6) — single source for the slides and the syllabus.

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
            "`cd ~/ai4se/calcapp` (since yesterday `main` holds your v0.1); install GSE-One on a branch "
            "merged into `main` (commands just before this sheet; same install command as day 1, installation step 5).",
            "Start `opencode`, type `/gse-go`, answer the profile questions in plain language.",
            "At the mode Gate choose Full; apply the 3-question grid and write your answers in the tracking sheet.",
            "Open `.gse/profile.yaml` (do you recognise yourself?) and `.gse/status.yaml`, then run `/gse-status`.",
            "Ask the agent to commit straight on `main`. Look for its Gate: the agent refuses by itself, explains "
            "the protect-main guardrail and offers safe paths (a branch, …). Pick one, and note the Gate. "
            "(The hook would block the commit only if the agent tried anyway.)",
        ],
        "done_when": "`/gse-status` shows the project in Full mode, and the guardrail Gate (refusal + safe options) "
                     "is noted in the tracking sheet.",
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
        "debrief": "What did GSE-One's plan see that your `docs/plan.md` missed — and the other way round? "
                   "How many Gates did you accept as proposed? (After a run of them, the coach asks you to pick Discuss once.)",
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
        "goal": "Three measures of the quality of your code (the quality kit was added at 09:00).",
        "steps": [
            "`npm run lint`: how many problems?",
            "`npm run test:coverage`: which percentage? Which source files are missing from the table, and why?",
            "On GitHub, tab Actions: open the last CI run of your repository. Which steps ran? Green or red?",
            "`/gse-health`: compare with your three numbers.",
        ],
        "done_when": "The three numbers and the CI colour are written in the tracking sheet.",
        "midpoint": None,
        "if_stuck": "No CI run? The kit is not pushed: `git push mine --all`. Then your tutor window → raise your hand.",
        "debrief": "What does coverage not tell you? Hint: a file no test loads is not even listed. "
                   "And are green tests a green build? (Each check sees a different thing.)",
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
    # ── Day 5 ───────────────────────────────────────────────────────────────
    "sprint": {
        "cycle": "All cycles · Exercise E20 (your mini-project, Lightweight mode)",
        "time": "Day 5 · 09:45 → day 6 · 11:30",
        "title": "Your Mini-Project Sprint",
        "goal": "Apply the loop you learned, on your own, in Lightweight mode: plan → requirements → production → delivery.",
        "steps": [
            "`/gse-plan`: a sprint of 8 to 10 complexity points; its last task, day 6 from 11:00, the empty-shell hunt "
            "and the README (sheet E22). What does not fit goes to the backlog (`/gse-backlog`).",
            "`/gse-reqs`: 2 to 5 requirements with Given / When / Then criteria, at least one of them a measurable "
            "non-functional requirement (sheet E21: you run it on two models).",
            "Show your plan and requirements to the trainer: day 5, 15:15-16:30, one by one.",
            "`/gse-produce`, task by task: each task on its branch, its tests run. Lightweight has no `/gse-tests` "
            "step: a minimal test strategy is generated for you.",
            "At every Gate, the 3-question grid: at least one change or one refusal per activity, in the tracking sheet.",
            "Every evening: `/gse-pause`, then `git push --all origin`.",
            "Day 6, 11:30: first delivery with `/gse-deliver` (sheet E22).",
        ],
        "done_when": "Day 5, 16:30: requirements and plan validated by the trainer. "
                     "Day 6, 11:30: the first delivery is on `main`.",
        "midpoint": "Day 5, 12:15 — the plan is validated and the requirements are written.",
        "if_stuck": "Your tutor window (project outside `~/ai4se`? `~/ai4se/ai4se-kit/tutor add <path>`) → the back of "
                    "your orientation page, \"when the agent drifts\" → raise your hand. No recovery tag: the project is yours.",
        "debrief": "Day 5, 16:30: what did you move to the backlog to hold the 11:30 delivery? Which Gate did you change, and why?",
    },
    "model_comparison": {
        "cycle": "CCSET05 and CCSET10 · Exercise E21",
        "time": "Day 5 · 09:45 · 60 min, with the plan",
        "title": "Compare Two Models",
        "goal": "Keep the better version of your requirements, by giving the same instruction to two models.",
        "steps": [
            "After `/gse-plan`, copy your project next to it, for the second model: `cp -R . ../<project>-model-b`.",
            "Model A, in your project — the course model `openrouter/deepseek/deepseek-v4.1-flash`: run `/gse-reqs` "
            "and write down your answers to its questions.",
            "Model B, in the copy: start `opencode`, type `/models`, pick `openrouter/minimax/minimax-m3.1-flash`, "
            "then `/gse-reqs` with the same answers.",
            "Fill the grid for each model: number of requirements, testable ones (Given / When / Then), the "
            "non-functional requirement it forgot, the questions it asked, the cost (sidebar: tokens, $ spent).",
            "Compare the structure, not the words. Keep the better version: if it is B, copy its "
            "`docs/sprints/sprint-01/reqs.md` over yours and ask the agent to check it against your plan.",
        ],
        "done_when": "The grid is filled for both models and the version you keep is noted in the tracking sheet.",
        "midpoint": None,
        "if_stuck": "`/models` does not show the model? Type part of its name to filter the list. "
                    "Then your tutor window → raise your hand.",
        "debrief": "Which model asked the better questions? Did the cheaper run lose anything that matters? "
                   "Compare the structure, not the words.",
    },
    "deploy_calcapp": {
        "cycle": "CCSET16 · Exercise E19",
        "time": "Day 5 · waves of 5 learners, 11:00-14:45 · 35-45 min per wave",
        "title": "Deploy CalcApp",
        "goal": "CalcApp online at its own address, to learn the path before your project.",
        "steps": [
            "Steps: to be written once the deployment server is chosen. Wait for your wave; the trainer guides it.",
        ],
        "done_when": "CalcApp answers at its address.",
        "midpoint": None,
        "if_stuck": "The trainer, at the deployment table.",
        "debrief": "At 16:30, debrief of cycle 16: what got stuck, and where you read your logs.",
    },
    # ── Day 6 ───────────────────────────────────────────────────────────────
    "deliver_freeze": {
        "cycle": "CCSET08 and CCSET14 · Exercise E22",
        "time": "Day 6 · 11:30 · 45 min",
        "title": "Deliver, Then Freeze",
        "goal": "A version you can present, honest about its limits.",
        "steps": [
            "From 11:00, the last task of your sprint, through GSE-One like any other (on its task branch): hunt the "
            "empty shells (`git grep -n -E \"NotImplemented|TODO|FIXME\"`, click every button, run your demo); write the "
            "README project card (pitch, how to run it, live address — CalcApp's if not deployed, \"Known limits\", "
            "an \"Ethics and compliance\" placeholder for E23).",
            "11:30, `/gse-deliver`: its integrity check lists at most 5 findings; a HIGH one stops the merge until you "
            "decide (fix it, or accept the risk as a recorded decision). Choose the merge strategy at the Gate.",
            "Push the delivery, then mark it as the demo version (a tag, not a commit): `git push origin main --tags`, "
            "`git tag demo main`, `git push origin demo`.",
            "12:00, freeze: no more change to the app's code. Rehearse your demo, step by step.",
            "A limit found after the delivery? Say it yourself in the demo; it becomes the first task of the next sprint.",
        ],
        "done_when": "The tag `demo` is on GitHub, on the delivered commit, and its README shows the project card and the known limits.",
        "midpoint": "12:00 — the delivery is on `main`, tagged `demo` and pushed; the freeze starts.",
        "if_stuck": "A HIGH finding blocks the merge? Small: fix it now. Otherwise accept the risk at the Gate and list it "
                    "in the known limits. Then your tutor window → raise your hand.",
        "debrief": "How many empty shells did you find? Which limit would you rather say yourself than have a visitor find? "
                   "After the course: the delivered sprint is closed; `/gse-task` (or `/gse-plan`) opens the next one — "
                   "new task branches, a new `/gse-deliver`.",
    },
    "project_audit": {
        "cycle": "CCSET03 applied · Exercise E23",
        "time": "Day 6 · 12:15 · 30 min",
        "title": "Audit Your Project",
        "goal": "Check your own project against the AI Act, licences, secrets and personal data.",
        "steps": [
            "AI Act: does your app use AI? If so, which risk level (day 1: unacceptable, high, low or minimal)? "
            "Does the user know they deal with an AI, or with AI-made content (transparency)?",
            "Licences: a `LICENSE` file in your repository? The licence of each direct dependency "
            "(`npm view <package> license`, `pip show <package>`): does one forbid your use?",
            "Secrets: `git log --all --oneline -- .env` prints nothing; `git grep -n -i -E \"api.?key|secret|password|token\"` "
            "shows no real value. A leaked key is revoked, not just deleted.",
            "Personal data: which ones does your app keep (names, e-mails, health…), where, why, for how long? "
            "Keep the fewest; demo with made-up data.",
            "Write the four answers in the README section \"Ethics and compliance\", as the first task of a new sprint: "
            "`/gse-task` opens it, `/gse-deliver` delivers it; push.",
        ],
        "done_when": "The README of `main`, on GitHub, has a section \"Ethics and compliance\" with your four answers.",
        "midpoint": None,
        "if_stuck": "Not sure of a risk level or a licence? Write \"not sure, because…\": an honest doubt is a valid answer. "
                    "Then your tutor window → raise your hand.",
        "debrief": "Who found a secret in their history, or a licence they did not know? What would change for a real client?",
    },
    "gallery_demo": {
        "cycle": "All cycles · Exercise E24",
        "time": "Day 6 · 13:45 · 15 min + 14:00 · 90 min",
        "title": "Gallery Demo",
        "goal": "Show your approach in 5 to 7 minutes, and test the projects of the others.",
        "steps": [
            "13:45, prepare: launch your app from the `demo` tag (`git switch --detach demo`); open the files you will show.",
            "Your 5-7 minutes, in this order: the problem (who, what) · the product, live · one GSE moment (a Gate you "
            "changed, a finding, a refusal) · one lesson · questions.",
            "Two rotations (14:00 and 14:45): half of the room presents at their laptop, the other half visits; then swap.",
            "As a visitor: try the product yourself, ask the 3 questions of the visitor grid, write one line per project.",
        ],
        "done_when": "You presented during one rotation and visited during the other, with one line of notes per project visited.",
        "midpoint": "14:45 — swap roles.",
        "if_stuck": "The app breaks during the demo? Show the requirements, the tests and the release notes instead: "
                    "the process is what is judged.",
        "debrief": "Which GSE moment did you see most often? Which project would you use tomorrow? (Taken up in E25.)",
    },
    "lessons": {
        "cycle": "All cycles · Exercise E25",
        "time": "Day 6 · 15:45 · 50 min",
        "title": "Lessons Learned and Monday Morning",
        "goal": "What you keep, change or drop, and one first concrete step at work.",
        "steps": [
            "Alone, 5 min: three notes — one thing to keep, one to change, one to drop (the agent, the method, your habits).",
            "At your table, 15 min: group the notes; choose the table's top keep, change and drop.",
            "One voice per table: 2 minutes for the room.",
            "16:15, alone: your Monday-morning plan — the first thing you will do differently at work, when, "
            "and how you will know it worked.",
            "Tell it to your neighbour in one minute.",
        ],
        "done_when": "Your table's keep / change / drop is reported, and your Monday-morning plan is in the tracking sheet.",
        "midpoint": "16:15 — the table lists are reported.",
        "if_stuck": "No idea for Monday? Pick one habit of this week: a plan before code, tests first, a branch per task, "
                    "the Gate grid, a README that states its limits.",
        "debrief": "The trainer collects the table lists: they feed the next edition, like your issues labelled `ai4se-ed2`.",
    },
}
