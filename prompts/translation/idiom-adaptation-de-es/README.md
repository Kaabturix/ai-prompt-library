# Idiom Adaptation (German → Spanish)

## The problem
Literal translation of idioms produces nonsense. "Das ist nicht mein Bier"
translated word-for-word is "Eso no es mi cerveza" — grammatically fine,
meaningless in context. The intended meaning is closer to "Eso no es
mi problema."

## Why German → Spanish
As a native Spanish speaker with working knowledge of German, I can
evaluate whether an idiom adaptation actually lands naturally in Spanish,
rather than just checking whether the literal meaning survived.

## What this prompt does differently
It explicitly tells the model to detect idiomatic language and substitute
a natural Spanish equivalent, rather than translating word-for-word — and
to do so silently, without breaking the flow of the translation to explain
itself.

## Example

**Input:**
> Das ist nicht mein Bier.

**Literal (bad) translation:**
> Eso no es mi cerveza.

**Target-quality translation:**
> Eso no es mi problema.

## Known failure modes
- Ambiguous idioms with multiple possible Spanish equivalents (depending
  on tone or regional variant) sometimes get a technically valid but
  tonally mismatched substitution.
- Idiom detection can fail silently on obscure or regional German idioms
  the model may not recognize — no fallback/flagging mechanism yet.

## Test cases
See `evaluation/test_cases.json` — IDs `trans-de-es-01` and `trans-de-es-02`.