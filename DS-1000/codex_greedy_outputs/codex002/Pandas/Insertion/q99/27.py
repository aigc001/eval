
# Filter rows where absolute value of any columns is more than 1
filtered_df = df[df.filter(like='Value').abs().gt(1).any(axis=1)]

# Remove 'Value_' in each column
filtered_df.columns = [col.replace('Value_', '') for col in filtered_df.columns]

print(filtered_df)
