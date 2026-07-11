# AI Prompt Library

Professional prompt collection for localization, translation, and
multilingual AI workflows — with an evaluation layer, not just a list.

## Why this exists

Most "prompt library" repos are static lists of prompt text with no way
to tell whether the prompts actually work. This one is different: every
prompt is paired with test cases and scored automatically by an LLM judge
against a quality rubric (accuracy, fluency, tone preservation, idiom
handling). The goal is to demonstrate not just prompt writing, but prompt
*evaluation* — the part most collections skip.

## Repo structure

```
ai-prompt-library/
├── prompts/
│   ├── localization/
│   │   └── tone-preservation-en-es/
│   │       ├── prompt.txt      <- the actual prompt template
│   │       └── README.md       <- problem, rationale, known failure modes
│   └── translation/
│       └── idiom-adaptation-de-es/
│           ├── prompt.txt
│           └── README.md
└── evaluation/
    ├── test_cases.json         <- inputs used to test each prompt
    ├── evaluate.py              <- runs prompts + scores them via LLM judge
    └── sample_report.md         <- example output
```

## How it works

1. `evaluate.py` loads a prompt template and a test case's variables
2. It sends the rendered prompt to Claude and gets a translation
3. It sends that translation to Claude *again*, this time asking it to act
   as an independent judge and score the result against a fixed rubric
4. Results are saved as a JSON report you can review or turn into a
   summary table

This two-step generate-then-judge pattern is a standard technique for
evaluating LLM output at scale, since you rarely have hand-labeled
reference translations available for every input.

## Setup

You'll need Python 3.9+ and an Anthropic API key.

```bash
# 1. Clone the repo and move into it
git clone https://github.com/<your-username>/ai-prompt-library.git
cd ai-prompt-library

# 2. Create a virtual environment (keeps dependencies isolated)
python3 -m venv venv
source venv/bin/activate      # on Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your API key
cp .env.example .env
# then open .env and paste your key in

# 5. Run the evaluation
cd evaluation
python evaluate.py
```

To run just one test case instead of all of them:

```bash
python evaluate.py --id loc-en-es-01
```

## Adding a new prompt

1. Create a new folder under `prompts/<category>/<prompt-name>/`
2. Add `prompt.txt` with your template — use `<<variable_name>>` for
   anything that should be filled in dynamically
3. Add a `README.md` documenting the problem it solves, an example, and
   known failure modes (see existing prompts for the format)
4. Add one or more test cases to `evaluation/test_cases.json`
5. Run `python evaluate.py --id <your-new-test-id>` to see how it scores

## About this project

Built as part of a portfolio focused on language technology — the
intersection of translation/localization expertise and practical AI
tooling. Feedback and pull requests welcome.
