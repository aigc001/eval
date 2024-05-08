
    # Convert the sparse matrix to a dense array
    dense_transform_output = transform_output.toarray()

    # Convert the dense array to a DataFrame
    df_transformed = pd.DataFrame(dense_transform_output, columns=df.columns)

    # Concatenate the original DataFrame and the transformed DataFrame
    result = pd.concat([df, df_transformed], axis=1)

    return result
