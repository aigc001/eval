
# Create a function that will interpolate over the first axis of the array
def interpolate_along_axis(array, x, x_new):
    # Create an empty array to hold the result
    new_array = np.zeros((len(x_new),) + array.shape[1:])
    
    # Iterate over the other axes of the array
    for i in range(array.shape[1]):
        for j in range(array.shape[2]):
            # Interpolate the values along the first axis
            new_array[:, i, j] = scipy.interpolate.interp1d(x, array[:, i, j])(x_new)
    
    return new_array

new_array = interpolate_along_axis(array, x, x_new)
