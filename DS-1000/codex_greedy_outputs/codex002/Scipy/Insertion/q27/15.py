
labels, num_features = ndimage.label(img < threshold)
print(f"Number of regions below threshold: {num_features}")
