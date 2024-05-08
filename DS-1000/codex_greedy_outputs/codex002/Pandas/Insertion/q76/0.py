
# Create a new column 'group' which groups every 3 rows together
df['group'] = df.index // 3

# Group by this new column and take the mean of 'col1'
df_binned = df.groupby('group').mean().reset_index(drop=True)

# Only keep the 'col1' column
df_binned = df_binned[['col1']]
