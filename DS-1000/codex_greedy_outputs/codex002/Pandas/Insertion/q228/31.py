
# Create a list of dataframes
dataframes = [a, b]

# Create a list of column names
columns = ['one', 'two']

# Create a list to store the tuples
tuples = []

# Iterate over the rows of each dataframe
for i in range(max(len(df) for df in dataframes)):
    # Create a list to store the tuples for this row
    row_tuples = []
    
    # Iterate over the dataframes
    for df in dataframes:
        # If the row index is valid for this dataframe, add the tuple of values
        if i < len(df):
            row_tuples.append(tuple(df.iloc[i]))
        # Otherwise, add a tuple of NaN values
        else:
            row_tuples.append(tuple([np.nan]*len(columns)))
    
    # Add the row of tuples to the list of rows
    tuples.append(row_tuples)

# Create the final dataframe
a_b = pd.DataFrame(tuples, columns=columns)
