# 📊 Stock Price Fluctuation

> Analysing historical volatility, return distributions, and price momentum in equity markets.

---

## 📌 Objective

Understanding how and why stock prices move is foundational to equity research, risk management, and trading strategies. This project analyses **historical stock price data** across selected equities to characterise return distributions, measure volatility clustering, and visualise drawdown behaviour — the kind of analysis done in S&T desks and quant research teams.

---

## 🛠️ Tools & Libraries

| Category | Tools |
|----------|-------|
| Language | Python 3.x |
| Data | yfinance (Yahoo Finance API), pandas, NumPy |
| Statistical Analysis | scipy.stats, statsmodels |
| Visualisation | matplotlib, seaborn |

---

## 📁 Project Structure

```
Stock Price Fluctuation/
│
├── Datasets/                       # Historical OHLCV data
├── Stock_Price_Fluctuation.py      # Main analysis script
└── README.md
```

---

## 🔍 Analysis Framework

**1. Price & Return Analysis**
- Adjusted closing prices (dividend and split corrected)
- Daily simple returns and log returns
- Cumulative return comparison across tickers

**2. Volatility Analysis**
- Rolling 30-day and 90-day annualised volatility
- Volatility clustering visualisation (GARCH-like patterns)
- Historical volatility vs. implied volatility comparison (where available)

**3. Return Distribution**
- Histogram with normal distribution overlay
- Skewness and excess kurtosis (fat tails test)
- Jarque-Bera normality test

**4. Risk Metrics**
- Maximum Drawdown and drawdown duration
- Rolling Sharpe Ratio (annualised)
- VaR (Value at Risk) at 95% and 99% confidence levels (historical method)

**5. Correlation & Beta**
- Pairwise return correlation heatmap
- Rolling beta against a benchmark index (e.g. Nifty 50 / S&P 500)

---

## 📊 Key Findings

- Return distributions showed **negative skewness** and **excess kurtosis** — consistent with the empirical observation that equity returns have fat tails
- Volatility clustering evident: periods of high volatility (earnings, macro events) followed by sustained high-vol regimes
- Maximum drawdown analysis highlighted the asymmetry between loss accumulation and recovery periods

---

## 🚀 How to Run

```bash
pip install yfinance pandas numpy matplotlib seaborn scipy statsmodels

python Stock_Price_Fluctuation.py
```

Edit the `tickers` and `start_date` / `end_date` variables to change the analysis universe.

---

## 💡 Extensions & Next Steps

- [ ] Fit a **GARCH(1,1)** model to formally model volatility clustering
- [ ] Build a momentum factor backtest (12-1 month momentum strategy)
- [ ] Add Bollinger Bands and RSI as technical overlays
- [ ] Extend to an **event study** framework around earnings announcements
- [ ] Cross-asset analysis: equity vs. INR/USD FX vs. bond yields

---

*Part of [xaulok/Projects](https://github.com/xaulok/Projects) · B.Sc Economics, CUAP '27*
