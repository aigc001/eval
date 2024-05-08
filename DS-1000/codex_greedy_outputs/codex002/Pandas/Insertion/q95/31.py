
df = pd.melt(df, id_vars=['Country', 'Variable'], var_name='year')
df['year'] = df['year'].astype(int)
df = df.sort_values(['Country', 'Variable', 'year']).reset_index(drop=True)
