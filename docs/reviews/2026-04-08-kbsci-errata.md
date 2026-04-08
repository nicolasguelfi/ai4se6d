# KBSCI Errata — Issues found during AI4SE6D cross-module review

**Date**: 2026-04-08
**Document**: `sota-ai-4-se-EN.tex` (State of the Art — Methodological Approaches for Generative AI-Driven Software Engineering)
**Location**: `ul-ai-4-se/sota-ai-4-se-EN.tex`

This file collects errors or discrepancies found in the KBSCI document during the cross-module review of the AI4SE6D training modules. Each entry should be verified and corrected in the KBSCI source.

---

## Errata Registry

| # | Section | Claim in KBSCI | Correct Value | Source verified | Bibkey | Status |
|---|---------|---------------|---------------|-----------------|--------|--------|
| E1 | S6 (Empirical Evidence) | "84% of developers using or planning to use AI tools" | **76%** | StackOverflow Developer Survey website (verified 2026-04-08) | `stackoverflow-survey2025` -> `stackoverflow-survey2026` | TO FIX |
| E2 | S6 (Empirical Evidence) | "51% of developers using AI tools daily" | **63%** | StackOverflow Developer Survey website (verified 2026-04-08) | `stackoverflow-survey2025` -> `stackoverflow-survey2026` | TO FIX |
| E3 | S6 (Empirical Evidence) | Bibkey `stackoverflow-survey2025` | Rename to `stackoverflow-survey2026` | Convention alignment with training modules | all cite() calls | TO FIX |
| E4 | S6 (Empirical Evidence) | Trust decline "down from 40%" | **43%** in SO 2024 survey (not 40%) | SO 2024 survey page: 43% trust accuracy | `stackoverflow-survey2025` | TO VERIFY |

---

## Notes

- E1/E2/E3: The trainer verified the StackOverflow Developer Survey directly on the website (April 2026). Correct figures: 76% adoption, 63% daily, 82% regularly. The KBSCI cites 84%/51% — likely from a different question or a misread. The bibkey should be renamed to `stackoverflow-survey2026` to reflect the consultation date.
- The training modules have already been corrected to use `stackoverflow-survey2026` with the verified figures.
- **Action**: Update `sota-ai-4-se-EN.tex` — correct the figures and rename the bibkey.
