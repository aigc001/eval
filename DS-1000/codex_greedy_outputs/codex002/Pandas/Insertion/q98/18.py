
# Get the columns that start with 'Value'
value_cols = [col for col in df.columns if col.startswith('Value')]

# Filter the dataframe where the absolute value of any of the 'Value' columns is greater than 1
filtered_df = df[(df[value_cols].abs() > 1).any(axis=1)]

print(filtered_df)
