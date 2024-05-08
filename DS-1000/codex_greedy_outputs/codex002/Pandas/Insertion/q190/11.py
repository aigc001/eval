
# Define a function to apply to each column
def custom_agg(col):
    if col.name == 'D':
        return col.sum()
    elif col.name == 'E':
        return col.mean()

# Use apply on the result of the pivot_table
pivot_table = pd.pivot_table(df, values=['D','E'], rows=['B'])
result = pivot_table.apply(custom_agg)
