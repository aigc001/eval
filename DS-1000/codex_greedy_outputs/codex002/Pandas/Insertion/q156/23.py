
df = pd.DataFrame(s, columns=['Revenue'])

# replace ',' with ''
df['Revenue'] = df['Revenue'].str.replace(',','')

# convert to float
df['Revenue'] = pd.to_numeric(df['Revenue'], errors='coerce')

print(df)
