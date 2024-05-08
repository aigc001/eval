
# Create a structuring element for the binary dilation
s = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]])
# Perform binary dilation
dilated = scipy.ndimage.binary_dilation(square, structure=s)
# Subtract the dilated image from the original to isolate single pixels
result = square - dilated
# Set the single pixels to 0
result[result == 1] = 0
