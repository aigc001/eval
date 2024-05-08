
# Use np.isnan to find the nan values and ~ to invert the result
x = x[~np.isnan(x)]
# Reshape the result into a list of lists
x = x.tolist()
