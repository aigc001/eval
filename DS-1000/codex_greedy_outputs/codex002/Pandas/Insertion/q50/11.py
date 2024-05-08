
# Using dictionary comprehension and pandas assign function to add new columns
df = df.assign(**{f"inv_{col}": 1/df[col] for col in df.columns})
