
# Get the column names that do not contain 'group'
value_cols = [col for col in df.columns if 'group' not in col]

# Group by 'group' and take the mean of all other columns
grouped_df = df.groupby('group')[value_cols].mean()

print(grouped_df)
