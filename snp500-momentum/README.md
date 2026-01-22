# S&P 500 Momentum Calculator

A Python application to calculate and rank S&P 500 stocks based on momentum scores.

## Momentum Formula

For a given lookback period of X months:
- **Price Ratio**: (Price at end of period - Price at start) / Price at start
- **Period**: Last X months, excluding the most recent 30 days
- **Momentum Score**: Price Ratio × Market Capitalization

## Features

- Fetches current S&P 500 stock list from Wikipedia
- Downloads up to 20 years of historical price data
- Caches data locally to avoid repeated API calls
- **8 built-in momentum formulas** with easy customization
- Calculates momentum scores with customizable parameters
- Normalizes scores to 0-100 range
- Displays results sorted by momentum (descending)
- Optional CSV export

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

Calculate momentum for the past 12 months (default):
```bash
python momentum_calculator.py
```

### Custom Parameters

Specify end date and lookback period:
```bash
python momentum_calculator.py --end-date 2024-01-01 --months 6
```

### Show More/Fewer Results

Show top 50 stocks:
```bash
python momentum_calculator.py --top 50
```

Show all stocks:
```bash
python momentum_calculator.py --top 0
```

### Export to CSV

```bash
python momentum_calculator.py --output results.csv
```

### Use Different Momentum Formulas

List all available formulas:
```bash
python momentum_calculator.py --list-formulas
```

Use a specific formula:
```bash
python momentum_calculator.py --formula cagr --months 12
```

Available formulas:
- `classic`: Price ratio × Market cap (default)
- `log_return`: Log returns × Market cap
- `volatility_adjusted`: Risk-adjusted returns
- `cagr`: Compound annual growth rate
- `weighted`: Volume-weighted momentum
- `max_drawdown`: Drawdown-adjusted momentum
- `percentile`: Price percentile ranking
- `trend_strength`: Trend consistency weighted
- `spmo`: SPMO (Invesco S&P 500 Momentum ETF) methodology

See [CUSTOM_FORMULAS.md](CUSTOM_FORMULAS.md) for details on each formula and how to create your own.

### Replicate SPMO ETF Strategy

To replicate the Invesco S&P 500 Momentum ETF (SPMO) methodology:

```bash
python momentum_calculator.py --formula spmo --months 12 --allocation market_cap_weighted
```

Or with position size limit:

```bash
python momentum_calculator.py --formula spmo --months 12 --allocation market_cap_weighted --max-position 10
```

To match a specific SPMO rebalancing date (SPMO rebalances semi-annually in May and November):

```bash
python momentum_calculator.py --formula spmo --months 12 --end-date 2024-11-30 --allocation market_cap_weighted --max-position 10
```

This uses the same methodology as SPMO:
- 12-month lookback period (excluding most recent month)
- Volatility-adjusted returns (price change / volatility)
- Selects top 100 stocks by momentum score
- Weights holdings by market capitalization (not momentum score)
- Optional position size caps to limit concentration

### Portfolio Allocation

Calculate portfolio allocations based on momentum scores:

List available allocation strategies:
```bash
python momentum_calculator.py --list-allocations
```

Use an allocation strategy:
```bash
python momentum_calculator.py --allocation proportional
```

Cap maximum position size:
```bash
python momentum_calculator.py --allocation proportional --max-position 10
```

This will ensure no single stock gets more than 10% allocation.

Available allocation strategies:
- `proportional`: Allocate proportional to normalized scores
- `equal_weight`: Equal weight to top N stocks
- `tiered`: Different percentages to different tiers
- `inverse_variance`: Inverse variance weighting
- `logarithmic`: Log-based allocation (reduces impact of outliers)
- `threshold`: Only allocate to stocks above a threshold score
- `rank_based`: Weight by rank (top stock gets most weight)
- `market_cap_weighted`: Select top N by momentum, then weight by market cap (SPMO methodology)

### Complete Example

```bash
python momentum_calculator.py \
  --end-date 2024-01-01 \
  --months 12 \
  --top 30 \
  --formula volatility_adjusted \
  --allocation proportional \
  --max-position 8 \
  --output momentum_results.csv
```

This will:
1. Calculate momentum for the past 12 months ending 2024-01-01
2. Use the volatility-adjusted formula
3. Show top 30 stocks
4. Compute portfolio allocation proportional to scores
5. Cap any single position at 8%
6. Save results including allocation percentages to CSV

## Command Line Arguments

| Argument | Description | Default |
|----------|-------------|---------|
| `--end-date` | End date for calculation (YYYY-MM-DD) | Today |
| `--months` | Number of months to look back | 12 |
| `--top` | Number of top stocks to display (0 = all) | 20 |
| `--formula` | Momentum formula to use | `classic` |
| `--list-formulas` | List all available formulas and exit | - |
| `--allocation` | Portfolio allocation strategy to use | None |
| `--max-position` | Maximum allocation % per position | None |
| `--list-allocations` | List all allocation strategies and exit | - |
| `--output` | Save results to CSV file | None |
| `--cache-dir` | Directory for caching data | `.cache` |

## Output Columns

- **Ticker**: Stock symbol
- **StartPrice**: Stock price at start of lookback period
- **EndPrice**: Stock price at end of lookback period (30 days before end date)
- **PriceRatio**: Percentage change in price
- **MarketCap**: Market capitalization at end of period
- **Momentum**: Raw momentum score (PriceRatio × MarketCap)
- **NormalizedScore**: Momentum score normalized to 0-100 range
- **Allocation**: Portfolio allocation percentage (only when --allocation is used)

## Caching

The application caches:
- S&P 500 ticker list (refreshed every 30 days)
- Historical price data (refreshed every 7 days)

Cache files are stored in `.cache/` directory by default.

To force refresh of cache, delete the `.cache/` directory:
```bash
rm -rf .cache
```

## Notes

- First run will take several minutes to download historical data for all 500+ stocks
- Subsequent runs will be much faster due to caching
- Market cap is calculated as: Share Price × Shares Outstanding
- Some stocks may be excluded if data is unavailable for the specified period
- The application uses the current S&P 500 composition (not historical)

## Requirements

- Python 3.8+
- Internet connection (for initial data fetch)

## Example Output

```
================================================================================
TOP MOMENTUM STOCKS (as of 2024-01-01, 12 months lookback)
================================================================================
  Ticker  StartPrice   EndPrice  PriceRatio      MarketCap      Momentum  NormalizedScore
    NVDA      145.23     495.67      2.4123  1.234567e+12  2.977e+12          100.00
    TSLA      180.45     248.92      0.3792  7.890123e+11  2.991e+11           85.32
     AMD       75.12     185.34      1.4675  2.345678e+11  3.442e+11           82.15
...
```
