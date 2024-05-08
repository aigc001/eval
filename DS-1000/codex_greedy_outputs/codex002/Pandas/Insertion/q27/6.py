
# Shift the data up by one row
df.loc['1980-01-01'] = df.loc['1980-01-02']
df.loc['1980-01-02'] = df.loc['1980-01-03']
df.loc['1980-01-03'] = df.loc['1980-01-04']
df.loc['1980-01-04'] = df.loc['1980-01-05']

# Put the first row of data at the bottom
df.loc['1980-01-05'] = df.iloc[0]

# Print the result
print(df)
