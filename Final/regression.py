import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

# Selected features
data = pd.read_csv("./train_data/train.csv")

X = data[
    [
        "Life_Expectancy_M",
        "SLE",
        "Population",
        "GDP",
        "Honey",
    ]
]

y = data["Demand"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

plt.scatter(y_test, y_pred)
plt.title(f"Linear Regression - MSE: {mse:.4f}, R2 Score: {r2:.4f}")
plt.xlabel("True Values")
plt.ylabel("Predictions")
plt.savefig("./plot/regression.png")
plt.show()

new_data = pd.read_csv("./year_data/normalized/2022.csv")

X_new = new_data[
    [
        "Life_Expectancy_M",
        "SLE",
        "Population",
        "GDP",
        "Honey",
    ]
]

y_pred_new = model.predict(X_new)

new_data["Predicted_Demand"] = y_pred_new

new_data["Discrepancy"] = new_data["Predicted_Demand"] - new_data["Demand"]

plt.figure(figsize=(12, 8))
x_values = np.arange(len(new_data))

bar_width = 0.35
plt.bar(
    x_values - bar_width / 2,
    new_data["Demand"],
    width=bar_width,
    label="Actual",
    color="blue",
)
plt.bar(
    x_values + bar_width / 2,
    new_data["Predicted_Demand"],
    width=bar_width,
    label="Predicted",
    color="orange",
)

plt.xlabel("Data Points")
plt.ylabel("Demand")
plt.title("Actual vs Predicted Demand with Discrepancy")
plt.xticks(x_values, new_data.index)
plt.legend()

plt.twinx()
plt.plot(
    x_values,
    new_data["Discrepancy"],
    color="red",
    marker="o",
    label="Discrepancy",
)
plt.ylabel("Discrepancy")

plt.legend(loc="upper left")
plt.savefig("./plot/prediction.png")
plt.show()

# PCA

data_pca = pd.read_csv("./train_data/pca.csv")
data = data.drop(data.tail(31).index)  # drop 2022 data

X = data[["Principal Component 1", "Principal Component 2"]]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

plt.scatter(y_test, y_pred)
plt.title(f"Linear Regression - MSE: {mse:.4f}, R2 Score: {r2:.4f}")
plt.xlabel("True Values")
plt.ylabel("Predictions")
plt.savefig("./plot/regression.png")
plt.show()

new_data = pd.read_csv("./year_data/normalized/2022.csv")

X_new = new_data[
    [
        "Life_Expectancy_M",
        "SLE",
        "Population",
        "GDP",
        "Honey",
    ]
]

y_pred_new = model.predict(X_new)

new_data["Predicted_Demand"] = y_pred_new

new_data["Discrepancy"] = new_data["Predicted_Demand"] - new_data["Demand"]

plt.figure(figsize=(12, 8))
x_values = np.arange(len(new_data))

bar_width = 0.35
plt.bar(
    x_values - bar_width / 2,
    new_data["Demand"],
    width=bar_width,
    label="Actual",
    color="blue",
)
plt.bar(
    x_values + bar_width / 2,
    new_data["Predicted_Demand"],
    width=bar_width,
    label="Predicted",
    color="orange",
)

plt.xlabel("Data Points")
plt.ylabel("Demand")
plt.title("Actual vs Predicted Demand with Discrepancy")
plt.xticks(x_values, new_data.index)
plt.legend()

plt.twinx()
plt.plot(
    x_values,
    new_data["Discrepancy"],
    color="red",
    marker="o",
    label="Discrepancy",
)
plt.ylabel("Discrepancy")

plt.legend(loc="upper left")
plt.savefig("./plot/prediction.png")
plt.show()
