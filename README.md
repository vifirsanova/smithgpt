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
- Bug reports are provided in the user interface

![bug report example](https://github.com/user-attachments/assets/43eb12ca-2e64-4218-a24a-fef376365ffe)
*Bug report example*

**Limitations**: the model works best with documents containing < 100 lines.

## Quick Start

1. Install requirements:
   ```bash
   chmod +x run.sh
   ./run.sh
   ```
2. Access the web interface at http://localhost:5000
3. Type your code in the chat interface, or upload files for code review and analysis

## Examples

Graphical user interface supports both file uploading and input text message analysis. No additional prompts needed! 

![graphical user interface](https://github.com/user-attachments/assets/b07939bf-650d-4e92-9078-2851fa022176)

![graphical user interface](https://github.com/user-attachments/assets/4dce4f6a-7145-40c3-bd9d-b821d13aeada)

## Requirements  

The app works best with NVIDIA GPU. The app was tested on GeForce RTX 4070.

## Perspectives 

- AMD GPU integration
- New features: API integration for documentation analysis
- Chat history
- Multimodality
