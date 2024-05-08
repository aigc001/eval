
    # Create a dictionary to map names to unique IDs
    name_to_id = {name: i+1 for i, name in enumerate(df['name'].unique())}

    # Replace the names with their respective IDs
    df['name'] = df['name'].map(name_to_id)

    return df
