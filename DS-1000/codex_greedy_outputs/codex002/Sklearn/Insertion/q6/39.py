
# Create a new dataframe from the last column
df_new = pd.DataFrame(df.Col4.values.tolist(), index=df.index)

# Use get_dummies to convert the new dataframe into one-hot-encoded columns
df_new = pd.get_dummies(df_new, columns=df_new.columns)

# Join the new dataframe with the original dataframe
df = pd.concat([df, df_new], axis=1)

# Drop the original Col4
df = df.drop('Col4', axis=1)
