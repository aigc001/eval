
# Create a list to store the column names that contain 1
cols = []

# Iterate over the columns and if a 1 is found, append the column name to the list
for col in df.columns:
    if 1 in df[col].values:
        cols.append(col)

# Create a new column by joining the column names together
df['category'] = df[cols].apply(lambda row: ''.join(row.index[row]), axis=1)

print(df)
