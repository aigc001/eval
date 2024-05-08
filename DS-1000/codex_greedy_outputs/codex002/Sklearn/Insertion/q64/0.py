
# Create a hierarchical clustering
cluster = sklearn.cluster.AgglomerativeClustering(n_clusters=2, affinity='precomputed', linkage='complete')
# Perform the clustering
labels = cluster.fit_predict(data_matrix)
