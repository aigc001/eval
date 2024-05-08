
melted_df = pd.melt(df.T.reset_index(), id_vars=['index'], value_vars=df.columns.tolist())
melted_df['variable_0'] = melted_df['variable'].apply(lambda x: x[0])
melted_df['variable_1'] = melted_df['variable'].apply(lambda x: x[1])
melted_df['variable_2'] = melted_df['variable'].apply(lambda x: x[2])
melted_df.drop(columns='variable', inplace=True)
melted_df.rename(columns={'value': 'variable_3'}, inplace=True)
