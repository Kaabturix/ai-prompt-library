# Tone Preservation (Spanish → English)

## The problem
General-purpose translation prompts tend to "flatten" register — casual,
slangy Spanish often gets translated into neutral or even slightly formal
English, and emotional markers (sarcasm, affection, urgency) get smoothed
out. This is a common, subtle failure mode that generic prompts don't guard
against.

## What this prompt does differently
It explicitly instructs the model to preserve register and emotional tone
as first-class goals, not just "translate accurately." This matters because
a technically accurate translation can still fail a translator's actual job:
sounding like the same person said it in a different language.

## Example (illustrative — replace with your own run once you execute
`evaluate.py`)

**Input (informal, Mexican Spanish):**
> Oye, ¿qué onda? Hace siglos que no nos vemos, ¡qué milagro!

**Weak/generic translation:**
> Hello, how are you? It has been a long time since we last saw each other.

**Target-quality translation (what this prompt aims for):**
> Hey, what's up? It's been ages since we last saw each other, what a
> surprise!

## Known failure modes
- On very short inputs with no context, the model sometimes can't tell
  formal from informal register and defaults to neutral. The `context`
  field helps but doesn't fully solve this — worth testing further.
- Regional slang (e.g. Mexican vs. Argentine vs. Spanish Spanish) is not
  explicitly handled yet. A future version could add a `region` variable.

## Test cases
See `evaluation/test_cases.json` — IDs `loc-es-en-01` and `loc-es-en-02`.
