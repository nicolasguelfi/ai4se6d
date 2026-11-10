# Les six journées en une page (vue formateur)

**But** : juger chaque déroulé en ayant la semaine entière sous les yeux.
**Source** : le programme public `ai4se-kit/syllabus/00-programme.md` (en anglais, pour les apprenants et le tuteur). Ce tableau le résume, il ne le remplace pas. En cas d'écart, c'est le programme qui fait foi, puis les déroulés détaillés.
**Déroulé en cycles des six journées (fait foi)** : `2026-11-10-012-six-days-cycles-plan.html` (16 cycles CCSET, 25 fiches d'exercice). Il remplace les tableaux ci-dessous pour les jours 3 à 6. Production des jours 1 à 4 : `2026-11-10-013-production-days1-4.md` (supports rédigés le 10/11, à répéter).
**Déroulés minutés antérieurs** : jour 1 `2026-11-09-008-day1-plan.md`, jour 2 `2026-11-09-007-day2-plan-b.md`, jours 3 à 6 `2026-11-10-011-days3-6-plan.md` (première version provisoire, 8 points ouverts).
**Légende** : ✅ définitif (rédigé, pas encore répété) · 🟡 provisoire (à confirmer en phase 2 ou 3) · ⬜ supports à écrire.

## Le fil de la semaine

| Bloc | Ce que l'apprenant apprend | Sur quoi il travaille |
|---|---|---|
| Jours 1-2 (26-27/11) | La discipline à la main : piloter un agent, planifier, tester, relire, git comme filet | FreeSelfApp (jour 1), puis CalcApp v0.1 (jour 2) |
| Jours 3-4 (03-04/12) | La même boucle, pilotée par une méthode (GSE-One), puis mesurer la qualité | CalcApp, avec GSE-One en mode Complet |
| Jours 5-6 (10-11/12) | Tout appliquer à son propre petit projet, le déployer, le présenter | Mini-projet, GSE-One en mode Allégé |

## Les 12 demi-journées

| Demi-journée | Horaire | Temps forts (heure de début) | Supports | État |
|---|---|---|---|---|
| **HD01** J1 matin | 09:00-12:15, pause 10:35 | 09:00 accueil, tour de table · 09:30 les 6 objectifs, comment on travaille · 09:45 IA générative + notions 1-3 · 10:50 du vibe coding au vibe engineering · 11:35 acte IV outils + notion 4 (AI Act, règles pratiques) | modules `genai_intro`, `vibecoding` (repris de l'édition 1, blocs `_ed2`) · déroulé `008-day1-plan.md` | ✅ |
| **HD02** J1 après-midi | 13:15-17:00, pause 15:15 | 13:15 installation en salle (75 min) · 14:30 FreeSelfApp partie 1 · 15:30 partie 2 · 16:15 débrief + quiz · 16:45 marge | module `setup` (nouveau) · `008-day1-plan.md` | ✅ |
| **HD03** J2 matin | 09:00-12:15, pause 10:45 | 09:00 rappel du jour 1 · 09:15 git d'abord (35 min) · 09:50 piloter opencode (3 démos + essais) · 11:00 atelier plan technique · 11:30 CalcApp v0.1 partie 1 (TDD) | module `day2` (nouveau) · déroulé `007-day2-plan-b.md` | ✅ |
| **HD04** J2 après-midi | 13:15-17:30, pause 15:00 | 13:15 CalcApp partie 2 · 14:30 revue de code avec l'IA · 15:15 revue du diff du jour · 16:15 livrer v0.1 · 16:30 pont vers GSE-One + quiz · 17:00 marge | module `day2` · `007-day2-plan-b.md` | ✅ |
| **HD05** J3 matin | 09:00-12:15, pause vers 10:30 | 09:00 accueil, CalcApp poussé sur GitHub · 09:15 **P1 découvrir GSE-One** (60 min, avant toute théorie) · 10:15 débrief P1 · 10:45 théorie allégée + page d'orientation · 11:30 P2 explorer `.gse/` | module `gensem` (édition 1, passe opencode à faire) | 🟡 ⬜ |
| **HD06** J3 après-midi | 13:15-17:00, pause vers 14:45 | 13:15 P3 planifier le sprint · 14:00 P4 classer les décisions (Auto / Inform / Gate) · 15:00 P5 exigences et conception · 16:15 débrief, push, quiz · 16:45 marge | module `gensem` | 🟡 ⬜ |
| **HD07** J4 matin | 09:00-12:15, pause vers 10:45 | 09:00 `/gse-resume` · 09:15 P6 tests, production, revue · 11:30 débrief du tri de la revue · 11:45 **mesurer la qualité** (30 min : lint, métriques, CI) | module `gensem` + branche CalcApp `v5-production` | 🟡 ⬜ |
| **HD08** J4 après-midi | 13:15-17:00, pause vers 14:45 | 13:15 P7 cycle complet (correction, livraison, capitalisation, santé) · 14:30 pause/reprise, backlog, tâche ponctuelle · 15:00 **lancement du mini-projet** (fiche projet) · 15:45 `/gse-go` mode Allégé · 16:30 push, débrief, quiz · 16:45 marge | module `gensem` | 🟡 ⬜ |
| **HD09** J5 matin | 09:00-12:15 | 09:00 `/gse-resume` · 09:15 comment marche le déploiement · 09:45 sprint du mini-projet (plan, exigences) **et en parallèle** vagues de déploiement de 5 | deck Marp de Tiago (`AI4SE6d/slides/day5`) + Dockerfile du starter | 🟡 ⬜ |
| **HD10** J5 après-midi | 13:15-17:00 | 13:15 suite du sprint, dernières vagues · 16:30 **jalon** : exigences et plan validés avec toi · 16:45 push, `/gse-pause`, marge | rien | 🟡 ⬜ |
| **HD11** J6 matin | 09:00-12:45 | 09:00 `/gse-resume` · 09:15 finir le sprint · 11:30 **première livraison** · 12:00 **gel** et chasse aux coquilles vides · 12:15 éthique appliquée à son projet (AI Act, licences, sécurité) | rien | 🟡 ⬜ |
| **HD12** J6 après-midi | 13:45-17:00, pause 15:30 | 13:45 préparer sa démo · 14:00 galerie, rotation 1 · 14:45 rotation 2 · 15:45 leçons apprises · 16:15 plan « lundi matin » · 16:35 questionnaire final · 16:50 certificats | rien | 🟡 ⬜ |

## Ce qui reste ouvert sur les jours 3 à 6

1. **Forme de la galerie (HD12)** : le programme dit « deux rotations, une moitié présente pendant que l'autre visite » ; la planche `peda1` disait « 4 tables de 5, puis 4 projets en plénière ». À trancher par NG (phase 3).
2. **Heure de comparaison de modèles** (P6) : décidée, mais pas encore placée dans un des créneaux des jours 3 à 5.
3. **Horaires des jours 3 à 6** : calqués sur les jours 1-2, pas encore éprouvés ; les pratiques peuvent s'allonger (P14).
4. **Déploiement (HD09-HD10)** : la forme exacte dépend de la répétition sur le serveur avec 3 comptes, avant le 10/12.
5. **Commandes de « mesurer la qualité » (HD07)** : lint, couverture et CI à choisir.
6. **Déjeuner du jour 6** : 12:45-13:45, parce que l'éthique est placée après le gel de midi.

## Calendrier de préparation

| Phase | Jours | Rédaction | Vérification |
|---|---|---|---|
| 1 | J1-J2 | rédigé le 09/11 (prévu jusqu'au 18/11) | relecture NG ; répétition 19-20/11 ; captures 23-24/11 ; fusion sur `main` vers le 25/11 |
| 2 | J3-J4 | 19/11 → 02/12 (hors 26-27/11) | répétition P1 → P7 ; contenu dans `2026-11-09-009-days3-6-specs.md` |
| 3 | J5-J6 | 04/12 → 09/12 | répétition du déploiement (3 comptes) avant le 10/12 |
