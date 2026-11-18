# Life Builders website

Source for lifebuilders.net, a ministry of Preston Woody Foundation Corporation (501(c)(3)).

## How it works
- `build.py` holds all page copy and generates the static site into `site/`.
- `site/assets/css/site.css` holds the design (navy #1C2340, gold #C09C49, cream #F7F5F0; Source Serif 4 headlines, Inter body).
- GitHub Pages serves the `site/` folder through the workflow in `.github/workflows/pages.yml`.

## Making a change
1. Edit the copy in `build.py` (or the CSS).
2. Run `python3 build.py`.
3. Commit and push. The site updates in about a minute.


The mentorship application and story form are Google Forms embedded in the `form-slot` boxes on `/mentorship/` and `/story/`. Responses land in Google Sheets.

## Giving
The Give buttons point to the GiveButter campaign (`GIVE_URL` at the top of `build.py`).
