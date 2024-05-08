
# Sort the dataframe by 'keep_if_dup' in descending order and 'url' in ascending order
df = df.sort_values(by=['keep_if_dup', 'url'], ascending=[False, True])

# Drop duplicates by 'url' while keeping the first occurrence
df = df.drop_duplicates(subset='url', keep='first')
