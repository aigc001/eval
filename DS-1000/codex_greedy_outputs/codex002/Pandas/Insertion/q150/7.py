
# Create a function to apply to each group
def sum_with_nan(group):
    return group['v'].sum(skipna=False)

# Apply the function to each group
result = df.groupby('l').apply(sum_with_nan)

# Reset the index to get the desired output
result = result.reset_index()

# Rename the columns
result.columns = ['l', 'v']

print(result)
