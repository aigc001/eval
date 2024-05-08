
# Create a duplicate DataFrame with the index of the last occurrence of each row
duplicate_df = df.drop_duplicates(subset=['col1','col2'], keep='last')
duplicate_df['index_original'] = duplicate_df.index

# Merge the original DataFrame with the duplicate DataFrame on the columns 'col1' and 'col2'
df = pd.merge(df, duplicate_df[['col1','col2','index_original']], on=['col1','col2'], how='left')

print(df)
