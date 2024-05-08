
labels, num_features = ndimage.label(img > threshold)
print(f"Number of regions: {num_features}")
