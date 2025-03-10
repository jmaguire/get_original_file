# My Theme Tool

My Theme Tool is a command-line utility that compares a master CSS file with a collection of theme CSS files and determines which theme is most similar to the master theme using TF-IDF vectorization and cosine similarity.

## Features

- **Fast Comparison:** Uses scikit-learn’s TF-IDF vectorizer and cosine similarity for efficient comparison of large CSS files.
- **Command-Line Interface:** Easily run comparisons directly from the terminal.
- **Shareable Package:** Packaged for quick installation and distribution via pip.

## Installation

### Using pip (if published on PyPI)

1. **Create and Activate a Virtual Environment (Optional but Recommended):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
