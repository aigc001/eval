
# Replace 'NULL' with np.nan
df['bar'] = df['bar'].replace('NULL', np.nan)

# Group by id1 and id2 and calculate the mean of foo and bar
res = df.groupby(["id1","id2"]).agg({"foo": "mean", "bar": "mean"})
