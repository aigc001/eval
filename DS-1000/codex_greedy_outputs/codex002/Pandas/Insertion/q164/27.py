
df.columns = pd.MultiIndex.from_tuples(df.columns, names=['Caps', 'Middle', 'Lower'])
df.index = pd.Index(['1', '2', '3', '4', '5'])
print(df)
