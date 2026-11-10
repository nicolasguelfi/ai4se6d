# Fiche des sources — jour 2 (édition 2)

Décision `peda1` P9 : chiffres **mis à jour à la source** + cette fiche formateur.
Cette fiche recense **tous les chiffres affichés dans le module `ai4se6d_day2`**, avec la source et la date
**telles que citées dans les blocs** (clé BibTeX dans `modules/shared-blocks/static/references.bib`).
Rédigée le 2026-11-09 à partir des blocs et de la bibliographie : les URL n'ont **pas** été rouvertes pour cette fiche
(colonne « Consulté » = « — ») ; à vérifier à la source avant le 26/11.

Statuts : **vérifié** (chiffre conservé, source confirmée) · **mis à jour** (chiffre ou libellé corrigé) ·
**retiré** (affirmation non vérifiable, supprimée ou reformulée) · **à vérifier** (repris de la bibliographie, source non rouverte).

## Module `ai4se6d_day2`

| Diapositive (fichier) | Chiffre / fait affiché | Source (titre, URL) | Date de la source | Consulté | Statut |
|---|---|---|---|---|---|
| `bck_review_paradox.py` | « 1.7× more issues per pull request in AI-co-authored code (10.83 vs 6.45, 470 open-source PRs) » ; présenté comme étude d'éditeur sur petit échantillon | Loker, *Our New Report: AI Code Creates 1.7x More Problems (State of AI vs. Human Code Generation)*, CodeRabbit Blog, https://www.coderabbit.ai/blog/state-of-ai-vs-human-code-generation-report (`coderabbit-ai-vs-human2025`) | 17/12/2025 | — | à vérifier |
| `bck_review_scale.py` | « 60 million Copilot code reviews by March 2026 — more than 1 in 5 code reviews on GitHub » | Gopu & Apirian, *60 Million Copilot Code Reviews and Counting*, GitHub Blog, https://github.blog/ai-and-ml/github-copilot/60-million-copilot-code-reviews-and-counting/ (`github-ccr-60m2026`) | 05/03/2026 | — | à vérifier |
| `bck_review_jones.py` | Efficacité d'élimination des défauts (min / moyenne) : inspection formelle 60 % / 85 % ; tests unitaires automatisés 20 % / 40 % ; tests fonctionnels 33 % / 40 % ; « data from 13,000+ projects » | Capers Jones, *Software Defect Removal Efficiency*, PPI SyEN 36, https://www.ppi-int.com/systems-engineering-newsjournal/ppi-syen-36/ (`jones-dre2011`) | 2011 | — | à vérifier |
| `bck_review_size.py` | « 200–400 lines per review — beyond that, defect detection drops » ; « no more than 60 minutes per session » | Cohen, *Best Kept Secrets of Peer Code Review*, Smart Bear Inc. (étude de cas Cisco MeetingPlace) ; conseils SmartBear, https://smartbear.com/learn/code-review/best-practices-for-peer-code-review/ (`cohen2006-peer-review`) | 2006 | — | à vérifier |
| `bck_bridge_quiz_answers.py` | « 200-400 lines per review » (réponse du quiz, reprise du chiffre précédent) | idem `cohen2006-peer-review` | 2006 | — | à vérifier (suit `bck_review_size.py`) |
| `bck_review_size.py` | « An agent writes 1,000 lines in a session » | — (ordre de grandeur illustratif, pas de source) | — | — | illustratif (à reformuler si contesté) |
| `bck_bridge_quiz.py` | « A 1,200-line diff » | — (cas fictif du quiz) | — | — | illustratif |
| `bck_review_readme_rule.py` | Règle « 80/20 » (l'agent écrit le QUOI 80 %, vous le POURQUOI 20 %) | — (règle pédagogique du cours, pas une mesure) | — | — | illustratif |
| `bck_review_catches.py` | Ce que la revue IA trouve / rate — qualitatif | — (synthèse du cours, pas de chiffre) | — | — | inchangé |

Le plan du jour 2 (`docs/plans/2026-11-09-007-day2-plan-b.md`, règles de forme) mentionne « 60-65 % des défauts » :
le module affiche le tableau de Capers Jones (60 % minimum / 85 % moyenne pour l'inspection formelle), pas ce libellé.
