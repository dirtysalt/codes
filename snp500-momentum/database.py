#!/usr/bin/env python3
"""
SQLite database module for caching S&P 500 stock data.

Caches:
- S&P 500 ticker list
- Historical price data and market caps
"""

import sqlite3
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Dict, Optional
import pandas as pd
import json


class StockDataCache:
    """SQLite-based cache for stock data."""

    def __init__(self, db_path: str = ".cache/stock_data.db"):
        """
        Initialize the database connection.

        Args:
            db_path: Path to the SQLite database file
        """
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(exist_ok=True)
        self.conn = None
        self._init_database()

    def _init_database(self):
        """Create database tables if they don't exist."""
        self.conn = sqlite3.connect(str(self.db_path))
        cursor = self.conn.cursor()

        # Table for S&P 500 ticker list
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS sp500_tickers (
                ticker TEXT PRIMARY KEY,
                updated_at TIMESTAMP NOT NULL
            )
        """)

        # Table for metadata (last update time, etc.)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS cache_metadata (
                key TEXT PRIMARY KEY,
                value TEXT NOT NULL,
                updated_at TIMESTAMP NOT NULL
            )
        """)

        # Table for historical price data
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS price_data (
                ticker TEXT NOT NULL,
                date DATE NOT NULL,
                close REAL NOT NULL,
                volume REAL,
                market_cap REAL,
                shares_outstanding REAL,
                updated_at TIMESTAMP NOT NULL,
                PRIMARY KEY (ticker, date)
            )
        """)

        # Create indexes for faster queries
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_price_data_ticker
            ON price_data(ticker)
        """)

        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_price_data_date
            ON price_data(date)
        """)

        self.conn.commit()

    def get_sp500_tickers(self, max_age_days: int = 30) -> Optional[List[str]]:
        """
        Retrieve S&P 500 ticker list from cache.

        Args:
            max_age_days: Maximum age of cached data in days

        Returns:
            List of ticker symbols or None if cache is stale/empty
        """
        cursor = self.conn.cursor()

        # Check when the ticker list was last updated
        cursor.execute("""
            SELECT value, updated_at FROM cache_metadata
            WHERE key = 'sp500_last_update'
        """)
        result = cursor.fetchone()

        if result:
            last_update = datetime.fromisoformat(result[1])
            age_days = (datetime.now() - last_update).days

            if age_days < max_age_days:
                # Cache is fresh, retrieve tickers
                cursor.execute("SELECT ticker FROM sp500_tickers ORDER BY ticker")
                tickers = [row[0] for row in cursor.fetchall()]
                if tickers:
                    return tickers

        return None

    def save_sp500_tickers(self, tickers: List[str]):
        """
        Save S&P 500 ticker list to cache.

        Args:
            tickers: List of ticker symbols
        """
        cursor = self.conn.cursor()
        now = datetime.now().isoformat()

        # Clear existing tickers
        cursor.execute("DELETE FROM sp500_tickers")

        # Insert new tickers
        cursor.executemany(
            "INSERT INTO sp500_tickers (ticker, updated_at) VALUES (?, ?)",
            [(ticker, now) for ticker in tickers]
        )

        # Update metadata
        cursor.execute("""
            INSERT OR REPLACE INTO cache_metadata (key, value, updated_at)
            VALUES ('sp500_last_update', ?, ?)
        """, (now, now))

        self.conn.commit()

    def get_price_data(
        self,
        ticker: str,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
        max_age_days: int = 7
    ) -> Optional[pd.DataFrame]:
        """
        Retrieve historical price data from cache for a specific ticker.

        Args:
            ticker: Stock ticker symbol
            start_date: Start date for data range
            end_date: End date for data range
            max_age_days: Maximum age of cached data in days

        Returns:
            DataFrame with price data or None if not in cache or stale
        """
        cursor = self.conn.cursor()

        # Check if we have any data for this ticker
        cursor.execute("""
            SELECT MAX(updated_at) FROM price_data WHERE ticker = ?
        """, (ticker,))
        result = cursor.fetchone()

        if not result[0]:
            return None

        # Check if cache is fresh
        last_update = datetime.fromisoformat(result[0])
        age_days = (datetime.now() - last_update).days

        if age_days >= max_age_days:
            return None

        # Build query based on date range
        query = """
            SELECT date, close, volume, market_cap
            FROM price_data
            WHERE ticker = ?
        """
        params = [ticker]

        if start_date:
            query += " AND date >= ?"
            params.append(start_date.strftime('%Y-%m-%d'))

        if end_date:
            query += " AND date <= ?"
            params.append(end_date.strftime('%Y-%m-%d'))

        query += " ORDER BY date"

        cursor.execute(query, params)
        rows = cursor.fetchall()

        if not rows:
            return None

        # Convert to DataFrame
        df = pd.DataFrame(rows, columns=['Date', 'Close', 'Volume', 'MarketCap'])
        df['Date'] = pd.to_datetime(df['Date'])
        df.set_index('Date', inplace=True)

        return df

    def save_price_data(self, ticker: str, data: pd.DataFrame, shares: Optional[float] = None):
        """
        Save historical price data to cache.

        Args:
            ticker: Stock ticker symbol
            data: DataFrame with columns: Close, Volume, MarketCap
            shares: Shares outstanding (optional)
        """
        cursor = self.conn.cursor()
        now = datetime.now().isoformat()

        # Prepare data for insertion
        records = []
        for date, row in data.iterrows():
            # Convert timezone-aware datetime to timezone-naive if needed
            if isinstance(date, pd.Timestamp) and date.tz is not None:
                date = date.tz_localize(None)

            date_str = date.strftime('%Y-%m-%d')

            records.append((
                ticker,
                date_str,
                float(row['Close']),
                float(row['Volume']) if pd.notna(row['Volume']) else None,
                float(row['MarketCap']) if pd.notna(row['MarketCap']) else None,
                shares,
                now
            ))

        # Delete existing data for this ticker in the date range
        if len(records) > 0:
            min_date = min(r[1] for r in records)
            max_date = max(r[1] for r in records)

            cursor.execute("""
                DELETE FROM price_data
                WHERE ticker = ? AND date >= ? AND date <= ?
            """, (ticker, min_date, max_date))

        # Insert new data
        cursor.executemany("""
            INSERT INTO price_data
            (ticker, date, close, volume, market_cap, shares_outstanding, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, records)

        self.conn.commit()

    def get_all_cached_tickers(self) -> List[str]:
        """
        Get list of all tickers that have cached price data.

        Returns:
            List of ticker symbols
        """
        cursor = self.conn.cursor()
        cursor.execute("SELECT DISTINCT ticker FROM price_data ORDER BY ticker")
        return [row[0] for row in cursor.fetchall()]

    def get_cache_stats(self) -> Dict:
        """
        Get statistics about the cache.

        Returns:
            Dictionary with cache statistics
        """
        cursor = self.conn.cursor()

        # Count tickers
        cursor.execute("SELECT COUNT(DISTINCT ticker) FROM price_data")
        ticker_count = cursor.fetchone()[0]

        # Count total records
        cursor.execute("SELECT COUNT(*) FROM price_data")
        record_count = cursor.fetchone()[0]

        # Get date range
        cursor.execute("SELECT MIN(date), MAX(date) FROM price_data")
        date_range = cursor.fetchone()

        # Get last update time
        cursor.execute("SELECT MAX(updated_at) FROM price_data")
        last_update = cursor.fetchone()[0]

        # Get S&P 500 list info
        cursor.execute("SELECT value FROM cache_metadata WHERE key = 'sp500_last_update'")
        sp500_update = cursor.fetchone()

        return {
            'tickers_cached': ticker_count,
            'total_records': record_count,
            'date_range': date_range,
            'last_update': last_update,
            'sp500_list_updated': sp500_update[0] if sp500_update else None
        }

    def clear_cache(self, ticker: Optional[str] = None):
        """
        Clear cached data.

        Args:
            ticker: If provided, only clear data for this ticker.
                   If None, clear all data.
        """
        cursor = self.conn.cursor()

        if ticker:
            cursor.execute("DELETE FROM price_data WHERE ticker = ?", (ticker,))
        else:
            cursor.execute("DELETE FROM price_data")
            cursor.execute("DELETE FROM sp500_tickers")
            cursor.execute("DELETE FROM cache_metadata")

        self.conn.commit()

    def close(self):
        """Close the database connection."""
        if self.conn:
            self.conn.close()

    def __enter__(self):
        """Context manager entry."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()
