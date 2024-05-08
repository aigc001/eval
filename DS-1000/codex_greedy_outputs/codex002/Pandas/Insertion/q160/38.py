
# Group by 'cokey' and sort each group by 'A'
grouped = df.groupby('cokey').apply(lambda x: x.sort('A'))

# Reset the index
grouped.reset_index(inplace=True, drop=True)

# Print the result
print(grouped)
