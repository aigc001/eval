
# Shuffle the DataFrame according to the list
df = df.iloc[List]

# Find the rows where Type is different from the original DataFrame
diff_rows = df.loc[df['Type'] != df['Type'].iloc[List]]

# Print the number of rows where Type is different
print(len(diff_rows))
