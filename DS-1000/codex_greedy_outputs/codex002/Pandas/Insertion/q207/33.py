
# Calculate the difference between each row for the 'Close' column
df['diff'] = df['Close'].diff()

# Create the 'label' column
df['label'] = df['diff'].apply(lambda x: 1 if x > 0 else (-1 if x < 0 else 0))

# Drop the 'diff' column
df.drop('diff', axis=1, inplace=True)

# Set the 'label' value for the first row to 1
df.loc[df.index[0], 'label'] = 1

print(df)
