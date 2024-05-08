
# Initialize CountVectorizer
vectorizer = CountVectorizer(token_pattern=r"(?u)\b\w+\b|[!?]|\"|\'")

# Fit and transform the data
data_matrix = vectorizer.fit_transform(text)

# Get the feature names
feature_names = vectorizer.get_feature_names()

# Create a dataframe
df = pd.DataFrame(data_matrix.toarray(), columns=feature_names)
