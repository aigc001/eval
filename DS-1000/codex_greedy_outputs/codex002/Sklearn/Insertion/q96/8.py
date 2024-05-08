
# Reshape the numpy array to a 1D array
np_array_reshaped = np_array.reshape(-1,1)

# Use MinMaxScaler fit_transform on the reshaped array
scaler = MinMaxScaler()
np_array_normalized = scaler.fit_transform(np_array_reshaped)

# Reshape the normalized array back to its original shape
np_array_normalized = np_array_normalized.reshape(np_array.shape)
