# Sample Evaluation Report

> **Note:** The evaluation script (`evaluate.py`) is fully built and functional —
> it successfully authenticates with the Anthropic API. Live evaluation runs are
> pending API credit funding. The table below shows the *expected* output format
> based on the scoring rubric; it will be replaced with real generated results
> once the script is run end-to-end.

| Test ID | Prompt | Accuracy | Fluency | Tone | Idiom Handling | Notes |
|---|---|---|---|---|---|---|
| loc-es-en-01 | tone-preservation-es-en | — | — | — | — | Pending live run |
| loc-es-en-02 | tone-preservation-es-en | — | — | — | — | Pending live run |
| trans-de-en-01 | idiom-adaptation-de-en | — | — | — | — | Pending live run |
| trans-de-en-02 | idiom-adaptation-de-en | — | — | — | — | Pending live run |

## How to regenerate this report with real data

```bash
python evaluate.py
```

This produces a timestamped JSON file in `evaluation/results/` with the
full translation output and judge reasoning for each test case.