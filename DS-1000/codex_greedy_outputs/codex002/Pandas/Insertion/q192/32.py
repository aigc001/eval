
# Define a custom aggregation function that applies different functions to different columns
def custom_agg(group):
    return pd.Series({'D': group['D'].sum(), 'E': group['E'].mean()})

# Use the custom aggregation function
pivot_table = df.groupby('B').apply(custom_agg).unstack()

# Rename the columns
pivot_table.columns = ['D_sum', 'E_mean']

print(pivot_table)
