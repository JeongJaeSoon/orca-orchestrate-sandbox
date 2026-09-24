# orca-orchestrate-sandbox

End-to-end sandbox for the `orchestrate` skill in [JeongJaeSoon/agent-skills](https://github.com/JeongJaeSoon/agent-skills): a tiny calculator, numbered migrations and role-named CI jobs (`lint`, `unit`) behind strict branch protection. Programs run here are throwaway.

## calc

- `calc.add(a, b)` — returns `a + b`, e.g. `calc.add(2, 3)` → `5`
- `calc.subtract(a, b)` — returns `a - b`, e.g. `calc.subtract(5, 3)` → `2`
- `calc.multiply(a, b)` — returns `a * b`, e.g. `calc.multiply(4, 3)` → `12`
- `calc.divide(a, b)` — returns `a / b`, e.g. `calc.divide(6, 3)` → `2.0`

## Development

Run both checks from the repository root before opening a PR:

```sh
python3 -m unittest discover -s tests
python3 -m tests.check_migrations
```
