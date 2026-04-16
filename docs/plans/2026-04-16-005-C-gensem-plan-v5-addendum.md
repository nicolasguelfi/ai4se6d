# Addendum v5 — Module ai4se6d_gensem

**Date**: 2026-04-16
**Cycle**: CE-GENSEM-004 (suite v4)
**Statut**: Implémenté dans `modules/ai4se6d_gensem/` (sessions 1-2 actives, 3-4 en pause dans `book.py`)
**Base**: `2026-04-14-004-C-gensem-plan-v4.md` (reste l'archive complète du plan initial)
**Référence technique**: `~/dev-dropbox/dvlpt/eclipse/git/github/gensem/_LOCAL/maintenance/2026-04-16-plan-yaml-living-plan-v2.md`

## 1. Contexte

Le plugin GSE-One a subi deux refontes post-v4 qui rendent des sections du plan obsolètes :

- **v0.20.0** (`e49ecc4`) — architecture `.gse/plan.yaml` vivant (remplace `docs/sprints/sprint-NN/plan.md`).
- **v0.20.1** (`90ad462`) — follow-ups : `activity_history`, FIX conditionnel, héritage `PLN-NNN`, desync warning, dashboard cards.

Cet addendum capture les corrections apportées au module pour s'aligner sur la v0.20.1, sans recopier l'intégralité du plan v4.

## 2. Résumé des modifications

17 propositions traitées une par une. 16 implémentées (#15 validée sans action), 1 documentaire (#17 = ce document).

| # | Fichier / artefact | Nature | Choix |
|---|---|---|---|
| 1 | `bck_gensem_ce_plan_artifact.py` + nouveau `bck_gensem_ce_plan_summary.py` | Refonte Markdown → YAML `.gse/plan.yaml` + nouveau bloc archive `plan-summary.md` | C (split en 2 blocs) |
| 2 | `bck_gensem_method_checklist.py` L45 | `docs/plan.md` → `.gse/plan.yaml` | A |
| 3 | `bck_gensem_practice_p3.py` L47, L85, L101 | 3 substitutions `plan.md` → `.gse/plan.yaml` | A |
| 4 | `bck_gensem_method_step2.py` L39 | `docs/plan.md` + « Cursor todos » → `.gse/plan.yaml` + « maintained by orchestrator » | A |
| 5 | `bck_gensem_t2_philosophy.py` L128 | Ordre LC02 corrigé (TESTS avant PRODUCE) dans tooltip | A |
| 6 | `bck_gensem_t2_commands.py` | Ajout `.gse/plan.yaml`, rename `plan → plan-summary`, `state → cursor` | A |
| 7 | `bck_gensem_t2_cmd_pause_resume.py` | Bullet « workflow trajectory » + tooltip « Living plan aware » | A |
| 8 | `bck_gensem_t2_cmd_backlog.py` | Tooltip « Plan sync check » + accent « desync warning » | A |
| 9 | `bck_gensem_t3_cmd_plan.py` | Tooltips « Living document », « Coherence alerts » + accent enrichi | A |
| 10 | `bck_gensem_t7_cmd_deliver.py` | 6ᵉ étape « 📦 Archive plan » + tooltip PLN-NNN inheritance | A |
| 11 | `bck_gensem_t6_cmd_fix.py` | Tooltip « Conditional insertion » + accent révisé | A |
| 12 | `bck_gensem_t6_engineering.py` | Réordonnancement : TESTS → Test Pyramid → PRODUCE (était PRODUCE → TESTS) | A |
| 13 | Nouveau `bck_gensem_ce_plan_living.py` | Slide dédiée « Living Plan — Coherence Monitoring » (3 alertes Inform-tier) | A |
| 14 | `bck_gensem_t2_cmd_status.py` + `bck_gensem_t2_commands.py` | Tooltips `activity_history[]` | A |
| 15 | Schéma plan.yaml | Aucune action — capitalisation sur `ce_plan_artifact` (prop #1) | A |
| 16 | `bck_gensem_t7_cmd_health.py` | Tooltip « Dashboard view » (Sprint Workflow + Coherence cards) | A |
| 17 | Plan de formation | Ce document (addendum v5) | B |

## 3. Table de substitution systématique

| Avant (v4) | Après (v0.20.1) | Occurrences traitées |
|---|---|---|
| `docs/sprints/sprint-NN/plan.md` | `.gse/plan.yaml` (living) + `docs/sprints/sprint-NN/plan-summary.md` (archive) | Props #1-4, #6, #10 |
| `plan_status` (dans status.yaml) | `plan.yaml.status` (active \| completed \| abandoned) | Implicite dans #6, #14 |
| LC02 = `REQS → DESIGN → PREVIEW → PRODUCE → TESTS → REVIEW → FIX → DELIVER` | LC02 = `REQS → DESIGN → PREVIEW → TESTS → PRODUCE → REVIEW → FIX → DELIVER` | Props #5, #12 |
| FIX systématique après REVIEW | FIX inséré conditionnellement (findings HIGH/MEDIUM uniquement) | Prop #11 |
| Plan = artefact statique généré par PLAN | Plan = artefact vivant maintenu à chaque transition par l'orchestrator | Props #1, #9, #13 |

## 4. Nouveaux blocs ajoutés à `book.py`

- `bck_gensem_ce_plan_summary` — slide « plan-summary.md — Sprint Archive » (inséré après `ce_plan_artifact` en T3 Séq 3.3).
- `bck_gensem_ce_plan_living` — slide « Living Plan — Coherence Monitoring » (inséré entre `t3_cmd_plan` et `ce_plan_antipattern` en T3 Séq 3.3).

Total Séq 3.3 : 5 → 7 slides actives.

## 5. Concepts désormais couverts

Concepts introduits par la refonte plugin et absents de v4, maintenant couverts par le module :

- **Living plan** — plan.yaml mis à jour après chaque transition d'activité.
- **Coherence alerts** (Inform-tier non bloquant) : `budget_pressure`, `scope_drift`, `velocity_risk`.
- **Scope changes log** (`coherence.scope_changes[]`).
- **Activity history** (`status.yaml.activity_history[]`) — source autoritative pour `workflow.completed`.
- **PLN-NNN inheritance** au moment de la génération de `plan-summary.md` (traçabilité P6).
- **Desync warning** — `/gse:backlog sprint` détecte la divergence backlog ↔ plan.yaml.
- **Conditional FIX insertion** — FIX absent de `workflow.expected`, inséré par l'orchestrator après REVIEW ssi findings.
- **Workflow trajectory** — `/gse:resume` affiche `workflow.active`, `pending`, `completed`, alerts.
- **Dashboard cards** Sprint Workflow + Coherence Alerts (mentionné dans tooltip `/gse:health`).

## 6. Cohérence vérifiée

- `uv run ruff check` — OK sur tous les blocs modifiés et nouveaux.
- Les blocs en sections commentées de `book.py` (sessions 3-4) ont été alignés pour éviter qu'ils ne soient réactivés avec des incohérences.
- Les 2 warnings E402 persistants dans `book.py` (imports `streamtex.styles` et `blocks` après lecture de `pyproject.toml`) sont préexistants et non introduits par cet addendum.

## 7. Référence

Pour la spécification complète de la refonte plugin (schema `plan.yaml`, protocole orchestrator, décisions d'ID, etc.), voir :

```
~/dev-dropbox/dvlpt/eclipse/git/github/gensem/_LOCAL/maintenance/2026-04-16-plan-yaml-living-plan-v2.md
```

Ce document est la source technique définitive. Le présent addendum traite uniquement des impacts sur le module StreamTeX de formation.
