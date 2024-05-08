
# Group by 'cokey' and sort by 'A' within each group
df_sorted = df.groupby('cokey').apply(lambda x: x.sort('A')).reset_index(drop=True)

# Reset the index and assign the new index to 'cokey'
df_sorted['cokey'] = df_sorted.index

# Print the sorted DataFrame
print(df_sorted)
