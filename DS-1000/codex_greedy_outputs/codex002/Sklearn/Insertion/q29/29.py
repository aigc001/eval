
# Fit the pipeline
pipe.fit(data)

# Get the TF-IDF matrix
tfidf_matrix = pipe.named_steps["tf_idf"].transform(data)

# Get the NMF matrix
nmf_matrix = pipe.named_steps["nmf"].transform(tfidf_matrix)
