from datetime import datetime, timezone
from time import sleep
from typing import Iterable, List, Dict, Any, Optional

from config import DEFAULT_DB_PATH, DEFAULT_SOURCE
import db
from sources import get_source


def fetch_and_store(
    symbol: str,
    start: str,
    end: str,
    source_name: str = DEFAULT_SOURCE,
    db_path: str = DEFAULT_DB_PATH,
    force_refresh: bool = False,
) -> int:
    conn = db.get_connection(db_path)
    db.init_db(conn)
    source = get_source(source_name)
    rows = source.fetch(symbol, start, end)
    filtered = [r for r in rows if start <= r.get("date", "") <= end]
    for row in filtered:
        row.setdefault("source", source_name)
        row.setdefault("fetched_at", datetime.now(timezone.utc).isoformat())
    return db.upsert_prices(conn, filtered, replace=force_refresh)


def query_range(
    symbol: str,
    start: str,
    end: str,
    db_path: str = DEFAULT_DB_PATH,
) -> List[Dict[str, Any]]:
    conn = db.get_connection(db_path)
    db.init_db(conn)
    return db.query_prices(conn, symbol, start, end)


def list_symbols(db_path: str = DEFAULT_DB_PATH):
    conn = db.get_connection(db_path)
    db.init_db(conn)
    return db.list_symbols(conn)


def remove_symbol(symbol: str, db_path: str = DEFAULT_DB_PATH) -> int:
    conn = db.get_connection(db_path)
    db.init_db(conn)
    return db.delete_symbol(conn, symbol)


def update_all(
    symbols: Iterable[str],
    start: str,
    end: str,
    source_name: str = DEFAULT_SOURCE,
    db_path: str = DEFAULT_DB_PATH,
    force_refresh: bool = False,
    sleep_seconds: float = 0.0,
    stop_on_error: bool = False,
) -> Dict[str, Any]:
    results: Dict[str, Any] = {"updated": [], "errors": []}
    for symbol in symbols:
        try:
            count = fetch_and_store(
                symbol=symbol,
                start=start,
                end=end,
                source_name=source_name,
                db_path=db_path,
                force_refresh=force_refresh,
            )
            results["updated"].append((symbol, count))
        except Exception as exc:  # noqa: BLE001
            results["errors"].append((symbol, str(exc)))
            if stop_on_error:
                break
        if sleep_seconds:
            sleep(sleep_seconds)
    return results
