
# Create a list of tuples where each tuple contains the column levels
value_vars = [(col[0], col[1], col[2]) for col in df.columns]

# Melt the dataframe
melted_df = pd.melt(df, value_vars=value_vars)

print(melted_df)
