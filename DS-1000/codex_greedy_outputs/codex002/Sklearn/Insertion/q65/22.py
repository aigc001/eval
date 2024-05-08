
# Convert the similarity matrix to a distance matrix
distM = 1 - simM
# Perform hierarchical clustering
cluster = sklearn.cluster.AgglomerativeClustering(n_clusters=2, affinity='precomputed', linkage='complete')
labels = cluster.fit_predict(distM)
