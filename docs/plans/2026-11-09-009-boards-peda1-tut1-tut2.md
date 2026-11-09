# Archive des planches peda1, tut1 et tut2 (2026-11-09)

Contenu intégral des trois planches de décision publiées en ligne, avec les réponses de NG.
But : garder dans le dépôt les constats (fichiers, lignes, chiffres) et le détail des options retenues,
qui servent à la rédaction des phases 2 (jours 3-4) et 3 (jours 5-6).

**Ordre d'autorité.** Les décisions font foi dans `2026-11-09-006-edition2-decisions.md` (§ 2bis pour peda1, § 2quater pour tut2).
Cette archive donne le contexte. En cas d'écart, le journal des décisions l'emporte.

**Passages dépassés depuis la planche** (à ne pas appliquer tels quels) :
- Toute mention d'un « courriel J-7 », d'une « installation faite à J-7 » ou de « prérequis GitHub à J-7 » : remplacée par P19 (aucun contact avant ni entre les blocs). Tout se fait en salle au jour 1.
- P5 (« solo ») et la planche tut1 entière : remplacés par la conception du tuteur de tut2 (§ 2quater). Il n'y a plus de `@tutor`.
- Calendrier de « ampleur » (semaines du 27/11 et du 04/12) : remplacé par les trois phases du § 2ter.
- Le calendrier de l'AI Act cité dans « concepts » a depuis été vérifié : règlement (UE) 2026/1744 « Omnibus » (voir § 3 du journal).

## Planche `peda1` — Pédagogie AI4SE éd. 2

En ligne : https://claude.ai/artifact/7wcS6JAZw17iYodeGYzjxV

**Ta demande.** Avant de lancer le travail sur les supports, une analyse qualitative du contenu **et de la forme pédagogique**, en tenant compte des commentaires existants. Rien n'a été modifié.

**Ce qui a été lu.** Six analyses en parallèle, en lecture seule : (1) les dépôts des 12 apprenants d'avril (≈ 530 messages réellement tapés, notes, transcripts) ; (2) les modules du jour 1 avec les revues de mars-avril ; (3) les decks du jour 1 après-midi et du jour 2 ; (4) la théorie GSE-One ; (5) les pratiques P1-P8 et les jours 5-6 ; (6) la conception d'ensemble (programme publié, fiche d'information, cahier des charges DLH, planning). Les commentaires pris en compte : les revues de contenu de mars-avril (beaucoup de points encore ouverts : interactivité, minutage, objectifs, quiz), les errata, le rapport de retours d'avril (côté plugin) et ce que disent les dépôts des apprenants.

**Le constat en une phrase.** L'arc du cours est excellent (coder sans règles, découvrir la discipline, piloter son projet) et les pratiques sont bien conçues, mais la forme n'est pas prête pour un formateur seul avec 20 apprenants sous opencode : supports encore centrés sur Cursor, aucun rattrapage, git trop tard, jours 5-6 non conçus, aucune évaluation ni aucun retour.

**À noter, hors planche.** Un fichier du dossier partagé d'avril (Drive, 260409-DLH/_trainer/.env.template) contient un vrai jeton Coolify : à retirer du dossier partagé en plus de la rotation déjà prévue. Les dépôts d'avril contiennent des noms réels : ne pas les réutiliser tels quels dans un support.

**Comment répondre.** Une ou plusieurs cases par question ; aucune case = « pas décidé ». Un commentaire par proposition, par question et un global. « Cocher les recommandations » part de mes choix ; « Copier ma sélection » copie une ligne commençant par `peda1` à coller dans la conversation. La question 1 fixe l'enveloppe ; les autres se lisent à l'intérieur de cette enveloppe.

**Ce que ça déclenche.** Rien avant ta ligne. Tout le travail se fera sur la branche `edition2` d'ai4se6d (aucun redéploiement), avec export de contrôle de chaque module.

### peda1 · `ampleur` — 1. Combien de temps investir dans la pédagogie avant le 26/11 ?

**Le problème.** Il reste 17 jours avant le jour 1, et le plan déjà décidé (import du jour 2, starter CalcApp, installation opencode, rafraîchissement ciblé) occupe déjà l'essentiel. Les analyses proposent en plus des changements de forme pédagogique (évaluation légère, git plus tôt, cadrage du mini-projet, kit pour formateur seul). Il faut choisir un niveau d'investissement, sinon tout sera fait à moitié.

**Ce qu'on a trouvé.** Les six analyses convergent sur 5 manques majeurs : (1) les supports parlent encore de Cursor partout, (2) aucun moyen de rattrapage pour un apprenant qui décroche, (3) git enseigné après en avoir eu besoin, (4) jours 5-6 non conçus (mini-projet, démos, dépôt), (5) aucune évaluation ni retour recueilli en édition 1. Les trois premiers jours de l'édition 2 sont les 26-27/11 ; les jours 3-4 le 03-04/12 ; les jours 5-6 le 10-11/12 : les semaines entre les blocs permettent d'étaler le travail.

**Recommandation de la planche.** Cocher « Ciblé et étalé » : on fait avant le 26/11 ce qui touche les jours 1-2 et l'installation, puis on prépare les jours 3-4 pendant la semaine du 27/11 et les jours 5-6 pendant celle du 04/12.

**Réponse de NG.** `cible-etale`, `complet`
> Si on travaille nuit et jour, ça devrait tenir. Mais effectivement tu peux le faire en trois phases d'abord les deux premiers jours suivi des deux suivants suivi des deux suivants et on verra bien ce qu'on arrive à faire. Et quel jour on est quand t'auras quand on aura fini les deux premiers jours.

- ✅ RETENUE — **`cible-etale` — Ciblé et étalé dans le temps (≈ 11 jours en plus du plan décidé, dont ≈ 5 avant le 26/11)** *(recommandée par la planche)*
  - Contenu : Avant le 26/11 : questions 2 à 8 (jour 2, opencode, rattrapage, kit solo, retours). Semaine du 27/11 : questions 9 à 13 (jours 3-4). Semaine du 04/12 : questions 14 à 17 (jours 5-6). Effort : ≈ 5 j avant le 26/11, ≈ 4 j semaine du 27/11, ≈ 2,5 j semaine du 04/12.
  - ➕ Chaque jour est prêt juste à temps
  - ➕ Les retours des jours 1-2 servent à ajuster la suite
  - ➖ Le plan décidé remplissait déjà presque tout le temps avant le 26/11 : il faudra couper dans sa vague 3 (après la formation)
  - ➖ Tu prépares les blocs suivants pendant que tu enseignes
  - ➖ Conséquence : Ordre de coupe si le temps manque : les questions sans « fort » d'abord, puis les options les plus coûteuses.
- **`minimal` — Minimal : seulement les corrections qui empêchent l'erreur (≈ 3 jours)**
  - Passe opencode, chiffres faux, déploiement J5 fiable, cadrage écrit du mini-projet. Pas de refonte du jour 2, pas d'évaluation.
- ✅ RETENUE — **`complet` — Refonte complète sur un nouveau squelette de 6 jours (≈ 10 jours et plus)**
  - Contenu : Adopter le squelette jour par jour proposé (23 % cours, 55 % pratique, 21 % interaction), 5 points de contrôle par tests, refonte du jour 2 et de la théorie GSE-One.
  - ➕ Cours nettement meilleur
  - ➕ Répond aussi à la demande d'évaluation continue de DLH
  - ➖ Dépasse le temps disponible
  - ➖ Risque de supports non relus le jour J
  - ➖ Conséquence : Probablement à reporter sur l'édition 3.

### peda1 · `j2` — 2. Quelle forme pour le jour 2 (import du deck de l'ancien co-formateur) ?

**Le problème.** Le jour 2 est la pièce la plus importante à reconstruire. L'idée directrice est excellente : le jour 1 on code « sans règles », le jour 2 on découvre la discipline (planifier, tests d'abord, revue par l'IA, git). Mais la forme a trois défauts : le plan que les apprenants écrivent n'est jamais utilisé (l'après-midi suit un script fixe), git arrive en dernier alors qu'on en a besoin dès le matin, et la matinée est passive (90 minutes de démonstration, 15 minutes de pratique, environ 35 notions nouvelles).

**Ce qu'on a trouvé.** Deck du jour 2 : ≈ 237 diapositives pour 345 minutes, ≈ 40 % de pratique réelle, 15 % entre 9h et 10h45. Contradictions de contenu : « l'humain écrit les tests » mais chaque exercice dit « demande à l'agent d'écrire le test » ; la revue de code porte sur un calcul de budget qui n'existe pas dans la v0.1 ; « ne jamais faire git add . » puis git add . dans l'exercice ; commits directement sur main alors que GSE-One bloque les commits sur main au jour 3. Traces d'avril : des apprenants dupliquaient le dossier du projet au lieu de faire des branches, l'un écrit « le moment où il faut faire git init… ».

**Recommandation de la planche.** Cocher « Hybride : ordre du deck gardé, git d'abord, plan utilisé » : il prend l'essentiel du plan B pour un coût proche du plan A.

**Réponse de NG.** `plan-b`

- ✅ RETENUE — **`plan-b` — Restructuré autour de CalcApp, git d'abord (plan B)**
  - Contenu : 9h15 : 35 min de git sur le starter (status, diff, commit, une branche par fonctionnalité, restaurer). Puis piloter l'agent opencode (AGENTS.md, contexte, agent plan/build). Le plan écrit par l'apprenant pilote ensuite la construction. Revue par l'IA sur le diff du jour avec un tri HIGH / MEDIUM / LOW (le format de GSE-One). Fin : une diapositive qui met la boucle manuelle du jour en face des commandes GSE-One. Effort : ≈ 3-4 j.
  - ➕ Chaque notion est pratiquée sur un fil unique
  - ➕ Prépare directement le jour 3 (branches, revue, tri)
  - ➕ Rattrapage possible grâce aux étiquettes git
  - ➖ Réécriture plus profonde
  - ➖ Moins de diapositives réutilisées telles quelles
  - ➖ Conséquence : Le starter CalcApp doit porter 3 étiquettes : j2-start, j2-part1, j2-v0.1.
- **`hybride` — Hybride : ordre du deck gardé, git d'abord, plan utilisé** *(recommandée par la planche)*
  - On garde la structure du deck condensé, mais : un bloc git de 35 min ouvre la journée (dans le starter cloné, branche par fonctionnalité) ; l'atelier de planification porte exactement sur les récits construits ensuite (le script devient une « solution de référence ») ; la matinée alterne « je montre 5 min / vous essayez 5 min » ; diapositive pont vers GSE-One en fin de journée. Effort : ≈ 2,5 j (≈ 1 j de plus que l'import condensé).
- **`plan-a` — Condensé fidèle (plan A)**
  - On garde l'ordre d'origine, on condense la matinée en alternance « je montre 5 min / vous essayez 5 min », on ajoute 10 min de git au démarrage, git complet reste en fin de journée. Effort : ≈ 2 j.
- **`statu-quo` — Import condensé sans changer la forme (décision 9 telle quelle)**
  - Traduction Cursor → opencode et suppression des doublons, sans toucher à l'ordre ni aux exercices. Effort : ≈ 1,5 j.

### peda1 · `opencode` — 3. Passer tous les supports à opencode

**Le problème.** Les apprenants utiliseront opencode, mais les supports parlent encore de Cursor partout : l'atelier du jour 1 dit « laissez Cursor tout générer », le principe 3 cite .cursorrules au lieu d'AGENTS.md, les pratiques GSE disent « ouvrez Cursor » et « dossier .cursor », la théorie GSE compte 33 mentions de Cursor contre 4 d'opencode, et 62 blocs affichent la forme /gse:go (Claude Code) alors qu'opencode utilise /gse-go. En avril, la confusion /gse: contre /gse- a déjà bloqué des apprenants (les deux formes mélangées chez 4 apprenants, plus des formes fausses comme « /gse go »).

**Ce qu'on a trouvé.** Vérifié dans les blocs : bck_exercise_vibecoding.py:51, bck_vibeeng_p_architecture.py:60-64, practice_p1.py:99-129, practice_p2 à p8 (une mention chacun), plugin_cursor.py, t4_decisions.py:250 (les hooks ne citent que Claude Code et Cursor). Le module « various » compare Claude Code et Cursor sans opencode et affirme à tort que Cursor n'a pas de hooks.

**Recommandation de la planche.** Cocher « Passe complète ».

**Réponse de NG.** `complete`

- ✅ RETENUE — **`complete` — Passe complète** *(recommandée par la planche)*
  - Contenu : Pratiques en forme /gse-…, théorie en /gse: avec un bandeau unique « dans opencode : /gse-… ». Le bloc plugin_cursor devient « GSE-One dans opencode » (.opencode/, AGENTS.md, /gse-go, la fenêtre de question, la commande d'installation épinglée v0.90.0). Hooks : ligne opencode ajoutée. Effort : ≈ 4-5 h.
  - ➕ L'apprenant retrouve exactement son outil
  - ➕ Supprime la friction la plus visible d'avril
  - ➖ Deux notations coexistent dans le deck
  - ➖ Conséquence : Les captures d'écran viennent de la répétition générale (question 4).
- **`texte` — Remplacement de texte seulement**
  - Cursor → opencode et /gse: → /gse- là où c'est une consigne ; plugin_cursor retiré. Effort : ≈ 1,5 h.
- **`rien` — Ne rien changer**
  - On garde le support tel quel sur ce point.

### peda1 · `rattrapage` — 4. Un point de départ unique et des points de reprise

**Le problème.** Avec 20 apprenants et un seul formateur, un apprenant qui rate une étape (installation, P1, P3) est hors jeu pour le reste de la journée, voire deux jours, car chaque exercice repart de son propre dépôt. Aujourd'hui il n'existe aucun point de reprise : les branches CalcApp v0 à v5 datent d'avant GSE (pas de dossier .gse/), la reprise annoncée au jour 2 (« 2 tests verts ») ne correspond à aucune branche, et le dépôt calcapp-course est privé, donc impossible à cloner par les apprenants. De plus, la pratique P1 parle d'un « dossier vide » alors que la décision 10 prévoit un starter : sur un dossier vide, GSE recommandera probablement le mode Micro, ce qui contredit la consigne « choisissez Full ».

**Ce qu'on a trouvé.** Vérifié : branches v0-plans … v5-production sans .gse/ ; la branche v1-skeleton contient déjà tout le résultat de la v0.1 (un apprenant remis à niveau n'aurait plus rien à faire) ; seule aide écrite en P8 : « demande à l'agent ce qu'il faut faire ».

**Recommandation de la planche.** Cocher « Starter public + étiquettes + répétition complète ».

**Réponse de NG.** `tags`

- ✅ RETENUE — **`tags` — Starter public + étiquettes de reprise + répétition générale P1 → P8** *(recommandée par la planche)*
  - Contenu : Rendre le starter clonable (dépôt modèle public ou miroir). Faire une répétition complète des jours 2 à 4 avec opencode, GSE v0.90.0 et le modèle de référence. À cette occasion, poser des étiquettes git à des points propres : j2-start, j2-part1, j2-v0.1, p3-start, p5-start, p6-start, p7-start, p8-start. Une diapositive « En retard de plus de 15 min ? » donne la commande de reprise (clone de l'étiquette, installation épinglée, /gse-go). Effort : ≈ 1,5-2 j.
  - ➕ Rattrapage en 3 minutes sans toi
  - ➕ La répétition donne les vraies durées et les résultats attendus
  - ➕ Fournit les captures d'écran opencode
  - ➖ Coût de la répétition
  - ➖ Le starter devient public (il ne contient rien de sensible)
  - ➖ Conséquence : La répétition est déjà nécessaire pour l'installation : on la rentabilise.
- **`binomes` — Binômes de secours seulement**
  - Le retardataire suit l'écran de son voisin jusqu'à la pause.
- **`rien` — Ne rien changer**
  - On garde le support tel quel sur ce point.

### peda1 · `solo` — 5. Un kit pour animer seul 20 apprenants

**Le problème.** En avril, il y avait deux formateurs pour 12 apprenants ; en décembre, un seul pour 20, soit environ 3 fois plus de demandes par formateur. Trois pics de support sont prévisibles : installation (jour 1), git (jours 2-3), déploiement (jour 5). Les supports reposent 11 fois sur « je circule, demandez au formateur ». Sans dispositif, tu ne vois que ceux qui lèvent la main, et ceux qui décrochent en silence (5 sur 12 en avril, sans aucune trace) passent inaperçus.

**Ce qu'on a trouvé.** La vue formateur en lecture seule et le script check-learner.sh sont déjà décidés (planche gsel1) mais pas écrits. Les traces d'avril montrent des attentes sans savoir si l'agent travaille (« c'est normal que ça prenne autant de temps ? ») et des messages renvoyés deux fois.

**Recommandation de la planche.** Cocher « Kit simple » et « Feuille de suivi partagée ».

**Réponse de NG.** aucune option cochée
> Je propose de développer un agent qui sera disponible sur opencode qu'il soit mon clone et que les participants peuvent solliciter pour toute question s'ils sont perdus tout au long de la formation

- **`kit` — Kit simple : binômes, cartons, FAQ** *(recommandée par la planche)*
  - Binômes fixes de niveaux mélangés (formés grâce à l'enquête de J-7). Règle « trois avant moi » : la fiche, le binôme, la FAQ, puis le formateur. Cartons vert / orange / rouge sur l'écran. FAQ imprimée des 10 erreurs les plus fréquentes (forme des commandes, choix du mode, clé, git, attente de l'agent, déploiement). Effort : ≈ 0,5 j.
- **`feuille` — Feuille de suivi partagée (une ligne par apprenant et par pratique)** *(recommandée par la planche)*
  - État, blocage, une ligne copiée de /gse-status. Alimentée en fin de pratique ; complétée par la vue formateur (lecture des dépôts GitHub) quand elle existe. Effort : ≈ 2 h.
- **`renfort` — Demander à DLH un renfort informatique aux deux pics**
  - Une personne de DLH le jour 1 de 13h30 à 15h et le jour 5 pendant le déploiement.
- **`rien` — Ne rien changer**
  - On garde le support tel quel sur ce point.

### peda1 · `modeles` — 6. Un modèle de référence pour les ateliers

**Le problème.** En avril, chaque apprenant choisissait son modèle (Codex, Opus, Composer, GPT, Sonnet, un modèle gratuit). Résultat : beaucoup de temps passé à comparer, des sorties impossibles à comparer entre voisins, et le modèle gratuit utilisé sous opencode coupait ses phrases et cassait 3 fois le fichier backlog.yaml. En décembre, chacun aura une clé plafonnée (décision 5) donnant accès à des dizaines de modèles : le problème sera plus fort, et un plafond épuisé en plein atelier bloque l'apprenant.

**Ce qu'on a trouvé.** 5 apprenants sur 7 ayant déposé ont changé de modèle ; une apprenante a construit CalcApp deux fois pour comparer et en a tiré une note très juste (« GPT suivait mieux le périmètre, Opus demandait plus de pilotage »).

**Recommandation de la planche.** Cocher « Modèle imposé pendant les ateliers + comparaison cadrée ».

**Réponse de NG.** `impose`

- ✅ RETENUE — **`impose` — Un modèle imposé pendant les ateliers, un modèle de secours, et une comparaison cadrée** *(recommandée par la planche)*
  - Contenu : Le modèle de référence est fixé dans la configuration opencode distribuée, testé avec GSE v0.90.0 pendant la répétition. Un modèle de secours moins cher si le plafond approche. Une phrase sur chaque fiche : « comparez la structure, pas les mots ». Une heure de comparaison cadrée (même consigne, deux modèles, une grille) transforme la curiosité en exercice. Effort : ≈ 4-6 h de tests.
  - ➕ Démos et résultats reproductibles
  - ➕ Coût prévisible des clés
  - ➖ On montre moins la diversité des modèles (gardée en démo et dans l'heure cadrée)
  - ➖ Conséquence : Le choix du modèle dépend du budget des clés, encore ouvert.
- **`libre` — Libre choix, avec une liste conseillée**
  - On recommande 2-3 modèles sans les imposer.
- **`rien` — Ne rien changer**
  - On garde le support tel quel sur ce point.

### peda1 · `retours` — 7. Recueillir enfin les retours des apprenants

**Le problème.** En avril, aucun retour pédagogique formel n'a été recueilli. Les seules traces sont les dépôts volontaires, qui ne montrent que les apprenants les plus avancés : ceux qui ont décroché ne laissent rien. Sans retour, impossible d'ajuster l'édition en cours ni de prouver la qualité à DLH.

**Ce qu'on a trouvé.** Dépôts d'avril : 7 apprenants sur 12 au dossier DAY04, 4 au DAY05, 5 au DAY06 ; rien pour les jours 1 à 3 ; 5 apprenants n'ont jamais rien déposé. DLH a peut-être son propre questionnaire de satisfaction (à demander).

**Recommandation de la planche.** Cocher « Trois instruments légers ».

**Réponse de NG.** `final`
> Pour pouvoir corriger des choses en cours de route, je préfère donner la possibilité aux participants de créer des tickets sur le site github de GSE puisque de toute façon la compétence est dans le kit

- **`trois` — Trois instruments légers** *(recommandée par la planche)*
  - Un ticket de sortie chaque soir (3 questions : ce que j'ai appris, où je bloque, une question ; 2 minutes, formulaire). Un « continuer / arrêter / commencer » à la fin du jour 4. Un questionnaire final rempli en salle avant la clôture, avec une question « promesse tenue ? » par session du programme. Demander d'abord à DLH s'ils ont le leur. Effort : ≈ 0,5 j.
- ✅ RETENUE — **`final` — Questionnaire final seulement**
  - Contenu : Un formulaire en fin de jour 6.
  - ➕ Très peu de travail
  - ➖ Rien ne peut être corrigé en cours de route
  - ➖ Conséquence : Utile seulement pour l'édition 3.
- **`rien` — Ne rien changer**
  - On garde le support tel quel sur ce point.

### peda1 · `verif` — 8. Vérifier ce qui est appris (évaluation légère, sans note)

**Le problème.** La décision 17 garde un certificat de simple présence, alors que le cahier des charges de DLH demande une « évaluation continue par validation de tests ». Sans aucun point de contrôle, tu ne sais pas qui a compris, et l'écart avec DLH reste entier. Le cahier des charges dit aussi qu'il n'y a « pas d'examen » : une vérification sans note est donc compatible avec la présence comme critère du certificat.

**Ce qu'on a trouvé.** Aucun quiz n'existe dans les modules, alors que les revues de mars-avril l'avaient déjà demandé (module GenAI, vibecoding, GSE-One : « 3 questions de vérification »). La matinée du jour 1 est à environ 90 % d'exposé entre 10h et 10h45.

**Recommandation de la planche.** Cocher « Quiz à main levée + points de contrôle par tests ».

**Réponse de NG.** `quiz-seul`

- **`quiz-tests` — Quiz à main levée + points de contrôle par tests verts** *(recommandée par la planche)*
  - Trois questions A/B/C/D affichées sur une diapositive après chaque grand bloc (main levée, aucun outil). Aux moments clés (fin du jour 2, fin des pratiques P5 et P7, fin du mini-projet), l'apprenant montre « tests verts » et pousse son code : c'est noté dans la feuille de suivi. Cela répond à la lettre de DLH (validation par tests) sans note. Effort : ≈ 1-1,5 j.
- **`vote` — Même chose avec un outil de vote en ligne (Wooclap, Mentimeter)**
  - Les quiz deviennent des votes enregistrés.
- ✅ RETENUE — **`quiz-seul` — Quiz à main levée seulement**
  - Contenu : Pas de points de contrôle par tests.
  - ➕ Léger
  - ➖ Aucune trace objective
  - ➖ Conséquence : L'écart avec DLH reste.
- **`rien` — Ne rien changer**
  - On garde le support tel quel sur ce point.

### peda1 · `chiffres` — 9. Remettre les chiffres et les faits à jour

**Le problème.** Des professionnels vérifient les sources. Plusieurs chiffres affichés sont faux ou datés, ce qui fragilise tout le discours « fondé sur des preuves ». Exemples : les chiffres d'adoption annoncés « 2026 » sont ceux de Stack Overflow 2024 (la source pointe vers 2024) ; « GPT-3 (2022) » au lieu de 2020 ; l'étude METR affichée « +19 % » sur une diapositive et « −19 % » sur une autre, alors que METR a lui-même déclaré ce résultat historique en février 2026 ; 29 % et 33 % de confiance sur la même diapositive ; benchmarks et modèles « de pointe » d'avril 2026 ; le chiffre Forrester toujours faux en théorie GSE ; GSE-One noté ✓✓ partout, y compris « entreprise », alors qu'il est en pré-version et que tu en es l'auteur.

**Ce qu'on a trouvé.** Fichiers : bck_poll_ai_result.py:44, references.bib:209-215, bck_genai_revolution.py:59, bck_vibecoding_danger_metr.py:59, bck_vibecoding_danger_trust.py:74-95, bck_llm_context_benchmark.py, evidence_perception.py, frameworks.py:179-255, fw_synthesis.py:36. Les errata E1 et E4 de la revue d'avril ne sont pas reportés.

**Recommandation de la planche.** Cocher « Correction et mise à jour, avec une fiche des sources ».

**Réponse de NG.** `maj`

- ✅ RETENUE — **`maj` — Correction et mise à jour, avec une fiche des sources** *(recommandée par la planche)*
  - Contenu : Passer aux chiffres Stack Overflow 2025 ou 2026 vérifiés à la source, corriger les dates et les signes, ajouter la mise à jour METR 2026, refaire les captures de benchmarks le 23-24/11 avec la mention « au 24/11/2026 », corriger Forrester, ajouter « auteur = formateur, pré-version » à la ligne GSE-One du comparatif. Une page formateur liste chaque chiffre affiché, sa source et sa date. Effort : ≈ 5-6 h.
  - ➕ Crédibilité restaurée
  - ➕ Tu es armé face aux objections
  - ➖ À refaire à chaque édition pour les benchmarks
  - ➖ Conséquence : La fiche des sources sert aussi aux éditions suivantes.
- **`erreurs` — Seulement les erreurs (dates, signes, sources fausses)**
  - On corrige ce qui est faux, on laisse les chiffres datés.
- **`rien` — Ne rien changer**
  - On garde le support tel quel sur ce point.

### peda1 · `concepts` — 10. Ajouter les notions qui manquent au jour 1

**Le problème.** Le jour 1 explique comment fonctionne un LLM, puis l'après-midi les apprenants pilotent un agent (opencode) qui lit des fichiers, lance des commandes et demande des permissions. Or la notion d'agent (modèle + outils + boucle + permissions) n'est expliquée nulle part le matin. Autres manques : le lien entre tokens et coût (chacun aura une clé plafonnée), le fait que le modèle n'a pas de mémoire entre les sessions (un apprenant croyait en avril que « la base de connaissance est sauvegardée dans le modèle »), le paysage réel des modèles (seulement 3 fournisseurs américains, sans modèles ouverts, sans Mistral, sans modèles chinois), et l'éthique réduite à 4 puces sans l'AI Act.

**Ce qu'on a trouvé.** AI Act : 0 occurrence dans les deux modules. Calendrier vérifié sur sources secondaires (à confirmer sur EUR-Lex avant affichage) : culture IA obligatoire pour les employeurs depuis le 2/2/2025 (article 4, accroche directe pour ta formation), obligations des modèles généraux depuis le 2/8/2025, application générale le 2/8/2026, report du haut risque au 2/12/2027 par l'accord « Digital Omnibus » de mai 2026.

**Recommandation de la planche.** Cocher « Quatre diapositives ciblées ».

**Réponse de NG.** `quatre`
> Attention, tu dois prendre en compte le fait que tout le matériel existe déjà dans différents modules de formation ici : streamtex-all-trainings. Donc il faut décider d'importer les blocs utiles pour cette formation GSE depuis les autres formations, en attendant une approche unifiée que nous puissions migrer toute la formation GSE dans all-trainings.

- ✅ RETENUE — **`quatre` — Quatre diapositives ciblées** *(recommandée par la planche)*
  - Contenu : (1) « Du LLM à l'agent » avec l'exemple d'opencode. (2) « Le modèle n'a pas de mémoire : la continuité, ce sont les fichiers et git » + « que faire pendant que l'agent travaille ». (3) Paysage en 4 familles (fermés américains, modèles ouverts, Mistral et UE, modèles chinois) + « ce que votre clé vous donne » + tokens = coût. (4) AI Act : frise + règles pratiques de la semaine (ce qu'on ne colle pas dans un prompt, quelles permissions donner à l'agent). Effort : ≈ 1 j.
  - ➕ Prépare directement l'après-midi et la clé plafonnée
  - ➕ Répond à la décision 18 (éthique et AI Act)
  - ➖ ≈ 1 jour
  - ➖ Le calendrier de l'AI Act doit être vérifié à la source
  - ➖ Conséquence : La matinée déborde déjà : à compenser par la question 12.
- **`deux` — Deux diapositives seulement (agent + mémoire)**
  - L'AI Act est renvoyé au jour 6, appliqué au projet de chacun.
- **`rien` — Ne rien changer**
  - On garde le support tel quel sur ce point.

### peda1 · `theorie` — 11. Alléger la théorie GSE-One du jour 3

**Le problème.** Le jour 3 commence, après une semaine de coupure, par environ 40 diapositives de recherche avant de voir GSE-One. Le bloc suivant introduit environ 60 termes nouveaux en 45 minutes (cycles, modes, 24 commandes, 11 agents, fichiers .gse/, identifiants…), et le mot « mode » y a 5 sens différents. Environ 25 diapositives répètent le bloc juste précédent (le profil de l'apprenant 2 fois, le cycle de vie 3 fois, la règle 80/20 5 fois, les cadres méthodologiques refaits en fin de jour 4). La répétition aide quand elle est espacée, pas quand elle est collée.

**Ce qu'on a trouvé.** book.py du module gensem : 95 blocs actifs, ≈ 140 infobulles qui portent l'essentiel des explications (visibles seulement si tu les survoles). La pratique P1 est appelée deux fois (lignes 122 et 152). Point fort à garder : P1 fait vivre la méthode avant la théorie, puis un débrief relie chaque vécu à un principe.

**Recommandation de la planche.** Cocher « P1 en premier + liste de diapositives à sauter ».

**Réponse de NG.** `leger`

- ✅ RETENUE — **`leger` — P1 en premier + liste de diapositives à sauter** *(recommandée par la planche)*
  - Contenu : Garder P1 juste après la vidéo d'ouverture (supprimer le doublon), présenter la recherche comme « pourquoi ce que vous venez de vivre existe ». Préparer une liste de diapositives sautées en direct (doublons). Désactiver les cadres méthodologiques du jour 4 (déjà vus au jour 3). Effort : ≈ 1 h.
  - ➕ On démarre par l'action
  - ➕ Aucun risque de casser les blocs
  - ➖ Les doublons restent dans le code
  - ➖ Conséquence : La vraie fusion des blocs se fait après le 11/12.
- **`fusion` — Fusionner réellement les blocs en double**
  - Réécrire les paires « synthèse + commande » de book.py.
- **`rien` — Ne rien changer**
  - On garde le support tel quel sur ce point.

### peda1 · `orientation` — 12. Une carte d'orientation et un aide-mémoire GSE-One

**Le problème.** En avril, la plainte la plus fréquente des apprenants était « on en est où ? », « c'est quoi la suite ? », « le sprint est-il fini ? » (6 apprenants sur 7 ayant déposé ; l'un a tapé 11 questions de ce type en une journée ; des projets ont gonflé jusqu'au sprint 6 ou 19). Les apprenants ne savent pas non plus quoi faire quand l'agent part de travers. Et la fiche finale « à emporter pour les jours 5-6 » décrit… l'ancienne méthode manuelle (règles Cursor), pas GSE-One.

**Ce qu'on a trouvé.** method_checklist.py:23-68 (« Carry this checklist for Day 5–6! », règles .cursor). Rien dans le cours sur la reprise : option « Discuss », /gse-status, pause et reprise, étiquettes de sauvegarde gse-backup/ (tout existe dans GSE-One v0.89-v0.90). Le choix entre les modes Complet / Allégé / Micro n'est pas guidé (4 apprenants concernés).

**Recommandation de la planche.** Cocher « Une page imprimée ».

**Réponse de NG.** `page`

- ✅ RETENUE — **`page` — Une page imprimée remise au jour 3 (et en PDF)** *(recommandée par la planche)*
  - Contenu : Recto : les activités dans l'ordre, « où suis-je ? » (/gse-status), quand un sprint est fini (livraison → capitalisation), règle des modes (CalcApp en Complet, mini-projet en Allégé), une seule forme de commande /gse-…. Verso : « quand l'agent dérape » en 6 étapes (Discuss → /gse-status → refuser le changement → /gse-pause puis /gse-resume → étiquette de sauvegarde → appeler le formateur) + 5 lignes « que faire si… ». Remplace la fiche de l'ancienne méthode. Effort : ≈ 3 h.
  - ➕ Répond à la première plainte d'avril
  - ➕ Rend les apprenants autonomes
  - ➖ Impression à prévoir
  - ➖ Conséquence : Une diapositive « quand l'agent dérape » est ajoutée en théorie.
- **`diapo` — Diapositives seulement**
  - Même contenu, projeté, sans support papier.
- **`rien` — Ne rien changer**
  - On garde le support tel quel sur ce point.

### peda1 · `gates` — 13. Apprendre à vraiment décider aux points de décision

**Le problème.** Le cœur de GSE-One est que l'humain décide aux moments importants (les « Gates » : l'agent s'arrête et propose des options). En avril, environ 23 % des messages des apprenants étaient des validations d'un mot (« go », « ok », « approved », « 1 ») ; un apprenant a répondu 15 fois « approved » d'affilée de la planification à la revue, un autre a demandé « plus d'autonomie, tu me demandes trop de choses ». La méthode est donc utilisée sans être comprise.

**Ce qu'on a trouvé.** Contre-exemples à montrer : deux apprenants ont fait de vraies revues (« 4 points à corriger et 3 à clarifier avant de valider », « étape 1 seulement, ne commence pas l'étape 2 »).

**Recommandation de la planche.** Cocher « Grille de 3 questions + règle d'un refus par activité ».

**Réponse de NG.** `grille`

- ✅ RETENUE — **`grille` — Grille de 3 questions + au moins une modification ou un refus par activité sur CalcApp** *(recommandée par la planche)*
  - Contenu : À chaque Gate : « je comprends ce qui est proposé ? », « qu'est-ce que je perds si c'est faux ? », « aurais-je choisi autrement ? ». Pendant les pratiques CalcApp, chaque apprenant doit modifier ou refuser au moins une proposition par activité, et le noter dans la feuille de suivi. Effort : ≈ 2 h.
  - ➕ Rend la décision humaine visible
  - ➕ Rejoint la pratique P4 (classer les décisions), le moment le plus actif de la théorie
  - ➖ Ralentit un peu les pratiques
  - ➖ Conséquence : Les deux bons exemples d'avril deviennent une diapositive (anonymisée).
- **`binome-revue` — Revue en binômes : l'un relit les décisions de l'autre**
  - Toutes les 45 minutes, échange de 5 minutes.
- **`rien` — Ne rien changer**
  - On garde le support tel quel sur ce point.

### peda1 · `exercices` — 14. Une fiche d'exercice standard et des durées réalistes

**Le problème.** Les pratiques sont bien conçues (3 niveaux, guidage décroissant de P1 à P8), mais le but, la durée et le livrable sont cachés dans une infobulle ; aucun critère visible ne dit « c'est fini quand… » ; il n'y a pas de débrief de P2 à P8 ; on ne sait pas qui choisit le niveau ni comment l'apprenant voit son niveau quand tu projettes les trois à la suite. Les durées sont irréalistes : P1 fait tenir en 45 minutes l'installation, le profil (jusqu'à 12 questions) et trois phases ; P8 demande environ 12 commandes et 7 critères en 45 minutes.

**Ce qu'on a trouvé.** practice_p3.py:42-50 (infobulle), practice_p8.py:54-180. Le déroulé minute par minute et le débrief final du plan d'avril ont disparu des blocs.

**Recommandation de la planche.** Cocher « Fiche standard + P1 à 60 min + P8 remplacé par le lancement du mini-projet ».

**Réponse de NG.** `fiche`
> Il ne faut pas hésiter à augmenter les durées de pratique effectivement si nécessaire

- ✅ RETENUE — **`fiche` — Fiche standard + P1 à 60 min + P8 remplacé par le lancement du mini-projet** *(recommandée par la planche)*
  - Contenu : Sur chaque diapositive d'exercice : but (1 ligne), étapes, « fini quand » observable (ex. « /gse-status affiche le plan validé »), point à mi-parcours, « si bloqué » (renvoi à la question 4), débrief de 5-10 minutes (2 questions + comparaison avec le voisin). Niveau = celui déclaré au profil ; l'apprenant ouvre le deck sur sa machine. P1 passe à 60 minutes (installation faite à J-7). P8 devient le lancement du mini-projet en fin de jour 4 (fiche projet + /gse-go). Effort : ≈ 1 j.
  - ➕ L'apprenant sait quand il a réussi
  - ➕ Le mini-projet mûrit une semaine au lieu de 20 minutes
  - ➖ Plus de sprint solo complet sur CalcApp
  - ➖ Conséquence : Libère du temps au jour 5.
- **`fiche-p8` — Fiche standard, P8 gardé avec une portée minimale et 75 minutes**
  - P8 = une petite fonctionnalité (thème sombre), critères réduits.
- **`rien` — Ne rien changer**
  - On garde le support tel quel sur ce point.

### peda1 · `depot` — 15. Le dépôt des travaux comme sous-produit du travail

**Le problème.** En avril, le dépôt des travaux était un geste séparé, volontaire, sans consigne de format ni de nommage : 5 apprenants sur 12 n'ont rien déposé, des fichiers ont été mal rangés, certains noms contenaient des noms réels. Pour un formateur seul, le dépôt est le principal capteur de ce qui se passe.

**Ce qu'on a trouvé.** Formats hétérogènes (exports Cursor, JSONL bruts, notes, captures). Un fichier du dossier partagé d'avril (_trainer/.env.template) contient un vrai jeton Coolify : la rotation est déjà dans ta liste, mais le fichier doit aussi sortir du dossier partagé.

**Recommandation de la planche.** Cocher « Dépôt GitHub dès le jour 3 ».

**Réponse de NG.** `github`

- ✅ RETENUE — **`github` — Dépôt GitHub dès le jour 3, poussé chaque soir, étiquette « demo » à la fin** *(recommandée par la planche)*
  - Contenu : L'adresse du dépôt est notée dans la feuille de suivi le matin du jour 3 ; push en fin de journée ; dépôt final = étiquette demo + README « fiche projet » (pitch, lancement, adresse en ligne) avant le créneau de démo ; contrôle à 12h15 le jour 6, relance pendant que tout le monde est en salle. Le dépôt GitHub est de toute façon nécessaire pour le déploiement du jour 5 et pour la vue formateur. Effort : ≈ 2 h.
  - ➕ Aucun geste supplémentaire
  - ➕ Code + fichiers .gse/ visibles
  - ➕ Alimente la vue formateur
  - ➖ Suppose git maîtrisé (question 2)
  - ➖ Les apprenants doivent t'inviter si leur dépôt est privé
  - ➖ Conséquence : Les transcripts d'agent ne sont plus collectés (sauf volontaires).
- **`drive` — Drive structuré comme en avril, mieux cadré**
  - Dossiers jour × apprenant créés d'avance, règle de nommage, export de session opencode, 10 minutes en fin de journée.
- **`rien` — Ne rien changer**
  - On garde le support tel quel sur ce point.

### peda1 · `deploy` — 16. Rendre le déploiement du jour 5 fiable

**Le problème.** Le déploiement de CalcApp sur le serveur de la formation risque d'échouer pour tout le monde. Je l'ai vérifié à la lecture : GSE-One classe CalcApp comme une application Node et utilise un modèle de conteneur qui retire les outils de développement (dont Vite), laisse l'étape de construction en commentaire et lance « npm start », alors que CalcApp n'a pas de script start. Le conteneur ne démarrera donc pas : même symptôme qu'en avril (vérification de santé en échec), pour une autre cause. La procédure d'installation du deck du jour 5 est aussi cassée (mode supprimé, commande /go), et les prérequis apprenant (compte GitHub, dépôt poussé, fichier .env.training) ne sont écrits nulle part.

**Ce qu'on a trouvé.** Vérifié : gse-one/src/templates/Dockerfile.node (npm ci --omit=dev, « # RUN npm run build », CMD npm start) ; deploy.py _detect_type (package.json ⇒ node) ; calcapp package.json (scripts dev/build/test, pas de start). En avril, un apprenant a demandé les identifiants administrateur de Coolify pour voir ses logs. À confirmer par un essai réel sur le serveur.

**Recommandation de la planche.** Cocher « Dockerfile testé dans le starter + mode opératoire + répétition ».

**Réponse de NG.** `dockerfile`

- ✅ RETENUE — **`dockerfile` — Dockerfile testé dans le starter + mode opératoire + répétition** *(recommandée par la planche)*
  - Contenu : Le starter fournit un Dockerfile connu (construction Node puis serveur web statique, vérification de santé sans curl) : GSE ne génère le sien que s'il n'en existe pas. Mode opératoire écrit : prérequis GitHub à J-7, dépôt public poussé, copie de .env.training, prénom comme identifiant, /gse-deploy, déploiement par vagues de 5, nettoyage en fin de cours. Répétition sur le serveur avec 3 comptes apprenants. Effort : ≈ 1 j.
  - ➕ Supprime le risque principal du jour 5
  - ➕ Aucune release GSE-One nécessaire
  - ➖ ≈ 1 jour avec la répétition
  - ➖ Conséquence : À faire avant le 10/12 ; les prérequis GitHub partent dans le courriel de J-7.
- **`gse-fix` — Corriger GSE-One : détecter Vite et utiliser un modèle « site statique construit »**
  - Release v0.90.x, nouvel épinglage pour la classe.
- **`demo` — Déploiement montré par toi seulement, les apprenants restent en local**
  - Une démonstration en direct, puis chacun lance son application sur sa machine.

### peda1 · `miniprojet` — 17. Cadrer le mini-projet en une page

**Le problème.** Le mini-projet n'a aucun cadre : « pas de contrainte de technologie, de cadre ni de périmètre ». En avril, 3 mini-projets visibles sur 5 n'ont abouti qu'à des squelettes (un projet avec quatre technologies lourdes en mode Complet n'a terminé que sa première tâche ; des fonctions « faites » n'étaient que des coquilles vides). À l'inverse, les apprenants au périmètre étroit ont déployé et fait une démo. La décision 15 demande un cadrage écrit.

**Ce qu'on a trouvé.** Deck du jour 5 : idée choisie en 10 minutes, aucun jalon, démo au format libre. Avec 20 apprenants à 7 minutes, les démos en plénière prendraient près de 2h45.

**Recommandation de la planche.** Cocher « Une page : règles, jalons, démo structurée ».

**Réponse de NG.** `page`

- ✅ RETENUE — **`page` — Une page : règles de portée, jalons, démo structurée** *(recommandée par la planche)*
  - Contenu : Objectif : montrer qu'on sait piloter un projet avec GSE-One ; on juge la démarche, pas la taille. Règles : un utilisateur, un problème, 2 à 4 exigences essentielles, premier sprint de 8 à 10 points, mode Allégé, pas d'infrastructure multi-services, une technologie déployable (ou son propre Dockerfile). Jalons : fiche projet en fin de jour 4 (validée par toi en 1 minute : « vert » ou « réduis »), exigences et plan validés le jour 5 à 16h30, première livraison le jour 6 à 11h30, gel à midi. Chasse aux coquilles vides le jour 6 au matin (rechercher NotImplemented et TODO, démontrer chaque fonction). Effort : ≈ 0,5 j.
  - ➕ Des projets qui aboutissent
  - ➕ Te protège des 20 entretiens de cadrage
  - ➖ Moins de liberté pour les plus ambitieux
  - ➖ Conséquence : Le projet professionnel reste possible, réduit à une petite évolution (/gse-go --adopt).
- **`catalogue` — Un catalogue de sujets déjà calibrés**
  - 5 à 8 sujets prêts, au choix.
- **`rien` — Ne rien changer**
  - On garde le support tel quel sur ce point.

### peda1 · `cloture` — 18. Concevoir la clôture du jour 6

**Le problème.** Le jour 6 n'est pas conçu : le planning d'avril n'a que des lignes vides et une session « Ethics of AI projects » de 0 minute. La démo du formateur est supprimée (décision 13). Le programme publié promet pourtant des démonstrations, le test des projets par les autres participants et des leçons apprises. C'est le moment le plus visible pour DLH.

**Ce qu'on a trouvé.** La formation se termine aujourd'hui sur un glossaire : ni synthèse, ni « et après ? », ni questionnaire.

**Recommandation de la planche.** Cocher « Galerie en deux rotations + éthique sur son projet + clôture ».

**Réponse de NG.** `galerie`

- ✅ RETENUE — **`galerie` — Galerie en deux rotations + éthique appliquée + clôture** *(recommandée par la planche)*
  - Contenu : Matin : fin du sprint, capitalisation (/gse-compound), puis 30-45 minutes d'éthique, AI Act, licences et sécurité appliquées à son propre projet (« auditez votre projet »). Après-midi : démos de 5-7 minutes à structure imposée (problème, produit, un « moment GSE » montré, leçon, questions) en galerie : 4 tables de 5, chacun présente à sa table, les autres testent avec une grille de 3 questions ; puis 4 projets en plénière. Fin : leçons apprises, plan « lundi matin », questionnaire en salle, certificats, ressources. Effort : ≈ 0,5 j.
  - ➕ Tient la promesse « test par les participants »
  - ➕ Tout le monde reste actif
  - ➖ Une grille d'une page à préparer
  - ➖ Conséquence : L'éthique ne peut plus être sacrifiée : elle passe avant le déjeuner.
- **`pleniere` — Démos de 4 minutes en plénière**
  - Chacun présente à tous (≈ 1h40).
- **`rien` — Ne rien changer**
  - On garde le support tel quel sur ce point.

### peda1 · `entre-blocs` — 19. Préparer l'arrivée et les semaines entre les blocs

**Le problème.** La formation s'étale sur 3 semaines (deux jours par semaine). Rien n'organise l'arrivée (la liste de contrôle à J-7 est décidée mais pas écrite), ni les semaines entre les blocs, ni la reprise de chaque bloc. On ne sait pas encore si les VM conservent le travail d'une semaine à l'autre. Le mini-projet est aujourd'hui choisi sur le moment le jour 5.

**Ce qu'on a trouvé.** Le programme annonce des développeurs expérimentés, mais le public d'avril était mélangé (de l'apprenant au sprint 19 à celui qui s'arrête après le profil). Les plus avancés préparaient leurs consignes avec une autre IA.

**Recommandation de la planche.** Cocher « Courriel J-7 + travail facultatif + rituel de reprise ».

**Réponse de NG.** `rien`
> Je n'ai pas la possibilité de contacter les personnes donc tout le travail doit se faire uniquement pendant la formation. On ne peut pas non plus leur donner du travail à la maison, deux semaines en semaine qui soit obligatoire ou indispensable.

- **`j7` — Courriel J-7 + travail facultatif entre les blocs + rituel de reprise** *(recommandée par la planche)*
  - Courriel le 19/11 : calendrier, pourquoi opencode remplace Cursor (outil ouvert, indépendant du modèle), compte GitHub, VM ou portable, script de vérification, enquête de niveau en 3 questions (sert aux binômes), une idée de projet en un paragraphe. Rappel à J-2. Entre les blocs : 30-60 minutes facultatives (idée de projet après le bloc 1, fiche projet après le bloc 2). Chaque reprise : 15 minutes de quiz + git pull ou /gse-resume. Règle avant de partir : push + /gse-pause. Effort : ≈ 0,5 j.
- ✅ RETENUE — **`rien` — Ne rien changer**
  - Contenu : On garde le support tel quel sur ce point.
  - ➕ Aucun effort
  - ➖ Le problème constaté reste
  - ➖ Conséquence : L'heure d'installation du jour 1 et la reprise de chaque bloc retombent sur toi.

### peda1 · `promesses` — 20. Les objectifs affichés et ce que DLH a demandé

**Le problème.** Les objectifs d'apprentissage publiés ne correspondent pas au cours : ils parlent de « prompts pour des tâches administratives et de support », sans TDD, git ni méthode (ils viennent probablement d'un autre cours). Le programme promet Cursor quatre fois. Le cahier des charges de DLH demande aussi des sujets non couverts : mesure de la qualité (linters, analyse statique, métriques), intégration continue, un petit module serveur, une comparaison solution humaine / solution IA. Tu as décidé de ne pas toucher au programme (décision 20), avec une phrase de cadrage le jour 1.

**Ce qu'on a trouvé.** La branche CalcApp v5-production contient déjà ESLint et une intégration continue, jamais enseignées. GSE-One occupe environ deux tiers du cours sans être nommé dans le programme : à présenter comme un exemple d'une méthode générale.

**Recommandation de la planche.** Cocher « Objectifs réels affichés + 30 minutes sur la qualité ».

**Réponse de NG.** `affiche`

- ✅ RETENUE — **`affiche` — Objectifs réels affichés le jour 1 et dans le courriel J-7, + 30 minutes « mesurer la qualité » le jour 4** *(recommandée par la planche)*
  - Contenu : Une diapositive de 6 objectifs réels rattachés aux sessions du programme ; le programme lui-même ne bouge pas. Le jour 4, 30 minutes sur lint, métriques et intégration continue à partir de la branche v5. Au débrief du jour 1, une mini-comparaison « ce que j'aurais fait à la main / ce que l'IA a fait ». Effort : ≈ 0,5-1 j.
  - ➕ Réduit l'écart avec DLH sans revenir sur la décision 20
  - ➕ Les attentes sont posées avant l'arrivée
  - ➖ 30 minutes à trouver au jour 4
  - ➖ Conséquence : Le module serveur reste hors périmètre (CalcApp est une application navigateur).
- **`dlh` — En plus, demander à DLH de corriger le champ « objectifs »**
  - Une ligne dans le courriel à DLH.
- **`rien` — Ne rien changer**
  - On garde le support tel quel sur ce point.

## Planche `tut1` — Tuteur AI4SE

En ligne : https://claude.ai/artifact/61HTR2iVvVwSfj84pBK26t

**Ta demande.** Une planche sur les différentes façons de parler au tuteur, pour bien comprendre l'expérience de l'apprenant, avec avantages et inconvénients.

**Où on en est.** Le tuteur est publié dans le kit public (`nicolasguelfi/ai4se-kit`), en lecture seule. Il est installé en mode A et testé avec opencode 2.2.6. Changer de mode demande une ligne dans le kit et l'ajustement d'une ou deux diapositives d'installation.

**Comment répondre.** Question 1 : coche le mode voulu (plusieurs cases si tu veux combiner). Question 2 : seulement si tu choisis E, commente si besoin, puis « Copier ma sélection » et colle la ligne `tut1` dans la conversation. Rien ne change avant ta ligne.

### tut1 · `mode` — Comment les apprenants parlent-ils au tuteur ?

**Le problème.** Le tuteur est l'agent d'aide qui te remplace pendant que tu es occupé avec un autre apprenant. Dans opencode 2, il y a deux sortes d'agents. Un agent « principal » est celui avec qui l'on dialogue ; on change d'agent principal avec la touche Tab (build pour travailler, plan pour réfléchir). Un « sous-agent » ne dialogue pas directement : c'est l'agent principal qui le lance et lui transmet la question. Le tuteur est installé aujourd'hui comme sous-agent. La question est de savoir lequel de ces fonctionnements donnera la meilleure expérience à un apprenant perdu.

**Ce qu'on a trouvé.** Vérifié aujourd'hui avec opencode 2.2.6, dans un dossier personnel isolé. Le tuteur en sous-agent répond bien quand l'agent principal le lance. Réglé sur « all », il apparaît à la fois dans la rotation Tab et comme sous-agent. Le lancement en ligne de commande « opencode run --agent tutor » existe aussi, mais il ne fait qu'un échange à la fois. Il ne figure donc pas comme option. Le tuteur est en lecture seule dans tous les cas : il ne peut ni écrire ni casser quoi que ce soit.

**Recommandation de la planche.** Cocher E : c'est D en mieux. Mêmes deux fenêtres, mais le tuteur connaît tout le cours, se met à jour pendant la formation et ne touche jamais au processus de travail.

**Réponse de NG.** aucune option cochée
> Réponse de NG : demande de la présente planche, puis proposition de deux sessions opencode (travail / kit), puis recadrage sur l'objectif « training tutor » → planche tut2. Aucun choix de tut1 n'est retenu.

- **`session-cours` — E. Une session « cours » ouverte dans le dossier du kit (ta proposition)** *(recommandée par la planche)*
  - Le jour 1, l'apprenant clone le kit dans ~/ai4se/ai4se-kit. Ce dossier contient le tuteur comme agent par défaut et tout le contenu du cours en texte : diapositives, fiches d'exercice, page d'orientation, FAQ. Deux terminaux : à gauche « opencode » dans son projet (travail, GSE-One) ; à droite « opencode » dans ~/ai4se/ai4se-kit, où le tuteur répond directement, sans Tab. Le tuteur lit le contenu du cours chez lui et lit le projet de l'apprenant en lecture seule (dossier ~/ai4se/…), sans jamais rien écrire. Tu corriges ou enrichis le contenu pendant la formation ; un « git pull » dans le kit suffit pour que tous les tuteurs en profitent. Effort : ≈ 0,5 j (export du contenu, réglages, test) + test à la répétition du 19-20/11.
- **`fenetre` — D. Une « fenêtre d'aide » : un second terminal réservé au tuteur**
  - Dès le jour 1, l'apprenant ouvre deux terminaux dans le même dossier : à gauche le travail (build, GSE-One), à droite l'aide. Dans la fenêtre d'aide, il lance « opencode » et appuie sur Tab jusqu'à « tutor » (une seule fois : la session d'aide reste sur le tuteur). Quand il est perdu, il passe à droite et dialogue. Le tuteur ne voit pas la conversation de travail. Il voit ce qui est sur le disque : état git, plan, état GSE-One dans .gse/. Il demande à l'apprenant de coller le message qui le bloque. Ce réglage technique est celui de C, et @tutor reste disponible pour une question rapide. Effort : ≈ 1 h + un test à la répétition du 19-20/11.
- **`appel` — A. « @tutor » dans la conversation de travail (installé et testé aujourd'hui)**
  - L'apprenant reste dans sa session de travail (CalcApp, avec GSE-One) et tape « @tutor je ne comprends pas cette question de l'agent ». L'agent principal lit le message, décide de lancer le tuteur et lui transmet un résumé. Le tuteur répond à l'agent principal, qui reformule la réponse dans la conversation de travail. Le tuteur reçoit donc la question telle que l'agent principal l'a comprise. Il ne connaît pas les échanges précédents avec lui. À la question suivante, il repart de zéro. L'échange reste visible comme une « sous-session », qu'on peut ouvrir (flèches) puis quitter (flèche haut). Reste à vérifier à la répétition si l'on peut continuer à y écrire.
- **`tab` — B. Bascule par Tab dans la même conversation**
  - Dans sa session de travail, l'apprenant appuie sur Tab jusqu'à voir « tutor » en bas de l'écran (build → plan → tutor). Il pose sa question et dialogue directement avec le tuteur. Le tuteur voit toute la conversation de travail : ce que l'apprenant a demandé, ce que l'agent a fait, les erreurs. Une fois débloqué, l'apprenant appuie sur Tab pour revenir sur build et reprend.
- **`les-deux` — C. Les deux : Tab et @tutor**
  - Une seule ligne change dans le kit : le tuteur devient accessible à la fois par Tab (comme B) et par @tutor (comme A). Testé aujourd'hui : opencode 2.2.6 accepte ce réglage (le tuteur apparaît comme agent « all »).

### tut1 · `contenu` — Si E : où mettre le contenu du cours que lit le tuteur ?

**Le problème.** Avec E, le tuteur lit le cours sous forme de fichiers texte dans le kit. Or le kit est un dépôt public sous licence MIT : ce qu'on y met devient lisible par tout le monde.

**Ce qu'on a trouvé.** Les diapositives sont à toi : celles de Tiago te sont transférées, et les blocs repris d'all-trainings viennent de ton autre dépôt.

**Recommandation de la planche.** Cocher « Public, sous CC BY 4.0 » si publier le texte des diapositives ne te gêne pas ; sinon « Dépôt privé ».

**Réponse de NG.** aucune option cochée
> Remplacé par tut2 (hebergement=public, syllabus=redige). Licence du code du kit : MIT (QCM du 9/11).

- **`public` — Public, dans le kit, sous CC BY 4.0 pour le contenu** *(recommandée par la planche)*
  - Le texte des diapositives et les fiches vont dans le kit. Le code reste sous MIT, le contenu passe sous CC BY 4.0 (réutilisation libre avec attribution).
- **`prive` — Un second dépôt privé « ai4se-course », cloné à côté du kit**
  - Le kit (public) contient le tuteur ; le contenu est dans un dépôt privé. Au jour 1, j'invite les comptes GitHub des apprenants (créés à l'étape GitHub) par une commande. Les apprenants clonent les deux dépôts.
- **`resume` — Seulement un résumé public (comme aujourd'hui, en plus riche)**
  - On garde le contenu en résumés et fiches rédigés pour le tuteur, sans le texte des diapositives.

## Planche `tut2` — Tuteur et syllabus AI4SE

En ligne : https://claude.ai/artifact/7SPrNkW6ckqUaeMgGDt8zU

**Ta demande.** Le but : chaque participant possède un ensemble d'artefacts et au moins un agent « training tutor », auquel il pose des questions de compréhension ou d'assistance pendant toute la formation. Ce tuteur doit avoir pour contexte : les dépôts git de l'apprenant (clonés ou créés), des documents qui permettent de comprendre le programme, le dépôt de la méthode GSE-One, et un **syllabus** qui remplace les diapositives, auxquelles les apprenants n'ont pas accès. Il faut aussi une vue d'ensemble des 12 demi-journées. Tu as demandé une analyse et des propositions, sans rien modifier. Rien n'a été modifié.

**Ce que ça change par rapport à aujourd'hui.** Le kit publié ce matin résume le cours en 16 Ko dans les consignes du tuteur, et le tuteur est appelé depuis la session de travail. La cible : un tuteur qui lit de vrais documents (syllabus, GSE-One, dépôts de l'apprenant) dans sa propre session. La planche précédente (`tut1`) est remplacée par celle-ci.

**Ce que l'apprenant possède à la fin.** Sous ~/ai4se/ : le kit (tuteur + syllabus), gensem à v0.90.0, FreeSelfApp, CalcApp avec ses étiquettes, son mini-projet, et GSE-One installé dans ses projets. Avec la licence, il peut garder et réutiliser le tout ; il lui faudra sa propre clé de modèle.

**Comment répondre.** Coche une ou plusieurs cases par question et commente si besoin, puis « Copier ma sélection » : colle dans la conversation la ligne qui commence par `tut2`. Rien ne bouge avant ta ligne.

### tut2 · `session` — 1. Où s'ouvre la session du tuteur ?

**Le problème.** Le tuteur doit pouvoir lire les dépôts de l'apprenant sans jamais se mêler de son travail. Dans opencode, une session s'ouvre dans un dossier, et ce dossier fixe ce que l'agent voit d'office. Il faut choisir ce dossier de départ.

**Ce qu'on a trouvé.** Testé le 9/11 avec opencode 2.2.6 et un modèle gratuit. Le tuteur ouvert dans le dossier du kit est l'agent par défaut. Il a lu un dépôt placé dans ~/ai4se/ et s'est vu refuser la configuration opencode, qui contient les clés. Par défaut, opencode laisse lire n'importe quel dossier extérieur : il faut tout interdire, puis autoriser ~/ai4se/ seulement. Les commandes git sur le dossier d'un dépôt ont été refusées : il faut autoriser la forme « git -C dossier … ».

**Recommandation de la planche.** Cocher A : c'est la forme testée. Le travail et l'aide sont deux processus séparés.

**Réponse de NG.** `kit`
> D'accord sur le principe, mais peux-tu vérifier ce qui empêche de permettre à opencode d'avoir accès à d'autres dossiers dans le système de fichiers de la même manière que Claude codes ou Codex peuvent de toute façon accéder à tous les endroits du Gestionnaire de fichiers, soit automatiquement sans avoir besoin de demander l'autorisation soit avec autorisation explicite manuelle. Mon idée était justement que dans la session du tuteur, il y a une configuration qui lui indique l'ensemble des dossiers où se trouvent les ressources et auxquels il peut avoir accès.

- ✅ RETENUE — **`kit` — A. Une session dédiée, ouverte dans le dossier du kit (~/ai4se/ai4se-kit)** *(recommandée par la planche)*
  - Contenu : Deux terminaux. Dans le premier, le travail : opencode dans le projet, avec GSE-One. Dans le second, l'aide : opencode dans le dossier du kit, où le tuteur est l'agent par défaut. Le tuteur lit ses documents chez lui et les dépôts sous ~/ai4se/ en lecture seule. Effort : ≈ 2 h de réglages + test à la répétition.
  - ➕ Testé
  - ➕ Aucune interférence avec le travail ni avec GSE-One
  - ➕ Pas de touche Tab à retenir
  - ➖ Deux fenêtres
  - ➖ Le tuteur ne voit pas la conversation de travail : l'apprenant colle le message qui le bloque
  - ➖ Conséquence : Une étape d'installation au jour 1 (« ouvre ta fenêtre tuteur ») et un rappel sur chaque fiche d'exercice.
- **`racine` — B. Une session ouverte à la racine de l'espace de travail (~/ai4se)**
  - Le tuteur s'ouvre dans ~/ai4se. Tous les dépôts sont alors dans son dossier de départ, sans autorisation extérieure.
- **`global` — C. Un tuteur disponible dans toutes les sessions (Tab ou @tutor)**
  - Le tuteur est installé pour toute la machine et appelé depuis la session de travail.

### tut2 · `depots` — 2. Quels dépôts le tuteur peut-il lire ?

**Le problème.** Le tuteur doit lire les dépôts que l'apprenant clone ou crée pendant la formation : FreeSelfApp, CalcApp, mini-projet, GSE-One. Tout ce qu'il lit part chez le fournisseur du modèle : il ne faut pas lui ouvrir tout l'ordinateur.

**Ce qu'on a trouvé.** Les supports déjà écrits placent les travaux sous ~/ai4se/ : ~/ai4se/freeselfapp, ~/ai4se/gse-check et CalcApp. Le mini-projet peut être un projet professionnel, qui vit peut-être ailleurs.

**Recommandation de la planche.** Cocher A + B : la règle simple pour tous, et une porte pour l'exception du mini-projet.

**Réponse de NG.** `convention`, `liste`, `tout`
> [sur convention] Est-ce que ton idée ici serait que le projet que va faire l'étudiant soit mis dans un sous-dossiers de ai4se ? Cela pose problème parce que nous allons avoir des repos git à l'intérieur d'autres repos git et ce n'est pas une bonne façon de gérer les repos. [sur tout] Je serai plus pour cette solution avec un fichier de configuration qui donne la liste des chemins vers les dossiers qui font partie du contexte de l'agent tuteur est avec bien entendu les règles de ne pas exposer les données confidentielles ou de Sécurité, mais qui sont dans des fichiers, typiquement exclus tel que .env qui qui sont gérés par des scripts locaux qui peuvent lire les valeurs et les utiliser au niveau CLI comme le fait Claude ou codex

- ✅ RETENUE — **`convention` — A. Règle : tout ce qui concerne la formation vit sous ~/ai4se/** *(recommandée par la planche)*
  - Contenu : Le tuteur lit tout ~/ai4se/** et rien d'autre. Les supports et l'installation imposent ce dossier, mini-projet compris.
  - ➕ Simple à dire et à vérifier
  - ➕ Aucune donnée personnelle hors de ~/ai4se envoyée au modèle
  - ➖ Un dépôt créé ailleurs est invisible pour le tuteur
  - ➖ Conséquence : Une phrase dans l'installation et dans la page du mini-projet.
- ✅ RETENUE — **`liste` — B. En plus : déclarer un dépôt hors de ~/ai4se** *(recommandée par la planche)*
  - Contenu : Une commande du kit (par exemple « ai4se-allow ~/work/monprojet ») ajoute ce dossier à la liste que le tuteur peut lire. Effort : ≈ 1 h.
  - ➕ Couvre le mini-projet professionnel
  - ➖ Un geste de plus, à faire consciemment
  - ➖ Conséquence : L'apprenant choisit ce qu'il expose au modèle.
- ✅ RETENUE — **`tout` — C. Lecture de tout le dossier personnel**
  - Contenu : Le tuteur peut lire n'importe quel fichier de l'utilisateur.
  - ➕ Aucune configuration
  - ➖ Clés, documents personnels ou d'entreprise peuvent partir chez le fournisseur du modèle
  - ➖ Conséquence : À écarter : contraire aux règles AI Act de la semaine.

### tut2 · `gse` — 3. Comment le tuteur accède-t-il à la méthode GSE-One ?

**Le problème.** Le tuteur doit expliquer la méthode GSE-One. Les documents de référence existent dans le dépôt public gensem : la spécification de la méthode et la conception de son implémentation. Mais ils sont gros, et chaque lecture consomme la clé plafonnée de l'apprenant.

**Ce qu'on a trouvé.** Dans gensem à l'étiquette v0.90.0 : gse-one-spec.md (271 Ko, ≈ 70 000 tokens, 16 chapitres, glossaire, annexe A « résumé des activités »), gse-one-implementation-design.md (197 Ko, ≈ 50 000 tokens), README (44 Ko), et les 24 activités dans gse-one/src/activities/. En plus, chaque projet où GSE-One est installé contient les commandes et agents exacts de la v0.90.0 dans .opencode/.

**Recommandation de la planche.** Cocher A : le dépôt complet à la bonne version, avec une règle de lecture économe.

**Réponse de NG.** `clone`

- ✅ RETENUE — **`clone` — A. Clone de gensem à v0.90.0 dans ~/ai4se/gensem + guide de lecture** *(recommandée par la planche)*
  - Contenu : Le jour 1, le kit clone gensem à l'étiquette v0.90.0 (la version épinglée du cours). Le syllabus contient une page « où trouver quoi dans la méthode » : chapitre de la spécification par question type, glossaire, annexe A. Le tuteur cherche d'abord par mots-clés, puis lit seulement la section utile ; il ne lit jamais un document entier. Effort : ≈ 2 h (page « où trouver quoi » + consignes).
  - ➕ Source exacte, à la bonne version
  - ➕ Le tuteur peut citer « spec § 10 — Version Control Strategy »
  - ➕ Rien à rédiger pour le fond de la méthode
  - ➖ Un clone de plus au jour 1
  - ➖ Si le tuteur lit mal (document entier), une question peut coûter cher
  - ➖ Conséquence : Une règle « chercher d'abord, lire une section » dans les consignes du tuteur, à vérifier à la répétition.
- **`installe` — B. Seulement ce qui est installé dans chaque projet (.opencode/)**
  - Le tuteur lit les commandes et agents GSE-One présents dans le projet de l'apprenant.
- **`synthese` — C. Une synthèse GSE-One dans le syllabus, sans le dépôt**
  - Une dizaine de pages rédigées pour le cours : principes, cycle, commandes, Gates, modes.

### tut2 · `syllabus` — 4. Quelle forme pour le syllabus (les apprenants n'ont pas les diapositives) ?

**Le problème.** Les apprenants ne pourront pas cloner le dépôt des diapositives. Le tuteur a donc besoin d'un ensemble de documents qui contient l'essentiel du cours, nécessaire et suffisant pour répondre de façon cohérente avec ce qui a été enseigné.

**Ce qu'on a trouvé.** Les diapositives sont du code StreamTeX : le texte y est télégraphique (titres, puces, notes formateur dans les info-bulles). Les plans de jour existent pour les jours 1 et 2 (docs/plans 007 et 008). Les jours 3 à 6 seront réécrits pendant les phases 2 et 3.

**Recommandation de la planche.** Cocher A : une vue d'ensemble des 12 demi-journées, puis une fiche rédigée par demi-journée.

**Réponse de NG.** `redige`

- ✅ RETENUE — **`redige` — A. Vue d'ensemble + 12 fiches de demi-journée rédigées** *(recommandée par la planche)*
  - Contenu : (1) « Programme » : les 12 demi-journées sur une page chacune, avec objectifs, notions, activités, artefacts produits, commandes, étiquettes de reprise et lien vers la fiche. (2) Une fiche par demi-journée : les notions expliquées en prose (ce que dit le formateur, pas seulement les puces), les fiches d'exercice au format standard, les erreurs fréquentes, les renvois vers GSE-One. (3) Glossaire, reprise et FAQ, page d'orientation, fiche des sources. Le tout en anglais, comme les supports. Effort : ≈ 0,5 j pour la vue d'ensemble, ≈ 2-3 h par demi-journée.
  - ➕ Le tuteur répond dans les termes du cours
  - ➕ Sert aussi aux apprenants (lecture directe) et à toi (vue d'ensemble)
  - ➕ Sert de base à la migration future vers all-trainings
  - ➖ Effort de rédaction
  - ➖ Deux sources à garder alignées : diapositives et syllabus
  - ➖ Conséquence : Règle de production : chaque modification d'une diapositive met à jour la fiche de la même demi-journée, dans le même commit.
- **`extrait` — B. Extraction automatique du texte des diapositives**
  - Un script extrait titres, puces et notes de chaque bloc StreamTeX vers du Markdown, demi-journée par demi-journée.
- **`hybride` — C. Hybride : fiches rédigées + extraits automatiques en annexe**
  - Les fiches de A, plus pour chaque demi-journée une annexe générée (titres et puces), qui sert à vérifier qu'aucune notion ne manque.

### tut2 · `calendrier` — 5. Quand produire le syllabus ?

**Le problème.** Les jours 3 à 6 ne sont pas encore réécrits : rédiger leurs fiches maintenant, c'est écrire sur un contenu qui va changer. Mais le tuteur doit pouvoir situer tout le programme dès le jour 1.

**Ce qu'on a trouvé.** Phase 1 (jours 1-2) rédigée ; phase 2 (jours 3-4) du 19/11 au 02/12 ; phase 3 (jours 5-6) du 04/12 au 09/12.

**Recommandation de la planche.** Cocher A : la vue d'ensemble complète maintenant, les fiches avec chaque phase.

**Réponse de NG.** `phases`

- ✅ RETENUE — **`phases` — A. Vue d'ensemble des 12 demi-journées maintenant ; fiches au fil des phases** *(recommandée par la planche)*
  - Contenu : Maintenant : vue d'ensemble complète + fiches des demi-journées 1 à 4 (jours 1-2) + page GSE-One « où trouver quoi ». Phase 2 : fiches 5 à 8, écrites en même temps que les diapositives. Phase 3 : fiches 9 à 12. Effort : ≈ 1,5 j maintenant, puis ≈ 1 j par phase.
  - ➕ Pas de double travail
  - ➕ Le tuteur est utile dès le jour 1
  - ➖ Les fiches des jours 3-6 arrivent au fil de la formation (git pull)
  - ➖ Conséquence : Le tuteur sait dire « cette partie sera détaillée au jour 3 ».
- **`tout` — B. Tout maintenant, à partir du contenu de l'édition 1**
  - Les 12 fiches sont écrites tout de suite et corrigées pendant les phases 2 et 3.

### tut2 · `hebergement` — 6. Où vivent le syllabus et le tuteur ?

**Le problème.** Les apprenants doivent pouvoir récupérer le kit (tuteur + syllabus) et ses mises à jour sans avoir accès au dépôt des diapositives.

**Ce qu'on a trouvé.** Le kit actuel (nicolasguelfi/ai4se-kit) est public, sous licence MIT. Le dépôt des diapositives (ai4se6d) est privé.

**Recommandation de la planche.** Cocher A : un seul dépôt public, le syllabus sous une licence de contenu.

**Réponse de NG.** `public`

- ✅ RETENUE — **`public` — A. Dans le kit public : code sous MIT, syllabus sous CC BY 4.0** *(recommandée par la planche)*
  - Contenu : Un clone le jour 1, un « git pull » pour les mises à jour.
  - ➕ Rien à administrer
  - ➕ Les apprenants gardent tout après la formation
  - ➖ Le syllabus de ton cours devient public (pas les diapositives elles-mêmes)
  - ➖ Conséquence : Une licence de contenu ajoutée au kit.
- **`prive` — B. Syllabus dans un dépôt privé, apprenants invités**
  - Le kit public garde le tuteur ; le syllabus vit dans un dépôt privé. Au jour 1, tu invites les 20 comptes GitHub.
- **`archive` — C. Archive à télécharger depuis le site du cours**
  - Un fichier .zip du kit, publié derrière le mot de passe du site.

### tut2 · `maj` — 7. Comment le contenu se met-il à jour pendant la formation ?

**Le problème.** Tu vas corriger et compléter le syllabus pendant les trois semaines : fiches des jours suivants, réponses aux tickets. Chaque tuteur doit en profiter.

**Ce qu'on a trouvé.** Avec un dépôt git, une commande suffit. gensem reste figé à v0.90.0, la version du cours.

**Recommandation de la planche.** Cocher A.

**Réponse de NG.** `rituel`

- ✅ RETENUE — **`rituel` — A. Rituel « git pull » du kit au début de chaque demi-journée** *(recommandée par la planche)*
  - Contenu : Une ligne sur la diapositive d'accueil de chaque demi-journée. Le tuteur compare la version du kit à celle du jour et rappelle de faire « git pull » si elle est ancienne. Effort : ≈ 1 h.
  - ➕ Simple
  - ➕ Contrôlé par le tuteur lui-même
  - ➖ Un geste de plus en début de session
  - ➖ Conséquence : Un fichier VERSION dans le kit.
- **`fige` — B. Pas de mise à jour pendant la formation**
  - Le kit est installé une fois au jour 1.

### tut2 · `reponses` — 8. Comment le tuteur doit-il répondre ?

**Le problème.** Le tuteur répond à deux sortes de questions : la compréhension (« que veut dire un Gate ? ») et l'assistance (« je suis bloqué »). Il faut éviter qu'il invente ou qu'il contredise le cours.

**Ce qu'on a trouvé.** La version publiée diagnostique déjà l'état (git, .gse/), donne le plus petit pas suivant, ne fait jamais le travail et renvoie vers toi les cas de clé, de serveur, de machine et de travail perdu.

**Recommandation de la planche.** Cocher A.

**Réponse de NG.** `source`

- ✅ RETENUE — **`source` — A. Réponses fondées sur le cours, avec la source citée** *(recommandée par la planche)*
  - Contenu : Pour la compréhension : réponse tirée du syllabus ou de GSE-One, avec la référence (« fiche demi-journée 5 », « spec § 9 — Guardrails »). Si le cours ne couvre pas la question, il le dit, puis donne une réponse générale marquée comme telle. Pour l'assistance : diagnostic d'abord, plus petit pas suivant, jamais le travail à la place de l'apprenant. Effort : ≈ 1 h.
  - ➕ Cohérent avec ce que tu enseignes
  - ➕ L'apprenant sait où relire
  - ➕ Les écarts deviennent visibles (et peuvent devenir des tickets)
  - ➖ Réponses un peu plus longues
  - ➖ Plus de lectures, donc un peu plus de coût
  - ➖ Conséquence : Les consignes du tuteur sont réécrites en ce sens.
- **`libre` — B. Réponses libres, le cours en simple contexte**
  - Le tuteur utilise le cours quand il le juge utile.
