
    # Reshape the array to 1D
    a = a.reshape(-1,1)
    # Use MinMaxScaler
    scaler = MinMaxScaler()
    a = scaler.fit_transform(a)
    # Reshape it back to 2D
    a = a.reshape(np_array.shape)
    return a
