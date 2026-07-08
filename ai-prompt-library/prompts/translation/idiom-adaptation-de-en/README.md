# Idiom Adaptation (German → English)

## The problem
Literal translation of idioms produces nonsense or unintentional comedy.
"Das ist nicht mein Bier" translated word-for-word is "That is not my
beer" — technically correct, meaningless in English. The intended meaning
is closer to "That's not my problem."

## What this prompt does differently
It explicitly tells the model to detect idiomatic language and substitute
a natural equivalent expression in the target language, rather than
translating word-for-word — and to do so silently, without breaking the
flow of the translation to explain itself.

## Example (illustrative — replace with your own run once you execute
`evaluate.py`)

**Input:**
> Das ist nicht mein Bier.

**Literal (bad) translation:**
> That is not my beer.

**Target-quality translation:**
> That's not my problem.

## Known failure modes
- Ambiguous idioms (ones with multiple possible English equivalents
  depending on tone) sometimes get a technically valid but tonally
  mismatched substitution. Worth cross-checking with the judge script's
  `tone_preservation` score.
- Idiom detection can fail silently on very obscure or regional German
  idioms the model may not recognize — no fallback/flagging mechanism yet.

## Test cases
See `evaluation/test_cases.json` — IDs `trans-de-en-01` and
`trans-de-en-02`.
