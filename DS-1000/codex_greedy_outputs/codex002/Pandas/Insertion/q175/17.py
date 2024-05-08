
# Using the isinstance function to check if the value in column A is an integer or a float
df = df[df['A'].apply(lambda x: isinstance(x, (int, float)))]
