
def prePro(text):
    return text.lower()

data = pd.DataFrame({'text': ['Hello World', 'Python is awesome', 'I love programming']})

vectorizer = TfidfVectorizer(preprocessor=prePro)
X = vectorizer.fit_transform(data['text'])
