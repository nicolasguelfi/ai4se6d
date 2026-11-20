# Production des jours 5 et 6 — suivi

**Lancée** : 2026-11-20, à la demande de NG, à partir du déroulé validé `2026-11-10-012-six-days-cycles-plan.html` (jours 5-6, fiches E19 à E25, points ouverts avec leurs valeurs par défaut validées le 10/11).
**Règles** : celles du suivi `2026-11-10-013-production-days1-4.md` (branche `edition2`, blocs aux mots-clés sans chiffre, désactiver au lieu de supprimer, chaque diapositive ajoutée a sa contrepartie dans la fiche HD de la même demi-journée, fiches d'exercice à source unique `modules/shared-blocks/exercise_sheets.py`, rendu syllabus par `scripts/sheets_markdown.py`, `uv run --frozen ruff check` et `uv run --frozen stx validate --build` avant chaque commit).
**Structure CCSET** : un seul nouveau cycle (CCSET16, déploiement) : théorie → illustration conceptuelle du plugin → fiche → débrief. L'éthique du jour 6 applique le cycle 03 du jour 1 (aucun nouveau concept).

Légende : `[x]` fait · `[ ]` à faire · `[~]` en cours · `[P]` gabarit en attente d'une décision de NG.

## Choix du module

Les jours 5-6 sont ajoutés au module `ai4se6d_gensem`, en quatre nouvelles séquences (`sequence_deployment` jour 5 matin, `sequence_sprint` jour 5 après-midi, `sequence_finish` jour 6 matin, `sequence_gallery` jour 6 après-midi), comme les jours 3-4. Pas de nouveau module : ajouter un module à la collection demande une application Coolify et une variable `STX_URL_…` de plus (`collection.toml`), donc une intervention sur le serveur, et les jours 5-6 poursuivent la même boucle GSE-One avec les mêmes composants partagés (`gse_solution`, `exercise_sheet`).

## Lot 1 — diapositives et fiches (ai4se6d, commit `83e1040`)

- [x] 7 références ajoutées à `references.bib` : Humble & Farley 2010, Merkel 2014, Wiggins 2011 (Twelve-Factor), Meli et al. 2019 (NDSS), Forsgren et al. 2018, AI Act (Règlement (UE) 2024/1689), RGPD (Règlement (UE) 2016/679).
- [x] 7 fiches ajoutées à la source unique : `sprint` (E20), `model_comparison` (E21), `deploy_calcapp` (E19, gabarit), `deliver_freeze` (E22), `project_audit` (E23), `gallery_demo` (E24), `lessons` (E25) ; 14 blocs `bck_gensem_sheet_*`.
- [x] J5 matin : accueil (`bck_gensem_today_project`, `bck_gensem_resume_project`) ; CCSET16, 6 diapositives de théorie + titre (`bck_deploy_*` : du code au service, image et conteneur avec le Dockerfile du starter simplifié, serveur et adresse, configuration et secrets, journaux, retour arrière) ; illustration `bck_gse_solution_deployment` (Dockerfile écrit seulement s'il manque, état dans `.gse/deploy.json`, vérification de la version en ligne) ; `bck_deploy_course_mode` [P] ; boucle Allégée (`bck_project_lightweight_loop`) ; grille E21 (`bck_project_model_grid`).
- [x] J5 après-midi : `bck_project_afternoon`, `bck_project_milestone` (ce que NG vérifie, validation au fil de l'eau 15:15-16:30), `bck_project_day_debrief` (jalon + débrief du déploiement).
- [x] J6 matin : `bck_gensem_today_finish`, `bck_project_finish_line`, `bck_project_readme_card` (fiche projet du README), `bck_ethics_recall` (cycle 03 appliqué ; renvoie aux blocs du jour 1 `bck_ide_ai_act`, `bck_ide_ai_rules`, `bck_gse_solution_plugin` du module `vibecoding`, et à hd01 § EU AI Act and rules for this week), `bck_ethics_readme_section`.
- [x] J6 après-midi : `bck_gallery_how` (deux rotations, point ouvert 10), `bck_gallery_visitor_grid`, `bck_closing_monday_plan`, `bck_closing_questionnaire` (gabarit « link given in class »), `bck_closing_resources`.
- [x] Vérification visuelle : export HTML paginé du livre gensem, captures Playwright 1920×1080 des 40 diapositives nouvelles ; aucun débordement ; deux retouches (commandes trop petites sur la boucle Allégée, citations UE trop longues).

## Lot 2 — syllabus (ai4se-kit, public, commit `f6218fb`)

- [x] `syllabus/hd09-day5-am.md`, `hd10-day5-pm.md`, `hd11-day6-am.md`, `hd12-day6-pm.md` ; fiches incluses à l'identique de `sheets_markdown.py` (vérifié).
- [x] `syllabus/00-programme.md` : HD09-HD12 réécrits (pauses 10:45 et 15:00 au jour 5, 10:30 au jour 6, point ouvert 12) ; plus de mention « provisoire ».
- [x] `glossary.md` : 15 entrées (conteneur/image, variable d'environnement, secret, journaux, contrôle de santé, retour arrière, étiquette `demo`, limites connues, licence, données personnelles, jalon, fiche projet, galerie, plan « lundi matin », contrôle d'intégrité minimal) ; Dockerfile complété.
- [x] `faq.md` : §17 mini-projet en retard, §18 deux modèles, §19 démo qui casse. `orientation.md` : une ligne « en retard sur le mini-projet ».

## Écarts au déroulé 012 (et pourquoi)

1. **E20 corrigée** : le déroulé dit `/gse-plan → /gse-reqs → /gse-tests → /gse-produce → /gse-review → /gse-fix`. Le mode Allégé de GSE-One n'a ni `/gse-tests`, ni `/gse-review`, ni `/gse-fix`, ni `/gse-compound` (spec §13.2 — Lightweight Mode : PLAN → REQS → PRODUCE → DELIVER ; stratégie de test minimale générée à PRODUCE ; passe d'intégrité minimale à DELIVER, 5 constats au plus, un HIGH bloque la fusion). La fiche suit la spec. La spécification `009` (« fin du sprint, puis `/gse-compound` » au jour 6) n'est pas reprise pour la même raison.
2. **E21 sur une copie du projet** : pour donner « la même consigne à deux modèles » sans que le modèle B écrase les exigences du modèle A, B tourne dans une copie (`cp -R . ../<project>-model-b`) ; changement de modèle par `/models` dans opencode ; coût lu dans la barre latérale d'opencode (« $ spent »). Version B retenue : on recopie son `reqs.md` et on demande à l'agent de le vérifier contre le plan.
3. **E22, ordre des étapes** : `/gse-deliver` à 11:30, puis à 12:00 le gel, la fiche projet et les limites connues du README sur une branche `docs/demo`, fusionnée dans `main` par l'apprenant (`git merge --no-ff`), puis l'étiquette `demo`. Raison : le garde-fou refuse un commit direct sur `main`, et le sprint est clos après la livraison. Voir la question 2.
4. **Illustration du plugin (09:35)** : le déroulé indiquait « à adapter (`t7_cmd_deploy`) ». Le bloc de l'édition 1 décrit l'installation complète d'un serveur Hetzner par le formateur (provision, durcissement, Coolify, DNS) : hors sujet pour l'apprenant. Remplacé par une diapositive `gse_solution` conceptuelle ; `bck_gensem_t7_cmd_deploy` reste sur disque.
5. **Budget de 8-10 points** : gardé (règle P17). La spec dit « Complexity budget: Not tracked » en Allégé (tableau §13.2), mais l'activité `plan.md` applique le contrôle de budget dans les deux modes (Step 4, défaut 10 points). Incohérence de la spec à signaler dans gensem (question 5).

## Gabarits en attente [P]

- Fiche E19 `deploy_calcapp` : but, durée, « Steps: to be written once the deployment server is chosen », fini quand, si bloqué, débrief. Diapositives `bck_gensem_sheet_deploy_calcapp_steps/check` et section E19 de hd09.
- Diapositive `bck_deploy_course_mode` (« How We Deploy in This Course ») et section « How we deploy in this course » de hd09 : liste ce qu'elle contiendra (identifiant, fichier de configuration copié, ordre des vagues, lecture des journaux), sans nom de serveur ni domaine.
- Diapositive `bck_closing_questionnaire` : « Link given in class » (questionnaire de DLH ou le nôtre).
- Décision attendue : planche `board-j56` (serveur, lecture des journaux, répétition).

## Points ouverts pour NG

1. Serveur de déploiement et lecture des journaux (bloque E19 et le mode opératoire). Par défaut : rien n'est écrit tant que la planche n'est pas tranchée.
2. E22 : fusion par l'apprenant d'une branche `docs/demo` dans `main` après la livraison (hors `/gse-deliver`). Par défaut : retenu ; alternative : écrire la fiche projet avant 11:30 sur la branche de la dernière tâche, pour que `/gse-deliver` l'emporte.
3. Grille des visiteurs de la galerie (3 questions) : « résout-il le problème annoncé (essayer soi-même) ? une exigence et le test qui la vérifie ? quelle limite ou quel risque ? ». Par défaut : celle-ci.
4. E21 : B dans une copie du projet. Par défaut : retenu ; alternative : comparer seulement au moment de la Gate de `/gse-reqs`, sans copie (plus rapide, moins comparable).
5. gensem : tableau §13.2 « Complexity budget: Not tracked » contre `plan.md` Step 4 (budget contrôlé). Par défaut : ticket au backlog de gensem, après la formation.

## Journal

- 2026-11-20 — lots 1 et 2 produits (diapositives `83e1040`, kit `f6218fb`) ; validation `ruff` et `stx validate --build` (2 avertissements connus : `uv.lock` source locale, image insérée de genai_intro) ; 40 captures dans le dossier `shots-j56` du bloc-notes de session.
