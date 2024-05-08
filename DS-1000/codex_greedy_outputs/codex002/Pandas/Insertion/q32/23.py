
# Create a list of all columns
columns = df.columns

# Create a dictionary to rename the columns
rename_dict = {col: 'X' + col for col in columns if not col.endswith('X')}

# Rename the columns
df = df.rename(columns=rename_dict)
