
    # Find the index of the maximum value in the flattened array
    max_index = np.argmax(a.ravel())

    # Convert the index back to the shape of the original array
    max_position = np.unravel_index(max_index, a.shape)

    return max_position
