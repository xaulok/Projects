import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, recall_score, roc_auc_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
df = pd.read_csv("Telco-Customer-Churn.csv")

print(df.head())
print(df.info())
le = LabelEncoder()

for col in df.select_dtypes(include=['object', 'string']).columns:
    df[col] = le.fit_transform(df[col])
    X = df.drop("Churn", axis=1)
y = df["Churn"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)
# Logistic Regression
log_reg = LogisticRegression(max_iter=1000)
log_reg.fit(X_train, y_train)
y_pred_log_reg = log_reg.predict(X_test)
accuracy_log_reg = accuracy_score(y_test, y_pred_log_reg)
recall_log_reg = recall_score(y_test, y_pred_log_reg)
roc_auc_log_reg = roc_auc_score(y_test, log_reg.predict_proba(X_test)[:, 1])
print(f"Logistic Regression - Accuracy: {accuracy_log_reg:.4f}, Recall: {recall_log_reg:.4f}, ROC AUC: {roc_auc_log_reg:.4f}")


# Random Forest
rf_clf = RandomForestClassifier(n_estimators=100, random_state=42)
rf_clf.fit(X_train, y_train)
y_pred_rf = rf_clf.predict(X_test)
accuracy_rf = accuracy_score(y_test, y_pred_rf)
recall_rf = recall_score(y_test, y_pred_rf)
roc_auc_rf = roc_auc_score(y_test, rf_clf.predict_proba(X_test)[:, 1])
print(f"Random Forest - Accuracy: {accuracy_rf:.4f}, Recall: {recall_rf:.4f}, ROC AUC: {roc_auc_rf:.4f}")    

#xgboost
from xgboost import XGBClassifier
xgb_clf = XGBClassifier(use_label_encoder=False, eval_metric='logloss', random_state=42)
xgb_clf.fit(X_train, y_train)
y_pred_xgb = xgb_clf.predict(X_test)
accuracy_xgb = accuracy_score(y_test, y_pred_xgb)
recall_xgb = recall_score(y_test, y_pred_xgb)
roc_auc_xgb = roc_auc_score(y_test, xgb_clf.predict_proba(X_test)[:, 1])
print(f"XGBoost - Accuracy: {accuracy_xgb:.4f}, Recall: {recall_xgb:.4f}, ROC AUC: {roc_auc_xgb:.4f}")

# Plotting feature importance for Random Forest
importances = rf_clf.feature_importances_
feature_names = X.columns
indices = np.argsort(importances)[::-1]
plt.figure(figsize=(12, 6))
plt.title("Feature Importances - Random Forest")
plt.bar(range(X.shape[1]), importances[indices], align="center")
plt.xticks(range(X.shape[1]), feature_names[indices], rotation=90)
plt.xlim([-1, X.shape[1]])
plt.tight_layout()
plt.show()

# Plotting feature importance for XGBoost
importances_xgb = xgb_clf.feature_importances_
indices_xgb = np.argsort(importances_xgb)[::-1]
plt.figure(figsize=(12, 6))
plt.title("Feature Importances - XGBoost")
plt.bar(range(X.shape[1]), importances_xgb[indices_xgb], align="center")
plt.xticks(range(X.shape[1]), feature_names[indices_xgb], rotation=90)
plt.xlim([-1, X.shape[1]])
plt.tight_layout()
plt.show()

# SHAP values for Random Forest
import shap
explainer_rf = shap.TreeExplainer(rf_clf)
shap_values_rf = explainer_rf.shap_values(X_test)
shap.summary_plot(shap_values_rf[1], X_test, feature_names=feature_names)

# SHAP values for XGBoost
explainer_xgb = shap.TreeExplainer(xgb_clf)
shap_values_xgb = explainer_xgb.shap_values(X_test)
shap.summary_plot(shap_values_xgb, X_test, feature_names=feature_names)


