
# Using apply function and lambda function to round the values
df['dogs'] = df['dogs'].apply(lambda x: round(x, 2) if pd.notnull(x) else x)
df['cats'] = df['cats'].apply(lambda x: round(x, 2) if pd.notnull(x) else x)
