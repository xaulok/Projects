library(data.table)
library(caret)
library(randomForest)
library(xgboost)

dt <- fread("Telco-Customer-Churn.csv")

dt$TotalCharges <- as.numeric(dt$TotalCharges)
dt <- na.omit(dt)

#Converting Target
dt$Churn <- as.factor(dt$Churn)

# Train-Test Split
dt$customerID <- NULL
set.seed(123)
train_index <- createDataPartition(
  dt$Churn,
  p = 0.8,
  list = FALSE
)
train <- dt[train_index]
test <- dt[-train_index]


# Logistic Regression
model_lr <- glm(
  Churn ~ .,
  data = train,
  family = binomial
)
pred_prob <- predict(
  model_lr,
  test,
  type = "response"
)
pred <- ifelse(pred_prob > 0.5,
               "Yes","No")
confusionMatrix(
  as.factor(pred),
  test$Churn
)

train <- na.omit(train)
test <- na.omit(test)
# Random Forest
rf_model <- randomForest(
  Churn ~ .,
  data = train,
  ntree = 200
)
rf_pred <- predict(
  rf_model,
  test
)
confusionMatrix(
  rf_pred,
  test$Churn
)