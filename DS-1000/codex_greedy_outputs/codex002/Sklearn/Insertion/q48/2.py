
    # Fit the KMeans model
    km.fit(X)
    # Get the cluster centers
    centers = km.cluster_centers_
    # Get the predicted labels for each sample
    labels = km.labels_
    # Get the indices of the samples that belong to the p-th cluster
    p_cluster_indices = np.where(labels == p)[0]
    # Get the p-th cluster center
    p_center = centers[p]
    # Compute the distances from the p-th cluster center to all samples
    distances = np.linalg.norm(X - p_center, axis=1)
    # Get the indices of the 50 samples closest to the p-th cluster center
    closest_indices = np.argsort(distances)[:50]
    # Return the 50 closest samples
    return X[closest_indices]
