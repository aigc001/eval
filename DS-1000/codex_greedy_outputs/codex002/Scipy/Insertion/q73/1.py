
    # Create a meshgrid of the coordinates
    y, x = np.mgrid[0:shape[0], 0:shape[1]]

    # Calculate the midpoint
    mid = np.array([shape[0]//2, shape[1]//2])

    # Calculate the distances
    distances = distance.cdist(np.column_stack((y.ravel(), x.ravel())), mid[None, :])

    # Reshape the distances to the original shape
    distances = distances.reshape(shape)

    return distances
