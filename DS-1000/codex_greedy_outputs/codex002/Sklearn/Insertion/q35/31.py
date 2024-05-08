
def preprocess(s):
    return s.upper()

# Create a sample dataframe
data = {'text': ['Hello, how are you?', 'I am fine.', 'Thank you.']}
df = pd.DataFrame(data)

# Create a TfidfVectorizer object and pass the preprocessor to it
vectorizer = TfidfVectorizer(preprocessor=preprocess)

# Fit and transform the data
X = vectorizer.fit_transform(df['text'])

# Print the transformed data
print(X.toarray())
