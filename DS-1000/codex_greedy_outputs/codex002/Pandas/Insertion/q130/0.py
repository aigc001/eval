
# Create a duplicate dataframe with the index of the first occurrence of each row
duplicate_index = df.duplicated(subset=['col1','col2'], keep='first')
duplicate_index[duplicate_index == True] = df.index[duplicate_index == True]

# Add the index of the first occurrence as a new column to the dataframe
df['index_original'] = duplicate_index

# Replace the NaN values in 'index_original' with the index of the row itself
df['index_original'].fillna(df.index, inplace=True)

# Cast 'index_original' to int
df['index_original'] = df['index_original'].astype(int)

print(df)
