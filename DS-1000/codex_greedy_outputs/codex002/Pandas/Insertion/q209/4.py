
# Convert the string "0" to NaT
df.arrival_time = pd.to_datetime(df.arrival_time.replace('0', 'NaT'))

# Shift the arrival_time by one row and subtract it from departure_time
df['Duration'] = df.departure_time.shift(-1) - df.arrival_time

# For the last row, the duration is NaT, so we replace it with the last valid index
df['Duration'].iloc[-1] = df['Duration'].iloc[-2]
