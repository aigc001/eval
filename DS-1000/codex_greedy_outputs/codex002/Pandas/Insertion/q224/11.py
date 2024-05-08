
# Calculate the number of NaN values
nan_count = df['Column_x'].isna().sum()

# Calculate the number of values to fill in each category
first_part = int(nan_count * 0.3)
second_part = int(nan_count * 0.6)

# Fill the first part with 0
df.loc[df['Column_x'].isna()[:first_part], 'Column_x'] = 0

# Fill the second part with 0.5
df.loc[df['Column_x'].isna()[first_part:second_part], 'Column_x'] = 0.5

# Fill the rest with 1
df.loc[df['Column_x'].isna()[second_part:], 'Column_x'] = 1
