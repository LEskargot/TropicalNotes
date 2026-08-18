---
id: TASK-5
title: Lier fievre-voyageur.html dans la navigation (page orpheline)
status: Done
assignee: []
created_date: '2026-08-17 15:18'
updated_date: '2026-08-18 15:37'
labels:
  - consistency
dependencies: []
priority: high
ordinal: 5000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Ce n'est pas une simple duplication : pages/syndromes/fievre-voyageur.html (97 Ko) est la SEULE page syndrome construite au nouveau design (Tailwind CDN + TOC flottante), issue de la conversion md-slides. La navigation pointe pourtant vers fievre.html (34 Ko), l'ancienne page Bootstrap qui référence dist/. La bonne page n'est donc pas servie aux lecteurs.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 La navigation pointe vers la page au nouveau design (Tailwind + TOC)
- [x] #2 Contenu utile de fievre.html récupéré si nécessaire
- [x] #3 Ancienne page supprimée, aucune page orpheline restante
<!-- AC:END -->

## Final Summary

<!-- SECTION:FINAL_SUMMARY:BEGIN -->
fievre-voyageur.html promue dans l'URL fievre.html (ancienne page Bootstrap supprimée, sous-ensemble strict : 6 sections/1 tableau contre 11 sections/13 tableaux). Les liens entrants depuis index.html et malaria.html restent valides. Prérequis découvert et traité : la page était en français désaccentué (20 caractères accentués sur 95 Ko, contre ~7 pour 1000 sur les pages comparables) — accents restaurés par table de correspondance appliquée aux seuls nœuds texte, 1919 balises inchangées, entités HTML intactes. Rendu vérifié au navigateur.
<!-- SECTION:FINAL_SUMMARY:END -->
