
# Use numpy's as_strided function to create a view into the array
# that has the desired shape (2, 2)
patches = np.lib.stride_tricks.as_strided(a, shape=(3, 3, 2, 2), strides=(a.strides[0], a.strides[0], a.strides[1], a.strides[1]))

# Now, we need to reshape the patches to the desired output shape
patches = patches.reshape((9, 2, 2))
