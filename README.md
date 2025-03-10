# my_theme_tool

A tool to find the most similar `theme.css` file using TF-IDF.

## Overview

`my_theme_tool` is a Python package that compares a master theme CSS file with candidate `theme.css` files found in various theme folders. It then identifies and returns the theme that is most similar to the master file.

## Project Structure

The repository is organized as follows:

my_theme_tool/ <-- Parent folder (repository root) ├── my_theme_tool/ <-- Python package directory │ ├── init.py │ └── main.py <-- Contains the main code and CLI entry point ├── README.md <-- This file ├── requirements.txt <-- Package dependencies └── setup.py <-- Package configuration and entry point definition


## Setup Instructions

### 1. Clone the Repository

Clone the repository to your local machine using Git:

```bash
git clone <repository-url>
cd my_theme_tool
```

### 2.  Create a Virtual Environment
It's recommended to use a virtual environment to manage dependencies. Create and activate one:

```bash
python3 -m venv venv
source venv/bin/activate
```
### 3. Install the Package in Editable Mode
With the virtual environment activated, install the package along with its dependencies. Installing in editable mode allows you to make changes that are immediately reflected:

```bash
pip install -e .
```

### 4. Usage
Once installed, you can run the command-line tool to compare a master theme with your themes folder. For example:

```bash
my_theme_tool path/to/master_theme.css path/to/themes
```
This command will output the path to the theme.css file that is most similar to the master theme, along with the similarity ratio.



