from datetime import datetime, timezone

import service


class FakeSource:
    def __init__(self, rows=None):
        self.rows = rows or []

    def fetch(self, symbol, start, end):
        return [dict(row, symbol=symbol.upper()) for row in self.rows]


def test_fetch_and_store(monkeypatch, tmp_path):
    db_path = tmp_path / "svc.db"
    fake_rows = [
        {
            "date": "2023-12-01",
            "open": 1,
            "high": 2,
            "low": 0.5,
            "close": 1.5,
            "volume": 100,
            "source": "fake",
            "fetched_at": datetime.now(timezone.utc).isoformat(),
        }
    ]

    monkeypatch.setattr(service, "get_source", lambda name: FakeSource(fake_rows))

    inserted = service.fetch_and_store(
        symbol="AAPL",
        start="2023-12-01",
        end="2023-12-31",
        source_name="fake",
        db_path=str(db_path),
        force_refresh=False,
    )
    assert inserted == 1

    results = service.query_range(
        symbol="AAPL", start="2023-12-01", end="2023-12-31", db_path=str(db_path)
    )
    assert len(results) == 1
    assert results[0]["close"] == 1.5


def test_update_all(monkeypatch, tmp_path):
    db_path = tmp_path / "svc.db"
    fake_rows = [
        {
            "date": "2023-12-01",
            "open": 1,
            "high": 2,
            "low": 0.5,
            "close": 1.5,
            "volume": 100,
            "source": "fake",
            "fetched_at": datetime.now(timezone.utc).isoformat(),
        }
    ]

    monkeypatch.setattr(service, "get_source", lambda name: FakeSource(fake_rows))

    result = service.update_all(
        symbols=["AAPL", "MSFT"],
        start="2023-12-01",
        end="2023-12-31",
        source_name="fake",
        db_path=str(db_path),
    )
    assert len(result["updated"]) == 2
    assert result["errors"] == []


def test_list_symbols(monkeypatch, tmp_path):
    db_path = tmp_path / "svc.db"
    fake_rows = [
        {
            "date": "2023-12-01",
            "open": 1,
            "high": 2,
            "low": 0.5,
            "close": 1.5,
            "volume": 100,
            "source": "fake",
            "fetched_at": datetime.now(timezone.utc).isoformat(),
        }
    ]
    monkeypatch.setattr(service, "get_source", lambda name: FakeSource(fake_rows))
    service.fetch_and_store(
        symbol="AAPL",
        start="2023-12-01",
        end="2023-12-31",
        source_name="fake",
        db_path=str(db_path),
        force_refresh=False,
    )
    symbols = service.list_symbols(db_path=str(db_path))
    assert symbols == ["AAPL"]


def test_remove_symbol(monkeypatch, tmp_path):
    db_path = tmp_path / "svc.db"
    fake_rows = [
        {
            "date": "2023-12-01",
            "open": 1,
            "high": 2,
            "low": 0.5,
            "close": 1.5,
            "volume": 100,
            "source": "fake",
        }
    ]
    monkeypatch.setattr(service, "get_source", lambda name: FakeSource(fake_rows))
    service.fetch_and_store(
        symbol="AAPL",
        start="2023-12-01",
        end="2023-12-31",
        source_name="fake",
        db_path=str(db_path),
        force_refresh=False,
    )
    deleted = service.remove_symbol(symbol="AAPL", db_path=str(db_path))
    assert deleted == 1
    assert service.list_symbols(db_path=str(db_path)) == []
