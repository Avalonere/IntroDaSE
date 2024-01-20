import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

# 读取CSV文件
data = pd.read_csv("./train_data/train.csv")

# 标准化数据
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

# 执行KMeans聚类并计算每个聚类数量的成本
cost = []
silhouette_scores = []

for num_clusters in range(2, 10):
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    kmeans.fit(scaled_data)

    # 计算每个数据点到其聚类中心的距离平方和（成本）
    cost.append(kmeans.inertia_)

    # 计算轮廓系数
    silhouette_avg = silhouette_score(scaled_data, kmeans.labels_)
    silhouette_scores.append(silhouette_avg)

# 绘制手肘法图
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(range(2, 10), cost, marker="o")
plt.title("Elbow Method for Optimal k")
plt.xlabel("Number of Clusters")
plt.ylabel("Cost")

# 绘制轮廓系数图
plt.subplot(1, 2, 2)
plt.plot(range(2, 10), silhouette_scores, marker="o")
plt.title("Silhouette Score for Optimal k")
plt.xlabel("Number of Clusters")
plt.ylabel("Silhouette Score")

plt.tight_layout()
plt.show()

n_clusters = 5
kmeans = KMeans(n_clusters=n_clusters)

clusters = kmeans.fit_predict(data)

plt.scatter(data.iloc[:, 0], data.iloc[:, 4], c=clusters, cmap="rainbow")
plt.title("KMeans Clustering")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()
