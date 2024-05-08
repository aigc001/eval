
# Select rows where A is a string
df_str = df[df['A'].apply(lambda x: isinstance(x, str))]
