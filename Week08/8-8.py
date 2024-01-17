# 导入所需的库
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer

# 加载乳腺癌数据集
cancer = load_breast_cancer()
# 将数据转换为pandas数据框
df = pd.DataFrame(cancer.data, columns=cancer.feature_names)
# 添加目标列，0表示恶性，1表示良性
df["target"] = cancer.target

# 绘制第一种图表：箱线图
# 选择四个特征作为示例
features = ["mean radius", "mean texture", "mean perimeter", "mean area"]
# 按目标分组绘制箱线图，比较不同类别的特征分布
sns.boxplot(
    x="target", y="value", data=pd.melt(df, id_vars="target", value_vars=features)
)
# 添加标题和坐标轴标签
plt.title("Boxplot of features by target")
plt.xlabel("Target")
plt.ylabel("Value")
# 显示图表
plt.show()

# 绘制第二种图表：小提琴图
# 选择四个特征作为示例
features = [
    "mean smoothness",
    "mean compactness",
    "mean concavity",
    "mean concave points",
]
# 按目标分组绘制小提琴图，比较不同类别的特征分布
sns.violinplot(
    x="target", y="value", data=pd.melt(df, id_vars="target", value_vars=features)
)
# 添加标题和坐标轴标签
plt.title("Violinplot of features by target")
plt.xlabel("Target")
plt.ylabel("Value")
# 显示图表
plt.show()

# 绘制第三种图表：热力图
# 计算所有特征之间的相关系数矩阵
corr = df.corr()
# 绘制热力图，显示相关系数的大小和方向
sns.heatmap(corr, cmap="coolwarm")
# 添加标题
plt.title("Heatmap of feature correlations")
# 显示图表
plt.show()
