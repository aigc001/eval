
# Shift the rows
df['#1'] = df['#1'].shift(1)
df['#2'] = df['#2'].shift(1)

# Fill the first row with the last row
df.iloc[0] = df.iloc[-1]

# Drop the last row
df = df.drop(df.index[-1])
