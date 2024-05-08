
# Create a new column 'group' which will be used for grouping
df['group'] = df.index // 3

# Group by 'group' and take the mean of 'col1'
result = df.groupby('group')['col1'].mean().reset_index(drop=True)
