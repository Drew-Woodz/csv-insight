import pandas as pd

def analyze_csv(filepath, head=5, show_missing=False):
    df = pd.read_csv(filepath)

    print(f"\n📊 Rows: {df.shape[0]} | Columns: {df.shape[1]}")
    print(f"\n🧱 Columns:\n{df.columns.tolist()}")

    print(f"\n🔍 Preview (Top {head} rows):")
    print(df.head(head))

    if show_missing:
        print(f"\n⚠️ Missing Values:\n{df.isnull().sum()}")
