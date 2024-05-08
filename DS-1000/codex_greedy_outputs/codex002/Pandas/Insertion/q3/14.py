
# Create a function to replace values based on value_counts
def replace_values(df):
    for col in df.columns:
        counts = df[col].value_counts()
        df[col] = df[col].apply(lambda x: 'other' if counts[x] < 3 else x)
    return df

# Apply the function to the dataframe
result = replace_values(df)
