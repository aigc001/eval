
# Create a mask of NaN values
mask = df.isnull()

# Use the mask to create a new DataFrame where NaNs are replaced with the last non-NaN value
df_new = df.where(~mask, df.ffill())
