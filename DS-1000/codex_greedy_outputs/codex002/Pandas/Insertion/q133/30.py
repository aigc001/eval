
# Create a duplicate dataframe with the same index
duplicate_df = df.duplicated(subset=['col1','col2', '3col'], keep='first')

# Get the index of the first occurrence of each duplicate row
first_occurrence_index = df.drop_duplicates(subset=['col1','col2', '3col']).index

# Create a new column in the duplicate dataframe with the index of the first occurrence
duplicate_df['index_original'] = duplicate_df.index.map(lambda x: first_occurrence_index[x])

# Filter the duplicate rows
duplicate = df.loc[duplicate_df == True]

# Add the index of the first occurrence to the duplicate rows
duplicate['index_original'] = duplicate.index.map(lambda x: first_occurrence_index[x])

print(duplicate)
