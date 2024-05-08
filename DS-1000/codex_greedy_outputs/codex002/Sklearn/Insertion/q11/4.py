
# Convert the sparse matrix to a dense matrix
dense_matrix = transform_output.toarray()

# Create a DataFrame from the dense matrix
df_transformed = pd.DataFrame(dense_matrix)

# Concatenate the original DataFrame and the transformed DataFrame
df_final = pd.concat([df_origin, df_transformed], axis=1)
