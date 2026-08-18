# Algorithmes (draw.io → SVG)

Les algorithmes sont dessinés dans **draw.io** (`*.drawio.xml`) puis rendus en
**SVG statique** servi par le site (`*.svg`).

## Pourquoi pas l'embed draw.io ?

Les pages utilisaient auparavant un `<iframe>` vers `viewer.diagrams.net` pointant
sur le fichier `.drawio.xml` via `raw.githubusercontent.com`. **Cela n'affichait
rien** : le viewer se chargeait mais rendait une page vide, et les diagrammes
étaient donc invisibles en production.

Le SVG auto-hébergé règle le problème et présente d'autres avantages :

- aucune dépendance à un tiers qui peut casser silencieusement ;
- aucune requête externe depuis le navigateur du lecteur (les médecins qui
  consultent le site ne sont pas exposés à un traceur tiers) ;
- affichage immédiat, sans JavaScript, et impression correcte.

## Régénérer un SVG après modification du diagramme

```bash
python3 scripts/drawio2svg.py \
  assets/diagrams/algo-diarrhee.drawio.xml \
  assets/diagrams/algo-diarrhee.svg \
  "Algorithme diarrhée du voyageur"

python3 scripts/drawio2svg.py \
  assets/diagrams/algo-dermatose.drawio.xml \
  assets/diagrams/algo-dermatose.svg \
  "Algorithme diagnostique des dermatoses du voyageur"
```

Le convertisseur gère le sous-ensemble utilisé ici : rectangles arrondis,
cellules texte, arêtes orthogonales avec `exitX`/`entryX` et points de passage,
libellés HTML (`<b>`, `<br>`, `<font>`), traits tiretés et libellés d'arête.
La taille de police est réduite automatiquement si le texte déborde de sa forme.
