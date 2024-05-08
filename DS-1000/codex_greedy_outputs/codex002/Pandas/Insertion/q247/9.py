
# Convert the series to a DataFrame
df = pd.DataFrame(series.values.tolist(), index=series.index)

# Add a column of indices
df.index.name = 'name'
df.reset_index(inplace=True)

print(df)
