
# Drop the rows where all elements are 0
df = df[df.sum(axis=1) != 0]

# Drop the columns where all elements are 0
df = df.loc[:, df.sum() != 0]

print(df)
