
# Convert the string to datetime
df['arrival_time'] = pd.to_datetime(df['arrival_time'])
df['departure_time'] = pd.to_datetime(df['departure_time'])

# Fill the first row of each group with the next row's arrival time
df['arrival_time'] = df.groupby('id')['arrival_time'].apply(lambda x: x.shift(-1).fillna(x))

# Calculate the time difference in seconds
df['Duration'] = (df['departure_time'] - df['arrival_time']).dt.total_seconds()

# Format the datetime columns
df['arrival_time'] = df['arrival_time'].dt.strftime('%d-%b-%Y %H:%M:%S')
df['departure_time'] = df['departure_time'].dt.strftime('%d-%b-%Y %H:%M:%S')
