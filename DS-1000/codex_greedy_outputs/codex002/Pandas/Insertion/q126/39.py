
# Create a list of the column names
cols = ['keywords_0', 'keywords_1', 'keywords_2', 'keywords_3']

# Use apply and lambda function to concatenate the values
df['keywords_all'] = df[cols].apply(lambda row: '-'.join(row.dropna().astype(str)), axis=1)

print(df)
