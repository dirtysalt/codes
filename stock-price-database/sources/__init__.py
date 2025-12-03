from .yahoo import YahooSource
from .stooq import StooqSource


SOURCES = {
    "yahoo": YahooSource,
    "stooq": StooqSource,
}


def get_source(name: str):
    try:
        return SOURCES[name]()
    except KeyError as exc:
        raise ValueError(f"Unknown source: {name}") from exc
