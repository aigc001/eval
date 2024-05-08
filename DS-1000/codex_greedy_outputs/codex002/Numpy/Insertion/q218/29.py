
# Find the rows and columns that are all zeros
rows_zeros = np.all(im == 0, axis=1)
cols_zeros = np.all(im == 0, axis=0)

# Remove the rows and columns that are all zeros
im = im[~rows_zeros, :]
im = im[:, ~cols_zeros]

# Print the result
print(im)
