# Custom Momentum Formulas Guide

This guide explains how to create and use custom momentum calculation formulas.

## Quick Start

The application includes 8 built-in momentum formulas. To see all available formulas:

```bash
python momentum_calculator.py --list-formulas
```

To use a specific formula:

```bash
python momentum_calculator.py --formula cagr --months 12
```

## Creating Your Own Formula

All formulas are defined in `formulas.py`. To create a custom formula:

### 1. Define Your Formula Function

Add a new function to `formulas.py`:

```python
def my_custom_momentum(start_price, end_price, market_cap, period_data):
    """
    Brief description of your formula.

    Formula: Mathematical expression here

    Your explanation here.
    """
    # Your calculation logic here
    # Example: simple price change weighted by market cap
    price_change = end_price - start_price
    return price_change * market_cap
```

### 2. Register Your Formula

Add your formula to the `AVAILABLE_FORMULAS` dictionary in `formulas.py`:

```python
AVAILABLE_FORMULAS = {
    'classic': classic_momentum,
    'log_return': log_return_momentum,
    # ... other formulas ...
    'my_custom': my_custom_momentum,  # Add your formula here
}
```

### 3. Use Your Formula

```bash
python momentum_calculator.py --formula my_custom
```

## Formula Function Signature

Each formula function must accept these parameters:

```python
def formula_name(start_price, end_price, market_cap, period_data):
    """
    Args:
        start_price (float): Stock price at the beginning of the lookback period
        end_price (float): Stock price at the end of the lookback period
        market_cap (float): Market capitalization at the end of the period
        period_data (DataFrame): Complete historical data for the period
                                 Columns: 'Close', 'Volume', 'MarketCap'
                                 Index: DatetimeIndex

    Returns:
        float: The momentum score
    """
    # Your calculation here
    return score
```

## Available Data in period_data

The `period_data` DataFrame contains:

| Column | Description |
|--------|-------------|
| `Close` | Daily closing prices |
| `Volume` | Daily trading volume |
| `MarketCap` | Daily market capitalization |

The DataFrame index is a DatetimeIndex with daily timestamps.

### Example: Accessing Historical Data

```python
def example_formula(start_price, end_price, market_cap, period_data):
    # Get all closing prices
    prices = period_data['Close']

    # Calculate daily returns
    daily_returns = prices.pct_change()

    # Calculate average volume
    avg_volume = period_data['Volume'].mean()

    # Get number of trading days
    num_days = len(period_data)

    # Your custom calculation
    momentum = (end_price / start_price - 1) * market_cap * avg_volume
    return momentum
```

## Example Custom Formulas

### Example 1: Simple Percentage Change

```python
def percent_change_momentum(start_price, end_price, market_cap, period_data):
    """
    Momentum based on simple percentage change.

    Formula: ((End Price - Start Price) / Start Price) * 100
    """
    percent_change = ((end_price - start_price) / start_price) * 100
    return percent_change
```

### Example 2: Volume-Weighted Price Change

```python
def volume_weighted_momentum(start_price, end_price, market_cap, period_data):
    """
    Price change weighted by average daily volume.

    Formula: Price Change * Average Volume
    """
    price_change = end_price - start_price
    avg_volume = period_data['Volume'].mean()
    return price_change * avg_volume
```

### Example 3: Stability-Adjusted Returns

```python
import numpy as np

def stability_adjusted_momentum(start_price, end_price, market_cap, period_data):
    """
    Returns adjusted for price stability (inverse of coefficient of variation).

    Formula: (Return / Coefficient of Variation) * Market Cap
    """
    total_return = (end_price - start_price) / start_price

    # Coefficient of variation = std / mean
    prices = period_data['Close']
    cv = prices.std() / prices.mean()

    # Avoid division by zero
    if cv == 0 or np.isnan(cv):
        cv = 0.01

    return (total_return / cv) * market_cap
```

### Example 4: Momentum with Minimum Price Threshold

```python
def high_price_momentum(start_price, end_price, market_cap, period_data):
    """
    Only awards positive momentum if end price is above threshold.

    Formula: Standard momentum if end_price > $50, else 0
    """
    if end_price < 50:
        return 0

    price_ratio = (end_price - start_price) / start_price
    return price_ratio * market_cap
```

### Example 5: Multi-Factor Momentum

```python
import numpy as np

def multi_factor_momentum(start_price, end_price, market_cap, period_data):
    """
    Combines multiple factors: return, trend strength, and volume.

    Formula: (Return * Trend * Volume Factor) * Market Cap
    """
    # Factor 1: Price return
    price_return = (end_price - start_price) / start_price

    # Factor 2: Trend strength (R-squared of linear fit)
    x = np.arange(len(period_data))
    y = period_data['Close'].values
    correlation = np.corrcoef(x, y)[0, 1]
    trend_strength = abs(correlation) ** 2  # R-squared

    # Factor 3: Volume factor (normalized)
    avg_volume = period_data['Volume'].mean()
    volume_factor = np.log1p(avg_volume) / 20  # Normalized log volume

    # Combine factors
    combined_score = price_return * trend_strength * volume_factor
    return combined_score * market_cap
```

## Best Practices

1. **Handle Edge Cases**: Always check for division by zero and NaN values

   ```python
   if denominator == 0 or pd.isna(denominator):
       return 0  # or some default value
   ```

2. **Use Appropriate Scaling**: Different formulas produce different magnitudes. The application will normalize scores to 0-100 range, but ensure your formula doesn't overflow.

3. **Document Your Formula**: Write clear docstrings explaining:
   - What the formula measures
   - The mathematical expression
   - Any assumptions or limitations

4. **Test with Different Time Periods**: Your formula should work with various lookback periods (1 month to 24+ months).

5. **Consider Market Cap**: Most formulas multiply by market cap to weight larger companies, but this is optional based on your strategy.

## Testing Your Formula

Create a simple test script:

```python
# test_formula.py
import pandas as pd
import numpy as np
from formulas import my_custom_momentum

# Create sample data
dates = pd.date_range('2023-01-01', periods=252, freq='D')
period_data = pd.DataFrame({
    'Close': np.linspace(100, 120, 252),  # Price increases from 100 to 120
    'Volume': np.random.randint(1000000, 5000000, 252),
    'MarketCap': np.linspace(1e9, 1.2e9, 252)
}, index=dates)

start_price = 100
end_price = 120
market_cap = 1.2e9

score = my_custom_momentum(start_price, end_price, market_cap, period_data)
print(f"Momentum score: {score:,.2f}")
```

## Comparing Formulas

Compare different formulas on the same data:

```bash
# Run with classic formula
python momentum_calculator.py --formula classic --months 12 --output classic.csv

# Run with CAGR formula
python momentum_calculator.py --formula cagr --months 12 --output cagr.csv

# Compare the results
import pandas as pd
classic = pd.read_csv('classic.csv')
cagr = pd.read_csv('cagr.csv')
print(classic[['Ticker', 'NormalizedScore']].merge(
    cagr[['Ticker', 'NormalizedScore']],
    on='Ticker',
    suffixes=('_classic', '_cagr')
).head(20))
```

## Advanced: Using External Libraries

You can use any Python library in your formula:

```python
import scipy.stats as stats

def statistical_momentum(start_price, end_price, market_cap, period_data):
    """Uses statistical tests to validate trend significance."""
    returns = period_data['Close'].pct_change().dropna()

    # Test if mean return is significantly different from zero
    t_stat, p_value = stats.ttest_1samp(returns, 0)

    # Only award momentum if trend is statistically significant
    if p_value > 0.05:
        return 0

    price_ratio = (end_price - start_price) / start_price
    return price_ratio * market_cap
```

Remember to add any new dependencies to `requirements.txt`:

```
scipy>=1.10.0
```

## Troubleshooting

**Formula returns NaN or infinity:**
- Check for division by zero
- Verify all inputs are valid numbers
- Handle cases where period_data is empty or has insufficient data

**Results seem incorrect:**
- Print intermediate values for debugging
- Test with known sample data
- Verify the formula logic matches your intention

**Formula is too slow:**
- Avoid loops when possible; use vectorized pandas/numpy operations
- Profile your code to find bottlenecks
- Consider simplifying complex calculations

## Formula Ideas

Here are some momentum concepts you might want to implement:

- **Relative Strength Index (RSI)** based momentum
- **Moving Average Convergence Divergence (MACD)** based scoring
- **Sortino Ratio** (downside risk-adjusted returns)
- **Calmar Ratio** (return / max drawdown)
- **Alpha vs S&P 500** benchmark
- **Seasonal/cyclical** patterns
- **Earnings-adjusted** momentum
- **Sector-relative** performance

Happy formula building!
