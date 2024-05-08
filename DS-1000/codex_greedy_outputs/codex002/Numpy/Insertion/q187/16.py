
# Create a mask of the non-diagonal elements
mask = np.ones_like(a)
np.fill_diagonal(mask, 0)

# Apply the mask
a *= mask
