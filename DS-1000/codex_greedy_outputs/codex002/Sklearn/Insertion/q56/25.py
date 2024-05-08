
query_tfidf = tfidf.transform(queries)
cosine_similarities = np.dot(query_tfidf, tfidf.components_.T)
