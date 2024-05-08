
# Create a function to find the most frequent value in a row
def find_frequent(row):
    values, counts = np.unique(row, return_counts=True)
    max_count_index = np.argmax(counts)
    return values[max_count_index]

# Create a function to find the count of the most frequent value in a row
def find_freq_count(row):
    values, counts = np.unique(row, return_counts=True)
    max_count_index = np.argmax(counts)
    return counts[max_count_index]

# Apply the functions to each row of the DataFrame
df['frequent'] = df.apply(find_frequent, axis=1)
df['freq_count'] = df.apply(find_freq_count, axis=1)
