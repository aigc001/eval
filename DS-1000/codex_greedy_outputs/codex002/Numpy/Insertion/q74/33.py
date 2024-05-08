
    # Create a new array with the desired size
    new_a = np.zeros(a.size + 1, dtype=a.dtype)

    # Copy the elements before the insert position
    new_a[:pos] = a[:pos]

    # Insert the new element
    new_a[pos] = element

    # Copy the elements after the insert position
    new_a[pos+1:] = a[pos:]

    return new_a
