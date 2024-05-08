
# Set the time column as the index
df.set_index('Time', inplace=True)

# Resample the data at a 2 minute frequency and take the mean
df = df.resample('2T').mean()

# Round the time column to the nearest minute
df.index = df.index.round('min')

# Reset the index to convert the time column back to a regular column
df.reset_index(inplace=True)
