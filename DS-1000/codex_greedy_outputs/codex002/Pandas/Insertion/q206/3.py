
# Create a new column 'Label' and initialize it with 1
df['Label'] = 1

# Compute the difference between the current and the next row
diff = df['Close'] - df['Close'].shift(-1)

# Update 'Label' based on the sign of the difference
df.loc[diff < 0, 'Label'] = 0

# Handle the first row separately
df.loc[0, 'Label'] = 1
