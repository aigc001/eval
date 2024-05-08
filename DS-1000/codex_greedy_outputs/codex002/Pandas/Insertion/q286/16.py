
def most_frequent(row):
    values, counts = np.unique(row, return_counts=True)
    max_count = max(counts)
    most_frequent_values = values[counts == max_count]
    return list(most_frequent_values)

df['frequent'] = df.apply(most_frequent, axis=1)

def freq_count(row):
    values, counts = np.unique(row, return_counts=True)
    max_count = max(counts)
    return max_count

df['freq_count'] = df.apply(freq_count, axis=1)
