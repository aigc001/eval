
# Convert the data matrix to a condensed form distance matrix
dist_matrix = scipy.spatial.distance.squareform(data_matrix)

# Perform hierarchical clustering
cluster = sklearn.cluster.AgglomerativeClustering(n_clusters=2, affinity='precomputed', linkage='complete')
labels = cluster.fit_predict(dist_matrix)

# Return the labels
return labels
