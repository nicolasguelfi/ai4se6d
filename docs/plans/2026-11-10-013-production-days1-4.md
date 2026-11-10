# Production des jours 1 à 4 — suivi

**Lancée** : 2026-11-10, à la demande de NG, à partir du déroulé validé `2026-11-10-012-six-days-cycles-plan.html` (16 cycles CCSET, fiches E1 à E18).
**Règles** : option A (branche `edition2`, désactiver au lieu de supprimer, nouveau bloc aux mots-clés sans chiffre quand le sens change, rapport `scripts/edition_diff.py` validé par NG avant fusion) ; chaque diapositive modifiée met à jour la fiche HD de la même demi-journée dans `ai4se-kit/syllabus/`, dans le même lot de commits ; `uv run ruff check` et `uv run stx validate --build` avant chaque commit de blocs ; diapositives en anglais.
**Illustration du plugin** (cycles 01 à 12) : une diapositive par cycle, mise en page commune `modules/shared-blocks/gse_solution.py`, texte seulement, ni démonstration ni capture d'exécution.

Légende : `[x]` fait · `[ ]` à faire · `[~]` en cours · `[R]` demande la répétition (exécution réelle de GSE-One avec un modèle).

## Lot 1 — jours 1-2 (échéance 18/11, répétition 19-20/11)

- [x] Composant partagé `gse_solution` (shared-blocks).
- [x] J1 · `genai_intro` : feuille de route des 6 jours mise à jour (`bck_intro_roadmap`) ; carte des 16 cycles (nouveau bloc) ; illustration CCSET01.
- [x] J1 · `vibecoding` : illustrations CCSET02 et CCSET03.
- [x] J1 · `setup` : débrief relié aux cycles 01-03.
- [x] J2 · `day2` : illustrations CCSET04 à CCSET08 ; le « pont » de 16:30 (`bck_bridge_loop`) est déjà le tableau « à la main / GSE-One au jour 3 », gardé tel quel.
- [x] Syllabus HD01-HD04 : cycles et illustrations.

## Lot 2 — jour 3 (phase 2)

- [x] `gensem` : livre réorganisé en séquences jour 3 / jour 4 (blocs non montrés retirés du livre, fichiers gardés).
- [x] CCSET09 : sélection des blocs `sdlc_*`, `evidence_*`, `fw_*` ; illustration (principes, cycle de vie, modes, Gates) ; grille des 3 questions ; page d'orientation (recto-verso, imprimable).
- [x] CCSET10 : cours « élicitation des exigences » (à écrire) + illustration.
- [x] CCSET11 : cours « exigences non fonctionnelles » (à écrire) + illustration.
- [x] CCSET12 : cours « vérification et validation » (à écrire) + illustration.
- [x] E11, E12, E13 : fiches à source unique (`modules/shared-blocks/exercise_sheets.py`, rendu `exercise_sheet.py`, syllabus par `scripts/sheets_markdown.py`) ; E14 à E18 écrites aussi.
- [x] Accueil du jour 3 (rappel des jours 1-2), débriefs, fin de journée.
- [x] Passe opencode : aucun « Cursor » dans les blocs repris aux jours 3-4 ; les blocs de commandes de l'édition 1 gardent la forme `/gse:` (décision P3 : bandeau à ajouter).
- [~] Fiche `docs/trainer/sources-day3.md` écrite ; chiffres de l'édition 1 encore à vérifier à la source (P9).
- [x] Syllabus HD05-HD06 + page d'orientation (`syllabus/orientation.md`) ; programme public HD05-HD08 réécrit (déjeuner du jour 3 12:30-13:30).

## Lot 3 — jour 4 (phase 2)

- [ ] CCSET12 en pratique : E14 (P6, stratégie de test d'abord).
- [ ] CCSET13 : cours « mesurer la qualité » (à écrire) + illustration + E15.
- [ ] Starter : étiquette ajoutant la couverture de tests et un `ci.yml` (dépôt `calcapp-starter`).
- [ ] CCSET14 : blocs `t7_*` repris + E16 (P7 avec continuité).
- [ ] CCSET15 : page du mini-projet ; import du deck de Tiago (sans Cursor) ; E17 (fiche projet), E18 (`/gse-go` Allégé).
- [ ] Syllabus HD07-HD08 ; programme public.

## Lot 4 — vérification

- [R] Étiquettes de reprise `p3-start`, `p5-start`, `p6-start`, `p7-start` posées en déroulant P1 → P7 avec GSE-One v0.90.0.
- [ ] `uv run python scripts/edition_diff.py` : rapport pour NG.
- [ ] Vue d'ensemble `2026-11-09-010-six-days-overview.md` mise à jour (états ✅).

## Journal

- 2026-11-10 — déroulé 012 validé et versionné (commit `feb5419`) ; suivi ouvert.
- 2026-11-10 — lot 1 : composant `gse_solution`, 8 diapositives d'illustration (CCSET01-08), carte des cycles, feuille de route, débrief du jour 1 relié aux cycles ; syllabus HD01-HD04. Règle de NG « aucun chiffre dans les noms de blocs » appliquée aux blocs de l'édition 2 : 103 blocs du jour 2 (`bck_d2_*` → mots-clés, ids de style `d2_*` aussi), 4 blocs `_ed2`, 2 blocs de `setup`, 2 images. Les fichiers de l'édition 1 gardent leur nom (option A). Rapport `edition_diff` : aucun fichier de l'édition 1 supprimé.
- 2026-11-10 — lot 2 (jour 3) : livre gensem réorganisé en 4 séquences (`sequence_concepts`, `sequence_discovery`, `sequence_quality`, `sequence_delivery` ; les deux dernières provisoires) ; 3 cours écrits (élicitation 9 diapositives, exigences non fonctionnelles 7, vérification et validation 7) + 4 illustrations CCSET09-12, grille des Gates, page d'orientation ; accueil et clôture du jour 3 ; 8 fiches d'exercice E11-E18 à source unique ; 13 références ajoutées à `references.bib` ; vérification visuelle par export HTML et captures (débordement corrigé).
