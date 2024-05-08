
# Create a new column based on the conditions
df['Family'] = (df['Survived'] > 0) | (df['Parch'] > 0)

# Group by the new column and compute the mean
grouped = df.groupby('Family')['SibSp'].mean()

# Rename the groups
grouped = grouped.rename({True: 'Has Family', False: 'No Family'})

print(grouped)
