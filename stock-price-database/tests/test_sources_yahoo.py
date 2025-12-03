from sources.yahoo import YahooSource


def test_parse_csv_fixture():
    src = YahooSource()
    with open("tests/fixtures/yahoo_sample.csv", "r", encoding="utf-8") as fh:
        content = fh.read()
    rows = src._parse_csv(content, symbol="AAPL")
    assert len(rows) == 2
    assert rows[0]["symbol"] == "AAPL"
    assert rows[0]["date"] == "2023-12-01"
    assert rows[0]["close"] == 105.0
