# Data Cleaner CLI

A command-line tool that ingests messy CSV files and outputs a cleaned, 
analyzed version automatically, built with Python and Pandas.

---

## Features

- Detects and removes duplicate rows
- Fills missing numeric values with column median
- Fills missing text values with 'Unknown'
- Strips whitespace from string columns
- Standardizes column names (lowercase + underscores)
- Generates a full inspection report before cleaning
- Saves cleaned output as a new CSV file

---

## ️Tech Stack

- Python 3.x
- Pandas
- Argparse

---

## Project Structure

```
data-cleaner-cli/
├── main.py           # CLI entry point
├── src/
│   └── cleaner.py     # loading, inspecting, and cleaning logic
├── data/
│   └── messy.csv       # sample file to test with
└── requirements.txt
```

## Usage

```
python main.py --input data/messy.csv --inspect
```

- `--input` (required): path to the CSV you want cleaned
- `--output`: where to save the cleaned file (defaults to `output/cleaned.csv`)
- `--inspect`: prints a full report on missing values, duplicates, and data types before cleaning

## Example output

```
📊 DATA INSPECTION REPORT
🔹 Shape: 6 rows × 4 columns
🔹 Missing Values:
   ⚠️  Age: 1 missing
   ⚠️  Salary: 1 missing

🧹 Cleaning data...
   ✅ Duplicates removed: 1 rows dropped
   ✅ 'age': 1 missing values filled with median
   💾 Cleaned file saved to: output/cleaned.csv
```

## Running it yourself

```
git clone https://github.com/olarewajumary/data-cleaner-cli
cd data-cleaner-cli
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python main.py --input data/messy.csv --inspect
```