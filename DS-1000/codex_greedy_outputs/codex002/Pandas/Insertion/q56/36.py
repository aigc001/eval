
# Find the min and max dates
min_date = df['dt'].min()
max_date = df['dt'].max()

# Create a new dataframe with all dates and users
new_df = pd.DataFrame({'dt': pd.date_range(start=min_date, end=max_date)})

# Create a multi-index from the 'user' and 'dt' columns
new_df.set_index(['user', 'dt'], inplace=True)

# Join the new dataframe with the original one
result = new_df.join(df.set_index(['user', 'dt']), how='left')

# Fill NaN values in 'val' column with 0
result['val'].fillna(0, inplace=True)

# Reset the index
result.reset_index(inplace=True)
