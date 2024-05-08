
    # Create a copy of the dataframe to avoid modifying the original one
    df_copy = df.copy()

    # Iterate over the columns
    for col in df_copy.columns:
        # Get the value counts for the column
        counts = df_copy[col].value_counts()

        # Get the values that appear at least 2 times
        values_to_keep = counts[counts >= 2].index

        # Replace the values that don't appear at least 2 times with 'other'
        df_copy[col] = df_copy[col].apply(lambda x: 'other' if x not in values_to_keep else x)

    return df_copy
