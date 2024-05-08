
# Convert the similarity matrix to a condensed form
distM = scipy.spatial.distance.squareform(1 - simM)

# Perform hierarchical clustering
Z = scipy.cluster.hierarchy.linkage(distM, method='ward')

# Cut the dendrogram to obtain the desired number of clusters
clusters = scipy.cluster.hierarchy.fcluster(Z, t=2, criterion='maxclust')

# Create a list of labels
labels = [''] * len(clusters)
for i, cluster in enumerate(clusters):
    labels[i] = 'Cluster' + str(cluster)
