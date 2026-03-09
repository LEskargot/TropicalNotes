# Design: traveldoctor.ch/professionnels Landing Page

**Date**: 2026-03-09
**Status**: Approved

## Purpose

Landing page for referring physicians arriving from TropicalNotes articles ("Référer un patient" links). Single-scroll page with phone + contact form + newsletter signup.

## Constraints

- Built as standalone HTML to paste into a Divi "Code" module on traveldoctor.ch (WordPress)
- Divi handles header/footer/nav — we only provide page body content
- Must match traveldoctor.ch palette: teal (#479793), mint (#12AD98), gold (#fad500), white background
- French only
- Contact form submits to ludovico.cobuccio@traveldoctor.ch
- Phone: dedicated referral line (placeholder until set up)
- Newsletter: link to traveldoctor.ch/newsletter (no provider yet, simple email collection)

## Page Structure

### Section 1: Hero
- **Headline**: "Avis spécialisé en infectiologie tropicale"
- **Credentials**: "Dr Ludovico Cobuccio — Spéc. FMH infectiologie · DTM&H Glasgow · Médecine des voyages ISTM"
- **One-liner**: "Conseil téléphonique pour les cas urgents. Formulaire pour les demandes non urgentes."
- Clean white background, centered text, no image

### Section 2: Two columns (phone | form)

**Left column — Urgent**
- Phone icon + large number: `+41 XX XXX XX XX` (placeholder, dedicated referral line)
- "Lun–Ven 08h30–18h00"
- "Conseil téléphonique immédiat"

**Right column — Non urgent**
- Simple form fields: Nom, Email, Message (textarea)
- Submit button → mailto: ludovico.cobuccio@traveldoctor.ch
- "Réponse sous 48h ouvrables"
- Form submission: WordPress/Divi native form handler or simple mailto fallback

### Section 3: Newsletter one-liner
- "Restez informé — actualités en médecine tropicale et des voyages"
- Email input + "S'inscrire" button
- Links to / submits to traveldoctor.ch/newsletter

## Separate Task: TropicalNotes Link Revert

Revert all `tel:` referral links across TropicalNotes articles back to `https://traveldoctor.ch/professionnels` so they point to this new page.

## Technical Notes

- HTML + inline styles (Divi Code module strips external CSS)
- Responsive: stacks to single column on mobile
- Form: use `<form action="mailto:ludovico.cobuccio@traveldoctor.ch" method="POST" enctype="text/plain">` as minimal fallback. Recommend replacing with Divi Contact Form module or WPForms after paste for better UX.
- Newsletter field: same mailto approach or Divi Email Optin module
