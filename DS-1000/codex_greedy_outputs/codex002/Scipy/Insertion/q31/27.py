
    # Make a copy of the sparse matrix
    sA_copy = sA.copy()

    # Iterate over the rows and columns
    for i in range(sA.shape[0]):
        for j in range(sA.shape[1]):
            # If the element at [i, j] is not zero
            if sA[i, j] != 0:
                # Set the corresponding element at [j, i] to be the same
                sA_copy[j, i] = sA[i, j]

    # Return the symmetric sparse matrix
    return sA_copy
