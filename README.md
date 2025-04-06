# Code Translator Project

A CLI tool for translating code between programming languages and analyzing code quality using Ollama's LLM llama3.2 locally.

## Features
- Translate code between programming languages
- Generate code analysis reports
- Supports both relative and absolute file paths
- Works with local Ollama models

## NOTE: Installation of ollama
- From ollama's official website donwload ollama onto your device 
  [ollama website](https://ollama.com/)
- After installation of ollama onto your device
- Run following command on your terminal:
```bash
    ollama run llama3.2 
```
- This shall install llama3.2 on your device if previosuly not installed and runs after that .you can also choose the model you prefer and correspondingly update that model in ollama_utils.py file


## Installation
```bash
git clone https://github.com/adarshpatelmulluru/code-translator-ai.git
cd code-translator-ai
pip install -r requirements.txt
```

## Usage
### Translation
```bash
python code_translator.cli_main --translate source-file destination-file
```

### Analysis
```bash
python code_translator.cli_main --analyze source-file
```
- For help use 
``` bash
python code_translator.cli_main -h
```

## Requirements
- Python 3.8+
- Ollama installed and running
- Llama3 or other suitable model pulled

## Project Structure
```
code_translator/
├── cli_main.py         # Main CLI interface
├── translate_anlyz.py  # Core translation logic
├── file_utils.py       # File operations
├── language_utils.py   # Language detection
├── ollama_utils.py     # Ollama interactions
├── prompt.py           # Prompt generation
└── __init__.py         # Package initialization
requiremennts.txt
readme.md
```

## Contributing
Pull requests welcome! For major changes, please open an issue first.

