
    labeled_array, num_features = ndimage.label(img > threshold)
    return num_features
