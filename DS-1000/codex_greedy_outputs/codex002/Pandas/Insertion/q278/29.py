
# Convert the dates to datetime
dates_to_remove = ['2020-02-17', '2020-02-18']
dates_to_remove = pd.to_datetime(dates_to_remove)

# Filter the dataframe
df = df[~df.index.date.isin(dates_to_remove)]
