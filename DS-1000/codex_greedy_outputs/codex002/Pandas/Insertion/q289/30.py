
df_c = pd.merge(df_a, df_b[['EntityNum','a_col']], on='EntityNum')
