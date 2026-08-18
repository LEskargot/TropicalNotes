---
id: TASK-4
title: 'Retirer Bootstrap 4 / jQuery / laravel-mix, garder le pipeline Tailwind'
status: To Do
assignee: []
created_date: '2026-08-17 15:18'
updated_date: '2026-08-18 14:18'
labels:
  - cleanup
dependencies: []
priority: medium
ordinal: 4000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
package.json déclare encore bootstrap ^4.5.3, jquery, popper.js, laravel-mix ^5.0.9, sass ; webpack.mix.js et src/scss/ existent toujours. Attention : ce n'est PAS une suppression simple — index.html et les 4 pages syndromes de l'ancien gabarit (fievre, diarrhee, dermatoses, eosinophilie) référencent encore dist/, et le script npm "tailwind" génère dist/css/prototype.css (toujours utilisé). Note : prototype.html a été supprimé (TASK-2) et retiré des globs tailwind. Les pages syndromes concernées doivent de toute façon être reconstruites (TASK-30/31/32), ce qui allégera d'autant la dépendance à dist/.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Inventaire des assets dist/ réellement utilisés
- [ ] #2 Dépendances Bootstrap/jQuery/laravel-mix retirées de package.json
- [ ] #3 webpack.mix.js et src/scss supprimés si inutilisés
- [ ] #4 Le rendu du site est inchangé
<!-- AC:END -->
