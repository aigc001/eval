
km.fit(X)
centers = km.cluster_centers_
distances = np.linalg.norm(X[:, np.newaxis] - centers, axis=2)
p_th_center_index = np.argsort(distances, axis=0)[p]
p_th_center_data = X[p_th_center_index]
closest_samples_indices = np.argsort(distances[:, p_th_center_index])[:50]
closest_samples = X[closest_samples_indices]
