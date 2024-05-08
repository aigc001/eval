
# Create a boolean mask for values less than the threshold
mask = df['value'] < thresh

# Create a new DataFrame with only the values less than the threshold
temp = df[mask]

# Sum the values and create a new row with the sum
temp = pd.DataFrame({'lab':'X', 'value':temp['value'].sum()}, index=['X'])

# Drop the rows that were aggregated
df = df[~mask]

# Append the new row to the DataFrame
df = df.append(temp)
