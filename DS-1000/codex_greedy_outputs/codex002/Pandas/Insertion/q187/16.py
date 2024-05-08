
df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%y')

# Counts per day
df['Count_d'] = df.groupby('Date').size()

# Counts per month
df['Count_m'] = df.groupby(df['Date'].dt.to_period('M')).size()

# Counts per year
df['Count_y'] = df.groupby(df['Date'].dt.year).size()

# Counts per weekday
df['Count_w'] = df.groupby(df['Date'].dt.weekday).size()

# Counts per unique Values
df['Count_Val'] = df.groupby('Val').size()

print(df)
