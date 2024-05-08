
# Count the number of NaN values
nan_count = df['Column_x'].isnull().sum()

# Calculate the index to split the NaN values
split_index = int(nan_count / 2)

# Split the dataframe into two parts at the calculated index
df_part1 = df.iloc[:split_index]
df_part2 = df.iloc[split_index:]

# Fill the NaN values in each part with the desired value
df_part1['Column_x'].fillna(0, inplace=True)
df_part2['Column_x'].fillna(1, inplace=True)

# Concatenate the two parts back together
df = pd.concat([df_part1, df_part2])
