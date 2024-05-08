
# Group by column 'b' and calculate the mean of column 'a' for each group
mean_series = df.groupby('b')['a'].mean()

# Group by column 'b' and calculate the standard deviation of column 'a' for each group
std_series = df.groupby('b')['a'].std()

# Create a new DataFrame from the two series
result = pd.DataFrame({'mean': mean_series, 'std': std_series})

print(result)
