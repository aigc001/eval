
# Group by column 'a' and calculate the mean and standard deviation of column 'b'
grouped = df.groupby('a')['b'].agg(['mean', 'std'])

# Reset the index to convert the grouped data back into a DataFrame
grouped.reset_index(inplace=True)

print(grouped)
