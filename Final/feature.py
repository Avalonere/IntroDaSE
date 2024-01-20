# 导入所需的库
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler

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


# PCA
# 提取目标变量
target_variable = "Demand"
y = data[target_variable]

# 提取特征变量
X = data.drop(target_variable, axis=1)

# 标准化数据
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 使用PCA进行降维
pca = PCA()
X_pca = pca.fit_transform(X_scaled)

# 查看每个主成分的方差解释比例
explained_variance_ratio = pca.explained_variance_ratio_
cumulative_explained_variance = explained_variance_ratio.cumsum()

# 输出每个主成分的方差解释比例
print("Explained Variance Ratio:")
print(explained_variance_ratio)

# 输出累积方差解释比例
print("\nCumulative Explained Variance:")
print(cumulative_explained_variance)

# 绘制累积方差解释比例曲线
plt.plot(
    range(1, len(cumulative_explained_variance) + 1),
    cumulative_explained_variance,
    marker="o",
)
plt.xlabel("Number of Principal Components")
plt.ylabel("Cumulative Explained Variance")
plt.title("Cumulative Explained Variance vs. Number of Principal Components")
plt.show()

# 使用matplotlib展示目标变量在主成分上的分布
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap="viridis", edgecolors="k", alpha=0.7)
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title(f"Distribution of {target_variable} on Principal Components")
plt.colorbar(label=target_variable)
plt.show()
