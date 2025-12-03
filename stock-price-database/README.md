# Stock Price Database

Scrape historical stock prices, store them in SQLite, and query them offline.

## Setup
```
pip install -r requirements.txt
```

## Commands
```
python cli.py init-db [--db-path stock_prices.db]
python cli.py fetch --symbol AAPL --start 2023-01-01 --end 2023-12-31
python cli.py query --symbol AAPL --start 2023-01-01 --end 2023-12-31 [--format table|json]
python cli.py update-all --symbols-file symbols.txt --start 2023-01-01 --end 2023-12-31
python cli.py list-symbols
python cli.py remove-symbol --symbol AAPL
```

Options:
- `--db-path`: path to SQLite file (defaults to env `STOCK_DB_PATH` or `stock_prices.db`).
- `--source`: data source name (default `stooq`, also supports `yahoo`).
- `--force-refresh`: overwrite existing rows.
- `--sleep`: seconds to pause between symbols in `update-all`.
- `--stop-on-error`: stop batch on first error.

## Tests
```
pytest
```

## Web App (offline viewer)
```
python webapp.py
# open http://localhost:19000
```
Pick symbols and a date range; the chart is rendered client-side from the local SQLite data (no external calls).
Use the “Normalize to first price” toggle to index each series to 100 at its first available price in the range (lets you compare relative growth).
## Notes
- Default data source uses Yahoo Finance CSV download endpoint.
- Schema: `prices(symbol, date, open, high, low, close, volume, source, fetched_at)` with PK `(symbol, date, source)`.
