
# Create a list to store the region index for each extra point
region_indices = []

# Iterate over each extra point
for point in extraPoints:
    # Find the region index that the point belongs to
    region_index = vor.point_region[vor.npoints + np.where(np.all(vor.points == point, axis=1))[0]][0]
    # Append the region index to the list
    region_indices.append(region_index)

# Convert the list to a numpy array
region_indices = np.array(region_indices)
