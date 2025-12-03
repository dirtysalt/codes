from datetime import datetime, timezone
import os

import db


def test_init_and_upsert(tmp_path):
    db_path = tmp_path / "test.db"
    conn = db.get_connection(str(db_path))
    db.init_db(conn)

    rows = [
        {
            "symbol": "AAPL",
            "date": "2023-12-01",
            "open": 1.0,
            "high": 2.0,
            "low": 0.5,
            "close": 1.5,
            "volume": 10,
            "source": "test",
            "fetched_at": datetime.now(timezone.utc).isoformat(),
        }
    ]
    inserted = db.upsert_prices(conn, rows, replace=False)
    assert inserted == 1

    # Duplicate insert ignored when replace=False
    inserted = db.upsert_prices(conn, rows, replace=False)
    assert inserted == 0

    # Replace should count as 1
    rows[0]["close"] = 2.0
    inserted = db.upsert_prices(conn, rows, replace=True)
    assert inserted == 1

    queried = db.query_prices(conn, "AAPL", "2023-12-01", "2023-12-31")
    assert len(queried) == 1
    assert queried[0]["close"] == 2.0
    symbols = db.list_symbols(conn)
    assert symbols == ["AAPL"]


def test_query_empty(tmp_path):
    db_path = tmp_path / "empty.db"
    conn = db.get_connection(str(db_path))
    db.init_db(conn)
    result = db.query_prices(conn, "MSFT", "2020-01-01", "2020-01-02")
    assert result == []


def test_delete_symbol(tmp_path):
    db_path = tmp_path / "delete.db"
    conn = db.get_connection(str(db_path))
    db.init_db(conn)
    rows = [
        {
            "symbol": "AAPL",
            "date": "2023-12-01",
            "open": 1.0,
            "high": 2.0,
            "low": 0.5,
            "close": 1.5,
            "volume": 10,
            "source": "test",
        },
        {
            "symbol": "AAPL",
            "date": "2023-12-02",
            "open": 1.1,
            "high": 2.1,
            "low": 0.6,
            "close": 1.6,
            "volume": 11,
            "source": "test",
        },
    ]
    inserted = db.upsert_prices(conn, rows, replace=False)
    assert inserted == 2
    deleted = db.delete_symbol(conn, "aapl")
    assert deleted == 2
    assert db.list_symbols(conn) == []
    assert db.query_prices(conn, "AAPL", "2023-12-01", "2023-12-31") == []
