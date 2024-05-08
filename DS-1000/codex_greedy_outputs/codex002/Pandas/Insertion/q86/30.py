
# Split the duration column into time and number
df[['time', 'number']] = df['duration'].str.split(expand=True)

# Replace the time column with the corresponding number of days
df['time_day'] = df['time'].replace({'year': 365, 'month': 30, 'week': 7, 'day': 1})

# Cast the number column to integer
df['number'] = df['number'].astype(int)
