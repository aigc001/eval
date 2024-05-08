
# Extract the number and the time separately
df['number'] = df.duration.str.extract(r'(\d+)')
df['time'] = df.duration.str.extract(r'(\w+)')

# Create a new column 'time_days' based on the values of 'time'
df['time_days'] = df.time.map({'year': 365, 'month': 30, 'week': 7, 'day': 1})
