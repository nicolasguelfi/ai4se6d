# Scientific Excellence — Reference Verification & Styling Rules

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
- [ ] Style follows the citation styling rules below (uniform light green italic)

## Citation Styling (MANDATORY)

All modules define a shared citation style on `Custom` in `custom/styles.py`:

```python
class Custom:
    citation = Style("color: #81C784; font-style: italic;", "citation")
```

Access: `s.project.citation`. This style carries **no font size** — size is always composed locally with `+`.

### Rules

1. **Source attribution lines** (bottom of slides) — use `s.project.citation + s.large + s.center_txt`:
   ```python
   # In BlockStyles:
   source = s.project.citation + s.large + s.center_txt
   # Usage:
   st_write(bs.source, cite("author-paper2024"))
   ```

2. **Inline citations** in body text — wrap `cite()` in a tuple with citation style at surrounding size:
   ```python
   st_write(bs.body, (bs.body, " — Transformer architecture "),
            (s.project.citation + s.Large, cite("vaswani2017attention")))
   ```

3. **Quote attributions** — compose with desired size, never use orange/highlight:
   ```python
   attribution = Style.create(s.project.citation + s.large, "my_attribution")
   ```

### What NOT to style with `s.project.citation`

- **Slide headings** with author names (e.g., "RCT 1: Peng et al. (2023)") — structural titles
- **Column headers** (e.g., "Cui et al. — Gains") — layout labels
- **Narrative mentions** in body text (e.g., "Hassan et al. propose...") — content flow

### Forbidden Patterns

- `s.project.titles.caption` or `s.project.colors.muted` for citation lines
- `s.project.colors.highlight` (orange) for citation attribution
- `(bs.body, cite(...))` — citations in body style with no visual distinction
- Hardcoding a font size in the base citation style definition

## Scope

This rule applies to:
- All `link=` parameters on `st_write` calls with source attributions
- All `# REF:` comments in block source code
- All references added during `/stx-ce:produce` and `/stx-ce:fix` phases
- All URL corrections during `/stx-ce:review` editorial findings
