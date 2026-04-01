---
title: Source gap analysis after plan creation
category: process
scope: collection
origin: ai4se6d (2026-04-01)
tags: [CE, plan, gap-analysis, source-document, confirmation-bias]
---

## Context

When creating a plan (Pathway C) from a dense source document, the planner extracts content matching stated objectives but misses relevant themes not explicitly targeted.

## Problem

Cognitive confirmation bias: we find what we look for, not what we don't know to look for. In our case, 6 out of 20+ relevant themes in a 3000-line LaTeX document were missed in the initial plan.

## Solution

Add a "Source Gap Analysis" phase to /stx-ce:plan after the initial plan is created:

1. **Extract plan themes**: List all topics/concepts covered in the plan
2. **Inverse search**: Search the source document for sections NOT matching any plan theme
3. **Relevance filter**: For each unmatched section, evaluate relevance to the document objectives
4. **Enrich**: Add high-relevance discoveries to the plan
5. **Document**: Record what was found and why it was included/excluded

This phase should be mandatory for Pathway C with source documents longer than 500 lines.

## Applicability

All CE Pathway C projects based on academic or technical source documents. Should be added to ce-plan.md skill in streamtex-claude.
