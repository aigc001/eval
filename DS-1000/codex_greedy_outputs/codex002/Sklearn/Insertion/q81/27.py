
# Extract the mse values
mse = df['mse'].values

# Create an array of indices
indices = np.array(range(len(mse)))

# Combine the mse values and their indices into a 2D array
X = np.array(list(zip(mse, indices)))

# Fit the KMeans model
kmeans = KMeans(n_clusters=2).fit(X)

# Get the labels for each data point
labels = kmeans.predict(X)

# Get the centroids of the clusters
centroids = kmeans.cluster_centers_

# Print the centroids and their corresponding labels
for i, centroid in enumerate(centroids):
    print(f"Cluster {i + 1}: Mean MSE = {centroid[0]}, Index = {int(centroid[1])}")
