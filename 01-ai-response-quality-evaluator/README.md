# AI Response Quality Evaluator

A small rubric-based evaluation tool for comparing two AI-generated answers.

## What it demonstrates
- Clear evaluation criteria
- Weighted scoring
- Identification of critical errors
- Reproducible QA decisions
- Human-readable reporting

## Rubric
Each response is scored from 0–5 on correctness, relevance, completeness, clarity, and safety. Correctness and safety receive higher weights.

## Run
```bash
python src/evaluator.py data/sample_cases.json
```

## Test
```bash
python -m unittest discover -s tests
```

The included cases are synthetic demonstrations.
