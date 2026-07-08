# Tone Preservation (English → Spanish, Mexican-neutral)

## The problem
Generic translation prompts tend to "flatten" tone when moving from English
to Spanish — sarcasm, affection, and casual register often get smoothed
into overly correct, textbook-neutral Spanish that no native speaker
would actually use in conversation.

## Why English → Spanish, and why "Mexican-neutral"
Professional translators generally work into their native language, not
out of it — nuance and natural register are much harder to judge reliably
in a second language. As a native Spanish speaker (Mexican Spanish), I can
evaluate output quality with real authority in this direction. "Mexican-neutral"
means the translation should carry a recognizable Mexican flavor without
using expressions so regional that speakers from other Spanish-speaking
countries wouldn't understand them.

## Example

**Input (casual, sarcastic):**
> Oh great, another Monday. Just what I needed.

**Weak/generic translation:**
> Oh bien, otro lunes. Justo lo que necesitaba.

**Target-quality translation (what this prompt aims for):**
> Ay qué bien, otro lunes. Lo que me faltaba.

The weak version is grammatically correct but reads flat — it loses the
sarcastic bite. The target version keeps the sarcasm and sounds like
something a Mexican Spanish speaker would actually say out loud.

## Known failure modes
- Sarcasm is the hardest register to preserve consistently; the model
  sometimes translates it literally and the sarcastic intent disappears.
- Without the `context` field, short ambiguous inputs can go either
  overly formal or overly slangy — worth testing further.

## Test cases
See `evaluation/test_cases.json` — IDs `loc-en-es-01` and `loc-en-es-02`.