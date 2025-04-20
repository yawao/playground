 # data_cleaner
 
 A simple Python package to ingest CSV data, clean/filter rows, compute summary statistics, and export cleaned data to JSON.
 
 Features
 --------
 - Read CSV data file into Python objects
 - Drop rows with missing values
 - Compute basic summary statistics (count, mean, min, max) for numeric columns
 - Export cleaned data as JSON
 - CLI `data_cleaner` for command-line usage
 - Unit tests with `pytest`
 
 Installation
 ------------
 
 1. Clone the repository:
    ```bash
    git clone <repo-url>
    cd data_cleaner
    ```
 
 2. (Optional) Set up a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
 
 3. Install the package:
    ```bash
    pip install -e .
    ```
 
 Usage
 -----
 
 **From Python**
 ```python
 from data_cleaner.ingest import read_csv
 from data_cleaner.clean import drop_missing
 from data_cleaner.stats import compute_stats
 from data_cleaner.export import export_to_json

 data = read_csv("data/sample.csv")
 cleaned = drop_missing(data)
 stats = compute_stats(cleaned)
 print(stats)
 export_to_json(cleaned, "data/cleaned_data.json")
 ```
 
 **CLI**
 ```bash
 data_cleaner data/sample.csv data/cleaned_data.json
 ```
 
 If `data/cleaned_data.json` is omitted, defaults to `cleaned_data.json` in the current directory.
 
 Running Tests
 -------------
 ```bash
 pytest
 ```