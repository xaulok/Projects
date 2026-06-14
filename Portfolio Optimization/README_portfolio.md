# 📈 Portfolio Optimization

> Constructing the efficient frontier using Modern Portfolio Theory — maximising return per unit of risk.

---

## 📌 Objective

This project implements **Harry Markowitz's Mean-Variance Optimization** framework to construct optimal equity portfolios. Given a universe of assets, the model identifies the **efficient frontier** — the set of portfolios that offer the highest expected return for a given level of risk — and locates the **Maximum Sharpe Ratio** and **Minimum Volatility** portfolios.

---

## 🛠️ Tools & Libraries

| Category | Tools |
|----------|-------|
| Language | Python 3.x |
| Optimisation | scipy.optimize (SLSQP), NumPy |
| Data | yfinance (historical price data), pandas |
| Visualisation | matplotlib (efficient frontier plot, Sharpe heatmap) |

---

## 📁 Project Structure

```
Portfolio Optimization/
│
├── Datasets/                   # Historical price data
├── Portfolio_Optimization.py   # Main optimisation script
└── README.md
```

---

## 🔍 Methodology

1. **Data Collection** — Download 3–5 years of daily adjusted closing prices via `yfinance`
2. **Returns Calculation** — Daily log returns → annualised mean return and covariance matrix
3. **Monte Carlo Simulation** — Generate 10,000 random portfolios to map the opportunity set
4. **Efficient Frontier** — SciPy optimiser traces the frontier by minimising variance for each target return
5. **Optimal Portfolios** — Identify max Sharpe ratio portfolio and minimum variance portfolio
6. **Visualisation** — Colour-mapped scatter plot (Sharpe ratio heat) with frontier overlay

---

## 📊 Key Outputs

- **Efficient Frontier Plot** — Visual of the risk-return tradeoff across all feasible portfolios
- **Maximum Sharpe Portfolio** — Weights, expected return, volatility, and Sharpe ratio
- **Minimum Volatility Portfolio** — Lowest-risk allocation across the asset universe

Example results (hypothetical 5-stock portfolio):

| Portfolio | Return (Ann.) | Volatility (Ann.) | Sharpe Ratio |
|-----------|--------------|-------------------|--------------|
| Max Sharpe | ~18.2% | ~14.1% | ~1.29 |
| Min Vol | ~12.6% | ~10.3% | ~1.22 |

---

## 🚀 How to Run

```bash
pip install numpy pandas scipy matplotlib yfinance

python Portfolio_Optimization.py
```

Edit the `tickers` list in the script to change the asset universe.

---

## 💡 Extensions & Next Steps

- [ ] Add **Black-Litterman model** to incorporate investor views
- [ ] Implement **CVaR (Conditional Value at Risk)** as a risk metric alongside variance
- [ ] Factor exposure analysis (Fama-French 3-factor model)
- [ ] Backtesting the optimal portfolio against a benchmark index
- [ ] Rebalancing simulation with transaction costs

---

*Part of [xaulok/Projects](https://github.com/xaulok/Projects) · B.Sc Economics, CUAP '27*
