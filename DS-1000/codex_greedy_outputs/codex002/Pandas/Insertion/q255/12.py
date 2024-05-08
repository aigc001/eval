
def reverse_and_join(lst):
    return ','.join(map(str, lst[::-1]))

df['col1'] = df['col1'].apply(reverse_and_join)
