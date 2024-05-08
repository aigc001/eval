
# Create a structuring element for the morphological operations
struct_el = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]])

# Perform morphological opening to remove isolated pixels
opened = scipy.ndimage.binary_opening(square, structure = struct_el)

# Perform morphological closing to restore original shape
closed = scipy.ndimage.binary_closing(opened, structure = struct_el)

# The result is a binary array where isolated pixels have been removed
result = closed.astype(np.uint8) * 255
