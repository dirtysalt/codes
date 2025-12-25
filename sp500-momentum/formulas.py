"""
Custom Momentum Formulas

This module contains different momentum calculation formulas.
Users can easily modify these or add their own custom formulas.

Each formula function receives:
- start_price: Stock price at the beginning of the period
- end_price: Stock price at the end of the period
- market_cap: Market capitalization at the end of the period
- period_data: Full DataFrame with 'Close' and 'MarketCap' columns for the period

Returns:
- momentum_score: A numeric momentum score
"""

import pandas as pd
import numpy as np


def classic_momentum(start_price, end_price, market_cap, period_data):
    """
    Classic momentum formula.

    Formula: (Price Ratio) × Market Cap

    Where Price Ratio = (End Price - Start Price) / Start Price
    """
    price_ratio = (end_price - start_price) / start_price
    return price_ratio * market_cap


def log_return_momentum(start_price, end_price, market_cap, period_data):
    """
    Logarithmic return momentum.

    Formula: log(End Price / Start Price) × Market Cap

    Log returns are more appropriate for compounding over time.
    """
    log_return = np.log(end_price / start_price)
    return log_return * market_cap


def volatility_adjusted_momentum(start_price, end_price, market_cap, period_data):
    """
    Volatility-adjusted momentum (Sharpe-like ratio).

    Formula: (Price Ratio / Volatility) × Market Cap

    Adjusts for risk by dividing by price volatility.
    """
    price_ratio = (end_price - start_price) / start_price

    # Calculate volatility (standard deviation of daily returns)
    returns = period_data['Close'].pct_change().dropna()
    volatility = returns.std()

    # Avoid division by zero
    if volatility == 0 or pd.isna(volatility):
        return 0

    risk_adjusted_return = price_ratio / volatility
    return risk_adjusted_return * market_cap


def cagr_momentum(start_price, end_price, market_cap, period_data):
    """
    Compound Annual Growth Rate (CAGR) momentum.

    Formula: CAGR × Market Cap

    Where CAGR = (End Price / Start Price)^(365/days) - 1
    """
    days = len(period_data)
    if days == 0:
        return 0

    cagr = (end_price / start_price) ** (365.0 / days) - 1
    return cagr * market_cap


def weighted_momentum(start_price, end_price, market_cap, period_data):
    """
    Volume-weighted momentum.

    Formula: (Price Ratio × Average Volume) × Market Cap

    Considers trading volume as an indicator of conviction.
    Note: Requires 'Volume' column in period_data.
    """
    price_ratio = (end_price - start_price) / start_price

    # If volume data is available, use it
    if 'Volume' in period_data.columns:
        avg_volume = period_data['Volume'].mean()
        # Normalize volume (divide by 1 million for scaling)
        volume_factor = avg_volume / 1_000_000
    else:
        volume_factor = 1

    return price_ratio * volume_factor * market_cap


def max_drawdown_adjusted_momentum(start_price, end_price, market_cap, period_data):
    """
    Maximum drawdown adjusted momentum.

    Formula: (Price Ratio / Max Drawdown) × Market Cap

    Penalizes stocks that had large drawdowns during the period.
    """
    price_ratio = (end_price - start_price) / start_price

    # Calculate maximum drawdown
    cumulative = (1 + period_data['Close'].pct_change()).cumprod()
    running_max = cumulative.expanding().max()
    drawdown = (cumulative - running_max) / running_max
    max_drawdown = abs(drawdown.min())

    # Avoid division by zero
    if max_drawdown == 0 or pd.isna(max_drawdown):
        max_drawdown = 0.01  # Use small value instead of zero

    return (price_ratio / max_drawdown) * market_cap


def percentile_rank_momentum(start_price, end_price, market_cap, period_data):
    """
    Percentile rank momentum.

    Formula: (Current Price Percentile Rank) × Market Cap

    Measures where the current price stands relative to the price range
    during the period (0 = lowest, 1 = highest).
    """
    price_range = period_data['Close'].max() - period_data['Close'].min()

    if price_range == 0:
        return 0

    percentile_rank = (end_price - period_data['Close'].min()) / price_range
    return percentile_rank * market_cap


def momentum_with_trend_strength(start_price, end_price, market_cap, period_data):
    """
    Momentum with trend strength.

    Formula: (Price Ratio × Trend Strength) × Market Cap

    Trend strength is measured by R-squared of linear regression,
    indicating how consistent the trend is.
    """
    price_ratio = (end_price - start_price) / start_price

    # Calculate trend strength using R-squared
    x = np.arange(len(period_data))
    y = period_data['Close'].values

    # Simple linear regression
    x_mean = x.mean()
    y_mean = y.mean()

    numerator = ((x - x_mean) * (y - y_mean)).sum()
    denominator = ((x - x_mean) ** 2).sum()

    if denominator == 0:
        return 0

    slope = numerator / denominator

    # Calculate R-squared
    y_pred = slope * (x - x_mean) + y_mean
    ss_res = ((y - y_pred) ** 2).sum()
    ss_tot = ((y - y_mean) ** 2).sum()

    if ss_tot == 0:
        r_squared = 0
    else:
        r_squared = 1 - (ss_res / ss_tot)

    # Trend strength factor (0 to 1)
    trend_strength = max(0, r_squared)

    return price_ratio * trend_strength * market_cap


# Dictionary mapping formula names to functions
AVAILABLE_FORMULAS = {
    'classic': classic_momentum,
    'log_return': log_return_momentum,
    'volatility_adjusted': volatility_adjusted_momentum,
    'cagr': cagr_momentum,
    'weighted': weighted_momentum,
    'max_drawdown': max_drawdown_adjusted_momentum,
    'percentile': percentile_rank_momentum,
    'trend_strength': momentum_with_trend_strength,
}


def get_formula(formula_name='classic'):
    """
    Get a momentum formula function by name.

    Args:
        formula_name: Name of the formula (default: 'classic')

    Returns:
        Formula function
    """
    if formula_name not in AVAILABLE_FORMULAS:
        raise ValueError(
            f"Unknown formula '{formula_name}'. "
            f"Available formulas: {list(AVAILABLE_FORMULAS.keys())}"
        )

    return AVAILABLE_FORMULAS[formula_name]


def list_formulas():
    """Print all available formulas with descriptions."""
    print("\nAvailable Momentum Formulas:")
    print("=" * 80)

    for name, func in AVAILABLE_FORMULAS.items():
        doc = func.__doc__.strip().split('\n')[0] if func.__doc__ else "No description"
        print(f"\n{name:20s} - {doc}")

        # Print formula if available in docstring
        if func.__doc__:
            lines = func.__doc__.strip().split('\n')
            for line in lines:
                if line.strip().startswith('Formula:'):
                    print(f"{'':20s}   {line.strip()}")

    print("\n" + "=" * 80)


if __name__ == "__main__":
    # Demo: List all available formulas
    list_formulas()
