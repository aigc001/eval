
# Create a boolean series that matches the index values of 'a'
a_filt = df.index.get_level_values('a').isin(filt[filt].index)

# Create a boolean series that matches the index values of 'b'
b_filt = df.index.get_level_values('b').isin(filt[filt].index)

# Combine the two boolean series with the logical operator '&' (and)
final_filt = a_filt & b_filt

# Apply the final boolean filter to the DataFrame
filtered_df = df[final_filt]
