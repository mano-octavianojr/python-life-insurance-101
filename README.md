# Python through life insurance

Ten story-based Jupyter lessons for high school students learning Python from scratch. Follow Maya and Leo from their first printed message to an educational policy explorer. Insurance terms are explained in everyday language, using fictional people, policies, prices, and data.

## Read the training online

The training website contains all ten lessons, code examples, exercises, hints, and expandable sample solutions. It works on phones and desktops. Download notebooks to run the code in Jupyter; the website itself is a reading companion.

The website files are in [docs/](docs/index.html). To preview locally from the project folder:

```bash
python3 -m http.server 8000 --directory docs
```

Open `http://localhost:8000` in your browser.

### Publish with GitHub Pages

In this repository, open **Settings → Pages**. Under **Build and deployment**, select **Deploy from a branch**, choose **main** and **/docs**, then save. GitHub will provide the website address after deployment. The expected address is `https://mano-octavianojr.github.io/python-life-insurance-101/`; availability depends on Pages being enabled and deployment completing.

### Update the website

The notebooks are the source of the lesson content. After editing them, activate your Python environment and run:

```bash
python scripts/build_site.py
python scripts/validate_site.py
```

Commit the updated files in `docs/` together with the notebooks. Website generation requires the dependencies in `requirements.txt`.

## Run in Google Colab

Click an **Open in Colab** badge below, on a website lesson card, or inside a notebook to run Python in your browser. Sign in to Google if prompted. Choose **File → Save a copy in Drive** to retain edits; your changes do not modify this GitHub repository. No local installation is needed. Lesson 08 loads the public synthetic CSV from GitHub if a local copy is unavailable, so that lesson requires an Internet connection.

## Get started

Use Python 3.10 or newer (validated with Python 3.12). From the project directory:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m jupyter lab
```

On Windows, activate with `.venv\Scripts\activate` instead. Open the `notebooks` folder in JupyterLab and start with lesson 01. Choose the Python kernel from your virtual environment. Press **Shift+Enter** to run a cell. Use **Restart Kernel and Run All Cells** to reset and run a complete lesson.

Allow about 45–60 minutes per lesson. Learn in order, predict outputs before running code, and attempt exercises before reading sample solutions. Student workspace cells contain comments so an untouched notebook can run completely. Do not enter personal financial or health information.

## Lessons

| Notebook | Python focus | Run online |
|---|---|---|
| [01 — Meet Maya](notebooks/01_first_program.ipynb) | Printing, strings, comments  [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mano-octavianojr/python-life-insurance-101/blob/main/notebooks/01_first_program.ipynb) |
| [02 — Monthly Payment Mystery](notebooks/02_premiums.ipynb) | Variables, arithmetic, formatted strings  [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mano-octavianojr/python-life-insurance-101/blob/main/notebooks/02_premiums.ipynb) |
| [03 — Who Receives the Money?](notebooks/03_beneficiaries.ipynb) | Lists and dictionaries  [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mano-octavianojr/python-life-insurance-101/blob/main/notebooks/03_beneficiaries.ipynb) |
| [04 — Coverage Has a Calendar](notebooks/04_coverage_calendar.ipynb) | Dates, comparisons, conditionals  [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mano-octavianojr/python-life-insurance-101/blob/main/notebooks/04_coverage_calendar.ipynb) |
| [05 — Maya Builds a Budget](notebooks/05_budget.ipynb) | Loops and totals  [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mano-octavianojr/python-life-insurance-101/blob/main/notebooks/05_budget.ipynb) |
| [06 — Policy Comparison Club](notebooks/06_policy_comparison.ipynb) | Records and filtering  [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mano-octavianojr/python-life-insurance-101/blob/main/notebooks/06_policy_comparison.ipynb) |
| [07 — Reusable Calculator](notebooks/07_functions.ipynb) | Functions and error handling  [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mano-octavianojr/python-life-insurance-101/blob/main/notebooks/07_functions.ipynb) |
| [08 — Messy Records](notebooks/08_messy_records.ipynb) | pandas and local CSV data  [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mano-octavianojr/python-life-insurance-101/blob/main/notebooks/08_messy_records.ipynb) |
| [09 — Tell the Story with Charts](notebooks/09_charts.ipynb) | matplotlib and interpretation  [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mano-octavianojr/python-life-insurance-101/blob/main/notebooks/09_charts.ipynb) |
| [10 — Learning Fair](notebooks/10_learning_fair.ipynb) | Policy explorer and quiz  [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mano-octavianojr/python-life-insurance-101/blob/main/notebooks/10_learning_fair.ipynb) |

Each notebook includes a story, learning goals, an insurance explanation, a Python toolbox, predictions, a guided demo, a challenge, a hint, a sample solution, executable checks, a story ending, and an exit ticket. See [PLAN.md](PLAN.md) for the curriculum plan.

## Validate the lessons

With the environment activated, run:

```bash
python scripts/validate_notebooks.py
```

The validator checks notebook format and lesson sections, runs every notebook in a fresh kernel, executes numerical assertions, checks that the chart renders, and saves executed copies under `.validation/`. Source notebooks stay free of outputs for students. If you change demonstration inputs, update their assertions as appropriate.

The CSV under `data/` is synthetic and intentionally contains invalid records for lesson 08. With the repository downloaded, no network calls or credentials are needed to execute lessons after dependencies are installed. In Colab, lesson 08 fetches its public sample CSV when no local copy exists.

## Insurance scope

Examples use Philippine pesos (₱ / PHP); they are not real quotations or Philippine legal guidance. Benefits depend on a covered death, policy terms, and applicable law. Premium totals are not savings balances or benefit amounts. Dates and budget filters cannot establish claim approval, eligibility, or suitability. The coverage-gap calculator is simplified classroom arithmetic, not financial advice. Teachers should discuss death sensitively and let students use fictional scenarios throughout.
