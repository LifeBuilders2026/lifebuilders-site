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

## Forms
The mentorship, story and contact forms are built into the site (`forms_spec.py` renders them, `site/assets/js/forms.js` runs them). Each one posts its answers into a matching Google Form, so responses land in the "Life Builders Form Responses" Google Sheet (tabs: Mentorship Applications, Story Submissions, Contact Messages) and trigger the alert email from `tools/form-alerts.gs`.

If you add, remove or reword a question in one of the Google Forms, update that form's entry in `forms_spec.py` to match (each field name is the Google Form's `entry.<id>`), rebuild, and send one test submission. Each site form links to its Google Form as a backup. `tools/create-forms.gs` is the script that created the Google Forms.

## Giving
The Give buttons point to the GiveButter campaign (`GIVE_URL` at the top of `build.py`).
