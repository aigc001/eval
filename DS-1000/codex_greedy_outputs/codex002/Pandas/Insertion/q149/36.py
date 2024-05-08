
# Group by 'r' and apply a function to 'v' that sums the values, skipping NaNs
grouped = df.groupby('r')['v'].apply(lambda x: x.sum(skipna=False))

# The result is a Series. Convert it to a DataFrame for pretty printing
result = pd.DataFrame(grouped).T

print(result)
