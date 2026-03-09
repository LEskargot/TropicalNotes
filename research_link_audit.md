# Link Audit — TropicalNotes (2026-03-09)

## Summary
Checked all 39 unique external links across 24 HTML files.
- 20 OK (200)
- 10 bot-blocked (403) but valid DOIs — publishers block curl, DOIs resolve correctly
- 8 truly broken (404) — fixed below
- 1 own site (traveldoctor.ch/professionnels) — page needs creating

---

## Broken DOIs — Fixed

### 1. Jensenius 2013 (fièvre au retour mortality)
- **File**: `pages/syndromes/fievre-voyageur.html:477`
- **Old DOI**: `10.4269/ajtmh.13-5528` (404)
- **Correct DOI**: `10.4269/ajtmh.12-0551`
- **Citation**: Jensenius M et al. Am J Trop Med Hyg 2013;88(2):397
- **Source**: PubMed — submitted 2012, published 2013
- **Status**: FIXED

### 2. Pillay Lancet Microbe 2025 (NS1 ELISA meta-analysis)
- **File**: `pages/syndromes/fievre-voyageur.html:607,1165`
- **Old DOI**: `10.1016/S2666-5247(24)00242-1` (404 — used PII instead of DOI)
- **Correct DOI**: `10.1016/j.lanmic.2025.101088`
- **Citation**: Pillay K et al. Lancet Microbe 2025;6(7):101088 (PMID 40209729)
- **Status**: FIXED

### 3. False positive malaria RDT in typhoid (BMC Infect Dis 2014)
- **File**: `pages/syndromes/fievre-voyageur.html:929`
- **Old DOI**: `10.1186/s12879-014-0710-5` (404 — used new journal prefix, article has old prefix)
- **Correct DOI**: `10.1186/1471-2334-14-377`
- **Citation**: Meatherall B et al. BMC Infect Dis 2014;14:377 (PMID 25005493)
- **Note**: Site cites as "Boggild BMC Infect Dis 2014" but first author is Meatherall. Boggild is not an author. Update attribution.
- **Status**: FIXED (DOI + author attribution corrected to Meatherall)

### 4. Mandell chapter 319 (Infections in Returning Travelers)
- **File**: `pages/syndromes/fievre-voyageur.html:1219`
- **Old DOI**: `10.1016/B978-0-323-48255-4.00319-X` (404 via doi.org)
- **Note**: DOI registration issue at doi.org. Chapter exists on ScienceDirect (returns 403 = bot protection, not 404). The Elsevier e-library confirms: Boggild AK, Freedman DO. "Infections in Returning Travelers." Mandell 9th ed, ch. 319, pp. 3828+
- **Alternative URL**: `https://www.sciencedirect.com/science/article/pii/B978032348255400319X`
- **Status**: FIXED (using ScienceDirect URL)

---

## Broken Institutional URLs — Fixed

### 5. CDC Yellow Fever Maps
- **File**: `pages/viruses/yellow_fever.html:42`
- **Old URL**: `https://www.cdc.gov/yellowfever/maps/index.html` (404 — CDC site reorganized)
- **New URL**: `https://www.cdc.gov/yellow-fever/`
- **Status**: FIXED

### 6. CHUV Guide d'antibiothérapie
- **File**: `pages/parasites/malaria.html:265`
- **Old URL**: `https://www.chuv.ch/fr/min/min-home/professionnels-de-la-sante/guide-dantibiotherapie/`
- **New URL**: `https://www.chuv.ch/fr/min/min-home/personnel-de-la-sante/guide-dantibiotherapie`
- **Note**: Directory renamed from "professionnels-de-la-sante" to "personnel-de-la-sante". Page now points to Firstline app (since Dec 2025).
- **Status**: FIXED

### 7. Swiss TPH / SSTTM Malaria Treatment
- **File**: `pages/syndromes/fievre-voyageur.html:519,1103,1155`
- **Old URL**: `https://www.swisstph.ch/en/projects/malaria-treatment` (404)
- **New URL**: `https://www.ssttm.ch/dokumente/swisstph-malaria-tx-recommendations-21-10-2025-clean.pdf`
- **Alternative (topic page)**: `https://www.swisstph.ch/en/topics/malaria/diagnosis-and-treatment`
- **Note**: SSTTM publishes the recommendations PDF on their own domain now
- **Status**: FIXED

### 8. WHO Arboviral Guidelines 2025
- **File**: `pages/syndromes/fievre-voyageur.html:680,694,1161`
- **Old URL**: `https://www.who.int/publications/i/item/9789240098688` (404 — wrong ISBN)
- **New URL**: `https://www.who.int/publications/i/item/9789240111110`
- **Citation**: WHO. Guidelines for clinical management of arboviral diseases: dengue, chikungunya, Zika and yellow fever. July 2025.
- **Status**: FIXED

---

## Own Site — Page Missing

### 9. traveldoctor.ch/professionnels
- **Files**: Site-wide nav (all article pages), giardiasis.html CTA, malaria.html CTA
- **URL**: `https://traveldoctor.ch/professionnels` (404)
- **Note**: This is Dr. Cobuccio's own site. The /professionnels landing page needs to be created on traveldoctor.ch (WordPress/Divi).
- **Status**: NOT A LINK FIX — owner action needed

---

## Valid Links (403 = bot protection, DOIs resolve correctly)

| DOI | Resolves to |
|-----|------------|
| 10.1056/NEJMoa1411680 | nejm.org |
| 10.1056/NEJMra1508435 | nejm.org |
| 10.1086/518173 | academic.oup.com |
| 10.1093/cid/ciw710 | academic.oup.com |
| 10.1093/jtm/taae030 | academic.oup.com |
| 10.1093/ofid/ofad259 | academic.oup.com |
| 10.1128/mBio.00105-18 | journals.asm.org |
| 10.4269/ajtmh.12-0551 | ajtmh.org |
| 10.4269/ajtmh.13-0046 | ajtmh.org |
| 10.4269/ajtmh.16-84256 | ajtmh.org |
| sciencedirect.com (Lancet 2006) | Bot-blocked but valid |
| thelancet.com (Lancet Global Health) | Bot-blocked but valid |
