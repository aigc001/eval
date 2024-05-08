
df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%y')

# Count per day
df['Count_d'] = df.groupby('Date').size()

# Count per month
df['Count_m'] = df.groupby(df['Date'].dt.to_period('M')).size()

# Count per year
df['Count_y'] = df.groupby(df['Date'].dt.year).size()

# Count per Val
df['Count_Val'] = df.groupby('Val').size()

print(df)
