
def count_e(group):
    return (group['key2'].str.endswith('e')).sum()

result = df.groupby('key1').apply(count_e)

print(result)
