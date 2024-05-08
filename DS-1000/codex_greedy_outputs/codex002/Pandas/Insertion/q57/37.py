
# Find the min and max dates
min_date = df['dt'].min()
max_date = df['dt'].max()

# Create a new dataframe with all dates and users
new_df = pd.DataFrame({'dt': pd.date_range(start=min_date, end=max_date), 'user': df['user'].unique()})

# Merge the new dataframe with the original one
result = pd.merge(new_df, df, how='left', on=['dt', 'user'])

# Fill NaN values in 'val' column with 0
result['val'].fillna(0, inplace=True)
