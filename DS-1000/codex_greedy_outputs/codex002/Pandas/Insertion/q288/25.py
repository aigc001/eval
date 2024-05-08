
# Replace 'NULL' with 0
df['bar'] = df['bar'].replace('NULL', 0)

# Cast 'bar' column to int
df['bar'] = df['bar'].astype(int)

# Group by 'id1' and 'id2' and calculate the mean of 'foo' and 'bar'
res = df.groupby(["id1","id2"]).agg({"foo": "mean", "bar": "mean"})
