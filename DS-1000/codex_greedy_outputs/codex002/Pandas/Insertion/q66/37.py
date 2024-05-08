
# Melt the dataframe
melted_df = pd.melt(df, id_vars=['user'], var_name='others', value_name='value')

# Sort the dataframe by 'user' and 'others'
melted_df.sort_values(by=['user', 'others'], inplace=True)

# Reset the index
melted_df.reset_index(drop=True, inplace=True)

print(melted_df)
