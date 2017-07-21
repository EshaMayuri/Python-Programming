import numpy as np
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt

X = np.array([[1,1],[1.1,1.1],[3,3],[4,4],[3,3.5], [3.5,4]])
plt.scatter(X[:,0], X[:,1], s=50)

linkage_matrix = linkage(X, "single")
dendogram = dendrogram(linkage_matrix, truncate_mode='none')
plt.title("Hierarchical clustering")
plt.show()

















# Hierarchical clustering a method of clustering which builds a hierarchy of clusters.
# It combines all the clusters into a single Cluster based on distances between the centroids of the clusters.
# Single-linkage clustering is one of the type of hierarchical clustering.
# It is based on grouping clusters in bottom-up fashion, at each step it combining two clusters that contains the closest pair of elements.
