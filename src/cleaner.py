import pandas as pd
import os


def load_csv(filepath):
    """Load a CSV file into a DataFrame."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")

    df = pd.read_csv(filepath)
    print(f"\n✅ File loaded: {filepath}")
    print(f"   Shape: {df.shape[0]} rows × {df.shape[1]} columns")
    return df


def inspect_data(df):
    """Print a full inspection report of the DataFrame."""
    print("\n" + "=" * 50)
    print("📊 DATA INSPECTION REPORT")
    print("=" * 50)

    print(f"\n🔹 Shape: {df.shape[0]} rows × {df.shape[1]} columns")

    print(f"\n🔹 Column Names:\n   {list(df.columns)}")

    print(f"\n🔹 Data Types:")
    for col, dtype in df.dtypes.items():
        print(f"   {col}: {dtype}")

    print(f"\n🔹 Missing Values:")
    missing = df.isnull().sum()
    for col, count in missing.items():
        status = "⚠️ " if count > 0 else "✅"
        print(f"   {status} {col}: {count} missing")

    print(f"\n🔹 Duplicate Rows: {df.duplicated().sum()}")
    print("=" * 50)


def clean_data(df):
    """Clean the DataFrame — remove duplicates, fix nulls, strip whitespace."""
    print("\n🧹 Cleaning data...")

    # Track original shape
    original_shape = df.shape

    # Remove duplicate rows
    df = df.drop_duplicates()
    print(f"   ✅ Duplicates removed: {original_shape[0] - df.shape[0]} rows dropped")

    # Strip whitespace from string columns
    str_cols = df.select_dtypes(include="object").columns.tolist()
    df[str_cols] = df[str_cols].apply(lambda col: col.str.strip())
    print(f"   ✅ Whitespace stripped from: {str_cols}")

    # Standardize column names (lowercase + underscores)
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    print(f"   ✅ Column names standardized")

    # Re-fetch column lists after renaming
    num_cols = df.select_dtypes(include="number").columns.tolist()
    str_cols = df.select_dtypes(include="object").columns.tolist()

    # Fill missing numeric values with column median
    for col in num_cols:
        missing = df[col].isnull().sum()
        if missing > 0:
            df[col] = df[col].fillna(df[col].median())
            print(f"   ✅ '{col}': {missing} missing values filled with median")

    # Fill missing text values with 'Unknown'
    for col in str_cols:
        missing = df[col].isnull().sum()
        if missing > 0:
            df[col] = df[col].fillna("Unknown")
            print(f"   ✅ '{col}': {missing} missing values filled with 'Unknown'")

    print(f"\n   📐 Final Shape: {df.shape[0]} rows × {df.shape[1]} columns")
    return df


def save_cleaned(df, output_path):
    """Save the cleaned DataFrame to a CSV file."""
    df.to_csv(output_path, index=False)
    print(f"\n💾 Cleaned file saved to: {output_path}")