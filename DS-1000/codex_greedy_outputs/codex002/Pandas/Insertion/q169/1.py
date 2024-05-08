
# Drop columns where all values are 0
df = df.loc[:, (df != 0).any(axis=0)]

# Drop rows where all values are 0
df = df.loc[(df != 0).any(axis=1)]

print(df)
