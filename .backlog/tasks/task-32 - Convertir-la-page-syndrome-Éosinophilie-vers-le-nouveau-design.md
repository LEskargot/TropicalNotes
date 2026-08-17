---
id: TASK-32
title: Convertir la page syndrome Éosinophilie vers le nouveau design
status: To Do
assignee: []
created_date: '2026-08-17 15:22'
labels:
  - content
dependencies: []
references:
  - >-
    /home/ubuntu/md-slides/topics/urgences-infectio-voyage/research/research-eosinophilia-travelers.md
documentation:
  - docs/plans/2026-03-08-syndrome-pages-design.md
modified_files:
  - pages/syndromes/eosinophilie.html
priority: high
ordinal: 32000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
pages/syndromes/eosinophilie.html utilise encore l'ancien gabarit Bootstrap (référence dist/, pas de Tailwind CDN, pas de TOC flottante). Seul fievre-voyageur.html a été converti au nouveau design. Source de vérité : /home/ubuntu/md-slides/topics/urgences-infectio-voyage/research/research-eosinophilia-travelers.md. Note : le script de pipeline `build-syndrome.js` décrit dans docs/plans/2026-03-08-syndrome-pages-design.md n'a jamais été écrit — fievre-voyageur.html a été construit à la main d'après son plan.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Page reconstruite avec Tailwind CDN + TOC flottante, comme fievre-voyageur.html
- [ ] #2 Contenu issu du research de md-slides
- [ ] #3 Section « Quand référer » → traveldoctor.ch/professionnels
- [ ] #4 Plus aucune référence à dist/ dans la page
<!-- AC:END -->
