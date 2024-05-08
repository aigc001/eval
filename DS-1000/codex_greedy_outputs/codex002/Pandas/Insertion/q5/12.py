
# Create a function to handle the replacement
def replace_values(df, column, min_count):
    counts = df[column].value_counts()
    df[column] = df[column].apply(lambda x: 'other' if counts[x] >= min_count else x)
    return df

# Apply the function to the columns
df = replace_values(df, 'Qu1', 3)
df = replace_values(df, 'Qu2', 2)
df = replace_values(df, 'Qu3', 2)
