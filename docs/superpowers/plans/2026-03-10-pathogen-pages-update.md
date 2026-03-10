# Pathogen Pages — Research & Content Update Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Update all 17 pathogen pages with literature-backed content via PubMed/Scholar Gateway research, replacing thin/image-only sections with proper textbook-style prose and tables.

**Architecture:** Sequential per pathogen: research (PubMed + Scholar MCP) → `docs/research/[pathogen].md` source file → update `pages/[category]/[pathogen].html` → commit + push. Each pathogen is independent and self-contained.

**Tech Stack:** PubMed MCP (`mcp__claude_ai_PubMed__*`), Scholar Gateway MCP (`mcp__claude_ai_Scholar_Gateway__semanticSearch`), Tailwind CDN (inline config, already in pages), vanilla HTML.

**Spec:** `docs/superpowers/specs/2026-03-10-pathogen-pages-research-workflow.md`

---

## Pathogen Order

1. **malaria** ← start here (template for all others)
2. dengue
3. rickettsiosis
4. enteric_fever
5. schistosomiasis
6. leishmaniasis
7. chikungunya
8. zika
9. yellow_fever
10. rabies
11. hepatitis_a
12. hepatitis_e
13. leptospirosis
14. african_trypanosomiasis
15. american_trypanosomiasis
16. giardiasis
17. intestinal_problems_parasites

---

## File Map

| File | Action | Role |
|------|--------|------|
| `docs/research/malaria.md` | Create | Source of truth — all clinical content |
| `pages/parasites/malaria.html` | Modify | Pathogen page — textbook style |
| *(repeat pattern for each pathogen)* | | |

---

## Chunk 1: Malaria

### Task 1 — Literature research: malaria

**Files:**
- Read: `C:\Users\ludov\Projects\md-slides\docs\plans\research-fever-syndromes.md` (existing malaria notes)
- Read: `pages/parasites/malaria.html` (current state)

- [ ] **Step 1: Read existing research notes from md-slides**

Read `C:\Users\ludov\Projects\md-slides\docs\plans\research-fever-syndromes.md` (section 1: PALUDISME). This contains Swiss-specific data already gathered: Senn et al. 2022, Bjorkman CID 2017, Vuuren J Travel Med 2024, Slack & Genton J Travel Med 2024, PADH data. Use these as a starting point — do not re-search what is already documented.

- [ ] **Step 2: PubMed search — Swiss epidemiology**

Tool: `mcp__claude_ai_PubMed__search_articles`
Query: `"imported malaria" Switzerland epidemiology`
Limit: 5 most recent. Extract: case counts, lethality, species distribution, trends.

- [ ] **Step 3: PubMed search — artemether-lumefantrine treatment failures**

Tool: `mcp__claude_ai_PubMed__search_articles`
Query: `artemether-lumefantrine treatment failure non-immune travelers`
Limit: 5. Extract: failure rates, weight dependency, follow-up recommendations.

- [ ] **Step 4: PubMed search — artesunate severe malaria + PADH**

Tool: `mcp__claude_ai_PubMed__search_articles`
Query: `artesunate severe malaria post-artesunate delayed hemolysis travelers`
Limit: 5. Extract: PADH incidence, timing, monitoring protocol.

- [ ] **Step 5: PubMed search — malaria diagnosis (TDR + thick film)**

Tool: `mcp__claude_ai_PubMed__search_articles`
Query: `malaria rapid diagnostic test thick blood film sensitivity travelers`
Limit: 5. Extract: TDR sensitivity for P. falciparum vs other species, repeat testing recommendations.

- [ ] **Step 6: Scholar Gateway search — WHO malaria treatment guidelines**

Tool: `mcp__claude_ai_Scholar_Gateway__semanticSearch`
Query: `WHO malaria treatment guidelines 2023 severe uncomplicated`
Limit: 5. Extract: first-line regimens, severe malaria criteria, dosing.

- [ ] **Step 7: Scholar Gateway search — P. vivax relapse prevention**

Tool: `mcp__claude_ai_Scholar_Gateway__semanticSearch`
Query: `Plasmodium vivax relapse prevention primaquine tafenoquine G6PD`
Limit: 5. Extract: primaquine/tafenoquine dosing, G6PD testing requirement, relapse rates.

---

### Task 2 — Write research file: `docs/research/malaria.md`

**Files:**
- Create: `docs/research/malaria.md`

- [ ] **Step 1: Create `docs/research/` directory**

```bash
mkdir -p C:\Users\ludov\Projects\TropicalNotes\docs\research
```

- [ ] **Step 2: Create research file with all findings**

Path: `C:\Users\ludov\Projects\TropicalNotes\docs\research\malaria.md`

Structure:
```markdown
# Research : Malaria (Paludisme)
_Date : 2026-03-10 | Sources : PubMed, Scholar Gateway, md-slides research-fever-syndromes.md_

## Contexte suisse / épidémiologie
[Swiss case counts, species distribution, lethality from Senn et al. + recent data]

## Présentation clinique
[Symptoms, severe malaria criteria, afebrile presentation pitfall]

## Diagnostic
[TDR sensitivity, thick film + frottis, PCR, when to repeat, OFSP declaration obligatoire]

## Traitement

### P. falciparum non compliqué
[Artemether-lumefantrine (Riamet): dosing, weight threshold >65kg, ECG monitoring, J28 follow-up]
[Atovaquone-proguanil (Malarone): alternative]

### P. falciparum sévère
[Artesunate IV dosing schedule, PADH — timing, monitoring (Hb/LDH/haptoglobine x4 semaines)]

### P. vivax / P. ovale (rechutes)
[Primaquine anti-rechute, G6PD testing required, tafenoquine alternative]

### P. malariae / P. knowlesi
[Chloroquine, notes on P. knowlesi severity]

## Points clés
### Piège
[TDR négatif ≠ paludisme exclu — sensibilité ~95% P. falciparum mais <80% P. vivax. Répéter à 12-24h.]
[Patient >65 kg sous Riamet: 1/10 recidive à J20-28]

### Perle
[Swiss TPH 24h/7j: +41 61 284 81 44]
[PADH: surveiller Hb pendant 4 semaines après artésunate IV]

## Références
1. [Numbered references with DOI]
```

- [ ] **Step 2: Verify file saved correctly**

Run: `ls C:\Users\ludov\Projects\TropicalNotes\docs\research\`
Expected: `malaria.md` appears.

---

### Task 3 — Update `pages/parasites/malaria.html`

**Files:**
- Modify: `pages/parasites/malaria.html`
- Reference: `docs/research/malaria.md` (source of truth)

**Key changes from current state:**
- Section `#diagnostic`: currently one image (CHUV guide scan) → replace with text content
- Section `#traitement`: currently 3 images (CHUV guide scans) → replace with text tables/sections
- Sections `#repartition`, `#clinique`, `#examen`, `#labo`: thin text → enrich with research data
- Add `#references` section at bottom
- Add `#syndrome-link` callout linking back to `pages/syndromes/fievre.html`
- Update TOC sidebar to include new sections

- [ ] **Step 1: Read current malaria.html fully**

Read `pages/parasites/malaria.html` in full to understand all existing content before editing.

- [ ] **Step 2: Update section — Répartition géographique**

Enrich with Swiss import data: keep map image, add paragraph with Swiss case numbers, dominant regions (Afrique de l'Ouest/Centrale = majority), species shift (P. vivax now 36% from Senn 2022).

- [ ] **Step 3: Update section — Présentation clinique + Examen + Labo**

**Keep the three sections separate** (do not merge). Enrich each:
- `#clinique`: Add severe malaria criteria (WHO): altered consciousness, Hb <7 g/dL, renal failure, ARDS, circulatory shock, acidosis, jaundice + other severity signs, parasitemia ≥2% (Swiss threshold). Clarify that up to 1/3 present without fever at time of consultation.
- `#examen`: Add splenomegaly prominence, jaundice in severe forms; note absence of rash (useful differential vs dengue/rickettsia).
- `#labo`: Add specific thresholds: thrombocytopenia <150 G/L (non-specific but frequent), elevated bilirubin (conjugated), creatinine elevation. Severe: Hb <7 g/dL, hypoglycemia, metabolic acidosis.

- [ ] **Step 4: Replace section — Diagnostic (remove image)**

Remove `malaria1.jpg` image. Replace with text:

```html
<section id="diagnostic" class="mb-10">
  <h2 class="font-serif text-2xl text-teal-900 mb-4">Diagnostic</h2>

  <h3 class="font-sans font-semibold text-teal-800 mb-2 mt-4">Bilan de première ligne</h3>
  <table class="article-table mb-4">
    <thead><tr><th>Examen</th><th>Remarque</th></tr></thead>
    <tbody>
      <tr><td>TDR HRP2 (PfHRP2)</td><td>Sensibilité ~95% pour P. falciparum ; &lt;80% pour P. vivax/ovale</td></tr>
      <tr><td>Frottis mince + goutte épaisse</td><td>Gold standard. Permet la quantification de la parasitémie</td></tr>
      <tr><td>Répétition à 12–24h</td><td>Si TDR négatif et forte suspicion clinique</td></tr>
      <tr><td>PCR Plasmodium</td><td>Si discordance TDR/frottis, ou faible parasitémie</td></tr>
    </tbody>
  </table>

  <div class="callout-danger">
    <p class="text-sm font-bold text-red-700 mb-1">⚠ Déclaration obligatoire</p>
    <p class="text-sm text-teal-800">Tout cas de paludisme est à déclarer à l'OFSP/BAG (formulaire en ligne).</p>
  </div>

  <div class="callout-piege">
    <p class="text-sm font-bold text-gold-700 mb-1">⚠ Piège</p>
    <p class="text-sm text-teal-800">Un TDR négatif n'exclut pas le paludisme. Étude CHUV (Slack &amp; Genton, J Travel Med 2024, n=4 972) : seuls 0.08% diagnostiqués sur 2e ou 3e test — mais le dogme du 3x reste valide face à forte suspicion.</p>
  </div>
</section>
```

- [ ] **Step 5: Replace section — Traitement (remove 3 images)**

Remove `malaria2.jpg`, `malaria3.jpg`, `malaria4.jpg`. Replace with text-based treatment content organized in sub-sections:

```html
<section id="traitement" class="mb-10">
  <h2 class="font-serif text-2xl text-teal-900 mb-4">Traitement</h2>

  <h3 ...>P. falciparum non compliqué</h3>
  <!-- 1re ligne: Riamet, dosing, ECG monitoring, weight note -->
  <!-- Alternative: Malarone -->
  <!-- Contrôle à J28 si >65 kg -->

  <h3 ...>P. falciparum sévère</h3>
  <!-- Artésunate IV schedule: 2.4 mg/kg H0, H12, H24, puis /24h -->
  <!-- Relais PO si parasitémie ≤1% -->
  <!-- PADH: 15-22%, survient J7-30, surveillance Hb/LDH/haptoglobine x4 sem -->

  <h3 ...>P. vivax / P. ovale (prévention rechutes)</h3>
  <!-- Primaquine 0.25-0.5 mg/kg/j x14j — test G6PD obligatoire avant -->
  <!-- Tafenoquine alternative (dose unique) -->

  <h3 ...>P. malariae / P. knowlesi</h3>
  <!-- Chloroquine. Note: P. knowlesi peut évoluer comme P. falciparum -->
</section>
```

- [ ] **Step 6: Add perle callout box**

For the perle (clinical pearl), use the existing `.callout-referer` CSS class (already mint-colored, defined in the `<style>` block). Do NOT use a `callout-perle` class — it does not exist. Example:
```html
<div class="callout-referer">
  <p class="text-sm font-bold text-mint-700 mb-1">✦ Perle</p>
  <p class="text-sm text-teal-800">Swiss TPH 24h/7j : <strong>+41 61 284 81 44</strong>. Patient &gt;65 kg sous Riamet : contrôle frottis à J28.</p>
</div>
```

- [ ] **Step 7: Add section — Références**

Below `#referer`, add `<section id="references" class="mb-10">` with numbered references from `docs/research/malaria.md`.

- [ ] **Step 8: Add syndrome back-link callout**

In the sidebar, add a callout box linking back to `pages/syndromes/fievre.html`:
```html
<div class="mt-4 p-4 bg-teal-50 border border-teal-200/50 rounded-xl">
  <p class="text-xs text-teal-700/70 mb-2">Contexte clinique</p>
  <a href="../syndromes/fievre.html" class="text-sm text-teal-600 hover:text-mint-600 font-medium transition-colors">
    → Fièvre au retour de voyage
  </a>
</div>
```

- [ ] **Step 9: Update TOC sidebar**

Add new TOC entries for any added sections (references, and sub-sections if needed).

- [ ] **Step 10: Visual check**

Open `pages/parasites/malaria.html` in browser (or use Playwright screenshot). Verify:
- No broken image references
- TOC links resolve to correct section IDs
- Callout boxes display correctly
- Treatment tables are readable

---

### Task 4 — Commit and push: malaria

- [ ] **Step 1: Stage files**

```bash
git add docs/research/malaria.md pages/parasites/malaria.html
```

- [ ] **Step 2: Commit**

```bash
git commit -m "Update malaria: research file + content refresh (replace image-based sections)"
```

- [ ] **Step 3: Push**

```bash
git push
```

- [ ] **Step 4: Verify live**

Navigate to `https://tropicalnotebook.ch/pages/parasites/malaria.html` — confirm new content visible, no broken sections.

---

## Template for subsequent pathogens (Tasks 5–21)

For each subsequent pathogen, repeat the same 4-task structure:
1. Literature research (PubMed + Scholar Gateway, 4–6 targeted searches)
2. Write `docs/research/[pathogen].md`
3. Update `pages/[category]/[pathogen].html`
4. Commit + push

**Key research axes per pathogen type:**

| Pathogen | Priority search axes |
|----------|---------------------|
| dengue | 2024 outbreak data, WHO 2025 arboviral guidelines, Qdenga (Swissmedic 2024), severe dengue management |
| rickettsiosis | Eschar diagnosis, doxycycline dosing/duration, Swiss/European import data |
| enteric_fever | XDR typhoid (azithromycin), blood culture sensitivity, Switzerland import data |
| schistosomiasis | Katayama fever, praziquantel timing, Swiss TPH data |
| leishmaniasis | Cutaneous vs visceral management, liposomal amphotericin B, Swiss referral |
| chikungunya | Chronic arthralgia (30-40%), neonatal transmission, Swissmedic status |
| zika | Neurological complications, pregnancy protocol, sexual transmission window |
| yellow_fever | Vaccine contraindications, SAE (AEFI), 17DD attenuated virus risk |
| rabies | Post-exposure prophylaxis protocol (D0/D3/D7/D14), Swiss VAR recommendations |
| hepatitis_a | Vaccination schedule, immune globulin, Swiss epidemiology |
| hepatitis_e | HEV genotype 3 (pigs, Europe), chronic HEV in immunosuppressed |
| leptospirosis | Weil's disease, penicillin/doxycycline, occupational + recreational risk |
| african_trypanosomiasis | Stage 1 vs 2, fexinidazole (oral, 2019 WHO), Swiss referral |
| american_trypanosomiasis | Chagas, benznidazole, screening migrants from endemic areas |
| giardiasis | Metronidazole vs tinidazole, treatment failure, post-infectious IBS |
| intestinal_problems_parasites | Broad scope: Ascaris, hookworm, Strongyloides, albendazole, mebendazole |
