
# Assuming the last column is the one you want to break down
# Let's call it 'fruit_list'

# First, we need to convert the list of fruits into a DataFrame
df_fruits = pd.DataFrame(df['fruit_list'].tolist())

# Now, we can use sklearn's OneHotEncoder to convert the fruit DataFrame into a one-hot-encoded DataFrame
from sklearn.preprocessing import OneHotEncoder
encoder = OneHotEncoder(sparse=False)
df_encoded = encoder.fit_transform(df_fruits)

# Now, we need to convert this numpy array back into a DataFrame
df_encoded = pd.DataFrame(df_encoded, columns=encoder.get_feature_names())

# Finally, we can join this new DataFrame with the original DataFrame
df = pd.concat([df, df_encoded], axis=1)

# And we can drop the original fruit list column
df = df.drop('fruit_list', axis=1)
