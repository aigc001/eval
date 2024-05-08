
# Get the index location of the column-wise maximum
max_idx = df.idxmax()

# Get the index location of the column-wise minimum
min_idx = df.idxmin()

# Create a mask where the max's before the minimum occurrence are ignored
mask = (df.max(axis=0) > df.min(axis=0)) & (df.idxmax() > df.idxmin())

# Apply the mask to get the index location of the first occurrence of the column-wise maximum down to the location of the minimum
result = max_idx[mask]

print(result)
