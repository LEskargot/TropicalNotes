---
id: TASK-5
title: Lier fievre-voyageur.html dans la navigation (page orpheline)
status: To Do
assignee: []
created_date: '2026-08-17 15:18'
updated_date: '2026-08-17 15:22'
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
- [ ] #1 La navigation pointe vers la page au nouveau design (Tailwind + TOC)
- [ ] #2 Contenu utile de fievre.html récupéré si nécessaire
- [ ] #3 Ancienne page supprimée, aucune page orpheline restante
<!-- AC:END -->
