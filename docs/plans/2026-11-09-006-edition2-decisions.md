# Édition 2 — décisions de préparation

**Date** : 2026-11-09
**Édition** : DLH, 26-27/11, 03-04/12, 10-11/12/2026 — NG seul (Tiago Sousa ne fait plus partie de la formation et a transféré à NG la propriété de ses supports)
**Source** : planches de décision `ai4se1` et `gsel1` (session Claude `ss2-ul-gse`, 2026-11-08/09) ; rapport d'état des lieux (artefact « AI4SE — état des lieux », v3)
**Branche de travail** : `edition2` (un push sur `main` redéploie les 4 apps Coolify : on ne fusionne qu'une fois l'édition prête)

## 1. Décisions (planche `ai4se1`)

| # | Sujet | Décision | Remarque / résolution |
|---|---|---|---|
| 1 | Statut DLH | Message à DLH (inscrits, contrat, salle) **sans attendre** pour travailler | NG est sûr qu'il y aura une édition |
| 2 | Ambition | Rafraîchissement **ciblé** | ≈ 17-20 j au total |
| 3 | Organisation | Viser **tout avant le 26/11**, l'ordre des 3 vagues sert de priorité si le temps manque | |
| 4 | Agent apprenants | **opencode** principal ; Cursor gratuit comme simple éditeur si besoin | Pas de sièges Cursor Pro |
| 5 | Accès modèles | **Une clé plafonnée par apprenant** (type OpenRouter) | Modèles gratuits opencode Zen limités par IP : écartés |
| 6 | Machines | VM DLH de référence ; portables personnels acceptés ; installation en salle pour qui n'est pas prêt ; liste de contrôle à J-7 | Pas de session à distance |
| 7 | GSE-One | **v0.89.1** (publiée le 2026-11-09) | Voir § 3 |
| 8 | Dépôts de Tiago | Nouveaux dépôts privés : `nicolasguelfi/ai4se6d-decks`, `nicolasguelfi/calcapp-course` (créés le 2026-11-09) | |
| 9 | Jour 2 | Import **condensé** du deck de Tiago en StreamTeX, dans ai4se6d | Cible ai4se6d choisie par NG (QCM) |
| 10 | CalcApp | **Starter épinglé** (Vite 7, Vitest 4, React Router 7, TS 5.9, package-lock) | |
| 11 | Outils jour 1 | **Acte IV** (bck_ide_*) réactivé + blocs opencode et LLM locaux repris de Tiago | |
| 12 | Encadrement | NG **seul**, sans dispositif particulier | Risque accepté |
| 13 | Démo jour 6 | **Supprimée** | Absente du programme publié |
| 14 | Traces de Tiago | **Retirer** sa fiche formateur et les mentions ; pas de crédit | |
| 15 | Mini-projet | Projet professionnel sous GSE-One, cadré par écrit | |
| 16 | Confidentialité | Pas de règle | Risque accepté |
| 17 | Évaluation | **Présence** seulement (certificat) | Écart connu avec le cahier des charges DLH (évaluation continue par tests) |
| 18 | Contenu GenAI | Rafraîchissement **ciblé** (LLM, outils, éthique/AI Act) | |
| 19 | gse-light | **Pas** présenté dans le cours | |
| 20 | Programme DLH | **Ne rien faire** | Une phrase de cadrage en ouverture du jour 1 (le programme annonce Cursor) |
| 21 | Secrets | Rotation **maintenant et après** la formation (par NG) | |
| 22 | StreamTeX | **Monter ai4se6d en 0.7.82** maintenant | Validation avant/après ; fait en premier pour découvrir les casses tôt |
| 23 | Lieu | Rester dans ai4se6d, **migrer après le 11/12** | |
| 24 | Langue | Slides en **anglais** | |

## 2. Décisions (planche `gsel1`, gse-light → GSE-One)

- Avant la formation : B2 (pas de livraison sur HIGH ouvert sans décision), B5 (deploy ne lit plus `.env` en entier), correction du README (installation épinglée), B6 (CI sur push) — **livrés en v0.89.1** ; B1 (script `check-learner.sh`) et B7 (vue formateur en lecture seule) **côté formation**.
- Après la formation : versions GSE-One de B1 et B7, puis B4, A2, A3, A1, B3, A5, A4, B8, B9, B10.
- Backlog : A7, B11, B15.
- Forme : les choix candidat par candidat sont respectés (pas de « tout livrer maintenant »).

## 3. Fait depuis

- 2026-11-09 — gensem **v0.89.1** publiée (commit 1b4f70a, tag v0.89.1, CI et release au vert).
- 2026-11-09 — dépôts `ai4se6d-decks` (branches master, feat/tools-ecosystem-lecture-content, refactor/day2-split-image-slides) et `calcapp-course` (v0-plans … v5-production) créés en privé.

## 4. Points ouverts

- **opencode 2** : la PR externe gensem #11 indique qu'opencode 2 ne charge plus le plugin de garde-fous GSE (format V1). Décision NG requise (voir conversation).
- Budget et fournisseur des clés de modèle (≈ 20 clés plafonnées).
- Mode d'accès aux VM DLH (protocole, distribution des identifiants sur fiche papier).
