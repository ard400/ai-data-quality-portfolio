# Dataset Quality Audit

A lightweight Python data-quality audit for CSV files.

## Checks
- Missing values by column
- Exact duplicate rows
- Numeric conversion failures
- Simple IQR-based outlier flags

## Run
```bash
python src/audit.py data/sample_dataset.csv
```

The sample dataset is synthetic and intentionally contains quality issues for demonstration.
