
# Create a LabelEncoder object
le = LabelEncoder()

# Use the fit_transform method on the 'Sex' column
df['Sex'] = le.fit_transform(df['Sex'])
