
# Get the mse values
mse_values = df['mse'].values

# Reshape the mse values to a 2D array
mse_values = mse_values.reshape(-1, 1)

# Fit the KMeans model
kmeans = KMeans(n_clusters=2).fit(mse_values)

# Get the labels
labels = kmeans.labels_

# Get the centroids
centroids = kmeans.cluster_centers_

# Print the centroids
print(centroids)
