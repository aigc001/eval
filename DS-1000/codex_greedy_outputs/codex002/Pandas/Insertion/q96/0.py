
# Melt the data frame
df = pd.melt(df, id_vars=['Country', 'Variable'], var_name='year')

# Convert the year column to integer
df['year'] = df['year'].astype(int)

# Sort the data frame by year in descending order
df = df.sort_values('year', ascending=False)

# Reset the index
df = df.reset_index(drop=True)

# Pivot the data frame
df = df.pivot_table(index=['Country', 'year'], columns='Variable', values='value')

# Reset the column level names
df.columns.names = [''] * len(df.columns.names)

# Reset the index
df = df.reset_index()

print(df)
