# Repository Guidelines

## Project Structure & Modules
- `cli.py`: user-facing CLI for init, fetch, query, batch update, list/remove symbols.
- `service.py`: orchestration layer; resolves sources, calls DB helpers, batches symbols.
- `db.py`: SQLite helpers (connection, schema, upsert/query/delete, indexing).
- `sources/`: pluggable data providers (`stooq.py`, `yahoo.py`, `get_source` factory).
- `webapp.py` + `static/`: lightweight offline viewer (Flask API + static HTML/JS).
- `tests/`: pytest suites and fixtures (`tests/fixtures/yahoo_sample.csv`).
- Config/data: `config.py`, `symbols.txt`, `stock_prices.db` (default local DB).

## Build, Test, and Dev Commands
- Install deps: `pip install -r requirements.txt`.
- Create DB schema: `python cli.py init-db`.
- Fetch sample data: `python cli.py fetch --symbol AAPL --start 2023-01-01 --end 2023-12-31`.
- Batch refresh: `python cli.py update-all --symbols-file symbols.txt --start ... --end ... [--sleep 0.5]`.
- Query as table/json: `python cli.py query --symbol AAPL --start ... --end ... --format json`.
- Run tests: `pytest`.
- Launch viewer: `python webapp.py` then open `http://localhost:19000`.

## Coding Style & Naming
- Python 3; follow PEP 8, 4-space indents, snake_case for functions/vars, UPPER_SNAKE for constants.
- Use type hints (see `cli.py`, `db.py`), keep functions small and testable.
- Prefer pure helpers in `service.py`; keep HTTP logic inside `sources/*`.
- Log/print only in CLI or Flask routes; leave library functions quiet.

## Testing Guidelines
- Framework: pytest; fixtures live in `tests/fixtures/`.
- Name tests `test_*.py` and functions `test_*`; use `tmp_path` + monkeypatch for isolation.
- Add targeted unit tests for new branches (error paths, date filtering, symbol casing).
- Run `pytest` before commits; aim to cover new code paths rather than global % goals.

## Commit & Pull Request Guidance
- Commits: short, imperative summaries (e.g., “add yahoo retry handling”); group related changes.
- Before pushing: run `pytest` and relevant CLI smoke checks noted above.
- PRs should include: purpose/impact, test results, any schema changes, and screenshots/GIFs for web UI tweaks; link to issue/ticket if available.

## Security & Configuration Tips
- Env vars: `STOCK_DB_PATH`, `STOCK_SOURCE` (default `stooq`), `STOCK_REQUEST_TIMEOUT`, `STOCK_USER_AGENT`.
- SQLite file is local; do not commit real `stock_prices.db` with private data.
- Network calls are read-only; respect provider rate limits (`--sleep` for batches).
