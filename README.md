# My Places (v2)

> A more colourful take on the Bump scratch map — places sorted into 8 lifestyle categories instead of 4 personas.

A redesign of [The Four Mes](https://bump-may-story.streamlit.app) that swaps the persona switcher for a left-side category panel and a bottom view-mode toolbar, inspired by the US Power Plants infrastructure-map look.

## What's new in v2

- **Left category panel** — places now classified into 8 colour-coded categories: 🏡 Home, ☕ Cafe, 💼 Work, 🥾 Hike, 🍜 Food, ✈️ Travel, 💆 Wellness, 📚 Study. Multi-select: click any category to dim it out.
- **Glowing category bubbles** — each tagged place renders as a soft halo + bright core, sized by log count and coloured by category.
- **Bottom view-mode toolbar** — Points / Heatmap / 3D Towers, each independently toggleable.
- **Personas demoted to a secondary view** — the original Home/Adventure/Traveler/Student personas still live in the left panel and drive the story-card flyout.

## Stack

Same as v1:

- **deck.gl 9** for 3D hex extrusion + scatter bubbles
- **MapLibre GL JS 5** basemap (CARTO dark-matter) with globe projection
- **h3-js 4** for Uber's H3 hexagonal indexing
- **D3.js 7** for the story-page charts
- **Streamlit** wrapper for hosting only

All visual libraries load from CDN. The dashboard (`bump_3d.html`) is one self-contained file.

## Files

| File | Purpose |
|------|---------|
| `app.py` | Streamlit wrapper, just embeds the HTML |
| `requirements.txt` | Python deps (just streamlit) |
| `bump_3d.html` | The dashboard, single self-contained file |
| `scratch_map_3221_hexes.csv` | Raw H3 hex log data (3,221 rows) |
| `places_87.csv` | 87 places tagged in Bump |
| `report.pdf` | Project report (4 pages) |
| `README.md` | This file |

## Running locally

```
pip install -r requirements.txt
streamlit run app.py
```

Or just open `bump_3d.html` directly in a browser. Both work.

## Tuning the categories

Category assignments are auto-generated from each place's name by regex rules at the top of `bump_3d.html` (search for `CAT_RULES`). To recategorise a place, either:

1. Tweak the regex pattern of the target category, or
2. Add a more-specific rule higher up in the list (first match wins).

## Note

This dashboard knowingly publishes a real home and workplace. The data subject and the publisher are the same person; consent is theirs to give. Do not replicate this pattern with someone else's data without explicit consent.
