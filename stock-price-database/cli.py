import argparse
import json
from typing import List

from config import DEFAULT_DB_PATH, DEFAULT_SOURCE
import db
from service import (
    fetch_and_store,
    query_range,
    update_all,
    list_symbols as svc_list_symbols,
    remove_symbol as svc_remove_symbol,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Stock price database CLI")
    parser.add_argument("--db-path", default=DEFAULT_DB_PATH, help="Path to SQLite DB file")
    parser.add_argument("--source", default=DEFAULT_SOURCE, help="Data source name (default: yahoo)")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("init-db", help="Initialize the database")

    fetch_p = sub.add_parser("fetch", help="Fetch prices for a symbol")
    fetch_p.add_argument("--symbol", required=True)
    fetch_p.add_argument("--start", required=True, help="YYYY-MM-DD")
    fetch_p.add_argument("--end", required=True, help="YYYY-MM-DD")
    fetch_p.add_argument("--force-refresh", action="store_true", help="Force overwrite existing data")

    query_p = sub.add_parser("query", help="Query prices from DB")
    query_p.add_argument("--symbol", required=True)
    query_p.add_argument("--start", required=True, help="YYYY-MM-DD")
    query_p.add_argument("--end", required=True, help="YYYY-MM-DD")
    query_p.add_argument("--format", choices=["table", "json"], default="table")

    update_p = sub.add_parser("update-all", help="Update multiple symbols from a list")
    group = update_p.add_mutually_exclusive_group(required=True)
    group.add_argument("--symbols-file", help="Path to newline-delimited symbols file")
    group.add_argument("--symbols", help="Comma-separated symbols list")
    update_p.add_argument("--start", required=True, help="YYYY-MM-DD")
    update_p.add_argument("--end", required=True, help="YYYY-MM-DD")
    update_p.add_argument("--force-refresh", action="store_true")
    update_p.add_argument("--sleep", type=float, default=0.0, help="Sleep seconds between symbols")
    update_p.add_argument("--stop-on-error", action="store_true")

    sub.add_parser("list-symbols", help="List all symbols stored in the DB")

    remove_p = sub.add_parser("remove-symbol", help="Delete all rows for a symbol")
    remove_p.add_argument("--symbol", required=True)

    return parser


def print_table(rows: List[dict]) -> None:
    if not rows:
        print("No rows found")
        return
    headers = rows[0].keys()
    widths = {h: max(len(str(h)), max(len(str(r.get(h, ""))) for r in rows)) for h in headers}
    line = " | ".join(f"{h:{widths[h]}}" for h in headers)
    print(line)
    print("-+-".join("-" * widths[h] for h in headers))
    for r in rows:
        print(" | ".join(f"{str(r.get(h, '')):{widths[h]}}" for h in headers))


def load_symbols(args) -> List[str]:
    if args.symbols_file:
        with open(args.symbols_file, "r", encoding="utf-8") as fh:
            return [line.strip() for line in fh if line.strip()]
    return [sym.strip() for sym in args.symbols.split(",") if sym.strip()]


def main(argv=None) -> None:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "init-db":
        conn = db.get_connection(args.db_path)
        db.init_db(conn)
        print(f"Initialized DB at {args.db_path}")
        return

    if args.command == "fetch":
        count = fetch_and_store(
            symbol=args.symbol,
            start=args.start,
            end=args.end,
            source_name=args.source,
            db_path=args.db_path,
            force_refresh=args.force_refresh,
        )
        print(f"Fetched and stored {count} rows for {args.symbol}")
        return

    if args.command == "query":
        rows = query_range(
            symbol=args.symbol,
            start=args.start,
            end=args.end,
            db_path=args.db_path,
        )
        if args.format == "json":
            print(json.dumps(rows, indent=2))
        else:
            print_table(rows)
        return

    if args.command == "update-all":
        symbols = load_symbols(args)
        results = update_all(
            symbols=symbols,
            start=args.start,
            end=args.end,
            source_name=args.source,
            db_path=args.db_path,
            force_refresh=args.force_refresh,
            sleep_seconds=args.sleep,
            stop_on_error=args.stop_on_error,
        )
        for sym, count in results["updated"]:
            print(f"{sym}: {count} rows")
        if results["errors"]:
            print("Errors:")
            for sym, err in results["errors"]:
                print(f"  {sym}: {err}")
        return

    if args.command == "list-symbols":
        symbols = svc_list_symbols(db_path=args.db_path)
        for sym in symbols:
            print(sym)
        return

    if args.command == "remove-symbol":
        deleted = svc_remove_symbol(symbol=args.symbol, db_path=args.db_path)
        print(f"Removed {deleted} rows for {args.symbol.upper()}")
        return


if __name__ == "__main__":
    main()
