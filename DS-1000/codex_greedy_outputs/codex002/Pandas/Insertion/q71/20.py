
    # Filter rows where column 'c' is greater than 0.5
    df_filtered = df[df.c > 0.5]

    # Select only the columns specified
    df_filtered = df_filtered[columns]

    # Add a new column 'sum' which is the sum of the selected columns
    df_filtered['sum'] = df_filtered.sum(axis=1)

    return df_filtered
