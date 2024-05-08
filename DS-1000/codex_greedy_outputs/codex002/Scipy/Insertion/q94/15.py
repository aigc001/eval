
distances = scipy.spatial.distance.cdist(centroids, data)
result = np.argsort(distances, axis=1)[:, k]
