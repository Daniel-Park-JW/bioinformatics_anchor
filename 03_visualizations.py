import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import seaborn as sns

# 1. Load the ML-ready data generated on Thursday
X = pd.read_csv('data/ML_ready_X.csv', index_col=0)
y = pd.read_csv('data/ML_ready_y.csv', index_col=0).iloc[:, 0]
stats = pd.read_csv('data/differential_expression_stats.csv', index_col=0)

# 2. Generate a Volcano Plot
# This visualizes the tradeoff between significance (p-value) and effect size (t-statistic)
plt.figure(figsize=(8, 6))
plt.scatter(stats['t_statistic'], -np.log10(stats['p_value']), c=stats['significant'], cmap='coolwarm', alpha=0.5)
plt.title("Volcano Plot: Differential Gene Expression")
plt.xlabel("T-Statistic (Effect Size)")
plt.ylabel("-Log10(p-value)")
plt.savefig('data/volcano_plot.png')
print("✅ Volcano Plot saved to data/volcano_plot.png")

# 3. Generate a PCA Plot
# This reduces the 10,891 dimensions down to 2, proving the data separates well
pca = PCA(n_components=2)
pca_results = pca.fit_transform(X)
pca_df = pd.DataFrame(data=pca_results, columns=['PC1', 'PC2'], index=X.index)
pca_df['label'] = y

plt.figure(figsize=(8, 6))
sns.scatterplot(data=pca_df, x='PC1', y='PC2', hue='label')
plt.title("PCA Plot: Sample Separation")
plt.savefig('data/pca_plot.png')
print("✅ PCA Plot saved to data/pca_plot.png")