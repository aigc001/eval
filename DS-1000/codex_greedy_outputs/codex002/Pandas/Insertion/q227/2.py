
# Create a list of dataframes
dataframes = [a, b, c]

# Create a list of column names
columns = ['one', 'two']

# Create a list to store the tuples
tuples = []

# Iterate over the rows of each dataframe
for i in range(len(dataframes[0])):
    # Create a list to store the tuples for this row
    row_tuples = []
    # Iterate over the dataframes
    for df in dataframes:
        # Append the tuple of values for this row from this dataframe to the row_tuples list
        row_tuples.append(tuple(df.iloc[i]))
    # Append the row_tuples list to the tuples list
    tuples.append(row_tuples)

# Create the final dataframe
a_b_c = pd.DataFrame(tuples, columns=columns)
