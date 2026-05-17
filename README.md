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