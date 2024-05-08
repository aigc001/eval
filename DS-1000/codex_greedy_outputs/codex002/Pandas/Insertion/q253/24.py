
# Create a new DataFrame from the list of lists
new_df = pd.DataFrame(df['codes'].tolist(), index=df.index)

# Rename the columns
new_df.columns = ['code_' + str(i) for i in range(1, len(new_df.columns) + 1)]

# Concatenate the new DataFrame with the original DataFrame
df = pd.concat([df, new_df], axis=1)

# Drop the original 'codes' column
df.drop('codes', axis=1, inplace=True)
