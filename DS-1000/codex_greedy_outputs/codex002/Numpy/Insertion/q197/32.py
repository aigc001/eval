
scaler = MinMaxScaler()

# Reshape the array to 2D
a_2d = a.reshape(-1, 1)

# Fit and transform the 2D array
a_scaled = scaler.fit_transform(a_2d)

# Reshape the scaled array back to 3D
a_scaled_3d = a_scaled.reshape(a.shape)

print(a_scaled_3d)
