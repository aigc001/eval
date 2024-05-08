
# Create a new column 'group' which increments every 4 rows
df['group'] = df.index // 4

# Group by this new column and sum the values in 'col1'
grouped_df = df.groupby('group').sum()

# Drop the 'group' column
grouped_df.drop(columns='group', inplace=True)

print(grouped_df)
