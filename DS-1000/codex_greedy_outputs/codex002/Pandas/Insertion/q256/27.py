
# Use apply to convert each list to a string
df['col1'] = df['col1'].apply(lambda x: ','.join(map(str, x)))
