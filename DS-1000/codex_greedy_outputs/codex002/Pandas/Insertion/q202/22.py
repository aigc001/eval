
# Replace 0 with NaN
df.replace(0, np.nan, inplace=True)

# Calculate the cumulative average
df['2001'] = df['2001']
for year in range(2002, 2007):
    df[year] = df[year-1] + (df[year] - df[year-1]) / (df[year] - df[year-1]).count()

# Replace NaN with 0
df.fillna(0, inplace=True)
