[![made-with-Python](https://img.shields.io/badge/Made%20with-Python-blue)](https://www.python.org/)
[![license](https://img.shields.io/badge/License-MIT-blue)](LICENSE)
[![issues](https://img.shields.io/github/issues/X-Projetion/split-files?color=blue)](https://github.com/X-Projetion/split-files/issues)


<p align="center">
    <img src="https://raw.githubusercontent.com/X-Projetion/split-files/main/split-files.png" alt="split files" width="60%">
</p>
<ul>
  <li><a href="#features">Features</a></li>
  <li><a href="#how-to-use">How to Use</a></li>
  <li><a href="#usage">Usage</a></li>
  <li><a href="#follow-the-prompts">Follow the Prompts</a></li>
  <li><a href="#installation-via-pypi">Installation via PyPI</a></li>
  <li><a href="#help">Help</a></li>
  <li><a href="#license">License</a></li>
</ul>

## File Splitter by Lines
This Python script provides a simple yet powerful way to split large text files into smaller files based on the specified number of lines per file. It is designed to facilitate easier management and processing of large datasets by breaking them down into manageable chunks.

### Features
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
