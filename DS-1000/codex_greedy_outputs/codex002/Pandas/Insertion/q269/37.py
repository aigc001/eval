
df_new = pd.DataFrame(df.values.flatten().reshape(1,-1), columns=df.columns)
