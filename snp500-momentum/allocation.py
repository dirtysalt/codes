"""
Portfolio Allocation Functions

Functions to compute portfolio share allocations based on momentum scores.
Users can easily modify these or add their own custom allocation strategies.

Each allocation function receives:
- scores: Array or Series of momentum scores (already normalized 0-100)
- tickers: Array or Series of ticker symbols (same length as scores)

Returns:
- Dictionary mapping ticker to allocation percentage (should sum to 100)
"""

import numpy as np
import pandas as pd
from typing import Dict, Union


def proportional_allocation(
    scores: Union[np.ndarray, pd.Series],
    tickers: Union[np.ndarray, pd.Series],
    max_position: float = None
) -> Dict[str, float]:
    """
    Proportional allocation based on normalized scores.

    Allocates portfolio weight proportional to each stock's score.

    Args:
        scores: Normalized momentum scores
        tickers: Stock ticker symbols
        max_position: Maximum percentage for any single position (optional)

    Returns:
        Dictionary of {ticker: allocation_percentage}
    """
    # Convert to numpy arrays
    scores = np.array(scores)
    tickers = np.array(tickers)

    # Filter out zero or negative scores
    mask = scores > 0
    scores = scores[mask]
    tickers = tickers[mask]

    if len(scores) == 0:
        return {}

    # Calculate proportional weights
    total_score = scores.sum()
    allocations = (scores / total_score) * 100

    # Apply position cap if specified
    if max_position is not None:
        allocations = _apply_position_cap(allocations, max_position)

    return dict(zip(tickers, allocations))


def equal_weight_allocation(
    scores: Union[np.ndarray, pd.Series],
    tickers: Union[np.ndarray, pd.Series],
    top_n: int = 10,
    max_position: float = None
) -> Dict[str, float]:
    """
    Equal weight allocation to top N stocks.

    Args:
        scores: Normalized momentum scores
        tickers: Stock ticker symbols
        top_n: Number of top stocks to include
        max_position: Maximum percentage for any single position (optional)

    Returns:
        Dictionary of {ticker: allocation_percentage}
    """
    # Convert to arrays and sort by score descending
    scores = np.array(scores)
    tickers = np.array(tickers)

    # Sort by score
    idx = np.argsort(scores)[::-1]
    top_tickers = tickers[idx][:top_n]

    # Equal allocation
    allocation = 100.0 / top_n

    # Apply cap if needed
    if max_position is not None and allocation > max_position:
        allocation = max_position
        # Redistribute remaining
        remaining = 100.0 - (allocation * top_n)
        if remaining > 0:
            # This would require more stocks, but we'll just normalize
            allocation = max_position

    return {ticker: allocation for ticker in top_tickers}


def tiered_allocation(
    scores: Union[np.ndarray, pd.Series],
    tickers: Union[np.ndarray, pd.Series],
    tiers: list = [(5, 0.5), (10, 0.3), (15, 0.2)],
    max_position: float = None
) -> Dict[str, float]:
    """
    Tiered allocation strategy.

    Allocates different percentages of portfolio to different tiers of stocks.

    Args:
        scores: Normalized momentum scores
        tickers: Stock ticker symbols
        tiers: List of (num_stocks, portfolio_percentage) tuples
               Example: [(5, 0.5), (10, 0.3), (15, 0.2)] means:
               - Top 5 stocks get 50% of portfolio
               - Next 10 stocks get 30% of portfolio
               - Next 15 stocks get 20% of portfolio
        max_position: Maximum percentage for any single position (optional)

    Returns:
        Dictionary of {ticker: allocation_percentage}
    """
    # Convert and sort
    scores = np.array(scores)
    tickers = np.array(tickers)
    idx = np.argsort(scores)[::-1]
    sorted_tickers = tickers[idx]

    allocations = {}
    current_idx = 0

    for num_stocks, portfolio_pct in tiers:
        tier_tickers = sorted_tickers[current_idx:current_idx + num_stocks]
        if len(tier_tickers) == 0:
            break

        # Equal weight within tier
        allocation_per_stock = (portfolio_pct * 100) / len(tier_tickers)

        for ticker in tier_tickers:
            allocations[ticker] = allocation_per_stock

        current_idx += num_stocks

    # Apply position cap if specified
    if max_position is not None:
        allocations = _apply_position_cap_to_dict(allocations, max_position)

    return allocations


def inverse_variance_allocation(
    scores: Union[np.ndarray, pd.Series],
    tickers: Union[np.ndarray, pd.Series],
    max_position: float = None
) -> Dict[str, float]:
    """
    Inverse variance allocation.

    Higher scores get more weight, but with diminishing returns
    (uses 1/variance = 1/score^2 weighting).

    Args:
        scores: Normalized momentum scores
        tickers: Stock ticker symbols
        max_position: Maximum percentage for any single position (optional)

    Returns:
        Dictionary of {ticker: allocation_percentage}
    """
    scores = np.array(scores)
    tickers = np.array(tickers)

    # Filter positive scores
    mask = scores > 0
    scores = scores[mask]
    tickers = tickers[mask]

    if len(scores) == 0:
        return {}

    # Inverse variance weighting (1 / score)
    # Higher scores get lower "variance" and thus higher weight
    weights = 1.0 / scores
    weights = weights / weights.sum()

    allocations = weights * 100

    # Apply position cap
    if max_position is not None:
        allocations = _apply_position_cap(allocations, max_position)

    return dict(zip(tickers, allocations))


def logarithmic_allocation(
    scores: Union[np.ndarray, pd.Series],
    tickers: Union[np.ndarray, pd.Series],
    max_position: float = None
) -> Dict[str, float]:
    """
    Logarithmic allocation.

    Uses log(score) for allocation, reducing impact of very high scores.

    Args:
        scores: Normalized momentum scores
        tickers: Stock ticker symbols
        max_position: Maximum percentage for any single position (optional)

    Returns:
        Dictionary of {ticker: allocation_percentage}
    """
    scores = np.array(scores)
    tickers = np.array(tickers)

    # Filter positive scores
    mask = scores > 1  # Need scores > 1 for positive log
    scores = scores[mask]
    tickers = tickers[mask]

    if len(scores) == 0:
        return {}

    # Log weighting
    log_scores = np.log(scores)
    allocations = (log_scores / log_scores.sum()) * 100

    # Apply position cap
    if max_position is not None:
        allocations = _apply_position_cap(allocations, max_position)

    return dict(zip(tickers, allocations))


def threshold_allocation(
    scores: Union[np.ndarray, pd.Series],
    tickers: Union[np.ndarray, pd.Series],
    threshold: float = 50,
    max_position: float = None
) -> Dict[str, float]:
    """
    Threshold-based allocation.

    Only allocates to stocks with scores above threshold,
    then proportionally within that group.

    Args:
        scores: Normalized momentum scores
        tickers: Stock ticker symbols
        threshold: Minimum score required for allocation
        max_position: Maximum percentage for any single position (optional)

    Returns:
        Dictionary of {ticker: allocation_percentage}
    """
    scores = np.array(scores)
    tickers = np.array(tickers)

    # Filter by threshold
    mask = scores >= threshold
    scores = scores[mask]
    tickers = tickers[mask]

    if len(scores) == 0:
        return {}

    # Proportional allocation among qualifying stocks
    allocations = (scores / scores.sum()) * 100

    # Apply position cap
    if max_position is not None:
        allocations = _apply_position_cap(allocations, max_position)

    return dict(zip(tickers, allocations))


def rank_based_allocation(
    scores: Union[np.ndarray, pd.Series],
    tickers: Union[np.ndarray, pd.Series],
    top_n: int = 20,
    max_position: float = None
) -> Dict[str, float]:
    """
    Rank-based allocation (inverse rank weighting).

    Rank 1 gets weight = N, Rank 2 gets N-1, etc.

    Args:
        scores: Normalized momentum scores
        tickers: Stock ticker symbols
        top_n: Number of stocks to include
        max_position: Maximum percentage for any single position (optional)

    Returns:
        Dictionary of {ticker: allocation_percentage}
    """
    scores = np.array(scores)
    tickers = np.array(tickers)

    # Sort by score
    idx = np.argsort(scores)[::-1]
    top_tickers = tickers[idx][:top_n]

    # Create rank weights: top stock gets top_n points, second gets top_n-1, etc.
    ranks = np.arange(top_n, 0, -1)
    allocations = (ranks / ranks.sum()) * 100

    # Apply position cap
    if max_position is not None:
        allocations = _apply_position_cap(allocations, max_position)

    return dict(zip(top_tickers, allocations))


def market_cap_weighted_allocation(
    scores: Union[np.ndarray, pd.Series],
    tickers: Union[np.ndarray, pd.Series],
    top_n: int = 100,
    max_position: float = None,
    market_caps: Union[np.ndarray, pd.Series] = None
) -> Dict[str, float]:
    """
    Market-cap weighted allocation (SPMO methodology).

    Selects top N stocks by momentum score, then allocates based on
    market capitalization weights. This replicates the SPMO ETF strategy.

    Args:
        scores: Normalized momentum scores
        tickers: Stock ticker symbols
        top_n: Number of top momentum stocks to select (default: 100)
        max_position: Maximum percentage for any single position (optional)
        market_caps: Market capitalization values for each stock (required)

    Returns:
        Dictionary of {ticker: allocation_percentage}
    """
    if market_caps is None:
        raise ValueError("market_caps parameter is required for market_cap_weighted allocation")

    scores = np.array(scores)
    tickers = np.array(tickers)
    market_caps = np.array(market_caps)

    # Sort by momentum score and select top N
    idx = np.argsort(scores)[::-1]
    top_indices = idx[:top_n]

    selected_tickers = tickers[top_indices]
    selected_market_caps = market_caps[top_indices]

    # Allocate based on market cap weights
    total_market_cap = selected_market_caps.sum()
    allocations = (selected_market_caps / total_market_cap) * 100

    # Apply position cap if specified
    if max_position is not None:
        allocations = _apply_position_cap(allocations, max_position)

    return dict(zip(selected_tickers, allocations))


def _apply_position_cap(allocations: np.ndarray, max_position: float) -> np.ndarray:
    """
    Apply position cap to allocation array and redistribute excess.

    Args:
        allocations: Array of allocation percentages
        max_position: Maximum percentage for any position

    Returns:
        Capped and renormalized allocations
    """
    # Iteratively cap and redistribute
    max_iterations = 100
    for _ in range(max_iterations):
        over_cap = allocations > max_position
        if not over_cap.any():
            break

        # Cap the over-allocated positions
        excess = (allocations[over_cap] - max_position).sum()
        allocations[over_cap] = max_position

        # Redistribute excess to under-cap positions
        under_cap = ~over_cap
        if under_cap.any():
            # Proportionally redistribute
            under_cap_total = allocations[under_cap].sum()
            if under_cap_total > 0:
                allocations[under_cap] += (allocations[under_cap] / under_cap_total) * excess
        else:
            # All are capped, just normalize
            break

    # Final normalization to ensure sum = 100
    allocations = (allocations / allocations.sum()) * 100

    return allocations


def _apply_position_cap_to_dict(
    allocations: Dict[str, float],
    max_position: float
) -> Dict[str, float]:
    """Apply position cap to dictionary of allocations."""
    tickers = np.array(list(allocations.keys()))
    values = np.array(list(allocations.values()))

    capped_values = _apply_position_cap(values, max_position)

    return dict(zip(tickers, capped_values))


# Dictionary of available allocation strategies
AVAILABLE_ALLOCATIONS = {
    'proportional': proportional_allocation,
    'equal_weight': equal_weight_allocation,
    'tiered': tiered_allocation,
    'inverse_variance': inverse_variance_allocation,
    'logarithmic': logarithmic_allocation,
    'threshold': threshold_allocation,
    'rank_based': rank_based_allocation,
    'market_cap_weighted': market_cap_weighted_allocation,
}


def get_allocation_function(name: str):
    """
    Get an allocation function by name.

    Args:
        name: Name of the allocation strategy

    Returns:
        Allocation function
    """
    if name not in AVAILABLE_ALLOCATIONS:
        raise ValueError(
            f"Unknown allocation strategy '{name}'. "
            f"Available: {list(AVAILABLE_ALLOCATIONS.keys())}"
        )
    return AVAILABLE_ALLOCATIONS[name]


def list_allocation_strategies():
    """Print all available allocation strategies."""
    print("\nAvailable Allocation Strategies:")
    print("=" * 80)

    for name, func in AVAILABLE_ALLOCATIONS.items():
        doc = func.__doc__.strip().split('\n\n')[0] if func.__doc__ else "No description"
        print(f"\n{name:20s} - {doc}")

    print("\n" + "=" * 80)


if __name__ == "__main__":
    # Demo
    list_allocation_strategies()

    # Example usage
    print("\n\nExample: Allocating to 5 stocks with different strategies\n")

    tickers = np.array(['AAPL', 'MSFT', 'NVDA', 'GOOGL', 'AMZN'])
    scores = np.array([100, 85, 95, 80, 75])

    print("Scores:")
    for ticker, score in zip(tickers, scores):
        print(f"  {ticker}: {score}")

    print("\n1. Proportional (no cap):")
    alloc = proportional_allocation(scores, tickers)
    for ticker, pct in alloc.items():
        print(f"  {ticker}: {pct:.2f}%")

    print("\n2. Proportional (max 25% per position):")
    alloc = proportional_allocation(scores, tickers, max_position=25)
    for ticker, pct in alloc.items():
        print(f"  {ticker}: {pct:.2f}%")

    print("\n3. Equal Weight (top 3):")
    alloc = equal_weight_allocation(scores, tickers, top_n=3)
    for ticker, pct in alloc.items():
        print(f"  {ticker}: {pct:.2f}%")

    print("\n4. Rank-based:")
    alloc = rank_based_allocation(scores, tickers, top_n=5)
    for ticker, pct in alloc.items():
        print(f"  {ticker}: {pct:.2f}%")
