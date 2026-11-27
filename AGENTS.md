# Mailroom

Mailroom is a newsletter tool.

## Rules

- Newsletter: Soft Technix, for the softtechnix team.
- Tests first: behavior is written as a test before the code.
- Never read today's date inside the logic.
- Emails never use emoji in the subject.
- Behaviors first: I give the expected answers, you write them as tests, show them failing, then write the code.
- The checks are now pytest tests in tests/, one test per behavior, each named for the behavior it checks. Run them with uv run pytest. There is no checks.py.
- Never edit data/subscribers.csv to try something out. Experiments use a copy outside the project.

## How I learn

I have read up to Step 13.8. Use only what I have read, and when something new appears, ask me to predict it before you explain it.
