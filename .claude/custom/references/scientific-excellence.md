# Scientific Excellence — Reference Verification Rules

Custom rule for all ai4se6d modules. Applies whenever a factual claim, statistic, or citation is added or modified.

## Verification Protocol (MANDATORY)

Before adding any `link=` parameter or `# REF:` comment with a URL:

1. **Verify the URL content matches the citation**. Open the URL (via WebSearch or WebFetch) and confirm that:
   - The paper title matches the topic being cited
   - The authors match the names in the attribution
   - The specific claim (statistic, quote, finding) actually appears in that source
2. **Never guess arXiv IDs or DOIs**. If unsure of the exact identifier, use WebSearch to find the correct paper by searching for author names + key findings.
3. **Prefer DOI or publisher links** over arXiv when the paper has been formally published (e.g., ACM DL, IEEE, Springer, USENIX).

## Common Errors to Avoid

- Hallucinated arXiv IDs: LLMs frequently generate plausible-looking but incorrect arXiv identifiers. ALWAYS verify.
- Wrong paper, right ID format: An arXiv ID that exists but points to an unrelated paper (e.g., citing a computer vision paper for a software security claim).
- Outdated URLs: Industry reports (Bain, Gartner, GitLab) change URLs yearly. Use the landing page or topic page, not a versioned URL.

## Quality Checklist (per reference)

Before committing any block with a new or modified reference:

- [ ] URL resolves to the correct source (verified via WebSearch)
- [ ] Paper/report title matches the claim in the slide
- [ ] Author names match the attribution text
- [ ] The specific statistic or finding cited actually appears in the source
- [ ] `# REF:` comment is present above the `st_write` call
- [ ] `link=` parameter points to the verified URL
- [ ] Style follows the visual rendering standard from design-guideline-maximize-viewport.md

## Scope

This rule applies to:
- All `link=` parameters on `st_write` calls with source attributions
- All `# REF:` comments in block source code
- All references added during `/stx-ce:produce` and `/stx-ce:fix` phases
- All URL corrections during `/stx-ce:review` editorial findings
