---
id: TASK-36
title: Afficher les algorithmes draw.io (invisibles en production)
status: Done
assignee: []
created_date: '2026-08-18 15:51'
labels:
  - consistency
dependencies: []
modified_files:
  - pages/syndromes/diarrhee.html
  - pages/syndromes/dermatoses.html
priority: high
ordinal: 36000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Signalé par l'auteur : les algorithmes n'apparaissaient pas sur le site. Cause : diarrhee.html et dermatoses.html intégraient un <iframe> vers viewer.diagrams.net pointant sur le .drawio.xml via raw.githubusercontent.com. Le fichier était bien accessible (HTTP 200, XML mxfile valide) et le viewer se chargeait (titre « draw.io »), mais rendait une page blanche — vérifié par capture d'écran, y compris avec le paramètre url encodé. Les pages portaient d'ailleurs la mention « s'affiche après déploiement GitHub Pages », signe que cela n'avait jamais fonctionné.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Les deux algorithmes s'affichent réellement
- [ ] #2 Aucune dépendance à un tiers
- [ ] #3 Régénération documentée
<!-- AC:END -->

## Final Summary

<!-- SECTION:FINAL_SUMMARY:BEGIN -->
Remplacement de l'iframe par un SVG auto-hébergé. Convertisseur écrit dans scripts/drawio2svg.py (rectangles arrondis, cellules texte, arêtes orthogonales exitX/entryX + points de passage, libellés HTML, tirets, libellés d'arête, réduction automatique de la police en cas de débordement). Sortie déterministe, vérifiée visuellement au navigateur pour les deux pages. Bénéfices annexes : plus aucune requête externe depuis le navigateur du lecteur, affichage sans JavaScript, impression correcte. Un chevauchement présent dans le diagramme source (légende sur la boîte « Bilan complet ») a été corrigé dans le .drawio.xml. Procédure de régénération dans assets/diagrams/README.md.
<!-- SECTION:FINAL_SUMMARY:END -->
