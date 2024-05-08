
# Scale the data
scaler = sklearn.preprocessing.StandardScaler()
scaled_data = scaler.fit_transform(data)

# Center the data
centered_data = scaled_data - np.mean(scaled_data, axis=0)
