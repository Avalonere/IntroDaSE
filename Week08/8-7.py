# 导入所需的库
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.linear_model import RidgeCV

# 加载糖尿病数据集
diabetes = load_diabetes()
X, y = diabetes.data, diabetes.target
feature_names = diabetes.feature_names

# 绘制散点图
plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], y, color="b", label="Data points")
plt.xlabel("Age")
plt.ylabel("Diabetes progression")
plt.title("Scatter plot of age and diabetes progression")
plt.legend()
plt.show()

# 使用岭回归模型计算每个特征的系数
ridge = RidgeCV(alphas=np.logspace(-6, 6, num=5)).fit(X, y)
coef = np.abs(ridge.coef_)

# 绘制柱状图
plt.figure(figsize=(8, 6))
plt.bar(feature_names, coef, color="g", label="Feature coefficients")
plt.xlabel("Features")
plt.ylabel("Absolute coefficient")
plt.title("Bar plot of feature importance")
plt.legend()
plt.show()

# 绘制箱线图
plt.figure(figsize=(8, 6))
plt.boxplot(X, labels=feature_names)
plt.xlabel("Features")
plt.ylabel("Values")
plt.title("Box plot of feature distribution")
plt.show()
