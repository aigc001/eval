
# Fit the pipeline up to the NMF step
pipe.fit(data.test)

# Transform the data with the TfidfVectorizer
tfidf_data = pipe.named_steps["tf_idf"].transform(data.test)

# Now you can apply the NMF to the tfidf_data
nmf_data = pipe.named_steps["nmf"].transform(tfidf_data)
