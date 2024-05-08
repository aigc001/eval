
# Reshape the numpy array to a single column
np_array_reshaped = np_array.reshape(-1, 1)

# Initialize the MinMaxScaler
scaler = MinMaxScaler()

# Fit and transform the numpy array
np_array_normalized = scaler.fit_transform(np_array_reshaped)

# Reshape the normalized numpy array back to its original shape
np_array_normalized = np_array_normalized.reshape(np_array.shape)
