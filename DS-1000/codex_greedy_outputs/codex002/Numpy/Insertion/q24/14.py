
# Find the columns that contain NaN
z = np.isnan(a).any(axis=0)

# Delete the columns
a = a[:, ~z]
