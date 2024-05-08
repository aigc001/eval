
# Reverse the dataframe
df = df[::-1]

# Create a new column 'group' which increments every 3 rows
df['group'] = (df.index // 3).astype(int)

# Group by 'group' and take the mean of 'col1'
df = df.groupby('group').mean().reset_index(drop=True)

# The result is the desired output
print(df)
