
# Define the vocabulary
vocabulary = ['Jscript','.Net','TypeScript','SQL', 'NodeJS','Angular','Mongo','CSS','Python','PHP','Photoshop','Oracle','Linux','C++',"Java",'TeamCity','Frontend','Backend','Full stack', 'UI Design', 'Web','Integration','Database design','UX']

# Create a dataframe from the vocabulary
df = pd.DataFrame(vocabulary, columns=['words'])

# Assign a unique integer to each word in the vocabulary
df['word_id'] = range(len(vocabulary))

# Create a dictionary where the keys are the words and the values are the word_ids
word_dict = df.set_index('words').to_dict()['word_id']

# Create a CountVectorizer object and pass the word_dict to the vocabulary parameter
vectorizer = CountVectorizer(binary=True, lowercase=False, vocabulary=word_dict)

# Fit the vectorizer to the corpus and transform the corpus
X = vectorizer.fit_transform(corpus)

# Print the feature names and the matrix X
print(vectorizer.get_feature_names())
print(X.toarray())
