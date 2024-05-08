
    # Create a new column 'index_original' with the index of the DataFrame
    df['index_original'] = df.index

    # Create a duplicate DataFrame
    duplicate_df = df.duplicated(subset=['col1','col2'], keep='first')

    # Get the index of the first occurrence of each duplicate row
    first_occurrence_index = df.index[duplicate_df]

    # Create a new column 'index_first_duplicate' with the index of the first occurrence of each duplicate row
    df['index_first_duplicate'] = df.index
    df.loc[duplicate_df, 'index_first_duplicate'] = first_occurrence_index

    # Return the modified DataFrame
    return df
