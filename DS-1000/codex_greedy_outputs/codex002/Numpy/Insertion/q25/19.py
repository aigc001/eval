
# Use np.isnan() to create a boolean mask of rows that contain NaN
mask = np.isnan(a).any(axis=1)

# Use the mask to filter out the rows
a = a[~mask]
