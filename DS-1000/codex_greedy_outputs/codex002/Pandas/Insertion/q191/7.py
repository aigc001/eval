
# Define the aggregation functions for each column
agg_func = {'D': np.sum, 'E': np.mean}

# Create the pivot table
pivot_table = pd.pivot_table(df, values=['D','E'], rows=['B'], aggfunc=agg_func)

# Print the pivot table
print(pivot_table)
