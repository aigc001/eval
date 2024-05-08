
# Rotate the image
data_rot = rotate(data_orig, angle)

# Calculate the center of the original image
center_orig = np.array([data_orig.shape[0] / 2, data_orig.shape[1] / 2])

# Calculate the center of the rotated image
center_rot = np.array([data_rot.shape[0] / 2, data_rot.shape[1] / 2])

# Calculate the coordinates of the point in the original image
coords_orig = np.array([x0, y0])

# Calculate the rotation matrix
rot_matrix = np.array([[np.cos(np.deg2rad(angle)), -np.sin(np.deg2rad(angle))],
                      [np.sin(np.deg2rad(angle)), np.cos(np.deg2rad(angle))]])

# Calculate the translation matrix
trans_matrix = center_rot - rot_matrix @ center_orig

# Calculate the new coordinates
coords_rot = rot_matrix @ (coords_orig - center_orig) + center_rot + trans_matrix
xrot, yrot = coords_rot
