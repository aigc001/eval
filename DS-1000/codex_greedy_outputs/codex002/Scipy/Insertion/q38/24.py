
# Get unique IDs
unique_ids = np.unique(example_array)
# Create a list of centroid coordinates for each unique ID
centroids = []
for id in unique_ids:
    # Get the indices of all pixels with this ID
    indices = np.where(example_array == id)
    # Calculate the centroid of these pixels
    centroid = np.mean(indices, axis=1)
    centroids.append(centroid)
# Convert the list of centroids to a numpy array
centroids = np.array(centroids)
# Calculate the pairwise distances between all centroids
distances = scipy.spatial.distance.cdist(centroids, centroids)
# Print the distances
print(distances)
