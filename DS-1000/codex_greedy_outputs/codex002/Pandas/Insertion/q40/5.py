
# replace 'null' with actual NaN
df = df.replace('null', pd.np.nan)

# count NaNs in each column
count_null = df.isnull().sum()

print(count_null)
