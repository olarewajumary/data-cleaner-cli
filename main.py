# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import argparse
import os
from src.cleaner import load_csv, inspect_data, clean_data, save_cleaned


def main():
    # Set up the CLI arguments
    parser = argparse.ArgumentParser(
        description="🧹 Data Cleaner CLI — Clean messy CSV files instantly"
    )

    parser.add_argument(
        "--input",
        type=str,
        required=True,
        help="Path to the input CSV file (e.g. data/messy.csv)"
    )

    parser.add_argument(
        "--output",
        type=str,
        default="output/cleaned.csv",
        help="Path to save the cleaned CSV (default: output/cleaned.csv)"
    )

    parser.add_argument(
        "--inspect",
        action="store_true",
        help="Show a full inspection report before cleaning"
    )

    args = parser.parse_args()

    # Make sure output folder exists
    os.makedirs(os.path.dirname(args.output), exist_ok=True)

    # Run the pipeline
    df = load_csv(args.input)

    if args.inspect:
        inspect_data(df)

    df_cleaned = clean_data(df)
    save_cleaned(df_cleaned, args.output)

    print("\n🎉 Done! Your data is clean and ready.\n")


if __name__ == "__main__":
    main()