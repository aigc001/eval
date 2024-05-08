
# set Date as index
df.set_index('Date', inplace=True)

# count zero values
result1 = df.applymap(lambda x: (x == 0).sum())

# count non-zero values
result2 = df.applymap(lambda x: (x != 0).sum())

print("Zero values:")
print(result1)
print("\nNon-zero values:")
print(result2)
