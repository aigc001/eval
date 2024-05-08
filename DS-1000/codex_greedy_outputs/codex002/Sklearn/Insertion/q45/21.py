
km.fit(X)
centers = km.cluster_centers_
distances = np.linalg.norm(X[:, None] - centers, axis=-1)
closest_samples = np.argsort(distances, axis=0)[p]
closest_samples_data = X[closest_samples]
