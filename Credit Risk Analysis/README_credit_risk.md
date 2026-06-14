# 💳 Credit Risk Analysis

> Predicting loan default probability using machine learning — a core problem in banking and risk management.

---

## 📌 Objective

Credit risk assessment is fundamental to lending institutions. This project models the **probability of default (PD)** for loan applicants using historical lending data, replicating the kind of scoring models used by banks and credit agencies. The goal is to identify high-risk borrowers before credit is extended.

---

## 🛠️ Tools & Libraries

| Category | Tools |
|----------|-------|
| Language | Python 3.x |
| ML Models | scikit-learn (Logistic Regression, Random Forest, XGBoost) |
| Data | pandas, NumPy |
| Visualisation | matplotlib, seaborn |
| Evaluation | ROC-AUC, Confusion Matrix, Precision-Recall |

---

## 📁 Project Structure

```
Credit Risk Analysis/
│
├── Datasets/               # Lending dataset (raw + processed)
├── Credit_Risk.py          # Main modelling script
└── README.md
```

---

## 🔍 Methodology

1. **EDA** — Distribution of defaults, correlation heatmap, missing value treatment
2. **Feature Engineering** — Debt-to-income ratio, credit utilisation, delinquency flags
3. **Preprocessing** — Label encoding, StandardScaler, train/test split (80/20)
4. **Modelling** — Logistic Regression (baseline) → Random Forest → XGBoost
5. **Evaluation** — ROC-AUC curve, Gini coefficient, KS statistic

---

## 📊 Key Results

| Model | ROC-AUC | Accuracy |
|-------|---------|----------|
| Logistic Regression | ~0.78 | ~80% |
| Random Forest | ~0.84 | ~83% |
| XGBoost | ~0.87 | ~85% |

- **Top predictors:** Payment history, credit utilisation ratio, number of derogatory marks
- XGBoost showed the best discrimination between defaulters and non-defaulters

---

## 🚀 How to Run

```bash
pip install scikit-learn xgboost pandas matplotlib seaborn

python Credit_Risk.py
```

---

## 💡 Extensions & Next Steps

- [ ] Implement SHAP values for model explainability (regulatory compliance angle)
- [ ] Scorecard development using Weight of Evidence (WoE) and Information Value (IV)
- [ ] Stress-test the model under macroeconomic shock scenarios
- [ ] Add LGD (Loss Given Default) and EAD (Exposure at Default) modelling

---

*Part of [xaulok/Projects](https://github.com/xaulok/Projects) · B.Sc Economics, CUAP '27*
