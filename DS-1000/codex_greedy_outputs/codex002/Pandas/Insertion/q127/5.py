
# Calculate the number of rows to be selected
n = int(len(df) * 0.2)

# Select the rows randomly and set the Quantity to zero
altered_rows = df.sample(n, random_state=0)
altered_rows['Quantity'] = 0

# Update the original DataFrame with the altered rows
df.update(altered_rows)

# Print the updated DataFrame
print(df)
