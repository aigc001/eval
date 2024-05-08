
# Convert the data matrix to a condensed form distance matrix
dist_matrix = scipy.spatial.distance.pdist(data_matrix, metric='euclidean')

# Perform hierarchical clustering
Z = scipy.cluster.hierarchy.linkage(dist_matrix, method='ward')

# Cut the dendrogram to obtain the desired number of clusters
clusters = scipy.cluster.hierarchy.fcluster(Z, t=2, criterion='maxclust')

# Create a list of labels
labels = list(clusters)
