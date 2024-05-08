
# Replace 0 with NaN
df.replace(0, np.nan, inplace=True)

# Calculate the average from end to head for each row
df.iloc[:, 1:] = df.iloc[:, 1:].apply(lambda x: x[::-1].cumsum() / (x[::-1].notna().cumsum()), axis=1)

# Replace NaN with 0
df.fillna(0, inplace=True)
