<h1 align="center">
  <img src="split-files.png" alt="split files" width="600px">
  <br>
</h1>
<p align="center">
  <a href="https://goreportcard.com/report/github.com/X-Projetion/split-files/"><img src="https://goreportcard.com/badge/github.com/X-Projetion/split-files"></a>
  <a href="https://github.com/X-Projetion/split-files/issues"><img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat"></a>
  <a href="https://github.com/X-Projetion/split-files/releases"><img src="https://img.shields.io/github/release/X-Projetion/split-files"></a>
  <br>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/made%20with-Python-pink.svg"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-pink.svg"></a>
  <a href="https://github.com/X-Projetion/split-files/issues"><img src="https://img.shields.io/github/issues/X-Projetion/split-files?color=pink"></a>
</p>

<p align="center">
  • <a href="#features">Features</a> •
  <a href="#how-to-use">How to Use</a> •
  <a href="#Usage">Usage</a> •
  <a href="#follow-the-prompts">Follow the Prompts</a> •
  <a href="#installation-via-pypi">Installation via PyPI</a> •
  <a href="#Help">Help</a>
  <a href="license">License</a>
</p>

## File Splitter by Lines
This Python script provides a simple yet powerful way to split large text files into smaller files based on the specified number of lines per file. It is designed to facilitate easier management and processing of large datasets by breaking them down into manageable chunks.

## Features
- **Command-line Interface:** Easily specify the input file and the number of lines per output file using command-line arguments (`-f/--files` and `-l/--lines`).
- **Clear Feedback:** Error messages are displayed in red for quick identification of issues, while success messages are shown in green upon successful file creation.
- **Cross-platform Compatibility:** Works seamlessly on Windows, Unix, and Linux systems.
- **Automatic Folder Creation:** Automatically creates a 'results' folder to store the split files if it doesn't already exist.
- **User-friendly Interface:** Includes an ASCII art banner for visual appeal and clear prompts for user interaction.

## How to Use
### Clone the Repository
```bash
git clone https://github.com/X-Projetion/split-files.git
cd split-files
```

## Usage
- python file_splitter.py -f input_file.txt -l 100
- Replace input_file.txt with your desired input file and 100 with the number of lines per output file.

## Follow the Prompts
- The script will create a 'results' folder (if not already present) and split the file accordingly.
- Follow on-screen instructions to exit or continue after completion.

## Installation via PyPI
### You can also install split-files via PyPI for easy access:
- pip install split-files

## Help
```bash
python3 main.py -h
   _____       ___ __  _______ __
  / ___/____  / (_) /_/ ____(_) /__  _____
  \__ \/ __ \/ / / __/ /_  / / / _ \/ ___/
 ___/ / /_/ / / / /_/ __/ / / /  __(__  )
/____/ .___/_/_/\__/_/   /_/_/\___/____/v1
    /_/        x-projetion.org

usage: main.py [-h] -f INPUT_FILE -l LINES_PER_FILE

File Splitter by Lines

optional arguments:
  -h, --help            show this help message and exit
  -f INPUT_FILE, --files INPUT_FILE
                        Input file name
  -l LINES_PER_FILE, --lines LINES_PER_FILE
                        Number of lines per file
```
## License
This project is licensed under the MIT License. See the <a href='https://raw.githubusercontent.com/X-Projetion/split-files/main/LICENSE'>LICENSE</a> file for details.
