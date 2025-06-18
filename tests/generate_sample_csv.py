import pandas as pd
import random
import argparse

def generate_csv(path="sample.csv", rows=100):
    data = {
        "id": list(range(1, rows + 1)),
        "score": [random.randint(50, 100) for _ in range(rows)],
        "passed": [random.choice([True, False]) for _ in range(rows)],
        "notes": [random.choice(["good", "average", "needs improvement", None]) for _ in range(rows)]
    }

    df = pd.DataFrame(data)
    df.to_csv(path, index=False)
    print(f"✅ Generated {rows} rows in {path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--rows", type=int, default=100, help="Number of rows to generate")
    parser.add_argument("--path", type=str, default="sample.csv", help="Output CSV path")
    args = parser.parse_args()

    generate_csv(path=args.path, rows=args.rows)
