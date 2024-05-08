
# Get the index location of each respective column minimum
min_idx = df.idxmin()

# Get the index location of each respective column maximum
max_idx = df.idxmax()

# Create a mask where the max's after the minimum occurrence are ignored
mask = (df.columns.values[:,None] == max_idx.values) & (df.index.values[:,None] > min_idx.values)

# Apply the mask to get the index location of the last occurrence of the column-wise maximum, up to the location of the minimum
result = df.index[np.argmax(mask, axis=0)]

# Create a DataFrame from the result
result_df = pd.DataFrame(result, index=df.columns, columns=['Last Max Before Min'])

print(result_df)
