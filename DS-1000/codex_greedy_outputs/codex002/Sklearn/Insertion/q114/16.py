
# Tokenize the descriptions
df['description'] = df['description'].apply(lambda x: x.split())

# Fit and transform the data
tfidf_matrix = tfidf.fit_transform(df['description'])

# Calculate the cosine similarity
cosine_similarity = sklearn.metrics.pairwise.cosine_similarity(tfidf_matrix)

# Create a DataFrame from the cosine similarity matrix
similarity_df = pd.DataFrame(cosine_similarity, index=df['items'], columns=df['items'])
