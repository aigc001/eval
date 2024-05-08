
distances = scipy.spatial.distance.cdist(centroids, data, 'euclidean')
result = np.argmin(distances, axis=1)
