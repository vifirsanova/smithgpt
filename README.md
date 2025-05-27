# Code Review Assistant SmithGPT

An LLM-based assistant that can review code and suggest improvements on your documentation and reports. Upload your files or type messages to get AI-powered feedback.

## Features

- Supports **40+ file extensions** including:
  - Code: `.py`, `.js`, `.java`, `.c`, `.cpp`, `.go`, `.rs`, `.php`, `.rb`, etc.
  - Web: `.html`, `.css`, `.scss`, `.json`, `.xml`, `.yaml`
  - Data: `.csv`, `.tsv`, `.ipynb` (Jupyter Notebooks)
  - Docs: `.pdf`, `.doc`, `.docx`, `.txt`, `.md`
  - Configs: `.ini`, `.conf`, `.toml`, `.env`

- Full in-memory processing (no files saved to disk)
- 16MB max file size limit

## Quick Start

1. Install requirements:
   ```bash
   chmod +x run.sh
   ./run.sh
   ```

2. Access the web interface at http://localhost:5000

3. Type messages in the chat interface, or upload files for code review and analysis
