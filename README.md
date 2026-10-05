# Geotechnical Report Template

A reusable Markdown template for geotechnical engineering reports, plus a
small script to fill in the project/client boilerplate automatically.

## Contents

- `template/geotechnical_report_template.md` — the master report template
  with the standard sections (Introduction, Site Description, Field
  Exploration, Laboratory Testing, Subsurface Conditions, Geologic and
  Seismic Hazards, Conclusions, Earthwork, Foundation Design, Seismic
  Design Criteria, Pavement/Slab-on-Grade, Construction Observation, and
  Limitations) and bracketed placeholders like `[PROJECT NAME]`.
  HTML comments (`<!-- PROJECT-TYPE NOTE: ... -->`) flag spots where
  wording should be adjusted for a residence vs. apartment vs. commercial
  project — those comments don't render/print in most Markdown viewers.
- `scripts/generate_report.py` — prompts for the core project fields
  (project name, type, address, client, firm, report number, date) and
  writes a filled-in copy to `output/<project-slug>_report.md`.

## Usage

1. Run the generator:

   ```bash
   python3 scripts/generate_report.py
   ```

2. Answer the prompts (press Enter to leave any field blank — the
   placeholder stays in the output for you to fill in later).
3. Open the generated file in `output/` and fill in the remaining
   bracketed placeholders: boring/test pit data, lab results, bearing
   pressure, seismic parameters, etc.

You can also skip the script entirely and just copy
`template/geotechnical_report_template.md` directly and edit it by hand.

## Important

This tool only automates assembling report boilerplate. All engineering
content — subsurface conditions, bearing capacity, seismic design
parameters, foundation recommendations, and conclusions — must still be
determined and reviewed by a licensed geotechnical engineer before the
report is issued.
