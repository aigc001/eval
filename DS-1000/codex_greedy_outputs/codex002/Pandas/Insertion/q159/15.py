
# Define the conditions
conditions = [(df['SibSp'] == 1) & (df['Parch'] == 1),
              (df['SibSp'] == 0) & (df['Parch'] == 0),
              (df['SibSp'] == 0) & (df['Parch'] == 1),
              (df['SibSp'] == 1) & (df['Parch'] == 0)]

# Define the group names
group_names = ['Has Family', 'New Family', 'No Family', 'Old Family']

# Apply the conditions to the Survived column
df['Survived'] = pd.cut(df['Survived'], bins=[0, 1], labels=group_names, include_lowest=True)

# Group by the new Survived column and take the mean
result = df.groupby('Survived').mean()
