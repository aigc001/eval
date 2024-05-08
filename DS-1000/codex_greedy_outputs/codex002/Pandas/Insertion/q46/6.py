
# Create a boolean mask where True values correspond to NaN values
mask = df.isnull()

# Use the mask to shift values downwards
df[mask] = df[mask].shift(1)

# Fill remaining NaN values with 0
df.fillna(0, inplace=True)
