import csv
import io
from datetime import datetime, date, timedelta
from typing import List, Dict, Any

import requests

from config import REQUEST_TIMEOUT, USER_AGENT


class YahooSource:
    base_url = "https://query1.finance.yahoo.com/v7/finance/download/{symbol}"

    def fetch(self, symbol: str, start: str, end: str) -> List[Dict[str, Any]]:
        start_dt = self._parse_date(start)
        end_dt = self._parse_date(end)
        period1 = int(datetime.combine(start_dt, datetime.min.time()).timestamp())
        period2 = int(
            datetime.combine(end_dt + timedelta(days=1), datetime.min.time()).timestamp()
        )
        url = self.base_url.format(symbol=symbol.upper())
        session, crumb = self._init_session()
        params = {
            "period1": str(period1),
            "period2": str(period2),
            "interval": "1d",
            "events": "history",
            "includeAdjustedClose": "true",
            "crumb": crumb,
        }
        resp = session.get(url, params=params, timeout=REQUEST_TIMEOUT)
        resp.raise_for_status()
        return self._parse_csv(resp.text, symbol)

    def _parse_csv(self, content: str, symbol: str) -> List[Dict[str, Any]]:
        reader = csv.DictReader(io.StringIO(content))
        rows: List[Dict[str, Any]] = []
        for raw in reader:
            if not raw or not raw.get("Date"):
                continue
            if raw.get("Close") in ("null", None):
                continue
            try:
                dt = self._parse_date(raw["Date"])
            except ValueError:
                continue
            try:
                rows.append(
                    {
                        "symbol": symbol.upper(),
                        "date": dt.isoformat(),
                        "open": float(raw["Open"]) if raw.get("Open") not in ("null", None) else None,
                        "high": float(raw["High"]) if raw.get("High") not in ("null", None) else None,
                        "low": float(raw["Low"]) if raw.get("Low") not in ("null", None) else None,
                        "close": float(raw["Close"]) if raw.get("Close") not in ("null", None) else None,
                        "volume": int(float(raw["Volume"])) if raw.get("Volume") not in ("null", None) else None,
                        "source": "yahoo",
                    }
                )
            except ValueError:
                continue
        return rows

    @staticmethod
    def _parse_date(value: str) -> date:
        return date.fromisoformat(value)

    def _init_session(self):
        session = requests.Session()
        session.headers.update({"User-Agent": USER_AGENT})
        crumb_resp = session.get(
            "https://query1.finance.yahoo.com/v1/test/getcrumb",
            timeout=REQUEST_TIMEOUT,
        )
        crumb_resp.raise_for_status()
        crumb = crumb_resp.text.strip()
        return session, crumb
