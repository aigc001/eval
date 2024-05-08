
# Find the min and max dates
min_date = df['dt'].min()
max_date = df['dt'].max()

# Create a new dataframe with all dates in the range
new_df = pd.DataFrame({'dt': pd.date_range(start=min_date, end=max_date)})

# Merge the new dataframe with the original one on 'dt'
merged_df = pd.merge(new_df, df, on='dt', how='left')

# Fill missing 'user' values with the last non-missing value
merged_df['user'].fillna(method='ffill', inplace=True)

# Fill missing 'val' values with the maximum value of 'val' for each 'user'
merged_df['val'].fillna(merged_df.groupby('user')['val'].transform('max'), inplace=True)

# Sort the dataframe by 'user' and 'dt'
merged_df.sort_values(['user', 'dt'], inplace=True)

# Reset the index
merged_df.reset_index(drop=True, inplace=True)
