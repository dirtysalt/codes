import json

import cli


class FakeSource:
    def fetch(self, symbol, start, end):
        return [
            {
                "symbol": symbol.upper(),
                "date": start,
                "open": 1,
                "high": 2,
                "low": 0.5,
                "close": 1.5,
                "volume": 10,
                "source": "fake",
            }
        ]


def run_cli(monkeypatch, argv, tmp_path):
    # monkeypatch source resolver
    import service

    monkeypatch.setattr(service, "get_source", lambda name: FakeSource())
    argv = ["--db-path", str(tmp_path / "cli.db"), "--source", "fake"] + argv
    cli.main(argv)


def test_cli_fetch_and_query(monkeypatch, tmp_path, capsys):
    run_cli(
        monkeypatch,
        ["fetch", "--symbol", "AAPL", "--start", "2023-12-01", "--end", "2023-12-31"],
        tmp_path,
    )
    capsys.readouterr()  # clear fetch output
    cli.main(
        [
            "--db-path",
            str(tmp_path / "cli.db"),
            "--source",
            "fake",
            "query",
            "--symbol",
            "AAPL",
            "--start",
            "2023-12-01",
            "--end",
            "2023-12-31",
            "--format",
            "json",
        ]
    )
    captured = capsys.readouterr()
    data = json.loads(captured.out)
    assert len(data) == 1
    assert data[0]["close"] == 1.5


def test_update_all(monkeypatch, tmp_path, capsys):
    symbols_file = tmp_path / "symbols.txt"
    symbols_file.write_text("AAPL\nMSFT\n", encoding="utf-8")
    run_cli(
        monkeypatch,
        [
            "update-all",
            "--symbols-file",
            str(symbols_file),
            "--start",
            "2023-12-01",
            "--end",
            "2023-12-31",
        ],
        tmp_path,
    )
    captured = capsys.readouterr()
    assert "AAPL" in captured.out
    assert "MSFT" in captured.out


def test_list_symbols(monkeypatch, tmp_path, capsys):
    run_cli(
        monkeypatch,
        [
            "fetch",
            "--symbol",
            "AAPL",
            "--start",
            "2023-12-01",
            "--end",
            "2023-12-31",
        ],
        tmp_path,
    )
    capsys.readouterr()
    cli.main(
        [
            "--db-path",
            str(tmp_path / "cli.db"),
            "--source",
            "fake",
            "list-symbols",
        ]
    )
    captured = capsys.readouterr()
    assert "AAPL" in captured.out.splitlines()


def test_remove_symbol(monkeypatch, tmp_path, capsys):
    run_cli(
        monkeypatch,
        [
            "fetch",
            "--symbol",
            "AAPL",
            "--start",
            "2023-12-01",
            "--end",
            "2023-12-31",
        ],
        tmp_path,
    )
    capsys.readouterr()
    cli.main(
        [
            "--db-path",
            str(tmp_path / "cli.db"),
            "--source",
            "fake",
            "remove-symbol",
            "--symbol",
            "AAPL",
        ]
    )
    removed_output = capsys.readouterr().out
    assert "Removed 1 rows" in removed_output
    cli.main(
        [
            "--db-path",
            str(tmp_path / "cli.db"),
            "--source",
            "fake",
            "list-symbols",
        ]
    )
    captured = capsys.readouterr()
    assert captured.out.strip() == ""
