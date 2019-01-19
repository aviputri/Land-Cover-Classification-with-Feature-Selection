from sklearn.cluster import SpectralClustering
import numpy as np

X = np.array([[1, 1], [2, 1], [1, 0],[4, 7], [3, 5], [3, 6]])

clustering = SpectralClustering(n_clusters=2, assign_labels="discretize", random_state=0).fit(X)

clustering.labels_