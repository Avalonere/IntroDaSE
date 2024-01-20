import matplotlib.pyplot as plt
import pandas as pd
from sklearn.decomposition import PCA

# 读取CSV文件
file_path = "./train_data/train.csv"
data = pd.read_csv(file_path)

# 选择特征列（去除目标列）
features = data.drop("Demand", axis=1)

# 使用PCA进行降维
pca = PCA(n_components=2)  # 选择降维到2维
principal_components = pca.fit_transform(features)

# 将降维后的数据和目标列合并
pca_df = pd.DataFrame(data=principal_components, columns=["PC1", "PC2"])
pca_df["Demand"] = data["Demand"]

# 绘制散点图
plt.scatter(
    pca_df["PC1"],
    pca_df["PC2"],
    c=pca_df["Demand"],
    cmap="viridis",
    edgecolors="k",
    alpha=0.7,
)
plt.title("PCA of Demand with 2 Components")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.colorbar(label="Demand")
plt.show()
