
# Convert the datetime strings to datetime objects
df.index = pd.to_datetime(df.index.get_level_values('datetime'))
