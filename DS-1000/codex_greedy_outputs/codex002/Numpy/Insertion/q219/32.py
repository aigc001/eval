
# Find the indices of non-zero elements
non_zero_indices = np.where(im != 0)
# Get the minimum and maximum indices for rows and columns
min_row_index = min(non_zero_indices[0])
max_row_index = max(non_zero_indices[0])
min_col_index = min(non_zero_indices[1])
max_col_index = max(non_zero_indices[1])
# Crop the image
im_cropped = im[min_row_index:max_row_index+1, min_col_index:max_col_index+1]
print(im_cropped)
