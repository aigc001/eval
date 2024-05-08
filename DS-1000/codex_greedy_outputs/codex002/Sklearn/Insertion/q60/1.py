
# Create a DataFrame from the list of lists
df = pd.DataFrame(features, columns=['f1', 'f2', 'f3', 'f4', 'f5', 'f6'])

# Fill missing values with 0
df.fillna(0, inplace=True)

# Convert the DataFrame to a NumPy array
features_array = df.values
