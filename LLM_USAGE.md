# LLM usage log

Every significant use of an LLM tool in this project is recorded here, one row per use (spec section 6):
the tool, what we asked, and how we used or changed the answer.

| Date | Member | Tool | What we asked | How we used/changed the answer |
| --- | --- | --- | --- | --- |
| 2026-10-13 | CaoThien1402 | Claude Code | Scaffold the repository: conda environment file, folder layout, download script, `src` stubs, empty notebook skeletons, README skeleton. No analysis, questions or findings. | TODO |
| 2026-11-01 | minhnguyen1210 | Claude Code | Project setup support: summarise the brief and dataset metadata, set up and pin the conda environment, fix the download script, extend the notebook skeletons and `src` helpers, draft the team workflow documents, and suggest candidate questions with feasibility checks. No analysis, answers or findings. | TODO |
| 2026-11-21 | minhnguyen1210 | Claude Code | Notebook 01, section 1 (Data collection): read the Kaggle metadata and the GameStatsHub repository (README, pipeline and ERD figures, collection scripts), verify the facts against the raw files (row counts, date ranges, review-vote parsing artefacts, missing game ids), draft sections 1.1–1.4 in English, and turn our own reasons for choosing the dataset (interest in games, following platform news, curiosity about the market and other players) into the English text of section 1.5, adding verified dataset strengths and stakeholders. | TODO |
| 2026-11-21 | minhnguyen1210 | Claude Code | Notebook 01, sections 2.1–2.8 (game side: `games`, `achievements`, `prices`): check dtypes, parser engines, NA handling and list columns on the raw files; write `GAME_READ_ARGS`, `load_game_table` and `parse_list_column` in `src/data_loading.py`; write the game-side exploration code (overview and data dictionary, joins, time coverage, numerical and categorical columns, missing data, relationships), the four `explore_*` figures and draft the observation notes from the outputs. Then review all game-side code (fixes: count each genre once per game, check zero prices against the USD price, compare pyarrow row counts). | TODO |
