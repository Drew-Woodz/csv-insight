import pandas as pd

def analyze_csv(filepath, head=5, show_missing=False, describe=False):
    df = pd.read_csv(filepath)

    print(f"\n📊  Rows: {df.shape[0]} | Columns: {df.shape[1]}")
    print(f"\n🧱  Columns:\n{df.columns.tolist()}")

    print(f"\n🔍 Preview (Top {head} rows):")
    print(df.head(head))

    for col in df.columns:
        print(f"\n🧾  {col}:")
        print(f"  Type: {df[col].dtype}")
        print(f"  Unique: {df[col].nunique()}")
        print(f"  Nulls: {df[col].isnull().sum()}")

        if pd.api.types.is_numeric_dtype(df[col]):
            print(f"  Min: {df[col].min()}  Max: {df[col].max()}")
            print(f"  Mean: {df[col].mean():.2f}")
        elif df[col].nunique() < 10:
            print(f"  Top values: {df[col].value_counts().to_dict()}")


    if show_missing:
        print(f"\n⚠️  Missing Values:\n{df.isnull().sum()}")

    if describe:
        print(df.describe(include='all'))

