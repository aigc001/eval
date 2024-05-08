
    # Create a new array of the desired shape, filled with zeros
    result = np.zeros(shape)

    # Copy the original array into the new array
    result[:arr.shape[0], :arr.shape[1]] = arr

    return result
