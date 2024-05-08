
df1 = df.groupby("item", as_index=False).agg({"diff": "min", "otherstuff": "first"})
