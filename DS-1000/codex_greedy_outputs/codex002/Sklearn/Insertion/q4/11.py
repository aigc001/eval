
# Create a new dataframe from the list in Col3
df_new = pd.DataFrame(df['Col3'].tolist(), index=df.index).fillna(False)

# Replace all True values with 1 and all False values with 0
df_new = df_new.astype(int)

# Concatenate the new dataframe with the original dataframe
df = pd.concat([df, df_new], axis=1)

# Drop the original Col3 from the dataframe
df = df.drop('Col3', axis=1)
