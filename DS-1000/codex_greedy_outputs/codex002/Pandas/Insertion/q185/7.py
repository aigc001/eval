
df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%y')

# Count per day
df['Count_d'] = df.Date.map(df.groupby('Date').size())

# Count per month
df['Count_m'] = df.Date.dt.month.map(df.groupby(df.Date.dt.to_period('M')).size())

# Count per year
df['Count_y'] = df.Date.dt.year.map(df.groupby(df.Date.dt.to_period('Y')).size())

print(df)
