# csv-insight

**csv-insight** is a lightweight Python CLI tool for quickly inspecting CSV files. Get instant stats like row/column counts, missing data, column types, unique values, and more — straight from your terminal.

---

## 📦 Features (Current)
- ✅ Print row and column counts
- ✅ Show column names
- ✅ Preview top N rows (`--head`)
- ✅ Display missing value counts (`--missing`)
- ✅ Per-column summaries:
  - Data type
  - Unique value count
  - Min/Max/Mean (for numerics)
  - Top values (for categoricals)
- ✅ Full `.describe()` output (`--describe`)

---

## 📂 Project Structure

```bash

csv-insight/
├── cli.py               # Main CLI entry point
├── core/
│   ├── __init__.py
│   ├── analyzer.py      # Core CSV analysis functions
│   └── utils.py         # Helper functions
├── tests/
│   └── test_analyzer.py
├── requirements.txt
├── README.md
└── setup.py

```

---

## 🚀 Usage

```bash

# Basic usage
python cli.py sample.csv

# Show more rows in preview
python cli.py sample.csv --head 10

# Include missing value stats
python cli.py sample.csv --missing

# Include pandas-style describe table
python cli.py sample.csv --describe

```

---

## 🔧 Requirements

- Python 3.7+

- pandas

- click

**Install dependencies:**

```bash

pip install -r requirements.txt

```

---

## 🛠️ To Do / Upcoming Features

Planned features include:

- `--column <name>` to inspect a single column in detail
- Export output to JSON or Markdown
- Highlight columns with >50% missing
- Detect duplicates
- GUI / Gradio extension (maybe)

Want to help? Open an issue or PR!

---

## 📄 License

MIT

---


