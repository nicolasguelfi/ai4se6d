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
- [x] Passe opencode : aucun « Cursor » dans les blocs repris aux jours 3-4 ; les blocs de commandes de l'édition 1 gardent la forme `/gse:` (décision P3) : diapositive « One Command Form » (`bck_gensem_command_form`) placée avant les blocs de commandes, aux jours 3 et 4.
- [~] Fiche `docs/trainer/sources-day3.md` écrite ; chiffres de l'édition 1 encore à vérifier à la source (P9).
- [x] Syllabus HD05-HD06 + page d'orientation (`syllabus/orientation.md`) ; programme public HD05-HD08 réécrit (déjeuner du jour 3 12:30-13:30).

## Lot 3 — jour 4 (phase 2)

- [x] CCSET12 en pratique : E14 (P6, stratégie de test d'abord).
- [x] CCSET13 : cours « mesurer la qualité » (4 diapositives) + illustration + E15 ; kit qualité présenté à 09:00.
- [x] Starter : étiquette `quality-kit` (commit `8744f3d`) : `ci.yml` (install, lint, tests avec couverture, build) et script `test:coverage` ; CI verte sur GitHub ; installation rejouée dans une copie propre.
- [x] CCSET14 : 4 diapositives de théorie (fusion, version, maintenance, rétrospective) + illustration + E16 (P7 avec continuité).
- [x] CCSET15 : défi, cadrage, règles (P17), idées (repris du deck de Tiago, sans Cursor ni crédit) + illustration ; E17, E18.
- [x] Syllabus HD07-HD08 ; programme public (liens, kit qualité).

## Lot 4 — vérification

- [~] Répétition de référence des jours 1 à 4 faite le 10/11 sur le modèle de la formation (journal : `rehearsals/2026-11-10-reference/logbook.html`, dépôt privé `nicolasguelfi/ai4se-rehearsals`, CalcApp de référence `nicolasguelfi/ai4se-reference-calcapp`). Étiquettes publiées sur le starter : `j2-part1`, `j2-v0.1`, `p3-start`. `p6-start` et `p7-start` dans le dépôt privé (à nettoyer : profil de l'apprenant de répétition, `__pycache__`). `p5-start` non produit.
- [ ] `uv run python scripts/edition_diff.py` : rapport pour NG.
- [x] Vue d'ensemble `2026-11-09-010-six-days-overview.md` : renvoi au déroulé 012 et à ce suivi.

## Journal

- 2026-11-10 — déroulé 012 validé et versionné (commit `feb5419`) ; suivi ouvert.
- 2026-11-10 — lot 1 : composant `gse_solution`, 8 diapositives d'illustration (CCSET01-08), carte des cycles, feuille de route, débrief du jour 1 relié aux cycles ; syllabus HD01-HD04. Règle de NG « aucun chiffre dans les noms de blocs » appliquée aux blocs de l'édition 2 : 103 blocs du jour 2 (`bck_d2_*` → mots-clés, ids de style `d2_*` aussi), 4 blocs `_ed2`, 2 blocs de `setup`, 2 images. Les fichiers de l'édition 1 gardent leur nom (option A). Rapport `edition_diff` : aucun fichier de l'édition 1 supprimé.
- 2026-11-10 — lot 2 (jour 3) : livre gensem réorganisé en 4 séquences (`sequence_concepts`, `sequence_discovery`, `sequence_quality`, `sequence_delivery` ; les deux dernières provisoires) ; 3 cours écrits (élicitation 9 diapositives, exigences non fonctionnelles 7, vérification et validation 7) + 4 illustrations CCSET09-12, grille des Gates, page d'orientation ; accueil et clôture du jour 3 ; 8 fiches d'exercice E11-E18 à source unique ; 13 références ajoutées à `references.bib` ; vérification visuelle par export HTML et captures (débordement corrigé).
- 2026-11-10 — lot 3 (jour 4) : accueil et kit qualité, 3 cours (qualité 4 diapositives, livraison et capitalisation 4, cadrage 4) + 3 illustrations, quiz ; séquences `sequence_quality` et `sequence_delivery` définitives ; starter `quality-kit` ; syllabus HD07-HD08.
- À reporter en phase 3 : en mode Allégé, GSE-One n'a pas d'activité de revue (`/gse-review`) ni de stratégie de test séparée (spec : PLAN → REQS → PRODUCE → DELIVER, revue d'intégrité minimale à la livraison) ; la fiche E20 du déroulé 012 (« `/gse-tests` … `/gse-review` → `/gse-fix` ») est à corriger.
- 2026-11-10 — répétition de référence (jours 1-4, DeepSeek V4.1 Flash via OpenRouter, clé `ai4se-prep`) : dépense totale 1,75 $. Constats à traiter : (1) jour 2 : « Tab » → « Maj+Tab » pour changer d'agent ; configuration MCP d'opencode 2 sous `mcp.servers` (préférer `opencode mcp add`) ; (2) fiche E5 : ajouter la question « manque-t-il quelque chose pour que l'application marche de bout en bout ? » ; (3) starter : exclure `.opencode` et `.gse` dans `eslint.config.js` (sinon lint rouge après installation de GSE-One) ; gensem : l'adaptateur `gse-guardrails.ts` utilise `any` ; (4) jour 3 : `main` contre `mywork` (GSE-One prend `main` comme référence) — fusionner `mywork` dans `main` à la fin du jour 2 ; (5) E11 : le garde-fou se manifeste par une Gate (refus et chemins sûrs), pas par un blocage visible ; (6) E15 : cas réel — CI rouge au build (erreur de type) alors que tests et revue étaient verts ; (7) le coach de GSE-One détecte l'approbation machinale (4 options recommandées de suite) : à montrer avec la grille des Gates.
- 2026-11-11 — constat (1) corrigé : « Maj+Tab » pour changer d'agent (jours 1-2) ; Context7 par `opencode mcp add context7 --url https://mcp.context7.com/mcp` (`mcp.servers`), vérification par la barre latérale « Connected » (diapositives `ff482ff`, kit `2e36ecd`).
- 2026-11-11 — constat (2) corrigé : fiche E5, question « manque-t-il quelque chose pour que l'application marche de bout en bout (câblage, point d'entrée, assemblage) ? » (`ff482ff`, kit `2e36ecd`).
- 2026-11-11 — constat (4) corrigé : fin d'E10, `git switch -C main mywork` (un `git merge --no-ff mywork` entre en conflit sur README, car `main` du starter porte le commit `quality-kit`) ; jour 3 depuis `main`, installation de GSE-One sur `chore/gse-one` fusionnée dans `main` ; reprise `p3-start` sur `main` (`ff482ff`, kit `2e36ecd`).
- 2026-11-11 — constat (5) corrigé : E11, l'apprenant cherche la Gate de l'agent (refus, garde-fou protect_main, chemins sûrs) ; le hook ne bloque que si l'agent essaie quand même (`ff482ff`, kit `2e36ecd`).
- 2026-11-11 — constat (3) corrigé : lint rouge après installation de GSE-One. Plugin : gensem **v0.90.1** (commit 1df436d, tag v0.90.1), adaptateur opencode exempté du lint (`/* eslint-disable */`), archive de release sans `__pycache__`, `dashboard.py` lit `clé: valeur  # commentaire`. Starter : `eslint.config.js` ignore `coverage`, `.opencode`, `.gse`, `.gse-sandbox` (commit 63d2e22, CI verte). Version épinglée passée à v0.90.1 dans le kit et les diapositives ; installation réelle de v0.90.1 vérifiée (aucun `__pycache__`, exemption présente).
- 2026-11-11 — écarts validés par NG : `git switch -C main mywork` à la place de la fusion, et pas de push le soir du jour 2. Choix d'une branche de référence configurable dans GSE-One : inscrit au backlog de gensem (BKL-50567ed2), pour après la formation.
