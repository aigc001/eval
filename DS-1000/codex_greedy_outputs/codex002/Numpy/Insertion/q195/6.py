
# Reshape the array to a 1D array
a_1d = a.reshape(-1, 1)

# Use MinMaxScaler fit_transform on the 1D array
scaler = MinMaxScaler()
a_normalized = scaler.fit_transform(a_1d)

# Reshape the normalized array back to 2D
a_normalized = a_normalized.reshape(a.shape)
