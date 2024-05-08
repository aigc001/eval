
# Deleting particular days
df = df[~df.index.isin(['2020-02-17', '2020-02-18'])]

# Getting the day of the week
df['Day'] = df.index.day_name()

# Printing the first 5 rows
print(df.head())
