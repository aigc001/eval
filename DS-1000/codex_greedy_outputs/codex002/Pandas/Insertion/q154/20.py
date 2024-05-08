
# Create an empty DataFrame to store the results
relationship_df = pd.DataFrame(index=df.columns, columns=df.columns)

# Iterate over each pair of columns
for col1 in df.columns:
    for col2 in df.columns:
        # Calculate the number of unique values in each column
        unique_col1 = df[col1].nunique()
        unique_col2 = df[col2].nunique()

        # Determine the type of relationship
        if unique_col1 == 1 and unique_col2 == 1:
            relationship = 'one-2-one'
        elif unique_col1 == 1 and unique_col2 > 1:
            relationship = 'one-2-many'
        elif unique_col1 > 1 and unique_col2 == 1:
            relationship = 'many-2-one'
        else:
            relationship = 'many-2-many'

        # Store the result in the DataFrame
        relationship_df.loc[col1, col2] = relationship
