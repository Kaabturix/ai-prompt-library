"""
evaluate.py

Runs prompts from the prompts/ library against test cases, generates
translations using Claude, then uses Claude again as an independent judge
to score each output against a quality rubric.

This is the "evaluation layer" that turns a static prompt collection into
something you can actually claim demonstrates prompt quality.

Usage:
    python evaluate.py                     # run all test cases
    python evaluate.py --id loc-es-en-01   # run just one test case
"""

import argparse
import json
import os
from datetime import datetime
from pathlib import Path

from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
MODEL = "claude-sonnet-5"  # model used both to run prompts and to judge them

ROOT = Path(__file__).parent.parent
PROMPTS_DIR = ROOT / "prompts"
TEST_CASES_FILE = Path(__file__).parent / "test_cases.json"
RESULTS_DIR = Path(__file__).parent / "results"

JUDGE_RUBRIC = """You are a professional translation quality evaluator. You will be given:
1. The original source text
2. A translation produced by an AI system
3. Notes about what the translation prompt was designed to test

Score the translation on these four criteria, each from 1 (poor) to 5 (excellent):
- accuracy: does it preserve the original meaning?
- fluency: does it read naturally in the target language?
- tone_preservation: does it match the register/emotional tone of the source (formal vs informal, sarcastic vs sincere, etc.)?
- idiom_handling: if the source contains idioms or colloquial expressions, are they adapted naturally rather than translated literally? (score 5 if there was no idiom to handle and none was needed)

Respond ONLY with valid JSON in this exact format, no other text, no markdown code fences:
{{
  "accuracy": <1-5>,
  "fluency": <1-5>,
  "tone_preservation": <1-5>,
  "idiom_handling": <1-5>,
  "notes": "<one or two sentence explanation of the scores>"
}}

Source text: {source_text}
Test notes: {test_notes}
Translation to evaluate: {translation}
"""


def load_prompt_template(prompt_path: str) -> str:
    """Load the raw prompt template text, e.g. 'localization/tone-preservation-es-en'."""
    file_path = PROMPTS_DIR / prompt_path / "prompt.txt"
    if not file_path.exists():
        raise FileNotFoundError(f"No prompt.txt found at {file_path}")
    return file_path.read_text(encoding="utf-8")


def render_prompt(template: str, variables: dict) -> str:
    """Replace <<placeholder>> markers in the template with actual values."""
    rendered = template
    for key, value in variables.items():
        rendered = rendered.replace(f"<<{key}>>", value)
    return rendered


def call_claude(prompt: str) -> str:
    """Send a prompt to Claude and return the text response."""
    response = client.messages.create(
        model=MODEL,
        max_tokens=1000,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.content[0].text.strip()


def judge_translation(source_text: str, translation: str, test_notes: str) -> dict:
    """Ask Claude to score a translation against the rubric. Returns a dict of scores."""
    judge_prompt = JUDGE_RUBRIC.format(
        source_text=source_text, translation=translation, test_notes=test_notes
    )
    raw_response = call_claude(judge_prompt)
    try:
        return json.loads(raw_response)
    except json.JSONDecodeError:
        return {
            "accuracy": None,
            "fluency": None,
            "tone_preservation": None,
            "idiom_handling": None,
            "notes": f"Could not parse judge response: {raw_response}",
        }


def run_test_case(test_case: dict) -> dict:
    """Run a single test case end-to-end: generate a translation, then score it."""
    template = load_prompt_template(test_case["prompt"])
    rendered_prompt = render_prompt(template, test_case["variables"])
    translation = call_claude(rendered_prompt)
    scores = judge_translation(
        source_text=test_case["variables"]["source_text"],
        translation=translation,
        test_notes=test_case.get("notes", ""),
    )
    return {
        "id": test_case["id"],
        "prompt": test_case["prompt"],
        "source_text": test_case["variables"]["source_text"],
        "translation": translation,
        "scores": scores,
    }


def main():
    parser = argparse.ArgumentParser(description="Run and score prompt library test cases.")
    parser.add_argument("--id", help="Run only the test case with this id", default=None)
    args = parser.parse_args()

    test_cases = json.loads(TEST_CASES_FILE.read_text(encoding="utf-8"))
    if args.id:
        test_cases = [tc for tc in test_cases if tc["id"] == args.id]
        if not test_cases:
            print(f"No test case found with id '{args.id}'")
            return

    RESULTS_DIR.mkdir(exist_ok=True)
    results = []

    for tc in test_cases:
        print(f"Running test case: {tc['id']} ...")
        result = run_test_case(tc)
        results.append(result)
        print(f"  -> scores: {result['scores']}")

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    output_file = RESULTS_DIR / f"report-{timestamp}.json"
    output_file.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nSaved full report to {output_file}")


if __name__ == "__main__":
    main()
