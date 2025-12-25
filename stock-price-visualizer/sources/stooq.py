import csv
import io
from datetime import date
from typing import List, Dict, Any

import requests

from config import REQUEST_TIMEOUT, USER_AGENT


class StooqSource:
    base_url = "https://stooq.pl/q/d/l/"

    def fetch(self, symbol: str, start: str, end: str) -> List[Dict[str, Any]]:
        cleaned = symbol.lower().replace(".", "-")
        params = {"s": f"{cleaned}.us", "i": "d"}
        resp = requests.get(self.base_url, params=params, headers={"User-Agent": USER_AGENT}, timeout=REQUEST_TIMEOUT)
        resp.raise_for_status()
        rows = self._parse_csv(resp.text, symbol)
        return [r for r in rows if start <= r.get("date", "") <= end]

    def _parse_csv(self, content: str, symbol: str) -> List[Dict[str, Any]]:
        reader = csv.DictReader(io.StringIO(content))
        rows: List[Dict[str, Any]] = []
        for raw in reader:
            if not raw or not raw.get("Data"):
                continue
            try:
                dt = self._parse_date(raw["Data"])
            except ValueError:
                continue
            rows.append(
                {
                    "symbol": symbol.upper(),
                    "date": dt.isoformat(),
                    "open": float(raw["Otwarcie"]) if raw.get("Otwarcie") else None,
                    "high": float(raw["Najwyzszy"]) if raw.get("Najwyzszy") else None,
                    "low": float(raw["Najnizszy"]) if raw.get("Najnizszy") else None,
                    "close": float(raw["Zamkniecie"]) if raw.get("Zamkniecie") else None,
                    "volume": int(float(raw["Wolumen"])) if raw.get("Wolumen") else None,
                    "source": "stooq",
                }
            )
        return rows

    @staticmethod
    def _parse_date(value: str) -> date:
        return date.fromisoformat(value)
