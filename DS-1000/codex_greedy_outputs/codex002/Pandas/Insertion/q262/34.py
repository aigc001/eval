
# Create a boolean series that matches the index level 'a' with the filt series
bool_indexer = filt[df.index.get_level_values('a')]

# Use the boolean series to filter the dataframe
filtered_df = df[bool_indexer]

print(filtered_df)
