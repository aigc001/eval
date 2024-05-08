
# Define the columns to be aggregated
value_cols = [col for col in df.columns if col.startswith('val') and col.endswith('2')]

# Define the aggregation functions
agg_funcs = {col: 'sum' for col in value_cols}
agg_funcs['group_color'] = 'first'

# Perform the aggregation
result = df.groupby('group').agg(agg_funcs)

print(result)
