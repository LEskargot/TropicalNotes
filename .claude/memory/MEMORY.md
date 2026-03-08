# TropicalNotes — Project Memory

## What this project is
Medical reference handbook (médecine tropicale & du voyage) for Swiss GPs/practitioners.
Live at **tropicalnotebook.ch** via GitHub Pages → `LEskargot/TropicalNotes` (main branch).

## Two sites in one repo
- `index.html` — old Bootstrap 4 site (still live, legacy)
- `prototype.html` — new Tailwind design (being rolled out as the main site)
- Existing pathogen pages (`pages/viruses/`, `pages/bacteria/`, `pages/parasites/`) use the old Bootstrap 4 template

## Build system
- **Tailwind CSS** (for prototype): `npm run tailwind` → builds `dist/css/prototype.css`
  - Entry: `src/css/prototype.css`, config: `tailwind.config.js`
  - Node.js v22 breaks Laravel Mix / webpack 4 (OpenSSL error) — use Tailwind CLI directly
- **Laravel Mix** (legacy SCSS): `npm run prod` — broken on Node v22, not needed for new work
- Node.js: v22.12.0 on this machine
- No `node_modules` committed; run `npm install` on fresh clone

## Content source: md-slides repo
Path: `C:\Users\ludov\Projects\md-slides\`
Two types of files:
- **Module files** — CME presentation slides in structured markdown (quiz → rationale format)
- **Research files** — in `docs/`

### Syndrome modules (→ become syndrome pages on the site)
All in `modules/urgences-infectio-voyage/`:
| File | Syndrome card on site | Key pathogens covered |
|------|-----------------------|-----------------------|
| `module_fievre_voyageur.md` | Fièvre au retour | Malaria (P. falciparum), Dengue, Rickettsiose, Typhoïde (XDR), Katayama/Schistosomiase |
| `module_diarrhee_voyageur.md` | Diarrhée du voyageur | E. coli, Campylobacter, Shigella, C. difficile, ESBL |
| `module_dermatoses_voyageur.md` | Dermatoses du voyageur | CLM (larva migrans), Myiase, Leishmaniose cutanée, Gale |
| `module_eosinophilie_voyageur.md` | Éosinophilie | Strongyloides, Schistosoma, Toxocara, Filaires |

### Module file format (structured markdown)
```
## slide: <id>
type: case|table|takeaway|image_text|...
title: ...
### vignette / question / options / table / bullets / piege / perle / retenir / evidence
```

## Existing pathogen pages (cross-link targets)
- `pages/parasites/`: malaria, leishmaniasis, schistosomiasis, african_trypanosomiasis, american_trypanosomiasis, giardiasis, intestinal_problems_parasites
- `pages/viruses/`: dengue, chikungunya, zika, yellow_fever, rabies, hepatitis_a, hepatitis_e
- `pages/bacteria/`: enteric_fever, rickettsiosis, leptospirosis

## Next task: syndrome pages
Build 4 syndrome pages in prototype Tailwind design, sourced from the md-slides modules.
Structure per page: diagnostic approach → workup table → key pathogens (cross-linked) → treatment → points clés (piège + perle + retenir) → evidence.
No quiz format — reference pages only.
Files to create: `pages/syndromes/fievre.html`, `diarrhee.html`, `dermatoses.html`, `eosinophilie.html`
Update prototype.html syndrome card links when pages are created.

## Design tokens (Tailwind custom colors in tailwind.config.js)
teal: 50–950, mint: 50–900, gold: 50–900, cream: 50–500
Fonts: DM Serif Display (serif), Source Sans 3 (sans)

## User preferences
- French throughout (medical content)
- Swiss context: OFSP/BAG, SSTTM, Swiss TPH references prioritized
- _italic_ for organism names
- Push to GitHub after completing work
