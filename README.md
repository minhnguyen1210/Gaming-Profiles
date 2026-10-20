# Gaming Profiles 2025 — CSC17104 final project

TODO: one-paragraph project summary.

## Team

| Name | Student ID |
| --- | --- |
| TODO | TODO |
| TODO | TODO |

## Question ownership & task breakdown

| Task | Owner | Notebook |
| --- | --- | --- |
| Data collection & exploration | TODO | `notebooks/01_collection_exploration.ipynb` |
| Question 1 | TODO | `notebooks/02_analysis_q1.ipynb` |
| Question 2 | TODO | `notebooks/02_analysis_q2.ipynb` |
| Question 3 | TODO | `notebooks/02_analysis_q3.ipynb` |
| ML question | TODO | `notebooks/03_ml_question.ipynb` |
| Summary & reflection | TODO | `notebooks/04_summary_reflection.ipynb` |

## Dataset

- **Description:** TODO
- **Source URL:** <https://www.kaggle.com/datasets/artyomkruglov/gaming-profiles-2025-steam-playstation-xbox>
- **License:** TODO
- **Collection method:** TODO
- **Related public notebooks & how we differ:** TODO

## Questions

1. TODO
2. TODO
3. TODO
4. ML question: TODO

## Key findings

TODO

## How to run

```bash
conda env create -f environment.yml
conda activate gaming-ds
bash scripts/download_data.sh
```

`download_data.sh` needs Kaggle API credentials in `~/.kaggle/kaggle.json` (or the
newer `~/.kaggle/access_token`); it prints setup instructions if none are found.
On Windows, run it from Git Bash.

Then run the notebooks in order: 01 → 02 → 03 → 04.

## Repository structure

```
.
├── environment.yml              # conda env "gaming-ds"
├── README.md
├── LLM_USAGE.md                 # log of LLM tool usage
├── data/
│   ├── raw/                     # downloaded dataset (not tracked)
│   └── processed/               # intermediate tables (not tracked)
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
    ├── config.py                # paths and constants
    └── data_loading.py          # table loaders (stubs)
```
