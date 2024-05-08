
# Convert the csr_matrix back to a DataFrame
df_transformed = pd.DataFrame(transform_output.toarray(), columns=['transformed_data'])

# Merge the transformed DataFrame with the original DataFrame
df_final = pd.concat([df_origin, df_transformed], axis=1)
