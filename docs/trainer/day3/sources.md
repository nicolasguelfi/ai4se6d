# Fiche des sources — jour 3 (édition 2)

Décision `peda1` P9 : chiffres **mis à jour à la source** + cette fiche formateur.
Cette fiche recense les chiffres affichés au jour 3 (séquences `sequence_concepts.py` et `sequence_discovery.py`
du module `ai4se6d_gensem`), avec la source telle que citée dans les blocs (clé BibTeX dans
`modules/shared-blocks/static/references.bib`). Rédigée le 2026-11-10 : les URL n'ont **pas** été rouvertes
(colonne « Consulté » = « — ») ; à vérifier à la source avant le 03/12, avec les captures du 23-24/11.

Statuts : **vérifié** · **mis à jour** · **retiré** · **à vérifier** (repris de la bibliographie, source non rouverte) ·
**référence classique** (ouvrage ou norme de référence, contenu stable, citation exacte à confirmer).

## Blocs nouveaux de l'édition 2 (cycles CCSET09 à CCSET12)

| Bloc | Chiffre ou affirmation | Source (clé) | Consulté | Statut |
|---|---|---|---|---|
| `bck_elicitation_cost.py` | « ×100 » : corriger un problème grave après livraison coûte souvent 100 fois plus qu'en exigences et conception | Boehm & Basili 2001, item 1 (`boehm-basili-top10-2001`) | — | référence classique |
| `bck_elicitation_good_requirement.py` | caractéristiques d'une bonne exigence | ISO/IEC/IEEE 29148:2018 (`iso29148-2018`) | — | référence classique |
| `bck_elicitation_techniques.py` | techniques d'élicitation, usages et limites (synthèse) | Zowghi & Coulin 2005 (`zowghi-coulin-elicitation2005`) | — | référence classique (tableau = synthèse du cours) |
| `bck_elicitation_user_stories.py` | INVEST | Wake 2003 (`wake-invest2003`) | — | référence classique |
| `bck_elicitation_acceptance.py` | gabarit Given / When / Then | North 2006 (`north-bdd2006`) | — | référence classique |
| `bck_elicitation_with_ai.py` | « la plupart des études sont à un stade précoce » | Cheng et al. 2025 (`cheng-genai-re2025`, « 90 %+ early-stage ») | — | à vérifier |
| `bck_nfr_versus_functional.py` | « la frontière n'est pas toujours nette » | Glinz 2007 (`glinz-nfr2007`) | — | référence classique |
| `bck_nfr_quality_model.py` | 9 caractéristiques de qualité | ISO/IEC 25010:2023 (`iso25010-2023`) | — | à vérifier (libellés anglais de l'édition 2023) |
| `bck_nfr_measurable.py` | échelle, mesure, but, tolérable | Gilb 2005 (`gilb-competitive2005`) | — | référence classique |
| `bck_nfr_scenarios.py` | scénario de qualité en 6 parties | Bass, Clements, Kazman 2021 (`bass-sap2021`) | — | référence classique |
| `bck_nfr_ai_blind_spots.py` | « 45 % des échantillons de code générés par IA échouent aux tests de sécurité » | Veracode 2025 (`veracode-genai2025`) | — | à vérifier (déjà affiché au jour 1) |
| `bck_nfr_ai_blind_spots.py` | « sollicité, un modèle propose des qualités pertinentes » | Lima et al. 2025 (`lima-nfr-iso25010-2025`, 80,4 % d'accord) | — | à vérifier |
| `bck_vv_definitions.py` | « building the product right / the right product » | Boehm 1984 (`boehm-vv1984`) | — | référence classique |
| `bck_vv_pyramid.py` | pyramide des tests | Cohn 2009 (`cohn-succeeding2009`) | — | référence classique |
| `bck_vv_test_design.py` | classes d'équivalence, valeurs limites | Myers et al. 2011 (`myers-testing2011`) | — | référence classique |
| `bck_vv_oracle_ai.py` | problème de l'oracle | Barr et al. 2015 (`barr-oracle2015`) ; Wang et al. 2025 (`wang-llm-testing2025`) | — | référence classique / à vérifier |
| `bck_nfr_measurable.py`, `bck_nfr_scenarios.py`, `bck_vv_test_design.py` | 200 ms, 1 000 dépenses, 100 essais, 0,01 € | — (exemples CalcApp du cours) | — | illustratif |

## Blocs de l'édition 1 repris (CCSET09 et références)

Chiffres repris tels quels de l'édition 1 ; **tous à vérifier** avant le 03/12 (décision P9 ; le fichier 009 cite
déjà `evidence_perception.py`, `frameworks.py:179-255` et `fw_synthesis.py:36`).

| Bloc | Chiffres affichés | Sources citées (clés) | Statut |
|---|---|---|---|
| `bck_gensem_evidence_rcts.py` | +55 % (+55,8 %), +26 %, −19 %, et 13 / 24 / 39 / 80 / 89 / 95 % | `peng-copilot2023`, `cui-fieldexperiments2024`, `metr2025` | à vérifier |
| `bck_gensem_evidence_perception.py` | 19-24 %, 38-40 %, 29 % | `metr2025`, `stackoverflow-survey2026` | à vérifier (`stackoverflow-survey2026` : même réserve qu'au jour 1 sur l'année) |
| `bck_gensem_sdlc_evidence.py` | 5 %, 15 %, 30 %, 55,8 %, 75,2 % | `gitlab-devsecops2025`, `metr2025`, `peng-copilot2023`, `soen101-2024` | à vérifier |
| `bck_gensem_sdlc_gravity.py` | 80 % | — | à vérifier (source absente du bloc) |
| `bck_gensem_sdlc_orchestrator.py` | 60 %, 80 % | — | à vérifier (source absente du bloc) |
| `bck_gensem_sdlc_phases.py` | 5-55 %, 67,3 % | `esposito-architecture2025`, `gao-maintenance2025`, `soen101-2024` | à vérifier |
| `bck_gensem_risks.py` | 21,7 %, 65 %, 80 %, 85 % | `basic-codesecurity-slr2025`, `spracklen-packages2025` | à vérifier |
| `bck_gensem_sota_takeaway.py` | « outil seul ~10 %, outil + processus 25-30 % » ; « planification et revue = 80 % de la qualité » | — | à vérifier ; la seconde affirmation est à **retirer ou sourcer** |
| `bck_gensem_fw_synthesis.py` | notes ✓✓ / ✓ / ✗ par méthode ; ligne GSE-One | — (appréciation de l'auteur) | à compléter : « auteur = formateur, pré-version » (fichier 009) |
| `bck_gensem_sdlc_re.py` | 238 articles, 67,3 %, 90 %+ | `cheng-genai-re2025` | à vérifier |
| `bck_gensem_sdlc_testing.py` | 15 % | `soen101-2024`, `wang-llm-testing2025` | à vérifier |
