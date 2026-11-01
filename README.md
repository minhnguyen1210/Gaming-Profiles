# Gaming Profiles 2025 — CSC17104 final project

Final project for **CSC17104 – Programming for Data Science** (Faculty of Information Technology,
University of Science, VNU-HCM). We carry out a complete data science workflow on the Kaggle dataset
*Gaming Profiles 2025 (Steam, PlayStation, Xbox)*. The project brief is in
[`docs/CSC17104_2026_Final_Project.pdf`](docs/CSC17104_2026_Final_Project.pdf).

TODO: one-paragraph project summary (written once the questions are fixed).

## Team

| Member | Student ID | GitHub |
| --- | --- | --- |
| TODO | TODO | TODO |
| TODO | TODO | TODO |

## Question ownership & task breakdown

Each member owns two questions (spec 3.3); at least one question uses a machine learning model.

| Task | Owner | Notebook |
| --- | --- | --- |
| Data collection & exploration | TODO | `notebooks/01_collection_exploration.ipynb` |
| Q1 (non-ML) | TODO | `notebooks/02_analysis_q1.ipynb` |
| Q2 (non-ML) | TODO | `notebooks/02_analysis_q2.ipynb` |
| Q3 (non-ML) | TODO | `notebooks/02_analysis_q3.ipynb` |
| Q4 (ML) | TODO | `notebooks/03_ml_question.ipynb` |
| Summary & reflection | both | `notebooks/04_summary_reflection.ipynb` |
| Slides | both | `slides.pdf` |

## Dataset

| | |
| --- | --- |
| **Name** | Gaming Profiles 2025 (Steam, PlayStation, Xbox) |
| **Source** | Kaggle: <https://www.kaggle.com/datasets/artyomkruglov/gaming-profiles-2025-steam-playstation-xbox> |
| **Author** | Artyom Kruglov; built by his GameStatsHub project: <https://github.com/Smipe-a/gamestatshub> |
| **Published** | Version 1, last updated 2025-02-25 (the download script is pinned to this version) |
| **License** | CC0: Public Domain |
| **Collection method** | Web scraping and public APIs: Steam + Steam Web API (Steam games and users), Exophase (PlayStation and Xbox player rankings and history), TrueAchievements (Xbox games), TrueTrophies (PlayStation games), PSPrices (daily PlayStation and Xbox prices) |
| **Temporal coverage** | 2008-09-12 to 2025-01-12 according to the GameStatsHub README; price snapshots run until 2025-02-25 |
| **Size** | 4.0 GB (4,034,016,221 bytes), 21 CSV files |

Each platform has six tables; Steam has three more.

| Table | One row is | Platforms |
| --- | --- | --- |
| `games` | a game (title, developers, publishers, genres, supported languages, release date) | all |
| `achievements` | an achievement / trophy of a game | all |
| `players` | a player profile | all |
| `history` | one achievement unlocked by one player, with timestamp | all |
| `purchased_games` | a player and the list of game ids in their library | all |
| `prices` | the price of a game on one date (USD, EUR, GBP, JPY, RUB) | all |
| `reviews` | a user review of a game | Steam |
| `friends` | a player and their list of friends | Steam |
| `private_steamids` | a Steam id whose profile is private | Steam |

TODO (team): known limitations and biases, in our own words (see notebook 01, section 1.4).

### Related public work and how we differ

| Work | What it covers |
| --- | --- |
| GameStatsHub [`analysis/overview.ipynb`](https://github.com/Smipe-a/gamestatshub/blob/main/analysis/overview.ipynb) (dataset author) | games per platform and per release year, genres, top publishers/developers, achievements per game, top player countries |
| GameStatsHub [`analysis/behavior.ipynb`](https://github.com/Smipe-a/gamestatshub/blob/main/analysis/behavior.ipynb) (dataset author) | 2024 activity by hour/weekday/month, detection of achievement manipulation, MAU/WAU, completion rates (Kruskal–Wallis + Dunn tests), share of never-launched games, purchases by region/year/genre, ARPU and LTV with GDP per capita |
| Kaggle notebooks on this dataset | TODO: list them from the dataset's *Code* tab |

TODO: how our questions differ from the work above.

## Questions

| # | Question | Owner | Type | Depth criteria |
| --- | --- | --- | --- | --- |
| Q1 | TODO | TODO | non-ML | TODO |
| Q2 | TODO | TODO | non-ML | TODO |
| Q3 | TODO | TODO | non-ML | TODO |
| Q4 | TODO | TODO | ML | — |

Depth criteria: D1 combining data, D2 reshaping & time, D3 derived variables, D4 controlling for a confounder,
D5 quantifying uncertainty, D6 robustness check. Each non-ML question uses at least two; together they cover
at least four.

## Key findings

TODO

## How to run

Requirements: conda (Miniconda or Miniforge), about 5 GB of free disk space, and a bash shell (Git Bash on Windows).

### 1. Create the environment

```bash
conda env create -f environment.yml
conda activate gaming-ds
```

The environment uses only the `conda-forge` channel. On a fresh Miniconda install, conda may stop with
`CondaToSNonInteractiveError` (Terms of Service of the default Anaconda channels). Either remove those
channels from your conda configuration and run the command again:

```bash
conda config --add channels conda-forge
conda config --remove channels defaults
```

or accept the Terms of Service with the `conda tos accept ...` commands printed in the error message.

### 2. Download the data (~4 GB, not committed)

**Option A — script (recommended).** Run from the repo root with `gaming-ds` active; on Windows, use Git Bash.
No Kaggle account is needed: the Kaggle CLI prints an "Authentication required" notice and then downloads
the public dataset anonymously.

```bash
bash scripts/download_data.sh           # skipped if all 21 files are already in data/raw/
bash scripts/download_data.sh --force   # download again
```

The script downloads version 1 of the dataset and checks that all 21 files are in place.

**Option B — manual.** On the Kaggle page, make sure *Version 1* is selected, click *Download* and unzip the
archive, then move the `steam/`, `playstation/` and `xbox/` folders into `data/raw/`.

Either way the files must end up as `data/raw/<platform>/<table>.csv`, e.g. `data/raw/steam/history.csv`.

### 3. Run the notebooks in order

`01_collection_exploration` → `02_analysis_q1` → `02_analysis_q2` → `02_analysis_q3` → `03_ml_question`
→ `04_summary_reflection`

Use the `gaming-ds` environment as the kernel: in VS Code, pick the `gaming-ds` interpreter; with JupyterLab,
run `jupyter lab` from a terminal where `gaming-ds` is active.

Intermediate tables are written to `data/processed/` (not committed).

## Team workflow

The internal working agreement and the phase plan are written in Vietnamese for the two team members:

- [`CONTRIBUTING.md`](CONTRIBUTING.md): Git workflow, commit conventions, review checklist.
- [`docs/PROJECT_PLAN.md`](docs/PROJECT_PLAN.md): phases, task breakdown and checklists derived from the brief.
- [`docs/DECISIONS.md`](docs/DECISIONS.md): log of decisions shared by both members (cleaning rules, thresholds, scope).
- [`docs/QUESTIONS.md`](docs/QUESTIONS.md): candidate research questions with feasibility evidence from the dataset (not final).

In short: every change reaches `main` through a pull request reviewed by the other member, each member commits
the work they own, and no data files are committed.

## Repository structure

```
.
├── README.md
├── environment.yml              # conda env "gaming-ds"
├── LLM_USAGE.md                 # required by the course brief (section 6)
├── CONTRIBUTING.md              # team working agreement (Vietnamese)
├── slides.pdf                   # presentation (added in phase 6)
├── .github/                     # pull request and issue templates
├── .githooks/commit-msg         # commit message check (see CONTRIBUTING.md)
├── data/
│   ├── raw/                     # downloaded dataset, data/raw/<platform>/<table>.csv (not tracked)
│   └── processed/               # intermediate tables (not tracked)
├── docs/
│   ├── CSC17104_2026_Final_Project.pdf   # project brief
│   ├── PROJECT_PLAN.md          # phase plan and task breakdown (Vietnamese)
│   ├── DECISIONS.md             # decision log (Vietnamese)
│   └── QUESTIONS.md             # candidate questions and evidence (Vietnamese)
├── notebooks/
│   ├── 01_collection_exploration.ipynb
│   ├── 02_analysis_q1.ipynb
│   ├── 02_analysis_q2.ipynb
│   ├── 02_analysis_q3.ipynb
│   ├── 03_ml_question.ipynb
│   └── 04_summary_reflection.ipynb
├── reports/
│   └── figures/                 # exported plots
├── scripts/
│   └── download_data.sh         # fetch the dataset into data/raw/
└── src/
    ├── __init__.py
    ├── config.py                # paths, platforms, table names, RANDOM_STATE
    ├── data_loading.py          # load_table / load_all
    └── utils.py                 # report_rows: row count after each step that changes the data
```
