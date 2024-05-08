
# Shift the first column down by one row
df['#1'] = df['#1'].shift(1)

# Fill the first row of the first column with the last value
df.loc[df.index[0], '#1'] = df['#1'].iloc[-1]

print(df)
