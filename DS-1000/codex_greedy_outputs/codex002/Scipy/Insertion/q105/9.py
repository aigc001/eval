
# Select only numeric columns
numeric_cols = df.select_dtypes(include=[np.number])

# Remove outliers
numeric_cols = numeric_cols[(np.abs(stats.zscore(numeric_cols)) < 3).all(axis=1)]

# Join back with original dataframe
df = pd.concat([numeric_cols, df.select_dtypes(exclude=[np.number])], axis=1)
