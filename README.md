# Python through life insurance

Ten story-based Jupyter notebooks teach high school students Python from scratch through simple life insurance examples. Follow Maya and Leo from their first printed message to a policy explorer, with guided demos, exercises, hints, and sample solutions. All people, policies, prices, and data are fictional educational examples.

## How to access

### Run in Google Colab

Click an **Open in Colab** button in the lessons table to run a notebook in your browser. No local installation is needed. Sign in to Google if prompted, then choose **File → Save a copy in Drive** to keep your work. Lesson 08 automatically loads its sample data from GitHub when no local copy is available.

### Run locally

Install Python 3.10 or newer, clone or download this repository, and open a terminal in the project folder. Run:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m jupyter lab
```

On Windows, use `.venv\Scripts\activate` to activate the environment. Open the `notebooks` folder in JupyterLab, start with lesson 01, and press **Shift+Enter** to run each cell.

## Lessons

| Notebook | Python focus | Run online |
|---|---|---|
| [01 — Meet Maya](notebooks/01_first_program.ipynb) | Printing, strings, comments | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mano-octavianojr/python-life-insurance-101/blob/main/notebooks/01_first_program.ipynb) |
| [02 — Monthly Payment Mystery](notebooks/02_premiums.ipynb) | Variables, arithmetic, formatted strings | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mano-octavianojr/python-life-insurance-101/blob/main/notebooks/02_premiums.ipynb) |
| [03 — Who Receives the Money?](notebooks/03_beneficiaries.ipynb) | Lists and dictionaries | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mano-octavianojr/python-life-insurance-101/blob/main/notebooks/03_beneficiaries.ipynb) |
| [04 — Coverage Has a Calendar](notebooks/04_coverage_calendar.ipynb) | Dates, comparisons, conditionals | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mano-octavianojr/python-life-insurance-101/blob/main/notebooks/04_coverage_calendar.ipynb) |
| [05 — Maya Builds a Budget](notebooks/05_budget.ipynb) | Loops and totals | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mano-octavianojr/python-life-insurance-101/blob/main/notebooks/05_budget.ipynb) |
| [06 — Policy Comparison Club](notebooks/06_policy_comparison.ipynb) | Records and filtering | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mano-octavianojr/python-life-insurance-101/blob/main/notebooks/06_policy_comparison.ipynb) |
| [07 — Reusable Calculator](notebooks/07_functions.ipynb) | Functions and error handling | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mano-octavianojr/python-life-insurance-101/blob/main/notebooks/07_functions.ipynb) |
| [08 — Messy Records](notebooks/08_messy_records.ipynb) | pandas and local CSV data | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mano-octavianojr/python-life-insurance-101/blob/main/notebooks/08_messy_records.ipynb) |
| [09 — Tell the Story with Charts](notebooks/09_charts.ipynb) | matplotlib and interpretation | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mano-octavianojr/python-life-insurance-101/blob/main/notebooks/09_charts.ipynb) |
| [10 — Learning Fair](notebooks/10_learning_fair.ipynb) | Policy explorer and quiz | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mano-octavianojr/python-life-insurance-101/blob/main/notebooks/10_learning_fair.ipynb) |

## Development approach

This project was built through vibe coding with AI assistance. The code and results were reviewed and validated by a human.
