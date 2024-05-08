
# Create a list of dataframes
dataframes = [a, b]

# Use the zip function to iterate over the dataframes simultaneously
# Use the map function to apply the zip function to each row of the dataframes
# Use the lambda function to convert the result of zip into a tuple
# Use the pd.DataFrame constructor to create a new DataFrame
a_b = pd.DataFrame(list(map(lambda x: list(zip(*x)), zip(*[df.values for df in dataframes]))), columns=['one', 'two'])
