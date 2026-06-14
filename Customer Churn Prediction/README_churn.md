# 📉 Customer Churn Prediction

> Identifying customers likely to leave — before they do. A binary classification problem with real business stakes.

---

## 📌 Objective

Customer churn (attrition) costs companies significantly more than retaining existing customers. This project builds a **churn prediction model** on a telecom dataset, identifying at-risk customers so targeted retention strategies can be deployed. The analysis focuses on both **predictive accuracy** and **business interpretability**.

---

## 🛠️ Tools & Libraries

| Category | Tools |
|----------|-------|
| Language | Python 3.x |
| ML Models | scikit-learn (Logistic Regression, Decision Tree, Random Forest) |
| Imbalance Handling | imbalanced-learn (SMOTE) |
| Data | pandas, NumPy |
| Visualisation | matplotlib, seaborn |

---

## 📁 Project Structure

```
Customer Churn Prediction/
│
├── Datasets/               # Telecom customer dataset
├── Churn_Prediction.py     # Main modelling script
└── README.md
```

---

## 🔍 Methodology

1. **EDA** — Churn rate breakdown, feature distributions by churn status
2. **Class Imbalance** — Dataset typically ~80% non-churn; handled using **SMOTE** oversampling
3. **Feature Engineering** — Tenure buckets, contract type encoding, usage aggregates
4. **Modelling** — Logistic Regression → Decision Tree → Random Forest
5. **Evaluation** — F1-score (prioritised over accuracy due to class imbalance), Precision-Recall AUC

---

## 📊 Key Results

| Model | F1-Score | Recall (Churn) |
|-------|----------|----------------|
| Logistic Regression | ~0.74 | ~71% |
| Decision Tree | ~0.78 | ~76% |
| Random Forest | ~0.82 | ~79% |

**Top churn drivers:**
- Month-to-month contract type
- Tenure < 12 months
- High monthly charges with no add-on services
- No online security / tech support subscription

---

## 🚀 How to Run

```bash
pip install scikit-learn imbalanced-learn pandas matplotlib seaborn

python Churn_Prediction.py
```

---

## 💡 Extensions & Next Steps

- [ ] Deploy as a Flask API for real-time churn scoring
- [ ] Build a Tableau dashboard for the churn risk distribution
- [ ] Add CLV (Customer Lifetime Value) to prioritise which churners to target
- [ ] Experiment with XGBoost and LightGBM for performance gains

---

*Part of [xaulok/Projects](https://github.com/xaulok/Projects) · B.Sc Economics, CUAP '27*
