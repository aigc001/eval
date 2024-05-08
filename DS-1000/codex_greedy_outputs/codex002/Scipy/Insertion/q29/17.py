
# Label the regions
labeled_array, num_features = ndimage.label(img > threshold)

# Calculate the center of mass for each region
centers = ndimage.center_of_mass(img, labeled_array, range(1, num_features + 1))

# Calculate the distance from the top left corner to each center
distances = [np.linalg.norm(np.array([0, 0]) - np.array(center)) for center in centers]
