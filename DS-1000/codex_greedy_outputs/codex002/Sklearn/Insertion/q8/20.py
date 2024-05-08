
# Assuming the last column is named 'fruit_list'
df = df.join(pd.DataFrame(df.fruit_list.tolist(), columns='Apple Orange Banana Grape'.split()))
df = df.fillna(1)
df.loc[df.Apple == 'Apple', 'Apple'] = 0
df.loc[df.Orange == 'Orange', 'Orange'] = 0
df.loc[df.Banana == 'Banana', 'Banana'] = 0
df.loc[df.Grape == 'Grape', 'Grape'] = 0
df = df.drop('fruit_list', axis=1)
