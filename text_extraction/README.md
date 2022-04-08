# Text Extraction using Tika & Data Preprocessing

This folder contains code for the extracting the text from PDF files using Tika and getting the data ready to feed into the Grover.

Look `grover_preparation_test.ipynb` for more details, this notebook file will write `Bik_text.jsonl` and `Bik72_text.jsonl`.

## Datasets

- `Bik_text.jsonl` is a file containing all the metadata for each .pdf paper including texts, authors, date, domain etc.. Each line represents a one paper with total 214 lines. This file is a main input file that Grover will use to generate fake text.
- `Bik72_text.jsonl` is file containing 72 randomly sampled papers from the main 214 papers. Shares same format with `Bik.text.jsonl`.
- `PDFs` folder contains all the scientific literatures in `Bik_v2.tsv` file as a .pdf format. Total 214 pdf files.

