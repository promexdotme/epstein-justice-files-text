# Jeffrey Epstein Justice Files - CONTAINS MANY UNREDACTED - Plain Text Corpus

This repository contains the plain text versions of the released court documents regarding the Jeffrey Epstein/Ghislaine Maxwell cases, originally sourced from the [United States Department of Justice](https://www.justice.gov/).

## IMPORTANT NOTE — UNREDACTED TEXT RECOVERED
**Many PDFs used overlay redaction boxes. When extracting with Python, a large set of files revealed the underlying text (UNREDACTED).** This is a key aspect of this corpus.

**Purpose:**
The original documents are provided as PDFs, which are difficult to process programmatically. This repository provides flattened, UTF-8 encoded text files to facilitate:
- Natural Language Processing (NLP)
- Retrieval-Augmented Generation (RAG) for LLMs
- Full-text search and analysis
- Data mining and research

## Data Source
All documents were originally downloaded from the official release portals.
*   **Original Format:** PDF (Scanned/OCR) - Not uploaded [50GB size] of 2024-2025 files but a LINKS page included if you wish to load into a downloader.
*   **Converted Format:** Plain Text (.txt)

## Dataset Status (1 to 12)
Datasets 1 through 12 are now included, with datasets 9 to 12 added. The full collection of PDFs (over 350 GB) has been stripped of useless data sizes via Python scripts and converted to plain text.

Each text set in folders like `volume1` has been merged into ONE TEXT dataset per folder. This reduces the count to a little over 1,000 text files, each with an LLM-suitable size of ~1, 2, or 3 MB. A few folders went overboard in size (over 50 MB) but are rare and can be split if needed, while still remaining LLM-readable.

## Folder Structure & Naming Convention
To make the dataset easier to ingest, the original nested folder structure has been "flattened." The folder path is preserved in the filename using double underscores (`__`).

Ingested in a vector database and chat agent created for the files here (temporarily disabled due to token abuse by non-researchers):
`https://promex.ai/epstein`

If someone wants to donate an access key (OpenAI / Grok / Gemini), we can re-open full access.

Meanwhile, I have a limited per-user access link:
`https://promex.me/app/epstein-files/`
This grants $5 in free tokens and allows signup/registration via WhatsApp code to prevent anonymous spam or token abuse.

Single Pages of OCR results are added as a zip file in Packages as an asset.


