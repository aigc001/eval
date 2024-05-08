
# Create a boolean mask for values above the threshold
mask = df['value'] > thresh

# Create a new dataframe with values above the threshold
df_above_thresh = df[mask]

# Calculate the average of the values above the threshold
avg = df_above_thresh['value'].mean()

# Create a new row with this average
new_row = pd.DataFrame({'lab':['X'], 'value':[avg]})

# Set the new row's index to 'X'
new_row = new_row.set_index('lab')

# Drop the rows above the threshold from the original dataframe
df = df[~mask]

# Append the new row to the original dataframe
df = df.append(new_row)
