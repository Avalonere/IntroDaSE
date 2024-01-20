import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor

# read data
data = pd.read_csv("./train_data/train.csv")

# correlation
corr = data.corr()
corr = corr[["Demand"]]
corr = corr.drop("Demand")
corr = corr.apply(lambda x: abs(x))
corr = corr.sort_values("Demand", ascending=False)
sns.heatmap(
    data.corr(),
    cmap="coolwarm",
    xticklabels=1,
    yticklabels=1,
    linewidths=0.5,
)
plt.xticks(rotation=90, fontsize=6)
plt.yticks(rotation=0, fontsize=6)
plt.title("Feature Correlation Heatmap")
plt.tight_layout()
plt.savefig("./plot/feature_heatmap.png")
plt.show()


# Random forest
y = data["Demand"]
X = data.drop("Demand", axis=1)
rf = RandomForestRegressor()
rf.fit(X, y)
feature_importances = rf.feature_importances_
plt.barh(X.columns, feature_importances)
plt.xlabel("Importance")
plt.ylabel("Feature")
plt.title("Feature Importance for Demand")
plt.tight_layout()
plt.savefig("./plot/feature_importance.png")
plt.show()
