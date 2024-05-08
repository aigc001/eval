
# Replace 'null' with actual None
df = df.replace('null', None)

# Get the value counts for each column
value_counts = df.apply(lambda x: x.value_counts())

# Replace None with 'null' again
value_counts = value_counts.replace(None, 'null')

print(value_counts)
