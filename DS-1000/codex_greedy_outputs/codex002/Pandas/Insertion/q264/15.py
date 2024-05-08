
# Get the rows we're interested in
row0 = df.iloc[0].dropna()
row8 = df.iloc[8].dropna()

# Get the columns that are different
diff_cols = row0[row0 != row8].index

print(diff_cols)
