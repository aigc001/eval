
# Create a series from the dictionary
s = pd.Series(dict)

# Map the values in 'Member' column to the series index
df['Date'] = df['Member'].map(s)

# Fill NaN values with a default value
df['Date'] = df['Date'].fillna('17/8/1926')
