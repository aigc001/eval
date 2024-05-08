
# Find the min and max dates
min_date = df['dt'].min()
max_date = df['dt'].max()

# Create a new dataframe with all dates in the range
new_df = pd.DataFrame({'dt': pd.date_range(start=min_date, end=max_date)})

# Add the user and val columns to the new dataframe
new_df['user'] = df['user'].values[0]
new_df['val'] = df.groupby('user')['val'].max().values[0]

# Convert the date column to the desired format
new_df['dt'] = new_df['dt'].dt.strftime('%d-%b-%Y')

# Sort the dataframe by user and date
new_df = new_df.sort_values(['user', 'dt'])

# Reset the index
new_df.reset_index(drop=True, inplace=True)

print(new_df)
