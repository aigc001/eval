
# Convert the string to datetime
df['arrival_time'] = pd.to_datetime(df['arrival_time'])
df['departure_time'] = pd.to_datetime(df['departure_time'])

# Fill NaT with the next row's arrival time
df['arrival_time'].fillna(method='bfill', inplace=True)

# Calculate the time difference in seconds
df['Duration'] = (df['departure_time'] - df['arrival_time']).dt.total_seconds()
