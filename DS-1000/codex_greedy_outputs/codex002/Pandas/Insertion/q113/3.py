
# Create an empty list to store the integer values
integer_values = []

# Iterate over each row in the dataframe
for index, row in df.iterrows():
    # Check if the value in the 'Field1' column is an integer
    if isinstance(row['Field1'], int):
        # If it is, append it to the list
        integer_values.append(row['Field1'])

print(integer_values)
