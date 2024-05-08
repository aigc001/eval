
df_c = pd.merge(df_a, df_b, on='EntityNum', how='left')
df_c = df_c.drop('a_col', axis=1)
