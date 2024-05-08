
    # Get unique IDs
    unique_ids = np.unique(example_array)
    unique_ids = unique_ids[unique_ids != 0]

    # Create a list to store the coordinates of each unique ID
    coords = []
    for id in unique_ids:
        coords.append(np.argwhere(example_array == id))

    # Calculate pairwise distances
    distances = scipy.spatial.distance.cdist(coords, coords, 'euclidean')

    return distances
