# Sample Evaluation Report

> **Note:** This is an illustrative example showing the expected shape of
> output, written before running the script against a live API key. Replace
> this file with your own generated report once you run `evaluate.py` —
> that real output is more valuable on your CV than this placeholder.

| Test ID | Prompt | Accuracy | Fluency | Tone | Idiom Handling | Notes |
|---|---|---|---|---|---|---|
| loc-es-en-01 | tone-preservation-es-en | 5 | 5 | 4 | — | Casual greeting preserved well, slight loss of exclamatory energy |
| loc-es-en-02 | tone-preservation-es-en | 5 | 5 | 5 | — | Formal register correctly maintained |
| trans-de-en-01 | idiom-adaptation-de-en | 5 | 5 | 4 | 5 | Idiom correctly adapted to natural English equivalent |
| trans-de-en-02 | idiom-adaptation-de-en | 5 | 4 | 4 | 5 | Idiom adapted correctly, slightly stiff phrasing |

## How to regenerate this report with real data

```bash
python evaluate.py
```

This produces a timestamped JSON file in `evaluation/results/` with the
full translation output and judge reasoning for each test case. Once you
have a real run you're happy with, convert the key numbers into a table
like the one above and replace this file.
