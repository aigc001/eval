
# Calculate the zoom factors
zoom_x = shape[0] / x.shape[0]
zoom_y = shape[1] / x.shape[1]

# Apply the zoom
resized = scipy.ndimage.zoom(x, (zoom_x, zoom_y), order=1)

# The result will be larger than the target shape, so we need to crop it
resized = resized[:shape[0], :shape[1]]
