
def nested_dict(df):
    d = {}
    for row in df.itertuples():
        d[row.name] = d.get(row.name, {})
        d[row.name][row.v1] = d[row.name].get(row.v1, {})
        d[row.name][row.v1][row.v2] = row.v3
    return d

print(nested_dict(df))
