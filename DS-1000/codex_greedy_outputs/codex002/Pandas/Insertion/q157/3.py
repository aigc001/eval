
# Create a new column 'Family' based on the conditions
df['Family'] = ['Has Family' if (row['SibSp'] > 0 or row['Parch'] > 0) else 'No Family' for index, row in df.iterrows()]

# Group by 'Family' and take the mean of 'Survived'
mean_df = df.groupby('Family')['Survived'].mean()

print(mean_df)
