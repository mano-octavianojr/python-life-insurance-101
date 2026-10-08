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
