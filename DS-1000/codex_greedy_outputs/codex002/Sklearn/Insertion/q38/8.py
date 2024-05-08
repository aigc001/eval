
# Apply the preprocessing
scaled_data = preprocessing.scale(data.values)

# Create a new DataFrame using the scaled data and the original column names
scaled_dataframe = pd.DataFrame(scaled_data, columns=data.columns, index=data.index)
