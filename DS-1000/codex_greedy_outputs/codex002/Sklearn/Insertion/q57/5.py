
    query_matrix = tfidf.transform(queries)
    cosine_similarities = np.dot(query_matrix, tfidf.components_.T)
    return cosine_similarities
