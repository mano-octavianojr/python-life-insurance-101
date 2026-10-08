# Validation results

Validated on 2026-10-08 using Python 3.12.14 and the dependency ranges in requirements.txt (JupyterLab 4.6.4, nbclient 0.10.4, nbformat 5.11.1, ipykernel 7.4.0, pandas 2.3.3, matplotlib 3.11.2).

Command: `python scripts/validate_notebooks.py`

- All 10 notebook schemas and required lesson sections passed.
- All 40 code cells executed in order in fresh, independent kernels, with no error outputs.
- Assertions verified arithmetic, beneficiary shares, date boundaries, budget totals, filtering, coverage-gap calculations, data-cleaning results, chart values, quiz scores, and invalid-input rejection.
- The chart produced a PNG output; visual inspection confirmed readable axes, PHP units, a legend, and the expected two lines.
- `python -m pip check` reported no broken requirements.
- `git diff --check` passed.

Executed copies are generated locally under the ignored `.validation/` directory. Committed source notebooks intentionally contain no outputs or execution counts.

Content was reviewed for consistency with the plan, beginner explanations, fictional examples, and the distinction between payments, benefits, eligibility, and claim approval. See TEACHER_GUIDE.md for expected answers and review details. No external insurance professional or classroom pilot reviewed the curriculum. Software execution checks do not establish student comprehension or accuracy for a particular real policy.

## Training website

The static website is generated directly from the source notebooks using `python scripts/build_site.py`.

- `python scripts/validate_site.py` passed for all 11 pages and 250 local links.
- All lesson sections are present, exported code matches notebook code, notebook downloads match their sources, and sample solutions are grouped in disclosure panels.
- The downloadable CSV matches the source dataset.
- Local HTTP requests returned 200 and expected content for all 11 pages.
- Git whitespace checks passed.

The layout includes a mobile viewport, responsive columns, keyboard focus styles, a skip link, and native expandable solutions. Browser visual testing was not performed in this environment. GitHub Pages activation and public deployment were not verified; README.md documents how to enable branch deployment from main /docs.

## Google Colab links

Added official Open in Colab badges for every source notebook, README lesson row, website card, and lesson page. The website validator checks the expected repository/branch/notebook targets and all ten catalog badges. All 10 notebooks and 40 code cells passed again. Lesson 08 also executed successfully from a directory without local data, exercising its public GitHub CSV fallback. Actual signed-in Google Colab sessions were not tested.
