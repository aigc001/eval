
# Resample the data to 3 minutes and sum the values
df = df.set_index('Time').resample('3T').sum().reset_index()

# Interpolate the missing values
df['Value'] = df['Value'].interpolate(method='time')

print(df)
