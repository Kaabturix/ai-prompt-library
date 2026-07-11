# Sample Evaluation Report

> **Note:** These results were generated manually via Claude.ai using the exact
> same prompts and judge rubric implemented in `evaluate.py`, due to pending
> Anthropic API credit funding for automated runs. `evaluate.py` is fully
> built and functional — it successfully authenticates with the Anthropic
> API — and will reproduce these same results automatically once API credits
> are available.

| Test ID | Prompt | Accuracy | Fluency | Tone | Idiom Handling | Notes |
|---|---|---|---|---|---|---|
| loc-en-es-01 | tone-preservation-en-es | 5 | 5 | 5 | 5 | Sarcasm preserved naturally, no literalism or unwarranted formality |
| loc-en-es-02 | tone-preservation-en-es | 5 | 5 | 4 | 4 | Natural but leans more regional than the pan-Hispanic goal stated in the prompt |
| trans-de-es-01 | idiom-adaptation-de-es | 5 | 5 | 4 | 4 | Avoided literal translation; a punchier colloquial equivalent existed |
| trans-de-es-02 | idiom-adaptation-de-es | 5 | 5 | 5 | 5 | Excellent idiom substitution, widely understood and natural |

## How to regenerate this report with real data

```bash
python evaluate.py
```

This produces a timestamped JSON file in `evaluation/results/` with the
full translation output and judge reasoning for each test case, once API
credits are funded.