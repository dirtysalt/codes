import os

DEFAULT_DB_PATH = os.environ.get("STOCK_DB_PATH", "stock_prices.db")
DEFAULT_SOURCE = os.environ.get("STOCK_SOURCE", "stooq")
REQUEST_TIMEOUT = int(os.environ.get("STOCK_REQUEST_TIMEOUT", "15"))
USER_AGENT = os.environ.get(
    "STOCK_USER_AGENT",
    "stock-price-db/0.1 (+https://example.com)",
)
