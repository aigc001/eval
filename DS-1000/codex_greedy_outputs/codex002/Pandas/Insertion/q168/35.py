
# Define functions for softmax and min-max normalization
def softmax(x):
    return np.exp(x) / np.sum(np.exp(x))

def min_max_normalization(x):
    return (x - np.min(x)) / (np.max(x) - np.min(x))

# Apply functions to each group
df['softmax'] = df.groupby('a')['b'].transform(lambda x: softmax(x))
df['min-max'] = df.groupby('a')['b'].transform(lambda x: min_max_normalization(x))
