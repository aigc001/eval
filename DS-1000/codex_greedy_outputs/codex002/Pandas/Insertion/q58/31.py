
# Find the min and max dates
min_date = df['dt'].min()
max_date = df['dt'].max()

# Create a new dataframe with all dates in the range
new_df = pd.DataFrame({'dt': pd.date_range(start=min_date, end=max_date)})

# Add the user and val columns to the new dataframe
new_df['user'] = 'a'
new_df['val'] = 233

# Merge the new dataframe with the original one
result = pd.concat([df, new_df]).sort_values(by='dt')

# Fill missing values
result['user'].fillna(method='ffill', inplace=True)
result['val'].fillna(method='ffill', inplace=True)

# Reset index
result.reset_index(drop=True, inplace=True)
