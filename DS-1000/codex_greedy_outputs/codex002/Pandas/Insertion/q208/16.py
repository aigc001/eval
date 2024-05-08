
# Create a new column 'label' and set the first value to 1
df['label'] = 0
df.loc[0, 'label'] = 1

# Calculate the difference between each row for the 'Close' column
df['diff'] = df['Close'].diff()

# Assign the label value based on the sign of the difference
df['label'] = df['diff'].apply(lambda x: 1 if x > 0 else (-1 if x < 0 else 0))

# Drop the 'diff' column
df.drop('diff', axis=1, inplace=True)

# Format the 'DateTime' column
df['DateTime'] = df['DateTime'].dt.strftime('%d-%b-%Y')

print(df)
