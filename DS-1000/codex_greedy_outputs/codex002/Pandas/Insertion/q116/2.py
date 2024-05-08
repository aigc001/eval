
# Compute the total for each column
total = df.sum(axis=0)

# Divide each value by the total of its column
df_percentage = df.div(total)

print(df_percentage)
