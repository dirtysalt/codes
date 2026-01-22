#!/usr/bin/env python3
"""
S&P 500 Momentum Calculator

Calculates momentum scores for S&P 500 stocks based on historical price performance
and market capitalization.

Momentum formula:
- Price increase ratio over X months (excluding recent 30 days) * Market Value
"""

import argparse
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Tuple, Callable
import pandas as pd
import numpy as np
import yfinance as yf
from tqdm import tqdm
import requests
from io import StringIO

# Import custom momentum formulas and allocation strategies
import formulas
import allocation
from database import StockDataCache


class SP500MomentumCalculator:
    """Calculator for S&P 500 stock momentum."""

    def __init__(self, cache_dir: str = ".cache"):
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(exist_ok=True)
        db_path = self.cache_dir / "stock_data.db"
        self.db = StockDataCache(str(db_path))

    def get_sp500_tickers(self) -> List[str]:
        """Fetch S&P 500 ticker symbols from Wikipedia."""
        # Check cache first (refreshes every 30 days)
        cached_tickers = self.db.get_sp500_tickers(max_age_days=30)
        if cached_tickers:
            return cached_tickers

        print("Fetching S&P 500 ticker list from Wikipedia...")
        url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"

        # Use requests with user agent to avoid 403 errors
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        tables = pd.read_html(StringIO(response.text))
        sp500_table = tables[0]
        tickers = sp500_table['Symbol'].tolist()

        # Clean tickers (some may have special characters)
        tickers = [ticker.replace('.', '-') for ticker in tickers]

        # Cache the tickers in database
        self.db.save_sp500_tickers(tickers)

        print(f"Found {len(tickers)} S&P 500 stocks")
        return tickers

    def fetch_historical_data(
        self,
        tickers: List[str],
        years: int = 20
    ) -> Dict[str, pd.DataFrame]:
        """
        Fetch historical price and market cap data for all tickers.

        Args:
            tickers: List of stock ticker symbols
            years: Number of years of historical data to fetch

        Returns:
            Dictionary mapping ticker to DataFrame with price and market cap data
        """
        end_date = datetime.now()
        start_date = end_date - timedelta(days=years * 365)

        print(f"\nFetching historical data from {start_date.date()} to {end_date.date()}")
        print("(This may take a few minutes on first run...)")

        data = {}
        failed_tickers = []

        for ticker in tqdm(tickers, desc="Downloading stock data"):
            # Check if we have recent cached data for this ticker in database
            cached_df = self.db.get_price_data(
                ticker,
                start_date=start_date,
                end_date=end_date,
                max_age_days=7
            )

            if cached_df is not None:
                data[ticker] = cached_df
                continue

            # Fetch fresh data from yfinance
            try:
                stock = yf.Ticker(ticker)
                hist = stock.history(start=start_date, end=end_date)

                if hist.empty:
                    failed_tickers.append(ticker)
                    continue

                # Get market cap data
                # We'll approximate market cap using shares outstanding * price
                info = stock.info
                shares = info.get('sharesOutstanding', None)

                # Create DataFrame with necessary columns
                df = pd.DataFrame({
                    'Close': hist['Close'],
                    'Volume': hist['Volume'],
                    'MarketCap': hist['Close'] * shares if shares else None
                })

                # Convert timezone-aware index to timezone-naive for consistency
                if df.index.tz is not None:
                    df.index = df.index.tz_localize(None)

                data[ticker] = df

                # Save to database cache
                self.db.save_price_data(ticker, df, shares)

            except Exception as e:
                print(f"\nError fetching {ticker}: {str(e)}")
                failed_tickers.append(ticker)
                continue

        if failed_tickers:
            print(f"\nFailed to fetch data for {len(failed_tickers)} tickers: {failed_tickers[:10]}...")

        print(f"\nSuccessfully fetched data for {len(data)} stocks")
        return data

    def calculate_momentum(
        self,
        historical_data: Dict[str, pd.DataFrame],
        end_date: datetime,
        months: int,
        formula_func: Callable = None
    ) -> pd.DataFrame:
        """
        Calculate momentum scores for all stocks.

        Args:
            historical_data: Dictionary of ticker -> historical price/market cap data
            end_date: End date for calculation
            months: Number of months to look back (excluding recent 30 days)
            formula_func: Optional custom formula function to use

        Returns:
            DataFrame with tickers, momentum scores, and normalized scores
        """
        # Use classic formula if none specified
        if formula_func is None:
            formula_func = formulas.classic_momentum
        results = []

        # Calculate dates
        lookback_end = end_date - timedelta(days=30)  # Exclude recent 30 days
        lookback_start = lookback_end - timedelta(days=months * 30)  # Approximate months

        print(f"\nCalculating momentum from {lookback_start.date()} to {lookback_end.date()}")
        print(f"End date: {end_date.date()} (excluding last 30 days)")

        for ticker, df in tqdm(historical_data.items(), desc="Calculating momentum"):
            try:
                # Filter data for the lookback period
                mask = (df.index >= lookback_start) & (df.index <= lookback_end)
                period_data = df[mask]

                if len(period_data) < 2:
                    continue

                # Get start and end prices
                start_price = period_data['Close'].iloc[0]
                end_price = period_data['Close'].iloc[-1]

                # Calculate price increase ratio
                price_ratio = (end_price - start_price) / start_price

                # Get market cap at the end of period
                market_cap = period_data['MarketCap'].iloc[-1]

                if pd.isna(market_cap) or market_cap is None:
                    # If market cap is not available, skip this stock
                    continue

                # Calculate momentum using the specified formula
                momentum = formula_func(start_price, end_price, market_cap, period_data)

                results.append({
                    'Ticker': ticker,
                    'StartPrice': start_price,
                    'EndPrice': end_price,
                    'PriceRatio': price_ratio,
                    'MarketCap': market_cap,
                    'Momentum': momentum
                })

            except Exception as e:
                print(f"\nError calculating momentum for {ticker}: {str(e)}")
                continue

        if not results:
            raise ValueError("No valid momentum calculations produced")

        # Create DataFrame and sort by momentum
        df_results = pd.DataFrame(results)
        df_results = df_results.sort_values('Momentum', ascending=False)

        # Normalize scores to 0-100 range
        min_momentum = df_results['Momentum'].min()
        max_momentum = df_results['Momentum'].max()
        df_results['NormalizedScore'] = (
            (df_results['Momentum'] - min_momentum) /
            (max_momentum - min_momentum) * 100
        )

        return df_results

    def run(
        self,
        end_date: str,
        months: int,
        top_n: int = None,
        formula_name: str = 'classic'
    ) -> pd.DataFrame:
        """
        Main execution method.

        Args:
            end_date: End date in YYYY-MM-DD format
            months: Number of months to look back
            top_n: Optional, number of top stocks to return
            formula_name: Name of the momentum formula to use

        Returns:
            DataFrame with momentum results
        """
        # Parse end date
        end_dt = datetime.strptime(end_date, '%Y-%m-%d')

        # Get formula function
        formula_func = formulas.get_formula(formula_name)

        # Get S&P 500 tickers
        tickers = self.get_sp500_tickers()

        # Fetch historical data
        historical_data = self.fetch_historical_data(tickers)

        # Calculate momentum
        results = self.calculate_momentum(historical_data, end_dt, months, formula_func)

        # Filter to top N if specified
        if top_n:
            results = results.head(top_n)

        return results


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description='Calculate momentum scores for S&P 500 stocks'
    )
    parser.add_argument(
        '--end-date',
        type=str,
        default=datetime.now().strftime('%Y-%m-%d'),
        help='End date for calculation (YYYY-MM-DD). Default: today'
    )
    parser.add_argument(
        '--months',
        type=int,
        default=12,
        help='Number of months to look back (default: 12)'
    )
    parser.add_argument(
        '--top',
        type=int,
        default=20,
        help='Number of top stocks to display (default: 20, use 0 for all)'
    )
    parser.add_argument(
        '--formula',
        type=str,
        default='classic',
        help=f'Momentum formula to use (default: classic). '
             f'Available: {", ".join(formulas.AVAILABLE_FORMULAS.keys())}'
    )
    parser.add_argument(
        '--list-formulas',
        action='store_true',
        help='List all available momentum formulas and exit'
    )
    parser.add_argument(
        '--allocation',
        type=str,
        help=f'Allocation strategy to use (optional). '
             f'Available: {", ".join(allocation.AVAILABLE_ALLOCATIONS.keys())}'
    )
    parser.add_argument(
        '--max-position',
        type=float,
        help='Maximum allocation percentage per position (e.g., 10 for 10%%)'
    )
    parser.add_argument(
        '--list-allocations',
        action='store_true',
        help='List all available allocation strategies and exit'
    )
    parser.add_argument(
        '--output',
        type=str,
        help='Optional: Save results to CSV file'
    )
    parser.add_argument(
        '--cache-dir',
        type=str,
        default='.cache',
        help='Directory for caching data (default: .cache)'
    )

    args = parser.parse_args()

    # List formulas if requested
    if args.list_formulas:
        formulas.list_formulas()
        return

    # List allocation strategies if requested
    if args.list_allocations:
        allocation.list_allocation_strategies()
        return

    # Create calculator
    calculator = SP500MomentumCalculator(cache_dir=args.cache_dir)

    # Run calculation
    top_n = args.top if args.top > 0 else None
    results = calculator.run(args.end_date, args.months, top_n, args.formula)

    # Display results
    print("\n" + "="*80)
    print(f"TOP MOMENTUM STOCKS (as of {args.end_date}, {args.months} months lookback)")
    print(f"Formula: {args.formula}")
    print("="*80)
    print(results.to_string(index=False))

    # Calculate allocations if requested
    if args.allocation:
        print("\n" + "="*80)
        print(f"PORTFOLIO ALLOCATION (Strategy: {args.allocation})")
        if args.max_position:
            print(f"Maximum position size: {args.max_position}%")
        print("="*80)

        # Get allocation function
        alloc_func = allocation.get_allocation_function(args.allocation)

        # Calculate allocations
        kwargs = {}
        if args.max_position:
            kwargs['max_position'] = args.max_position

        # Pass market cap data for market_cap_weighted strategy
        if args.allocation == 'market_cap_weighted':
            kwargs['market_caps'] = results['MarketCap'].values
            # Default to top 100 for SPMO replication if not specified
            if 'top_n' not in kwargs and top_n is None:
                kwargs['top_n'] = 100

        allocations = alloc_func(
            results['NormalizedScore'].values,
            results['Ticker'].values,
            **kwargs
        )

        # Create allocation dataframe
        alloc_df = pd.DataFrame([
            {'Ticker': ticker, 'Allocation': pct}
            for ticker, pct in allocations.items()
        ]).sort_values('Allocation', ascending=False)

        print(alloc_df.to_string(index=False))
        print(f"\nTotal Allocation: {alloc_df['Allocation'].sum():.2f}%")

        # Add allocations to results dataframe
        results['Allocation'] = results['Ticker'].map(allocations).fillna(0)

    # Save to file if requested
    if args.output:
        results.to_csv(args.output, index=False)
        print(f"\nResults saved to {args.output}")


if __name__ == "__main__":
    main()
