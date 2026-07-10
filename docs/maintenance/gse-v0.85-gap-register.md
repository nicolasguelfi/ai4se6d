# Registre d'écarts — alignement du support AI4SE sur GSE-One v0.85.0

- **Date** : 2026-07-10
- **Branche** : `align-gse-one-v0.85.0`
- **Corpus de référence** : dépôt `gensem` @ VERSION 0.85.0 ; depuis le 2026-07-10 **v0.85.1** (unique changement : correction du nom Generic → Generative, décidée en Q16 — la lecture seule a été levée ponctuellement pour ce fix, pipeline complet exécuté)
- **Méthode** : vérification exhaustive par 11 agents parallèles (un lot thématique chacun).
  Chaque verdict a été rendu après lecture du bloc du support ET du/des fichiers corpus
  correspondants (spec `gse-one-spec.md`, `gse-one/src/activities|agents|principles|templates/`).
  CHANGELOG et rapports post-audit utilisés comme guides seulement. Vérifications-clés
  contre-vérifiées par l'orchestrateur (nom officiel, 24 commandes, 11 agents, HUG 13 dim).
- **Baseline du support** : enseigne v0.20.4 + postscript jusqu'à v0.60.1 → ~43 releases d'écart.

## 0. Totaux globaux

| Lot | EXACT | PÉRIMÉ | À VÉRIFIER |
|---|---|---|---|
| T2 commandes/philosophie (9 blocs) | 79 | 20 | 2 |
| T3 découverte/plan (10 blocs) | 72 | 18 | 1 |
| T4 décisions/git (5 blocs) | 32 | 16 | 2 |
| T5 requirements/CalcApp (14 blocs) | 38 | 24 | 7 |
| T6 ingénierie (10 blocs) | 73 | 34 | 4 |
| T7 delivery (8 blocs) | 46 | 16 | 8 |
| T8 plugin/modes (9 blocs) | 37 | 35 | 8 |
| Postscript recap v0.60 (1 bloc, 16 slides) | 54 | 9 | 5 |
| Pratiques P1-P8 + méthode + CE (27 blocs) | 78 | 24 | 12 |
| Glossaire/périphérie (11 fichiers) | 38 | 17 | 7 |
| Conceptuel SDLC/évidence/frameworks (41 blocs) | 13 | 1 | 1 |
| **TOTAL** | **≈560** | **≈214** | **≈57** |

Gravité des PÉRIMÉ : ~35 **haute** (comportement faux enseigné), ~90 moyenne (chiffre/vocabulaire), reste basse.

---

## 1. Écarts transverses (candidats au lot mécanique groupé)

| # | Écart | Valeur v0.85.0 (source corpus) | Fichiers touchés |
|---|---|---|---|
| M1 | « 23 commands » / « 12 categories » / liste sans `/gse:audit` | **24 commandes, 9 catégories** (spec §3, Appendix A « Total: 24 commands ») | t2_commands, glossary, title, book.py (commentaires), plugin_architecture, t8_advanced |
| M2 | « 9 agents » / « 8 + 1 Orchestrator » / « 8 specialists » | **11 agents = 10 spécialisés + 1 orchestrateur** (+ coach, deploy-operator ; spec §1.6) | t2_commands, glossary, title, book.py, plugin_architecture, plugin_cursor, t8_advanced |
| M3 | HUG « 11 dimensions » / « Human Understanding Gathering » | **13 dimensions**, « Human **User Grounding** » (spec §3.2.1, §16) | glossary, t2_commands, t2_philosophy (×2), ce_five_phases |
| M4 | ~~GSE-One = « Generative Software Engineering One »~~ **[INVERSÉ 2026-07-10]** — c'était le CORPUS qui était fautif depuis son commit initial (« Generic » = glissade de rédaction). L'auteur du concept confirme : GSE = Generative Software Engineering, GSE-One = première instanciation. Corpus corrigé en **gensem v0.85.1** (5 occurrences + régénération, tag poussé) ; support restauré (« Generative … first instantiation ») dans glossary, shared_glossary, gse-competitors-sota.md. Leçon : l'alignement mécanique sur une source ne vaut que si la source porte l'intention de l'auteur. | glossary, shared_glossary, gse-competitors-sota.md ; corpus gensem |
| M5 | « GenSEMOne » (variante Cursor-native inexistante) | **GSE-One** (le terme GenSEMOne n'existe pas dans le corpus) | shared_glossary (définition fausse — gravité haute), session_map (×2, orphelin), day5_bridge (orphelin), method_checklist (étiquette) |
| M6 | « 19 templates », « 57 files total », « 17 lifecycle events/hooks » | **29 templates** (28 + MANIFEST), inventaire « 57 » caduc, **3 hooks système + 7 agent behaviors** (spec §1.1.4, §P13) | plugin_architecture, t8_advanced, plugin_cursor |
| M7 | Chemin rapports de campagne `docs/sprints/sprint-NN/tests/TCP-NNN.md` | `docs/sprints/sprint-NN/test-reports/campaign-{YYYY-MM-DD}-{TASK-ID}.md` ; `campaign_ref` = chemin complet (spec §6.3 step 4, §12.3) | t6_cmd_tests, t6_test_run, t6_test_evidence, t6_cmd_produce |
| M8 | IDs « FR-001 » / « NFR-002 » + champ « Test file » | **REQ-001..099** (functional) / **REQ-101..199** (non-functional) ; lien via `traces.tested_by` (templates/sprint/reqs.md) | calcapp_fr_example, calcapp_nfr_example, calcapp_v03_overview, calcapp_discussion, practice_p5 |
| M9 | Requirements « output of /gse:assess » | Produits par **`/gse:reqs`** ; `/gse:assess` = gap analysis (activities/assess.md, reqs.md) | calcapp_fr_example (l.48), calcapp_nfr_example (l.41), ce_brainstorm_plan (l.34) |
| M10 | « Tests/docs/renames = free (0 pt) » | Règle **abrogée** : Cost Assessment Grid, 0/1/2-5 pts au cas par cas (spec §8.1 + Appendix B) | t3_discovery (l.151, 172), t2_agile_bridge (l.60) |
| M11 | Artefact fantôme `.gse/inventory.yaml` (sortie + input d'assess) | Scan COLLECT **éphémère** (console) ; seul `.gse/sources.yaml` persiste ; ASSESS re-scanne inline (spec §4.1, §4.7.1) | t3_cmd_collect (l.31, 61, 35), t3_cmd_assess (l.32) |
| M12 | Pyramide de tests sans colonne **Policy** ; chiffres domaines | Policy 5 % partout, Unit réduit de 5 pts sur 7 domaines ; web = 20/20/30/20/5/5 (spec §6.1) | t6_engineering (l.43, 93-94, 107-119), t6_cmd_tests (l.50) |
| M13 | Review « 5/6 perspectives », « 3 reviewers » ; « HIGH seul bloque » | **6 sous-agents parallèles + devil's advocate = 7 perspectives** (test-strategist manquant) ; **HIGH ET MEDIUM** exigent /gse:fix avant DELIVER (review.md Steps 2a-2f, 3, 6) | t6_engineering, t6_cmd_review, t6_test_review_tiers (l.47), ce_review_nversion |
| M14 | « 6 Foundation Principles (P1-P6) » | Foundations = **5** principes (P1, P2, P3, P5, P6) ; P4 est en « Risk & Communication » (spec §2) | t2_philosophy (l.81-84), book.py (commentaire l.167) |
| M15 | « Visual test = verification » | Visual = **validation** (trace REQ- UI ; spec §6.1, §1.5) | t6_vv (l.40, 59) |
| M16 | Sous-facteurs git-hygiene : « worktree count, naming compliance, backup freshness » | 6 réels : Active branches 20 / Stale 20 / Uncommitted 20 / **Merge conflicts 20** / Main status 10 / **Unreviewed branches 10** (spec §7.4) | t7_cmd_health (l.49) |
| M17 | « /gse:deploy warns if health < 5 before deploying » ; « 5 étapes » | Ce warn **n'existe pas** dans deploy (seulement avant /gse:deliver et pendant review) ; pipeline = **6 phases** (Setup en tête) (deploy.md) | t7_cmd_deploy (l.37-38, 43) |
| M18 | Flag `/gse:plan --interactive` | **Inexistant** — options : `--strategic` / `--tactical` / `--help` (plan.md) | t2_philosophy (l.408) |
| M19 | 7 signaux de complexité (mauvais noms) + pré-filtre « <3 files » | Signaux : dependencies, persistence, entry points, multi-component, existing tests, CI/CD, git maturity ; pré-filtre Micro = pas de manifest ET pas de git ET ≤2 fichiers source ; règle Full contractuelle first-match-wins (spec §13.2, §14.3 Step 6) | t8_modes (l.70-75), t2_philosophy (l.360) |
| M20 | Ordre « PRODUCE → TESTS » | **TESTS (stratégie) précède PRODUCE** ; exécution post-code via le run canonique (spec §14 LC02) | practice_p6 (l.38), practice_p8 (l.130) |
| M21 | Weighted average du health score ; « 8 dimensions » sans nuance | **Moyenne simple** des dimensions actives ; affichage mode-aware : 8 Full / 3 Lightweight / 0 Micro (health.md Step 2, spec §13.2) | t7_cmd_health (l.44, titre), t7_delivery (l.124), t2_cmd_status (enrichissement) |
| M22 | Lightweight : « Auto + Gate only », « Hard guardrails », « Plan artifact only », « skips to IMPL » | Inform conservé (notices) ; REQS Hard mais TESTS Soft ; artefact sprint = **reqs.md only** ; pas de tier IMPL mais **Minimal Integrity Pass** au DELIVER Step 1.6 (spec §13.2 ; deliver.md) | t8_modes (l.30-37), t2_philosophy (l.362), t6_test_review_tiers (l.73) |
| M23 | Divers petits : « §D »→§6.5 ; scope commit 3→2 segments ; numérotation steps produce ; « --deep-review = all three » ; « findings → backlog »→review.md ; catégorie assess « missing »→« Uncovered » ; « LC02a »→LC02 ; Step 0→0.5 (reqs) ; enum frontmatter `plan`→`plan-summary` (+test-campaign) ; 4→7 types de traces / 12 préfixes | (voir tables des lots) | t6_test_review_tiers, t6_engineering, t6_cmd_produce, t6_cmd_review, t3_frontmatter, t5_requirements, t5_cmd_reqs |

## 2. Écarts nécessitant une décision individuelle (non mécaniques)

| # | Sujet | Problème | Fichiers |
|---|---|---|---|
| P-GITPROFILES | Slide « 3 Git workflow profiles A/B/C » + « Future commands » | Taxonomie A/B/C inexistante en v0.85.0 (remplacée par `git.strategy` worktree/branch-only/none × modes) ; les 6 « commandes futures » (/gse:sync, /gse:pr, /gse:merge, /gse:handoff, /gse:status --team, /gse:review --pr) n'apparaissent nulle part, ni comme futures ; support équipe réel = spec §13.3 + `/gse:hug --team`. Réécriture structurelle. | ce_git_profiles, ce_git_mapping (lignes Compound→tag = DELIVER) |
| P-GUARDRAILS-WORK | Slide « scope enforcement temps réel + test-first » | Modèle remplacé : stratégie de tests avant PRODUCE, exécution après ; Scope Reconciliation à la clôture (Gate 4 options), pas de blocage fichier-par-fichier. | ce_work_guardrails, ce_work_review (inputs PR/URL, perspective « learning ») |
| P-P13 | Contenu des 2 catégories de hooks | Les 3 hooks système réels : protect-main (Hard), block force-push incl. +refspec (Emergency), review-findings-on-push (Soft) ; les 7 agent behaviors réels ≠ listes du deck. | t4_decisions (l.248-249, 261, 265) |
| P-PREVIEW | Variante scaffold-as-preview absente | v0.85.0 : Gate Step 1.5 choisit static OU scaffold exécutable (recommandé web/mobile → CalcApp) qui devient la base de PRODUCE. | t5_cmd_preview, t5_requirements (l.111) |
| P-CURSOR-CMDS | Forme des commandes dans les exercices | Sous Cursor/opencode : `/gse-go` (tiret) ; `/gse:go` = Claude Code plugin / Gemini (README §Commands). Tous les P1-P8 disent Cursor + `/gse:`. Décision : forme tiret, ou changer le runtime des exercices. | practice_p1..p8 (toutes invocations) |
| P-MODE-FULL | Pratiques P3/P5/P6/P7 supposent le mode Full | Sur CalcApp vide, /gse:go recommandera Micro/Lightweight ; COLLECT/ASSESS, DESIGN/PREVIEW, REVIEW, COMPOUND, budget, 8 dimensions n'existent qu'en Full. Ajouter la consigne « choisir Full à la Gate de mode ». | practice_p3, p5, p6, p7 (briefings) |
| P-CE-VOCAB | **[RECTIFIÉ 2026-07-10 puis TRAITÉ Q6]** Compound Engineering (CE) est une méthodologie externe réelle (plugin officiel `EveryInc/compound-engineering-plugin`, « parent idéologique direct » de GSE-One selon le doc SOTA §3.6). Les `/ce:*`, « 5 phases », 80/20 appartiennent à CE — **faux positifs** vis-à-vis de GSE-One pour les blocs SOTA. Écarts réels traités : attributions CE→GSE-One sur les blocs câblés (80/20 ≠ Design Philosophy 7 piliers ; « 5-phase » ≠ lifecycle 4 étapes ; 4 outputs CE mappés sur les 3 axes). Blocs SOTA orphelins rafraîchis contre l'upstream Every (6 phases dont Simplify, `/ce-<skill>`, `/ce-code-review`, 29 skills/0 agent). Bib `[compound-engineering]` réparée (ancienne URL 404). | ce_philosophy, ce_8020_example, method_vs_vibecoding, ce_compound, t8_advanced, ce_transition, ce_demo_preview, ce_brainstorm_antipattern, ce_toolsupport, ce_work_review, references.bib, gse-competitors-sota.md |
| P-TOOLSUPPORT | **[RECTIFIÉ — fusionné dans P-CE-VOCAB]** `ce_toolsupport` décrit le plugin CE (10+ outils = fait CE exact), pas GSE-One — faux positif. Rafraîchi contre l'upstream Every (liste de plateformes réelle, installation native, manifests vérifiés). Les cartes cross-tool de `t8_advanced` (bloc câblé GSE-One) ont été réattribuées : opencode primaire + Codex/Gemini expérimentaux. | ce_toolsupport, t8_advanced |
| P-INSTALL | Commandes d'installation inexistantes | « gse install --target … » et « gse sync » n'existent pas : `curl …/install.sh \| sh` ou `python3 install.py --platform … --mode …`. | t8_advanced (l.45-46), plugin_architecture (l.91-106) |
| P-SPECIALIZE | « 5 types de spécialisation » / « 4 steps variant » | Mécanismes absents du corpus ; customisation réelle = `.gse/config.yaml` (spec §13.1-13.3). Réécriture ou re-cadrage « proposition du cours ». | ce_specialization, ce_spec_5types, t8_advanced (l.82) |
| P-RECAP | Postscript v0.20.4→v0.60.1 | 9 écarts internes (dont : « Three Platforms »→5 ; `_LOCAL/audits/`+`latest.md`→`audit.json` ; Sprint Freeze 4→8 activités ; option « Auto » du Gate git identity inexistante ; « every guardrail can be overridden » faux pour Emergency ; 30→28/29 templates) + **trou de couverture v0.60.1→v0.85.0** (43 releases, 10 thèmes majeurs identifiés — cf. §4). Décision : corriger + second postscript, ou refondre. | recap_v060, book.py (commentaire) |
| P-GLOSSARY | Lacunes du glossaire | Aucune entrée Sprint, Spike, Decision tier, Mode — devenus « Essential Concepts » v0.85.0 (sprint/spike **complexity-boxed**, spike ≤3 pts, tiers, modes, domaine 9 valeurs). | glossary |
| P-ORPHANS | Blocs orphelins | session_map et day5_bridge ne sont pas référencés dans book.py (et citent GenSEMOne). Corriger ou supprimer ? | session_map, day5_bridge |
| P-BRAND | Titre du module | `page_title` « GSE-One — Generative Software Engineering » vs expansion officielle « Generic ». Choix éditorial (titre de cours vs exactitude). | book.py, title, collection.toml, intro_roadmap |
| P-CREATIVITY | Affirmation invérifiable | « /gse:review explicitly checks for creative diversity » — aucune trace corpus ; reformuler vers P16 (devil's advocate, alternatives non considérées). | human_creativity (l.32) |
| P-METHOD-LABEL | Checklist GenSEMOne étiquetée « GSE-One workflow » | Le Step 0-5 manuel (`.cursor/rules`, `docs/requirements.md`) n'est pas le workflow GSE-One (LC00-LC03). Ré-étiqueter. | method_checklist |
| P-FLYWHEEL | Chiffres illustratifs incohérents | t7_delivery (Sprint 1→10 règles…) vs ce_compound_flywheel (Cycle 3→10…) — séries décalées ; hors corpus, à harmoniser. | t7_delivery (l.83), ce_compound_flywheel |
| P-COMPOUND-FILTER | Filtre Axe 2 « 2+ sprints » | Remplacé : concret + groupé par thème + dédupliqué + cap 3/sprint + Gates (compound.md 2.3-2.5). | t7_cmd_compound (l.32, 54) |
| P-DELIVER-NEW | Nouveautés DELIVER non enseignées | Delivery Map (Step 0.0), guardrails test-evidence bloquants (Step 1.5, §9.3.1), integrity pass Lightweight (Step 1.6). Enrichissement optionnel. | t7_cmd_deliver, t6_test_review_tiers |
| P-ENRICH | Enrichissements optionnels divers | Pause Commit Gate ; resume Step 0 + git_state.head/clean ; Sprint Freeze (task Step 0) ; Root-Cause Discipline (fix) ; requirements-analyst pass (reqs 7.5) ; Shared State (design 2.5) ; OQ Gate Step 0 ; cross-cutting + AUDIT/BACKLOG/DEPLOY ; statuts backlog 9 symboles ; plan.yaml schéma (complexity entier, completed objets, preview) ; UX Heuristic Pass. | t2_cmd_pause_resume, t2_cmd_task, t6_cmd_fix, t5_cmd_reqs, t5_cmd_design, t2_philosophy, t2_cmd_status, ce_plan_artifact, ce_plan_summary, t5_cmd_preview |

## 3. À VÉRIFIER MANUELLEMENT (~57 items)

- **Images IA / logos / vidéo** (16 blocs `st_image`) : vérifier que les visuels (lifecycle 4 étapes, pipeline hexagonal, logos GSE) reflètent les contenus corrigés.
- **Données d'atelier CalcApp** (78 tests, 9 exigences, timings, features 2-8 pts) : hors corpus, cohérence interne à contrôler.
- **Jugements éditoriaux** (tableaux comparatifs frameworks, « Learning Low », stats analystes Gartner/Bain/McKinsey/Forrester) : choix d'auteur.
- **Timers et logistique** des pratiques (45 min, horaires handover).
- **Recap** : « +40 releases », « ~76 corrections / 5 faux positifs », « 6 aligned enums », fenêtre « v0.51→v0.60 », libellés des 9 clusters (recouvrement partiel avec le rapport corpus).

## 4. Trou de couverture du postscript (v0.60.1 → v0.85.0, 43 releases)

Thèmes majeurs à couvrir si le postscript est étendu (SUGGESTIONS issues du CHANGELOG, à re-vérifier au moment de la rédaction) :
1. 2 plateformes secondaires : Codex CLI + Gemini CLI (v0.72.0), orchestrateur-lite.
2. Installeur `curl | sh` + modes local/sandbox (v0.62.7, v0.73, v0.74, v0.80) ; fixes installeur v0.85.0.
3. Refonte audit : `_LOCAL/audit/audit.json` + backlog durable (v0.75.0, v0.85.0).
4. Réparation de la couche hooks (CLAUDE_TOOL_INPUT → stdin-JSON, v0.63.0) ; +refspec fermé (v0.85.0).
5. Sprint Freeze étendu à 8 activités (v0.63.0).
6. Intégrité renforcée : counters.py, DA isolé, delivery-integrity, P15 escalade (v0.66-0.70, v0.82, v0.85).
7. P8 anti-framing : « Excluded alternative » obligatoire (v0.68.0).
8. Déploiement privé GitHub App + formation (v0.62.3, v0.64.0, v0.85.0).
9. Feedback cohorte DAY06 : Delivery Map, Open Items, version deployée (v0.62.6).
10. Trains de méta-audit v0.62.8 et v0.84.0 (126 findings, 0 faux positif) ; tests 72→125.

## 5. Suivi de traitement (Phase 3)

| Lot / Problème | Statut | Commits |
|---|---|---|
| Lot mécanique M1-M23 (Q3) | ✅ traité en 4 passes + 1 correctif | `1c0d593`, `1aeecb4`, `680ca69`, `b0a8e2a`, `9c8a4e5` |
| Correctif GenSEMOne | ✅ GenSEMOne = méthode manuelle du cours (pas un alias de GSE-One) ; entrée glossaire rétablie et clarifiée | `9c8a4e5` |
| P-CURSOR-CMDS (Q4) | ✅ encart « Command form » P1 + rappels P2-P8 (forme tiret Cursor) | `1a17394` |
| P-MODE-FULL (Q5) | ✅ consigne « choose Full » P1 + prérequis P3/P5/P6/P7 | `39306e9` |
| P-CE-VOCAB + P-TOOLSUPPORT (Q6, rectifiés) | ✅ réattributions CE↔GSE-One + rafraîchissement SOTA upstream + bib | `2f9ecd0` + commit SOTA |
| P-GITPROFILES (Q7) | ✅ slides git réécrites : stratégies × modes, commandes fantômes supprimées | `5966f7a` |
| Lot 2 quasi-mécanique (Q8) | ✅ P-P13, P-INSTALL, P-CREATIVITY, P-COMPOUND-FILTER, P-METHOD-LABEL, P-FLYWHEEL | `96c09c6` |
| P-GUARDRAILS-WORK (Q9) | ✅ slide réécrite « strategy before, reconciliation after » | `4ddf0a9` |
| P-PREVIEW + P-GLOSSARY (Q10) | ✅ scaffold-as-preview + 4 entrées Essential Concepts | `f029f3d` |
| Analyse pureté méthodologie (Q11) | ✅ rapport `gse-methodology-purity-findings.md` (gensem intact) | `e7b6a2d` |
| P-SPECIALIZE (Q12, reformulé « fork ») | ✅ deux voies : configurer (config.yaml) / dériver (fork outillé) | `cd3a350` |
| P-RECAP (Q13 puis DÉCISION FINALE) | ✅ **postscript supprimé** — principe : les formations se font toujours sur la dernière version, aucun récapitulatif inter-versions ni référence aux versions antérieures du plugin dans le support (le postscript consolidé v0.20.4→v0.85.0 de `4fc7f54` a été retiré ; contenu récupérable dans git). Les v0.x restants dans le deck = versions de l'app CalcApp (atelier), pas du plugin | `4fc7f54` puis suppression |
| P-BRAND (Q15) | ✅ ABANDONNÉ — sa prémisse était l'erreur de nommage du corpus ; les titres « Generative Software Engineering » étaient justes | — |
| Nommage GSE (Q16, réponse 3) | ✅ corpus gensem corrigé et **release v0.85.1** publiée (Generic → Generative, 5 sources + régénération 5 plateformes, 125 tests verts, tag poussé) ; support restauré avec la sémantique « first instantiation » ; M4 inversée | gensem `34c7a39` + commit support |
| P-ORPHANS (Q14) | ✅ statu quo : session_map et day5_bridge restent en réserve (non câblés, corrects, réutilisables pour un format multi-jours) | — |
| P-DELIVER-NEW/P-ENRICH (Q17, réponse 3) | ✅ enrichissement ciblé : guardrails test-evidence de DELIVER (Step 1.5, §9.3.1) + Sprint Freeze de /gse:task (Step 0) ; phrase non attestée « l'orchestrateur suggère un spike » retirée. Autres enrichissements (Pause Commit Gate, resume git_state, Root-Cause Discipline, reqs 7.5, Shared State, 9 statuts, UX Pass) volontairement laissés au registre pour une itération future | commit Q17 |

## 6. Détail par lot (extraits PÉRIMÉ — voir rapports d'agents pour les tables complètes)

Les tables complètes (y compris items EXACT) sont dans les transcripts des 11 agents de vérification
de la session du 2026-07-10. Ce registre reprend l'intégralité des écarts actionnables en §1-§2 ;
les gravités et lignes exactes y figurent. Résumé des blocs les plus touchés :

- `t8_modes`, `plugin_architecture`, `t8_advanced`, `ce_toolsupport` : lots T8 — le plus périmé (35 écarts).
- `t2_philosophy` : 8 écarts (Foundations, HUG, signaux, Lightweight, --interactive, FIX/skipped, cross-cutting).
- `t6_engineering`, `t6_test_review_tiers` : pyramide Policy, perspectives, conditions de blocage.
- `ce_git_profiles`, `ce_git_mapping`, `ce_work_guardrails` : modèles structurellement remplacés.
- Blocs **entièrement conformes** (0 écart) : t2_cmd_go, t2_cmd_status, t2_cmd_pause_resume, t6_cmd_fix, t7_cmd_integrate, ce_plan_living, ce_plan_antipattern, practice_p2/p3/p4/p7 (à la forme des commandes et au mode près).
