
# Reshape the DataFrame into a 3D NumPy array
array = df.values.reshape(len(names), len(times), len(df.columns))
