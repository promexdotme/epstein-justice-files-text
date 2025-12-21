# Jeffrey Epstein Justice Files - Plain Text Corpus

This repository contains the plain text versions of the released court documents regarding the Jeffrey Epstein/Ghislaine Maxwell cases, originally sourced from the [United States Department of Justice](https://www.justice.gov/).

**Purpose:**
The original documents are provided as PDFs, which are difficult to process programmatically. This repository provides flattened, UTF-8 encoded text files to facilitate:
- Natural Language Processing (NLP)
- Retrieval-Augmented Generation (RAG) for LLMs
- Full-text search and analysis
- Data mining and research

## Data Source
All documents were originally downloaded from the official release portals.
*   **Original Format:** PDF (Scanned/OCR) - Not uploaded [5GB size] but a LINKS page included if you wish to load into a downloader.
*   **Converted Format:** Plain Text (.txt)

## Folder Structure & Naming Convention
To make the dataset easier to ingest, the original nested folder structure has been "flattened." The folder path is preserved in the filename using double underscores (`__`).

**Format:**
`{Original_Folder}__{Original_Filename}.txt`

**Example:**
*   **Original:** `Court Records/Davies v. Indyke/001.pdf`
*   **Converted:** `Court Records__Davies v. Indyke__001.txt`

## File Content Format
Each text file includes a metadata header injected during conversion to preserve context, followed by the document content.

```text
METADATA_SOURCE: Court Records\Davies v. Indyke, No. 119-cv-10788 (S.D.N.Y. 2019)
METADATA_FILENAME: 011.pdf
----------------------------------------
[Actual Document Text Starts Here...]
