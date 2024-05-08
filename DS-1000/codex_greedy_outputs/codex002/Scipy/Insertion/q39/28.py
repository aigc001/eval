
# Get unique IDs
unique_ids = np.unique(example_array)
# Create a list of centroid coordinates for each unique ID
centroids = []
for id in unique_ids:
    # Get the coordinates of the pixels for the current ID
    id_coords = np.argwhere(example_array == id)
    # Calculate the centroid coordinates
    centroid = np.mean(id_coords, axis=0)
    centroids.append(centroid)
# Convert the list of centroids to a numpy array
centroids = np.array(centroids)
# Calculate the pairwise Manhattan distances
distances = scipy.spatial.distance.cdist(centroids, centroids, 'cityblock')
# Create a list of distances with corresponding IDs
dist_list = []
for i in range(distances.shape[0]):
    for j in range(distances.shape[1]):
        dist_list.append([unique_ids[i], unique_ids[j], distances[i, j]])
# Convert the list of distances to a numpy array
dist_array = np.array(dist_list)
