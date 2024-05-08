
# create a new dataframe from the list in Col3
df_new = pd.DataFrame(df['Col3'].tolist(), index=df.index).fillna(0)

# replace all '1's with the corresponding Col2 value
df_new = df_new.replace(1, df['Col2'])

# concatenate the new dataframe with the original dataframe
df = pd.concat([df, df_new], axis=1)

# drop the original Col3
df = df.drop('Col3', axis=1)
