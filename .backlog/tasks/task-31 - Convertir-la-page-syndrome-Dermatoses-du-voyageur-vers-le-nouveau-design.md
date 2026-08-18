---
id: TASK-31
title: Convertir la page syndrome Dermatoses du voyageur vers le nouveau design
status: To Do
assignee: []
created_date: '2026-08-17 15:22'
updated_date: '2026-08-18 14:17'
labels:
  - content
dependencies: []
references:
  - >-
    /home/ubuntu/md-slides/topics/urgences-infectio-voyage/research/research-dermatoses-voyageur.md
documentation:
  - docs/plans/2026-03-08-syndrome-pages-design.md
modified_files:
  - pages/syndromes/dermatoses.html
priority: high
ordinal: 31000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
pages/syndromes/dermatoses.html utilise encore l'ancien gabarit Bootstrap (référence dist/, pas de Tailwind CDN, pas de TOC flottante). Seul fievre-voyageur.html a été converti au nouveau design. Source de vérité : /home/ubuntu/md-slides/topics/urgences-infectio-voyage/research/research-dermatoses-voyageur.md. Note : le script de pipeline `build-syndrome.js` décrit dans docs/plans/2026-03-08-syndrome-pages-design.md n'a jamais été écrit — fievre-voyageur.html a été construit à la main d'après son plan.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Page reconstruite avec Tailwind CDN + TOC flottante, comme fievre-voyageur.html
- [ ] #2 Contenu issu du research de md-slides
- [ ] #3 Section « Quand référer » → traveldoctor.ch/professionnels
- [ ] #4 Plus aucune référence à dist/ dans la page
<!-- AC:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
ATTENTION en réutilisant docs/superpowers/plans/2026-03-10-syndrome-pages.md : ce plan (archive) fait copier la navbar avec des liens vers ../../prototype.html#syndromes. prototype.html a été SUPPRIMÉ (TASK-2) — il servait de fausse page d'accueil avec des menus déroulants morts. Utiliser ../../index.html (#syndromes, #about, #pathogenes existent). Prendre fievre-voyageur.html comme référence de navbar, pas le plan.
<!-- SECTION:NOTES:END -->
