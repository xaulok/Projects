# 🔮 Sales Forecasting

> Applying the Box-Jenkins methodology to forecast time series data — econometrics in practice.

---

## 📌 Objective

Accurate sales forecasting is critical for inventory planning, cash flow management, and strategic decision-making. This project applies **ARIMA/SARIMA** modelling using the **Box-Jenkins methodology** to forecast monthly sales, following rigorous stationarity testing and model selection procedures — the same framework used in applied econometrics and quantitative finance.

---

## 🛠️ Tools & Libraries

| Category | Tools |
|----------|-------|
| Language | Python 3.x |
| Time Series | statsmodels (ARIMA, SARIMAX, ACF/PACF) |
| Statistical Tests | ADF test, KPSS test, Ljung-Box test |
| Data | pandas, NumPy |
| Visualisation | matplotlib, seaborn |

---

## 📁 Project Structure

```
Sales Forecasting/
│
├── Datasets/               # Historical monthly sales data
├── Sales_Forecast.py       # Main forecasting script
└── README.md
```

---

## 🔍 Methodology (Box-Jenkins)

**Step 1 — Identification**
- Plot time series; visually inspect for trend and seasonality
- ADF and KPSS unit root tests to check stationarity
- Difference the series if non-stationary (d = 1 or 2)
- ACF and PACF correlograms to identify candidate p, q orders

**Step 2 — Estimation**
- Fit ARIMA(p, d, q) models
- Use AIC/BIC for model selection
- If seasonality present → extend to SARIMA(p,d,q)(P,D,Q)[s]

**Step 3 — Diagnostic Checking**
- Ljung-Box test on residuals (test for autocorrelation)
- Residual plots — normality, homoscedasticity
- ACF of residuals should resemble white noise

**Step 4 — Forecasting**
- Generate h-step ahead point forecasts with 95% confidence intervals
- Evaluate on hold-out test set using MAE, RMSE, MAPE

---

## 📊 Key Results

| Metric | Value |
|--------|-------|
| Best Model | SARIMA(1,1,1)(1,1,1)[12] |
| RMSE (test set) | ~[value] |
| MAPE | ~[value]% |
| Ljung-Box p-value | > 0.05 (residuals are white noise ✓) |

---

## 🚀 How to Run

```bash
pip install statsmodels pandas matplotlib seaborn scipy

python Sales_Forecast.py
```

---

## 💡 Extensions & Next Steps

- [ ] Compare ARIMA with **Prophet** (Facebook) and **ETS** models
- [ ] Add exogenous regressors (SARIMAX) — promotions, holidays, macro indicators
- [ ] Implement a **VAR model** for multivariate sales-inventory-price forecasting
- [ ] Build a Tableau dashboard for interactive forecast visualisation

---

*Part of [xaulok/Projects](https://github.com/xaulok/Projects) · B.Sc Economics, CUAP '27*
