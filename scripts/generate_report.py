#!/usr/bin/env python3
"""Fill in the geotechnical report template with project-specific values.

Usage:
    python3 generate_report.py

Prompts for the core project fields, substitutes them into
geotechnical_report_template.md, and writes the result to
output/<project-slug>_report.md. Any placeholder not covered by a
prompt (e.g. bearing pressure, boring counts, lab results) is left
in the output exactly as [BRACKETED TEXT] for manual completion —
this script only automates the project/client boilerplate, not
engineering content.

Looks for the template next to this script, in a template/ subfolder,
or in a sibling template/ folder (the repo layout), so it works whether
you cloned the repo or just downloaded the files into one flat folder.
"""
import datetime
import re
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
TEMPLATE_CANDIDATES = [
    SCRIPT_DIR / "geotechnical_report_template.md",
    SCRIPT_DIR / "template" / "geotechnical_report_template.md",
    SCRIPT_DIR.parent / "template" / "geotechnical_report_template.md",
]
TEMPLATE_PATH = next((p for p in TEMPLATE_CANDIDATES if p.exists()), None)
OUTPUT_DIR = SCRIPT_DIR / "output"

# Maps the placeholder text (as it appears in the template, without
# brackets) to the prompt shown to the user. Order controls prompt order.
FIELDS = [
    ("PROJECT NAME", "Project name"),
    ("PROJECT TYPE", "Project type (e.g. Single-Family Residence, Apartment Complex, Commercial Building)"),
    ("SITE ADDRESS", "Site address"),
    ("CLIENT NAME", "Client name"),
    ("CLIENT ADDRESS", "Client address"),
    ("REPORT NUMBER", "Report number"),
    ("PROJECT NUMBER", "Project number"),
    ("FIRM NAME", "Your firm name"),
    ("FIRM ADDRESS", "Your firm address"),
]


def slugify(text: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "_", text.strip()).strip("_").lower()
    return slug or "project"


def main() -> None:
    if TEMPLATE_PATH is None:
        checked = "\n".join(f"  - {p}" for p in TEMPLATE_CANDIDATES)
        raise SystemExit(
            "Template not found. Checked:\n" + checked +
            "\nMake sure geotechnical_report_template.md is in the same folder as this script."
        )

    print("Geotechnical report generator")
    print("Press Enter to leave a field blank (placeholder stays in the report).\n")

    values = {}
    for placeholder, prompt in FIELDS:
        answer = input(f"{prompt}: ").strip()
        if answer:
            values[placeholder] = answer

    report_date = input("Report date [default: today]: ").strip()
    if report_date:
        values["REPORT DATE"] = report_date
    else:
        values["REPORT DATE"] = datetime.date.today().strftime("%B %d, %Y")

    text = TEMPLATE_PATH.read_text(encoding="utf-8")
    for placeholder, value in values.items():
        text = text.replace(f"[{placeholder}]", value)

    project_name = values.get("PROJECT NAME", "project")
    OUTPUT_DIR.mkdir(exist_ok=True)
    output_path = OUTPUT_DIR / f"{slugify(project_name)}_report.md"
    output_path.write_text(text, encoding="utf-8")

    print(f"\nReport written to: {output_path}")
    print("Remaining [BRACKETED] placeholders still need to be filled in by hand "
          "(engineering content, boring data, lab results, etc.).")


if __name__ == "__main__":
    main()
