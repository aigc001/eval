
# Shift the first row of the first column down 1 row
df.loc['1980-01-01', '#1'] = df.loc['1980-01-02', '#1']
# Shift the last row of the first column up 1 row
df.loc['1980-01-05', '#1'] = df.loc['1980-01-04', '#1']

# Shift the last row of the second column up 1 row
df.loc['1980-01-05', '#2'] = df.loc['1980-01-04', '#2']
# Shift the first row of the second column down 1 row
df.loc['1980-01-01', '#2'] = df.loc['1980-01-02', '#2']

print(df)
