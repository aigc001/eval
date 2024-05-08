
# Get the number of rows and columns in the original array
rows, cols = a.shape

# Calculate the number of patches in each dimension
num_patches_rows = rows // patch_size
num_patches_cols = cols // patch_size

# Create an empty array to store the patches
patches = np.empty((num_patches_rows, num_patches_cols, patch_size, patch_size), dtype=a.dtype)

# Extract the patches
for i in range(num_patches_rows):
    for j in range(num_patches_cols):
        patches[i, j] = a[i*patch_size:(i+1)*patch_size, j*patch_size:(j+1)*patch_size]

print(patches)
