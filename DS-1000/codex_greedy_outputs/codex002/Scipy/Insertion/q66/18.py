
# Calculate the z-scores
z_scores = stats.zscore(df, axis=1)

# Create a new DataFrame with the z-scores
z_df = pd.DataFrame(z_scores, index=df.index, columns=df.columns)

print(z_df)
