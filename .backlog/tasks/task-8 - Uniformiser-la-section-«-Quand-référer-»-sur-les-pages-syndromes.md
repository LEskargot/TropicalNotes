---
id: TASK-8
title: Uniformiser la section « Quand référer » sur les pages syndromes
status: In Progress
assignee: []
created_date: '2026-08-17 15:18'
updated_date: '2026-08-18 15:37'
labels:
  - consistency
dependencies: []
priority: medium
ordinal: 8000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Aucune des pages syndromes n'utilise le titre « Quand référer », contrairement aux 16 pages pathogènes. Les liens /professionnels existent (sauf diarrhee.html) mais sans section identifiée.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Chaque page syndrome a une section « Quand référer » explicite
<!-- AC:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
Fait pour fievre.html : section « Quand référer ? » ajoutée selon le patron des pages pathogènes (h2 + div.callout-referer + liste d'indications + lien « Référer le patient → »), avec entrée dans la TOC. Les trois autres pages syndromes (diarrhee, dermatoses, eosinophilie) recevront la leur lors de leur conversion (TASK-30/31/32) — inutile de les modifier deux fois.
<!-- SECTION:NOTES:END -->
