import sqlite3
from datetime import datetime, timezone
from typing import Iterable, List, Dict, Any

from config import DEFAULT_DB_PATH


def get_connection(db_path: str = DEFAULT_DB_PATH) -> sqlite3.Connection:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


def init_db(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS prices (
            symbol TEXT NOT NULL,
            date TEXT NOT NULL,
            open REAL,
            high REAL,
            low REAL,
            close REAL,
            volume INTEGER,
            source TEXT NOT NULL,
            fetched_at TEXT NOT NULL,
            PRIMARY KEY(symbol, date, source)
        )
        """
    )
    conn.execute(
        """
        CREATE INDEX IF NOT EXISTS idx_prices_symbol_date
        ON prices(symbol, date)
        """
    )
    conn.commit()


def upsert_prices(
    conn: sqlite3.Connection, rows: Iterable[Dict[str, Any]], replace: bool = False
) -> int:
    if not rows:
        return 0
    conflict = "OR REPLACE" if replace else "OR IGNORE"
    query = (
        f"INSERT {conflict} INTO prices"
        " (symbol, date, open, high, low, close, volume, source, fetched_at)"
        " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
    )
    now = datetime.now(timezone.utc).isoformat()
    data = []
    for row in rows:
        data.append(
            (
                row["symbol"],
                row["date"],
                row.get("open"),
                row.get("high"),
                row.get("low"),
                row.get("close"),
                row.get("volume"),
                row.get("source"),
                row.get("fetched_at", now),
            )
        )
    cur = conn.executemany(query, data)
    conn.commit()
    return cur.rowcount if cur.rowcount is not None else 0


def query_prices(
    conn: sqlite3.Connection, symbol: str, start: str, end: str
) -> List[Dict[str, Any]]:
    cur = conn.execute(
        """
        SELECT symbol, date, open, high, low, close, volume, source, fetched_at
        FROM prices
        WHERE symbol = ? AND date BETWEEN ? AND ?
        ORDER BY date
        """,
        (symbol.upper(), start, end),
    )
    return [dict(row) for row in cur.fetchall()]


def list_symbols(conn: sqlite3.Connection) -> List[str]:
    cur = conn.execute("SELECT DISTINCT symbol FROM prices ORDER BY symbol")
    return [row[0] for row in cur.fetchall()]


def delete_symbol(conn: sqlite3.Connection, symbol: str) -> int:
    """Remove all rows for a symbol; returns number of rows deleted."""
    cur = conn.execute("DELETE FROM prices WHERE symbol = ?", (symbol.upper(),))
    conn.commit()
    return cur.rowcount if cur.rowcount is not None else 0
