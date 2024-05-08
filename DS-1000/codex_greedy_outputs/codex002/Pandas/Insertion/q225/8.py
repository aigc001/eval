
# Count the number of NaN values
nan_count = df['Column_x'].isnull().sum()

# Calculate the number of 0s and 1s to fill
zero_count = int(nan_count // 2)
one_count = nan_count - zero_count

# Fill the NaN values
df['Column_x'].fillna(0, inplace=True, limit=zero_count)
df['Column_x'].fillna(1, inplace=True, limit=one_count)
