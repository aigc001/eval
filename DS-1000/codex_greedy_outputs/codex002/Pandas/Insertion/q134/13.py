
# Find the index of the last occurrence of each duplicate row
last_occurrence_index = df.drop_duplicates(subset=['col1','col2'], keep='last').index

# Create a new column in the dataframe that contains the index of the last occurrence of each row
df['index_original'] = df.index.map(lambda x: last_occurrence_index[x] if x in last_occurrence_index else pd.np.nan)

# Filter the dataframe to only include the rows that are duplicates
duplicates = df.loc[df.duplicated(subset=['col1','col2'], keep='last')]

print(duplicates)
