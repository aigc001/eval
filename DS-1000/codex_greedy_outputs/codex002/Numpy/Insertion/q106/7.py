
    # Generate n random numbers in the range 0 to 1
    x = np.random.uniform(0, 1, n)

    # Take the logarithm of the random numbers to get logarithmically distributed numbers
    y = np.log(x)

    # Scale the logarithmically distributed numbers to the desired range
    y = y * (max - min) + min

    # Return the logarithmically distributed numbers
    return y
