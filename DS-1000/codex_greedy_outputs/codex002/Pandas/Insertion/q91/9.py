
# Convert the date strings to datetime objects
df.index = df.index.set_levels(pd.to_datetime(df.index.levels[1]), level='date')
