# État de l'art des concurrents et alternatives à GSE-One

> **Document de maintenance — v2 (avril 2026)**
> **Périmètre** : panorama des approches, plug-ins, outils, frameworks, standards et méthodologies concurrents ou adjacents à **GSE-One (Generic Software Engineering One)** — référence méthodologique pour le génie logiciel dirigé par l'IA générative.
> **Finalité** : (a) positionner GSE-One dans le paysage réel, (b) identifier les écarts exploitables, (c) dessiner la prochaine version optimale.
> **Sources** : 120+ entrées ajoutées à `modules/shared-blocks/static/references.bib` (cycles 1 et 2). Les clés BibTeX sont citées en ligne `[clé]`.
> **Base normative** : `gensem/gse-one-spec.md` (2956 lignes) — spécification technique canonique.

## 0. Changelog v1 → v2

La v1 de ce document (passe initiale) reposait sur une lecture partielle des supports pédagogiques (`bck_gensem_*.py`). La v2 est alignée sur la spécification canonique `gse-one-spec.md`. Principales corrections :

| v1 affirmait | v2 corrige |
|---|---|
| 14 commandes `/gse:*` | **23 commandes** (table Appendix A de la spec) |
| 16 principes, P9 + P15–P16 comme piliers AI | **16 principes en 4 catégories** : Foundations (P1–P3, P5–P6), Risk & Communication (P4, P7–P11), Infrastructure (P12–P14), AI Integrity (P15, P16) |
| Portable Cursor + Claude Code + Copilot | **Claude Code + Cursor + opencode** (3 plateformes réelles) via plug-in mono-directory `[opencode-sst2024]` |
| *Compound* = capitalisation projet | **3 axes** : projet (`compound.md`) + **méthodologie (issue auto sur repo GSE-One)** + compétences (`/gse:learn` notes) |
| Suggestion d'ajouter `constitution.md` (Spec-Kit) | `.gse/config.yaml` + `decisions.always_gate[]` **remplissent déjà ce rôle** (non négociables) |
| Suggestion d'ajouter une "autonomy tolerance dimension" SAFE-AI | HUG a déjà `decision_involvement: autonomous|collaborative|supervised` — à enrichir, pas à créer |
| Suggestion "sécurité de 1ère classe dans TESTS" | `/gse:reqs` **inclut déjà** une check-list **ISO/IEC 25010** (Performance, Security, Reliability, Usability, Maintainability, Accessibility, Compatibility) + audit de dépendances à chaque session |
| Suggestion "team-aware HUG" | Section 13.3 de la spec implémente **per-user profiles + assignee/reviewer** |
| Suggestion "tests de régression cross-sprint" | Existe déjà dans `/gse:review` — comparaison avec `docs/sprints/sprint-{NN-1}/test-reports/` |
| Décrivait `/gse:deliver` livrant le code | `/gse:deliver` merge + **tag sémantique + changelog + post_tag_hook** (option déploiement) |

L'identification de ces erreurs a motivé le cycle 2 de recherche, ciblé sur les zones encore sous-explorées : outils PaaS auto-hébergés (support de `/gse:deploy`), outils ADR (support du `.gse/decisions.md`), dashboards qualité (support du health score 8 dimensions), outils IA de gestion de projet (support du `plan.yaml` vivant), outils RE avec ISO 25010, V&V pour code IA, et mécanismes de retour de terrain vers les mainteneurs.

---

## 1. GSE-One — Ce qui est, réellement

Référentiel de comparaison précis, tiré de la spec.

### 1.1 Architecture (Section 1 de la spec)

- **Plug-in mono-directory** consommé par 3 plateformes d'agents : Claude Code, Cursor, opencode `[opencode-sst2024, anthropic-claude-code2025, cursor-ainative2025]`. Les artefacts partagés (skills, agents, templates) sont identiques sur les 3 ; les manifestes et hooks différent.
- **Concepts de plateforme** : coding-agent (Observe → Reason → Act), **agent** (rôle persona), **skill** (unité d'instruction à 3 politiques d'inclusion : always-on / on-demand / contextual), **hook** (commande déterministe hors boucle LLM, exit 0/2), **template** (squelette d'artefact). Mapping explicite des mécanismes Claude Code vs Cursor vs opencode.
- **9 agents** : 1 orchestrator + 8 spécialisés (requirements-analyst, architect, test-strategist, code-reviewer, security-auditor, ux-advocate, guardrail-enforcer, devil-advocate).

### 1.2 Cycle de vie (Sections 3, 14)

- **4 phases** : LC00 (onboarding) → LC01 (discovery & planning) → LC02 (development) → LC03 (capitalization).
- **23 commandes** réparties en 9 catégories :
  - Orchestration : `/gse:go /gse:status /gse:health /gse:pause /gse:resume /gse:task`
  - Onboarding : `/gse:hug`
  - Learning : `/gse:learn`
  - Backlog : `/gse:backlog`
  - Discovery : `/gse:collect /gse:assess /gse:plan`
  - Engineering : `/gse:reqs /gse:design /gse:preview /gse:tests /gse:produce /gse:deliver`
  - Quality : `/gse:review /gse:fix`
  - Deployment : `/gse:deploy`
  - Capitalization : `/gse:compound /gse:integrate`
- **PLAN est cross-cutting** (4 niveaux : projet / sprint / tâche / micro), pas confiné à LC01.
- **`[FIX]` conditionnel** : inséré uniquement si REVIEW détecte des findings HIGH/MEDIUM.

### 1.3 16 Principes (Section 2)

| Catégorie | Principes | Mécanismes concrets |
|---|---|---|
| **Foundations** | P1 Iterative · P2 Agile Terminology · P3 Artefacts Are Everything · P5 Planning at Every Level · P6 Traceability | YAML frontmatter obligatoire, 4 link types (`derives_from`, `implements`, `decided_by`, `related_to`) + cohérence bidirectionnelle ; 4 niveaux de planification |
| **Risk & Communication** | P4 HIL by Default · P7 Risk-Based Classification · P8 Consequence Visibility · P9 Adaptive Communication · P10 Complexity Budget · P11 Guardrails | Structured interaction pattern (Options + Discuss) · 6 dimensions de risque · **règle composite 3+ Modéré → Gate** · horizons **Now / 3 mois / 1 an** · beginner output filter (table de traduction) · 3 niveaux de guardrails Soft/Hard/Emergency |
| **Infrastructure** | P12 Version Control Isolation · P13 Event-Driven Behaviors · P14 Knowledge Transfer | Git worktree par tâche · safety tags `gse-backup/` (rétention 30j) · hooks système (3) + agent behaviors · notes d'apprentissage persistantes par topic |
| **AI Integrity** | P15 Agent Fallibility · P16 Adversarial Self-Review + User Pushback | 4 niveaux de confiance (Verified/High/Moderate/Low) · verification gates (preuve, pas assertion) · devil-advocate agent · **consecutive_acceptances counter** (seuils 3/5/8 par expertise) |

### 1.4 Artefacts & état (Section 12)

- **`.gse/` file-system layout** : config.yaml, profile.yaml (ou profiles/ en team mode), status.yaml, **plan.yaml (vivant)**, backlog.yaml, sources.yaml, inventory.yaml, decisions.md, decisions-auto.log, dashboard.py, backlog-archive.yaml, checkpoints/.
- **Backlog unifié** : TASK = item unique avec état git embarqué (branch, worktree, commits, uncommitted_changes, test_evidence).
- **Provenance** : champ `gse.source` (SRC-) + `source_origin` + `adaptation` pour tout artefact importé.
- **`test_evidence` structuré** par TASK : status, campaign_ref (TCP-), timestamp, pass_rate, code_coverage, summary.

### 1.5 Qualité & tests (Sections 6, 7)

- **Pyramide de tests par domaine** (8 domaines) : web / api / cli / data / mobile / library / embedded / scientific.
- **Test Review Layering** à 3 niveaux : STRATEGY / TST-SPEC / IMPL (les deux premiers conditionnels).
- **Détection de régression cross-sprint** : comparaison avec `docs/sprints/sprint-{NN-1}/test-reports/`.
- **Analyse multimodale de captures** en test visuel (best-effort, complémentée par Axe/Lighthouse/Playwright comparator).
- **Health score 0-10** agrégé sur 8 dimensions : requirements_coverage, test_pass_rate, design_debt, review_findings, complexity_budget, traceability, git_hygiene, ai_integrity.
- **Dashboard HTML autogénéré** (`dashboard.py`) via hook cross-platform + régénération explicite aux milestones.

### 1.6 Version control (Section 10)

- Arbre : `main` → `gse/sprint-NN/integration` → `gse/sprint-NN/{feat|fix|refactor|docs|test}/{desc}`.
- **Git Identity Verification Gate** avec 5 options (global/local/placeholder/self/discuss).
- **Backup tags `gse-backup/`** avant toute opération destructive, 30 jours.
- **Convention de commit `gse(scope): desc` + Sprint + Traces**.

### 1.7 Complexity Budget (Section 8)

- Budget dirigé en points par sprint (défauts : 15/12/8 selon Foundation/Feature/Stabilization).
- Table précise de coûts (dépendance utilitaire 1pt, framework 2-3pt, service externe 2-4pt, architecture 3-5pt, …).
- **Simplification credit** (points négatifs pour suppression).
- **Zero-cost items** (renommages, bug fixes sans architecture, tests).

### 1.8 Modes (Section 13.2)

- **Micro / Lightweight / Full** sélectionnés par analyse de **7 signaux structurels** (deps, persistence, entry points, multi-component, tests, CI/CD, git maturity) — **PAS par nombre de fichiers** (pré-filtre Micro seulement).

### 1.9 COMPOUND 3 axes (Section 3.9)

- **Axe 1** — project patterns → `docs/sprints/sprint-NN/compound.md`.
- **Axe 2** — methodology learnings → **issue auto-créée sur le repo GSE-One** (filtrée : actionnable + confirmée utilisateur OU observée en 2+ sprints).
- **Axe 3** — compétences → alimentation des notes `/gse:learn` via P14.

---

## 2. Panorama du paysage concurrentiel (v2)

Le paysage s'organise en **huit familles** — sept issues du cycle 1, plus une couche d'**outillage infrastructure** exposée par le cycle 2.

| Famille | Exemples clés | Ce qui concurrence GSE-One |
|---|---|---|
| **Méthodologies académiques AI-native** | SE 3.0 `[hassan-se30vision2024, hassan-se30-2025]`, Hoda `[hoda-beyondcode2025]`, Agentsway `[othman-agentsway2025]`, V-Bounce `[hymel-vbounce2025]`, Promptware `[chen-promptware2025]`, SAFE-AI `[navneet-safeai2025]` | Vision / roadmap / rôles |
| **Spec-Driven Development** | Spec-Kit `[github-speckit2025]`, Kiro `[aws-kiro2025]`, Tessl `[tessl-framework2025]`, OpenSpec `[openspec-fission2025]`, Grove `[grove-newcode2025]` | Spec = contrat exécutable |
| **Plug-ins méthodologiques portables** | Compound Engineering `[compound-engineering]`, BMAD-METHOD `[bmad-method2024]`, Task Master AI `[taskmaster-ai2024]`, AGENTS.md `[agentsmd-standard2025]` | **Concurrents directs** de GSE |
| **Context & runtime engineering** | Lütke `[lutke-contextengineering2025]`, Breunig `[breunig-contextfail2025]`, 12-Factor Agents `[horthy-12factor2025]`, ACE `[ace-playbooks2025]`, Context-Eng Survey `[contexteng-survey2025]` | Discipline de bas niveau complémentaire |
| **Adaptations d'agile/DevOps** | AgileGen `[zhang-agilegen2025]`, Agentic DevOps `[microsoft-agenticdevops2025]`, AI-DLC `[aws-aidlc2025]`, IDD 2026 `[kodenerds-idd2026]` | Greffe IA sur agile |
| **Recherche multi-agents** | MetaGPT `[hong-metagpt2024]`, ChatDev `[qian-chatdev2024]`, OpenHands SDK `[openhands-sdk2025]`, SWE-agent `[yang-sweagent2024]`, Agentless `[xia-agentless2024]`, HyperAgent `[phan-hyperagent2024]` | Systèmes fermés task-dedicated |
| **Outillage & infrastructure** *(nouveau cycle 2)* | PaaS, ADR, dashboards qualité, AI-PM, outils RE | Concurrence pièce-par-pièce sur les composants GSE |
| **Gouvernance & standards** | ISO/IEC 5338:2023 `[iso5338-2023]`, AAIF `[aaif-linuxfoundation2025]`, MCP Registry `[mcp-registry2025]`, FORGE `[forge-conference2025]`, AIware `[aiware-conference2025]` | Cadre normatif |

---

## 3. État de l'art par approche (v2)

Pour chaque entrée : **description**, **points communs avec GSE-One (corrigés)**, **points distinctifs**, **bénéfice potentiel** (en tenant compte de ce qui existe *réellement* dans la spec).

### 3.1 SE 3.0 / SASE — Hassan *et al.* `[hassan-se30vision2024, hassan-se30-2025]`

**Description** — Paradigme *intent-centric*, dualité **SE-for-Humans / SE-for-Agents**. Introduit deux workbenches (ACE / AEE) et l'artefact **Merge-Readiness Pack**.

**Points communs GSE-One** — Rôles explicites (orchestrator + 8 spécialisés), artefacts de 1ère classe, lifecycle formalisé.

**Points distinctifs** — SE 3.0 est vision/roadmap **sans outillage**. GSE-One a 23 commandes exécutables + state files + dashboard.

**Bénéfice potentiel** — Formaliser en sortie de `/gse:deliver` une **Merge-Readiness Pack** (diffs annotés, preuves tests, niveaux de confiance par fichier, empreinte SAFE-AI) consommable par CI/CD downstream. *Concret à implémenter : c'est un nouvel artefact TCP-like à ajouter à Section 12.2.*

### 3.2 V-Bounce — Hymel `[hymel-vbounce2025]`

**Description** — Adaptation V-model : LLM implémente, humain valide et vérifie.

**Points communs** — GSE a déjà la distinction **verification (DES-) / validation (REQ-)** et des tests correspondants (Section 6.1, table "Kind").

**Points distinctifs** — V-Bounce est monolithique ; GSE est lifecycle-multimode.

**Bénéfice** — Marginal : GSE couvre déjà la V&V formellement. Garder V-Bounce comme support pédagogique seulement.

### 3.3 Promptware Engineering — Chen *et al.* `[chen-promptware2025]`

**Description** — SDLC appliqué au prompt comme artefact.

**Points communs** — P3 (Artefacts Are Everything) + P6 (traceability) s'appliquent aux skills/prompts du plug-in GSE.

**Points distinctifs** — GSE ne versionne pas ses prompts comme des artefacts *par le même cycle* — ils sont dans `src/activities/*.md` figés.

**Bénéfice potentiel** — Ajouter un **meta-lifecycle** pour les skills du plug-in : quand un skill change, déclencher un REVIEW (P16 devil's advocate) + une entrée dans `maintenance/` du plug-in. *Piste pour la governance du plug-in.*

### 3.4 Agentsway — Othman *et al.* `[othman-agentsway2025]`

**Description** — Méthodologie end-to-end pour équipes d'agents, avec étape **Fine-Tuning** explicite + boucle rétrospective.

**Points communs** — Proche en structure (planification + orchestration humaine + boucle d'apprentissage = `/gse:compound`).

**Points distinctifs** — Inclut fine-tuning formel ; GSE-One reste *prompt-only* (P14 capitalisation sans adaptation de modèle).

**Bénéfice potentiel** — Spécialisation optionnelle **`/gse:tune`** (LC03, Full mode) capitalisant dans des embeddings few-shot ou adapters LoRA. À planifier en R&D, post-GSE-Two. *Dépendance : choix de fournisseur LLM, hors périmètre mono-plug-in actuel.*

### 3.5 Spec-Driven Development — Spec-Kit, Kiro, Tessl, OpenSpec `[github-speckit2025, aws-kiro2025, tessl-framework2025, openspec-fission2025, grove-newcode2025, fowler-sdd3tools2025, sdd-codecontract2026]`

**Description** — Mouvement convergent (2025–2026) où la spec est contrat exécutable. Spec-Kit impose `constitution.md` + 5 phases (constitution → specification → planning → tasks → implementation). Kiro a des **Agent Hooks** événementiels qui synchronisent spec ↔ code. Tessl maintient un **Spec Registry** (10 000+ specs OSS) pour prévenir les hallucinations d'API.

**Points communs GSE-One** — `.gse/config.yaml → decisions.always_gate[]` + lifecycle + guardrails **remplissent déjà le rôle de constitution** non négociable. Les REQS de GSE sont Given/When/Then (= contrat exécutable).

**Points distinctifs** — GSE est **process-centric** (le lifecycle est l'ossature), SDD est **spec-centric** (la spec est l'ossature). La spec de GSE cohabite avec design, tests, notes — pas de centre de gravité unique.

**Bénéfice potentiel** — Trois pistes concrètes :
1. **Export GSE → Spec-Kit** (commande `/gse:deliver --format spec-kit`) : `reqs.md` + `design.md` + `test-strategy.md` d'un sprint clos deviennent un pack Spec-Kit importable.
2. **Spec Registry local** (façon Tessl) : cache versionné de signatures d'API externes utilisées dans le projet, consulté par security-auditor pour bloquer les hallucinations de librairies (P15 verification gates).
3. **Renommage documentaire** : appeler `.gse/config.yaml` *"project constitution"* dans la doc utilisateur pour lever l'ambiguïté sémantique. Zéro changement de code.

### 3.6 Compound Engineering Plugin (Every) `[compound-engineering]`

**Description** — Plug-in OSS 4-phase (Plan → Work → Review → Compound) avec 26 agents spécialisés. **Parent idéologique direct** de GSE-One.

**MAJ 2026-07-10** — désormais 6 phases (Brainstorm, Plan, Work, Simplify, Review, Compound), 29 skills, 0 agent autonome ; commandes /ce-<skill> ; dépôt : EveryInc/compound-engineering-plugin (l'URL every-env/compound-plugin est morte).

**Points communs** — Même philosophie, même vocabulaire (compound), même positionnement plug-in.

**Points distinctifs** — GSE-One va au-delà : 23 commandes, 3 modes, 8-dim health dashboard, **Axe 2 methodology feedback** (inédit), safety tags git, beginner output filter.

**Bénéfice** — Maintenir la cartographie CE↔GSE (déjà en slide T7 du module) pour généalogie académique ; envisager contribution upstream vers Every pour éviter la fragmentation du courant.

### 3.7 BMAD-METHOD `[bmad-method2024, bmad-v6-ecosystem2026]`

**Description** — 37K+ stars GH. Framework YAML orchestrant 7 personas (Analyst, PM, Architect, SM, PO, Dev, QA). BMAD v6 introduit un module **Builder** pour extensions utilisateur.

**Points communs** — Rôles explicites, workflow multi-step, portable.

**Points distinctifs** — BMAD est **persona-first** (7 rôles), GSE est **phase-first** (4 LC). BMAD v6 Builder = extensions pull-based ; **GSE COMPOUND Axe 2 est push-based et filtré** — plus automatisé.

**Bénéfice potentiel** — Publier une **table d'équivalence BMAD ↔ GSE** dans `docs/maintenance/` pour faciliter les migrations entrantes.

### 3.8 AGENTS.md standard `[agentsmd-standard2025]`

**Description** — Standard ouvert AAIF (60K+ repos en 2026). opencode en est natif.

**Points communs** — GSE-One **consomme et produit déjà AGENTS.md** sur opencode (via `opencode/AGENTS.md` avec markers `<!-- GSE-ONE START -->`). Voir Section 1.1.4 de la spec.

**Points distinctifs** — Sur Claude Code et Cursor, GSE utilise l'agent par défaut et les rules `.mdc` ; pas d'AGENTS.md unique à la racine projet.

**Bénéfice potentiel** — **Émission optionnelle d'un AGENTS.md canonique** à la racine projet (pas seulement sous `opencode/`) comme résumé interop pour Codex/Devin/Factory/Gemini CLI. **À activer par flag HUG** (car l'étude ETH Zurich 2026 montre que des AGENTS.md auto-générés peuvent dégrader la performance — donc pas par défaut).

### 3.9 Context Engineering & 12-Factor Agents `[breunig-contextfail2025, horthy-12factor2025, contexteng-survey2025, ace-playbooks2025]`

**Description** — Mouvement méthodologique naissant : (a) taxonomie de failure modes du contexte (poisoning/distraction/confusion/clash) + patterns d'hygiène (tool loadout, quarantine, pruning, summarization, offloading) ; (b) 12-Factor = principes runtime (own your prompts, own your context window, stateless LLM-as-decision).

**Points communs** — Les skills `/gse:*` **sont** des scaffoldings déterministes autour de points de décision LLM (alignement exact 12-Factor). `.cursor/rules/` + COMPOUND implémentent une forme de context engineering.

**Points distinctifs** — GSE n'a pas de **taxonomie de failure modes du contexte** explicite, ni de **checklist de context hygiene** intégrée à `/gse:review`.

**Bénéfice potentiel** — Deux ajouts concrets :
1. **Checklist Breunig dans `/gse:review`** : détection de poisoning/distraction/confusion/clash dans le sprint, tagué `[CONTEXT]` dans les findings.
2. **Audit 12-Factor du plug-in GSE** comme tâche de maintenance : vérifier chaque skill (dont factor 4 : small focused agents). À consigner dans `docs/maintenance/12factor-audit-YYYYQN.md`.

### 3.10 Vibe Engineering & Fowler patterns `[willison-vibeengineering2025, fowler-abstraction2025, fowler-friction2025]`

**Description** — Willison définit vibe engineering comme *accountability-preserving* ; Fowler traite le LLM comme abstraction non déterministe ("dodgy collaborator").

**Points communs** — P15 (agent fallibility) + P16 (devil's advocate + user pushback) + verification gates = opérationnalisation de l'accountability.

**Points distinctifs** — GSE va plus loin que Willison : le **consecutive_acceptances counter** avec seuils (3/5/8) est une mesure quantitative, pas seulement une check-list.

**Bénéfice potentiel** — Intégrer explicitement Fowler dans le module T6 (Testing & Review) + ajouter une note `docs/maintenance/fowler-mapping.md` pointant quelles observations Fowler sont couvertes par quels principes GSE.

### 3.11 SAFE-AI — Navneet & Chandra `[navneet-safeai2025]`

**Description** — Taxonomie à 4 niveaux d'autonomie IA (suggestive/generative/autonomous/destructive) + 4 piliers (Safety, Auditability, Feedback, Explainability).

**Points communs GSE-One** — HUG a `decision_involvement: autonomous|collaborative|supervised` (3 niveaux, proches de SAFE-AI). Les 3 tiers de décisions (Auto/Inform/Gate) sont une expression opérationnelle.

**Points distinctifs** — SAFE-AI distingue explicitement "autonomous" vs "destructive" ; GSE a des guardrails Emergency pour le destructif mais pas de 4ᵉ niveau d'autonomie nommé.

**Bénéfice potentiel** — Ajouter un **niveau `destructive`** au spectre decision_involvement pour opérations irréversibles (rm -rf, prod deploy without review). *Clarification, pas refonte.*

### 3.12 Intent-Driven Development 2026 `[kodenerds-idd2026]` & AI-DLC `[aws-aidlc2025]`

**Description** — IDD 2026 : la qualité de la spec détermine le résultat ; 60/30/10 jugement produit / architecture / design. AI-DLC : Mob Elaboration + Mob Construction.

**Points communs** — Valorisation du planning (80/20 GSE). Section 13.3 Team Usage couvre déjà multi-user.

**Points distinctifs** — Les deux émergent côté collectif/mob ; GSE-One est centré **solo + AI**, team en extension.

**Bénéfice potentiel** — Patron **"Mob Review"** documenté pour `/gse:review` en team mode : co-revue par 2+ humains + devil-advocate agent (3ᵉ perspective). *Extension de Section 13.3, pas nouveau principe.*

### 3.13 Multi-agent research (MetaGPT, ChatDev, OpenHands, HyperAgent, SWE-agent, Agentless) `[hong-metagpt2024, qian-chatdev2024, yang-openhands2025, openhands-sdk2025, phan-hyperagent2024, yang-sweagent2024, xia-agentless2024]`

**Description** — Deux écoles : systèmes complexes (MetaGPT, ChatDev, OpenHands SDK — 72% SWE-Bench Verified) vs minimalistes (Agentless — 32% SWE-bench Lite sans orchestration).

**Points communs** — Orchestration de rôles, tests dans la boucle, staging explicite.

**Points distinctifs** — Recherche = systèmes *task-dedicated* (one-shot issue resolution). GSE = méthodologie ouverte multi-session + multi-sprint.

**Bénéfice potentiel** — (a) Pattern **Agentless-fallback** (commande `/gse:produce --agentless` minimaliste Localize→Repair→Validate quand le full lifecycle est overkill — équivalent renforcé du mode Micro existant). (b) Suivre l'OpenHands SDK de production pour patterns de sandboxing Docker.

### 3.14 Structured prompting — CoT, SCoT, Self-Refine, Reflexion, CodeAct `[wei-cot2022, li-scot2023, madaan-selfrefine2023, shinn-reflexion2023, wang-codeact2024, white-patterns2023]`

**Description** — Techniques de base des LLM, aujourd'hui universelles.

**Points communs** — Déjà utilisées implicitement par Claude/GPT/Gemini orchestrés par GSE.

**Points distinctifs** — Transverses.

**Bénéfice potentiel** — Documenter dans `docs/maintenance/prompting-techniques.md` quelle technique est employée où : Reflexion dans `/gse:review` (devil-advocate), SCoT dans `/gse:design`, CodeAct dans `/gse:produce`. Renforce la transparence et la traçabilité.

---

## 4. Nouvelle famille (v2) — Outillage & infrastructure adjacents

Le cycle 2 a identifié quatre sous-domaines où GSE a des équivalents pièce-par-pièce. Aucun ne propose une **intégration méthodologique** comparable — ils couvrent une tranche de la pile GSE.

### 4.1 PaaS auto-hébergés — concurrents de Coolify pour `/gse:deploy`

| Outil | Type | Positionnement vs Coolify `[coolify-paas2021]` |
|---|---|---|
| **Dokku** `[dokku-paas2013]` | CLI git-push + plugins | Plus léger, CLI-first, pas d'UI |
| **CapRover** `[caprover-paas2017]` | Docker Swarm + marketplace | Vitrine 1-click-apps ; failles connues (plaintext secrets) |
| **Dokploy** `[dokploy-paas2024]` | Docker multi-server | **Fastest-growing** 2024-2026 ; monitoring supérieur |
| **Easypanel** `[easypanel-paas2021]` | Freemium Docker | UI propre, templates |
| **Komodo** `[komodo-orchestrator2023]` | Orchestrateur Rust | Multi-host, graph-resource |
| **Dockge** `[dockge-docker-compose2023]` | docker-compose UI | Adjacent, pas full PaaS |

**Observation** — Aucun de ces outils ne s'intègre **nativement** à une méthodologie d'agents IA. Coolify est un choix *opinionated* défendable (50K+ stars, REST API documentée), mais **Dokploy mérite d'être surveillé** comme challenger direct.

**Bénéfice potentiel GSE-Two** — Factoriser `/gse:deploy` en backend pluggable (`deploy.provider: coolify | dokploy | dokku | fly | railway`) pour lever la dépendance mono-fournisseur. *Pas urgent, Coolify reste le meilleur défaut.*

### 4.2 ADR tooling — concurrents de `.gse/decisions.md`

| Outil | Type | Ce qui manque vs GSE Decision Journal |
|---|---|---|
| **adr-tools (Pryce)** `[pryce-adrtools2014]` | Bash CLI | Pas de consequence horizons, pas de link types typés |
| **Log4brains** `[vaillant-log4brains2020]` | Docs-as-code + web UI | Plus complet côté publication ; pas de risk dimensions |
| **MADR template** `[kopp-madr2017]` | Template markdown | Section Consequences libre (pas temporelle) |
| **AgenticAKM** `[agentic-akm2026]` | Recherche (4-agent AKM) | **Le plus proche** conceptuellement de GSE Decision Journal |
| **Context Strategies for ADR** `[context-strategies-adr2026]` | Recherche | Stratégies de contexte pour génération automatique |
| **Workik AI-ADR** | Prompt web gratuit | Génération one-shot, pas de cycle de vie |
| **Equal Experts "ADR buddy"** `[equalexperts-aiadr2024]` | Méthodologie | Pas d'outil |

**Observation forte** — **Aucun outil ADR public** n'implémente :
- les **horizons de conséquence** (Now / 3 mois / 1 an) avec confidence levels,
- les **6 dimensions de risque** + règle composite 3+ Moderate → Gate,
- les **4 link types typés** (`derives_from`, `implements`, `decided_by`, `related_to`) avec cohérence bidirectionnelle.

Le `.gse/decisions.md` est **réellement novateur** dans sa catégorie. Cela mérite une communication académique dédiée (FORGE 2026, RAISE).

**Bénéfice potentiel** — Publier un **micro-paper** (5-7 pages, FORGE 2026 ou AIware 2026 poster) décrivant uniquement le Decision Journal : le delta vs adr-tools/Log4brains est présentable en une section de Related Work serrée.

### 4.3 Health dashboards — concurrents du `/gse:health`

| Outil | Focus | Ce qui manque vs 8-dim GSE |
|---|---|---|
| **SonarQube / SonarCloud** `[sonarqube-sonarsource2008]` | Qualité + coverage + SCA | Pas de process signals (plan, decisions, traceability) |
| **Codacy** `[codacy-dashboard2012]` | Cloud quality + AI review | Pas de lifecycle coherence |
| **Code Climate** `[codeclimate-maintainability2011]` | Maintainability grade | Pas de sprint/lifecycle awareness |
| **DeepSource** `[deepsource-aiquality2019]` | AI-native quality score | Pas de lien artefacts↔decisions |
| **Qlty** `[qlty-codequality2024]` | Quality + analytics | Sucesseur Code Climate CLI |
| **Codecov** `[codecov-coverage2014]` | Coverage-focused | Une seule dimension |
| **LinearB** `[linearb-engineering2018]` | DORA dashboard | Git metadata seulement |
| **Jellyfish** `[jellyfish-engineering2017]` | Engineering investment | Management-level |
| **Swarmia** `[swarmia-devex2020]` | DORA + SPACE + DevEx | Team-wellness focus |

**Observation** — Les outils se scindent en deux : **code-artefact analyzers** (Sonar, Codacy, DeepSource, Qlty, Codecov) qui lisent le code ; **engineering analytics** (LinearB, Jellyfish, Swarmia) qui lisent les métadonnées Git/PM. **GSE-One est hybride** : il agrège des signaux **process** (plan health, complexity budget consumption, review findings open, trace density, AI integrity) + **code** (test pass rate, coverage via `test_evidence`) — via un dashboard HTML auto-régénéré hookable.

**Bénéfice potentiel** — Exposer `health.metrics` en format **Prometheus/OpenTelemetry** pour ingestion par Grafana/SigNoz : ajoute une **surface d'interop entreprise** sans complexifier le core. Non-bloquant, ajout R&D.

### 4.4 AI-PM & living plans — concurrents du `.gse/plan.yaml` vivant

| Outil | Année | Ce qui manque vs GSE plan.yaml |
|---|---|---|
| **Atlassian Rovo Dev + Agents in Jira** `[atlassian-rovo-jira-agents2026]` | 2026 | **Le plus proche** : assigner des tickets à des AI agents. Mais UI-cloud, pas file-native |
| **Atlassian Intelligence (Jira/Confluence)** `[atlassian-intelligence2025]` | 2025 | Smart summaries + NL→JQL ; pas de plan "vivant" Git-versionné |
| **Linear AI Triage + Linear Agent** `[linear-ai-agent2025]` | 2025 | Agent beta, MCP support natif ; cloud-only |
| **Notion AI + Agents** `[notion-ai-agents2025]` | 2025 | Planning docs, pas sprints |
| **ClickUp Brain + Autopilot** `[clickup-brain-autopilot2025]` | 2025 | Standups + Q&A AI ; pas de plan orchestrateur |
| **Asana Intelligence** `[asana-intelligence2024]` | 2024 | Project summaries AI |
| ~~Height AI~~ | (fermé sept 2025) | — |

**Observation majeure** — Aucun outil PM ne maintient un **plan.yaml agent-modifiable dans le dépôt Git**, tracé aux artefacts (REQ/DES/TST/DEC). Tous sont des SaaS-UI qui bolt AI onto a hosted DB. GSE-One a un **modèle architectural différent** : plan-as-code, vivable en offline, auditable, versionnable. C'est dans l'ADN de GSE : proche de Spec-Kit/OpenSpec pour les specs, appliqué au plan.

**Bénéfice potentiel** — (a) Documenter ce design choice comme **différenciateur architectural majeur** dans le pitch académique/commercial. (b) Pont bidirectionnel **`.gse/plan.yaml` ↔ Linear/Jira** via MCP : import initial + sync sélective, sans abandonner la source de vérité locale. *Commande `/gse:backlog sync --target=linear|jira`.*

---

## 5. V&V pour code IA — recherche active, GSE méthodologiquement en avance

Cycle 2 a inventorié les travaux 2024–2026 sur vérification/validation pour code LLM :

- **Formal verification de code LLM à partir de NL** `[formal-verification-llm2025]` — Formal Query Language pour intent vérifiable.
- **DafnyPro (POPL 2026)** `[dafnypro-popl2026]` — Claude Opus 4.5 + GPT-5.2 ensemble 98.2% annotation correctness.
- **Proof-Carrying Code Completions** `[kamran-pcc2024]` — PCC classique appliqué à la codegen LLM.
- **Meta ACH (FSE 2025)** `[meta-ach-mutation2025]` — mutation testing guidée LLM pour 10 795 classes Android.
- **Agentic Property-Based Testing (NeurIPS 2025)** `[agentic-pbt-neurips2025]` — agent autonome qui écrit des tests Hypothesis à partir des annotations de type.
- **PBT bridges LLM codegen and validation** `[pbt-bridges-llm2025]` — PBT comme complément validation manquant.
- **Standards-focused review of LLM assurance** `[standards-review-llm2025]` — mapping ISO/IEC 12207, 25010, 5055.

**Observation** — Ces travaux sont **outil-niveau** ou **technique-niveau**. **Aucun ne formalise la séparation V&V comme un principe de méthodologie**, avec test-types cartographiés (unit/integration = verification ; acceptance/E2E/visual = validation) et tracés bidirectionnellement. GSE-One le fait (Section 6.1 + `test_evidence` par TASK).

**Bénéfice potentiel** — Renforcer par :
- **Property-based testing** optionnel dans `/gse:tests` (Hypothesis Python, jqwik Java, fast-check TS) — tag `quality_gap: true` si activé pour un NFR de robustesse.
- **Mutation testing** optionnel post-sprint (mutmut, Stryker) pour évaluer la qualité des tests existants — sortie dans le health dashboard comme 9ᵉ dimension optionnelle.
- **Contract testing** (Pact `[pactflow-ai-contract2025]`) pour projets micro-services — extension du test pyramid "api" domain.

---

## 6. Requirements Engineering — GSE déjà au niveau de l'état de l'art

Cycle 2 a inventorié les outils RE + IA :

| Travail | Apport | Comparaison GSE reqs Step 0 + Step 7 |
|---|---|---|
| **Lima et al. — NFR with ISO 25010** `[lima-nfr-iso25010-2025]` | Pipeline LLM → 1 593 NFRs ISO 25010 | **Closest academic analog** ; 80.4% expert agreement |
| **LLMREI** `[llmrei-elicitation2025]` | Chatbot elicitation adaptatif | Couvre Step 0 conversationnel |
| **Jama Connect Advisor** `[jama-advisor2025]` | NLP ambiguity detection | Produit commercial, pas de matrice ISO |
| **IBM DOORS AI Assistant** `[ibm-doors-ai2025]` | watsonx.ai + DOORS Next | Produit commercial, pas de Given/When/Then auto |
| **Visure AI** `[visure-ai-rm2025]` | Traceability + inconsistency detection | Produit enterprise |
| **Acceptance Test Gen** `[acceptance-testgen-llm2025]` | User story → Gherkin → test | Couvre Step Given/When/Then |

**Observation** — GSE-One combine **dans une seule pipeline** (conversationnel Step 0 → formalisation REQ/NFR → check-list ISO 25010 Step 7 → quality coverage matrix persistée → Given/When/Then → validation tests). **Cette combinaison intégrée est rare** : Lima propose la matrice ISO mais ne persiste pas ; LLMREI est conversationnel mais pas ISO ; Jama/DOORS sont commerciaux mais pas Given/When/Then→tests.

**Bénéfice potentiel** — Publier la pipeline GSE reqs comme **retour d'expérience** dans une conférence RE (REFSQ, IEEE RE 2026) — c'est un angle académique fort.

---

## 7. Méthodologie auto-améliorante — le vrai différenciateur unique

Cycle 2 confirme : **`/gse:compound` Axe 2** (issue auto-créée sur repo GSE-One avec filtre "confirmé-utilisateur OU 2+ sprints observés") **semble être un first-mover en avril 2026**.

Comparaisons :

- **BMAD v6 Builder** `[bmad-v6-ecosystem2026]` — extensions pull-based manuelles, pas de télémétrie.
- **Spec-Kit community issues** `[github-speckit2025]` — triage manuel par vote.
- **GitHub Continuous AI for Accessibility** `[github-continuous-ai-a11y2026]` — parallèle architectural pour *produit*, pas méthodologie.
- **SAFLA** `[safla-selfaware2025]` — self-improvement pour agents, pas méthodologie.
- **Compound Engineering (Every)** `[compound-engineering]` — philosophie "chaque unité rend la suivante plus facile" mais sans mécanisme de retour vers mainteneurs.

**Conclusion** — Le pattern GSE "la méthodologie apprend de son usage et améliore sa propre spec via PR mainteneurs" est présentable comme **contribution originale**. À documenter en priorité dans un article de positionnement.

**Bénéfice potentiel** — Formaliser **un pipeline Axe-2→Triage→Spec-PR** côté maintainer : issues arrivent → classification (bug/suggestion/observation) → agrégation (quand ≥ N users rapportent la même chose, elle devient RFC) → PR sur `gse-one-spec.md` → regen du plugin. *C'est le système immunitaire de la méthodologie.*

---

## 8. Synthèse transversale — Matrice de positionnement v2

| Axe | GSE-One aujourd'hui (spec) | Concurrence la plus forte | Gap réel restant |
|---|---|---|---|
| **Lifecycle structuré** | 4 phases LC00-LC03 × 23 commandes × 9 catégories | Agentsway, BMAD-v6 (7 personas) | Aucun — GSE-One leader opérationnel |
| **Principes formalisés** | 16 P en 4 catégories avec mécanismes concrets | Hoda (valeurs), Navneet SAFE-AI (4 piliers) | Aucun — GSE-One plus riche |
| **Decision Journal + horizons** | `.gse/decisions.md` avec Now/3mo/1yr sur 6 dims + règle composite 3+ Moderate | adr-tools, Log4brains, AgenticAKM | **Aucun — GSE-One unique** ; à publier |
| **V&V distinction formalisée** | `/gse:tests` Section 6.1 Kind column | Lit. 2024-2026 (outil-niveau seulement) | **Aucun — GSE-One unique méthodologiquement** |
| **Health dashboard hybride** | 8 dims, HTML auto-regen, hooks | SonarQube (code) + LinearB (process) — jamais combinés | **Aucun concurrent hybride** ; exposer Prometheus |
| **Plan vivant file-native** | `.gse/plan.yaml` git-versionné, orchestrator-maintained | Linear Agent (UI beta), Rovo Dev Agents (UI) | **Aucun file-native** ; pont MCP↔Linear/Jira |
| **Safety backups git** | `gse-backup/` tags 30j avant destructif | — | — |
| **COMPOUND 3 axes** | Axe 2 = issue auto sur repo mainteneurs | — | **Unique — à publier** |
| **Portabilité cross-tool** | Claude Code + Cursor + opencode (mono-plugin) | AGENTS.md standard (passif) | Émission optionnelle AGENTS.md racine |
| **Spec-as-contract** | REQS Given/When/Then + config.yaml non-négociables | Spec-Kit, Kiro, Tessl (spec-centric) | Export GSE → Spec-Kit pack ; Spec Registry local |
| **Context engineering** | `.cursor/rules` + COMPOUND | Breunig (taxonomie), ACE (playbook) | Check-list Breunig dans `/gse:review` |
| **Benchmark public** | Aucun | SWE-bench, BigCodeBench | **Gap à combler** : run public |
| **Conformité ISO 5338** | Non mappée | ISO/IEC 5338:2023 | **Gap à combler** : livre blanc mapping |
| **RE pipeline ISO 25010** | Step 0 + Step 7 + Given/When/Then → tests | Lima, LLMREI (sous-ensembles) | **Aucun — GSE-One unique intégré** |

**Trois messages de la synthèse v2 :**

1. **GSE-One dépasse la concurrence sur 4 axes méthodologiques uniques** : Decision Journal avec consequence horizons, V&V formalisée, COMPOUND 3 axes (Axe 2 inédit), pipeline RE intégrée ISO 25010 → Given/When/Then → tests.
2. **GSE-One a une architecture unique** : plan-as-code + health hybride + state file-native, incompatibles avec les SaaS-UI PM mais alignés avec la vague spec-as-code (Spec-Kit, Tessl, OpenSpec).
3. **Les gaps réels à combler** sont : benchmark public (SWE-bench), mapping ISO 5338, et interop bidirectionnel avec outils externes (Linear/Jira/Prometheus).

---

## 9. GSE-Next — Vision d'évolution (v2 revue)

Les suggestions v1 qui **restent valides** :

- ✅ **Benchmark public GSE-on-SWE-bench / BigCodeBench** (gap réel) `[jimenez-swebench2023, zhuo-bigcodebench2024]`
- ✅ **Mapping GSE ↔ ISO/IEC 5338:2023** (gap réel) `[iso5338-2023]`
- ✅ **Émission AGENTS.md canonique** racine-projet en option (interop Codex/Devin/Factory)
- ✅ **Check-list Breunig** dans `/gse:review` (tag `[CONTEXT]`)
- ✅ **Merge-Readiness Pack** en sortie de `/gse:deliver` (inspiré SASE)

Les suggestions v1 à **retirer (déjà dans la spec)** :

- ❌ Ajouter `constitution.md` — `.gse/config.yaml + always_gate[]` le font déjà
- ❌ Sécurité-first dans TESTS — ISO 25010 Step 7 + dependency_audit + security-auditor agent existent
- ❌ Autonomy-tolerance dans HUG — `decision_involvement` existe (3 niveaux)
- ❌ Team-aware HUG — Section 13.3 implémente per-user profiles
- ❌ Tests de régression cross-sprint — `/gse:review` le fait déjà
- ❌ ACE cycle pour `/gse:compound` — les 3 axes GSE sont *plus sophistiqués* qu'ACE

### 9.1 Nouvelles évolutions (v2)

Onze évolutions prioritaires identifiées après la lecture de la spec + cycle 2 :

1. **Publication académique du Decision Journal** (Q3 2026) — Micro-paper FORGE/RAISE : "Consequence-Horizon Decision Records for AI-Augmented SE". Met en valeur l'unicité du `.gse/decisions.md`.

2. **Publication académique de la pipeline RE intégrée ISO 25010** (Q4 2026) — REFSQ/IEEE RE : Step 0 → Step 7 → Given/When/Then → validation tests comme retour d'expérience.

3. **Publication académique de COMPOUND Axe 2** (Q1 2027) — Pattern "Methodology Self-Improvement via Filtered User Telemetry" (FSE, AIware, ou EASE).

4. **Run public SWE-bench Verified + BigCodeBench** (Q2 2026) — Configurations Micro/Lightweight/Full × Claude Opus 4.7 / Sonnet 4.6 / GPT-5. Rapport technique dans `docs/benchmarks/`.

5. **Livre blanc GSE ↔ ISO/IEC 5338:2023** (Q4 2026) — Mapping LC00-LC03 ↔ processus standards (Data Process, Verification, Validation, Configuration Management, Risk Management). Ticket d'entrée dans les adoptions entreprise régulées.

6. **Pont MCP `/gse:backlog sync --target={linear|jira}`** (Q3 2026) — Import/export bidirectionnel sans abandonner `.gse/backlog.yaml` comme source de vérité. Référence : Linear MCP native `[linear-ai-agent2025]`.

7. **Export Prometheus/OpenTelemetry du health score** (Q3 2026) — Endpoint métriques, dashboard Grafana template. Aligne GSE sur l'observabilité SRE sans complexifier le core.

8. **Backend deploy pluggable** (Q4 2026) — `config.yaml → deploy.provider: coolify | dokploy | fly | railway | dokku`. Lève la dépendance mono-fournisseur. Référence : `[dokploy-paas2024]` comme next-gen Coolify.

9. **Check-list Breunig dans `/gse:review`** (Q2 2026) — Détection poisoning/distraction/confusion/clash, tagué `[CONTEXT]`. Ajout léger, impact pédagogique fort.

10. **AGENTS.md canonique optionnel** (Q2 2026) — Flag HUG `emit_agents_md: true`. Par défaut off (étude ETH Zurich sur dégradation). Référence : `[agentsmd-standard2025]`.

11. **PBT + Mutation testing en options** (Q1 2027) — `/gse:tests --pbt` (Hypothesis/jqwik) + 9ᵉ dimension health "test quality" (mutation score). Références : `[agentic-pbt-neurips2025, meta-ach-mutation2025]`.

### 9.2 Évolutions R&D (horizon 2027+)

12. **`/gse:tune` optionnel** (Agentsway-inspired) — fine-tuning léger / few-shot adapters de l'orchestrator à partir de l'historique projet. Dépendance : fournisseur LLM avec API fine-tuning.

13. **Spec Registry local façon Tessl** — Cache versionné de signatures d'API externes, consulté par security-auditor pour bloquer les hallucinations (P15 verification gates).

14. **Meta-lifecycle pour les skills du plug-in** (Promptware Engineering-inspired) — Chaque modification de skill déclenche REVIEW + entrée maintenance. Governance du plug-in lui-même.

15. **Mode "agent-first code"** (Ustynov-inspired) — `.gse/skeletons/` denses consommés par l'agent en Full autonomous. Expérimentation.

### 9.3 Feuille de route des versions

| Version | Thème | Éléments clés | Horizon |
|---|---|---|---|
| **v0.7.x (courant)** | Spec alignment | 23 commandes, opencode target, spec 2956 lignes | S1 2026 |
| **v0.8** | Publications & interop | Decision Journal paper, AGENTS.md canonique, Breunig check-list | Q2-Q3 2026 |
| **v0.9** | Observabilité & interop externe | Prometheus export, pont MCP Linear/Jira, deploy pluggable | Q3-Q4 2026 |
| **v1.0 (GSE-One stable)** | Normatif & benchmark | Mapping ISO 5338, run SWE-bench public, Merge-Readiness Pack | Q1 2027 |
| **v1.x** | PBT/Mutation, Spec Registry | 9ᵉ dim health, Tessl-like cache | S1-S2 2027 |
| **v2.0 (GSE-Two)** | Fine-tuning, agent-first code | `/gse:tune`, skeletons, meta-lifecycle | 2027+ |

### 9.4 Critères de succès GSE-Two

- **≥ 5 publications académiques** citant GSE-One (FORGE, AIware, FSE, RAISE, REFSQ, ou ICSE).
- **≥ 50 000 installations** plug-in cumulées (Cursor + Claude Code + opencode).
- **Run public SWE-bench** avec score dans le top 30 % sur Verified.
- **Mapping ISO/IEC 5338** avalisé par un comité ou cité par un cabinet (McKinsey, ThoughtWorks, Gartner).
- **≥ 3 intégrations bidirectionnelles** (Linear, Jira, Prometheus minimum).
- **≥ 1 retour de terrain ayant provoqué une mise à jour de la spec via Axe 2** (preuve de vie du cycle auto-amélioration).

### 9.5 Ce qui ne doit **pas** bouger

- **La règle 80/20** (socle pédagogique).
- **Le mono-plug-in + portabilité cross-tool** (différenciateur architectural).
- **Les 16 principes** (spec normative).
- **Le caractère file-native** du state (plan.yaml, decisions.md, backlog.yaml) — pas de SaaS-ification.
- **Le beginner output filter** (entrée pédagogique unique au-delà de 10 ans+).

---

## 10. Bibliographie — Index des ajouts

Tous les `[keys]` cités dans ce document pointent vers `modules/shared-blocks/static/references.bib`. Les sections ajoutées par cycle :

**Cycle 1 (v1, 80 entrées)** — Named methodologies & manifestos · AI-Native SE academic frameworks · Multi-agent SE frameworks · Prompting & agent techniques · Requirements engineering + GenAI · Human-AI collaboration · Benchmarks · Surveys · AI IDE tools & coding agents · Methodology plugins & workflow systems · Agent orchestration frameworks · MCP-based ecosystems · Industry frameworks, governance, standards.

**Cycle 2 (v2, ~40 entrées)** — Agent platforms (opencode) · Self-hosted PaaS · ADR tooling (adr-tools, Log4brains, MADR, AgenticAKM, Context Strategies for ADR) · Code quality dashboards (SonarQube, Codacy, DeepSource, Qlty, Codecov, LinearB, Jellyfish, Swarmia) · AI-PM (Atlassian Rovo/Intelligence, Linear, Notion, ClickUp, Asana) · Requirements AI tools (Lima-NFR-ISO25010, LLMREI, Jama Advisor, IBM DOORS AI, Visure, standards review) · V&V for AI code (DafnyPro POPL 2026, Formal Verification from NL, PCC Completions, Meta ACH mutation, Agentic PBT NeurIPS 2025, PBT bridges LLM) · Methodology self-improvement analogues (GitHub Continuous AI a11y, SAFLA, BMAD V6 Ecosystem).

**Total** : ~140 entrées. Révision semestrielle planifiée.

---

## 11. Annexes

### 11.1 Veille active (avril 2026 → octobre 2026)

- **Microsoft Agent Framework 1.0** `[msft-agentfw2026]` (GA 3 avril 2026) — potentiel standard d'entreprise ; impact target-matrix GSE.
- **Dokploy** `[dokploy-paas2024]` — challenger Coolify à surveiller pour backend `/gse:deploy` pluggable.
- **Linear Agent GA** `[linear-ai-agent2025]` — si stabilisé, pont MCP à prioriser.
- **Atlassian Rovo Dev Agents** `[atlassian-rovo-jira-agents2026]` — le plus proche analog "AI-maintained plan".
- **ETH Zurich AGENTS.md study (mars 2026)** — leçon déjà intégrée : fichiers de contexte auto-générés peuvent dégrader.

### 11.2 Conventions de maintenance

- Mise à jour **semestrielle minimum** alignée sur releases GSE majeures.
- Nouvelles entrées BibTeX par famille (respecter les sections).
- Chiffres datés (ex. "60K+ repos AGENTS.md") → ajouter `note = {... Consulted April 2026.}`.
- URLs Github vérifiées à chaque passe ; arXiv remplacés par versions publiées si disponibles.
- **v1 archivée** via git — lire le diff de commit pour historique des corrections.
