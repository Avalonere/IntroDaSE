import matplotlib.pyplot as plt
import pandas as pd
from sklearn.decomposition import PCA

df = pd.read_csv("./train_data/train_all.csv")

target_variable = "Demand"
X = df.drop(target_variable, axis=1)
y = df[target_variable]

pca = PCA()
X_pca = pca.fit_transform(X)

explained_variance_ratio = pca.explained_variance_ratio_

plt.bar(
    range(1, len(explained_variance_ratio) + 1),
    explained_variance_ratio,
    alpha=0.5,
    align="center",
)
plt.step(
    range(1, len(explained_variance_ratio) + 1),
    explained_variance_ratio.cumsum(),
    where="mid",
)
plt.xlabel("Principal Components")
plt.ylabel("Explained Variance Ratio")
plt.title("PCA Evaluation")
plt.savefig("./plot/pca_evaluation.png")
plt.show()

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

pca_df = pd.DataFrame(
    data=X_pca, columns=["Principal Component 1", "Principal Component 2"]
)
pca_df.insert(0, target_variable, y)

plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap="viridis")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("PCA Analysis")
plt.colorbar(label=target_variable)
plt.savefig("./plot/pca_result.png")
plt.show()

pca_df.to_csv("./train_data/pca.csv", index=False)
