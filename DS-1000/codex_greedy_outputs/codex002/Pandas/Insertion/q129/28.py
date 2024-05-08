
# Group by UserId and get the size of each group
group_sizes = df.groupby('UserId').size()

# Calculate the number of rows to be randomly selected for each group
rows_to_select = group_sizes.apply(lambda x: int(0.2 * x))

# Create a list to store the indexes of the rows to be altered
rows_to_alter = []

# For each group, randomly select 20% of the rows and set their Quantity to zero
for user_id, size in rows_to_select.items():
    rows = df[df['UserId'] == user_id].sample(n=size, random_state=0)
    df.loc[rows.index, 'Quantity'] = 0
    rows_to_alter.extend(rows.index)

# Print the altered DataFrame and the indexes of the altered rows
print(df)
print('Indexes of altered rows:', rows_to_alter)
