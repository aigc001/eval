
# Get the total vocabulary from the word2vec model
total_vocab = word2vec.wv.vocab

# Create a mapping from word to index
word_to_index = {word: index for index, word in enumerate(total_vocab)}

# Get the total number of words in the vocabulary
total_words = len(total_vocab)

# Create a matrix to hold the word vectors
weights_matrix = np.zeros((total_words, word2vec.vector_size))

# Fill in the weights_matrix with the word vectors
for word, index in word_to_index.items():
    weights_matrix[index] = word2vec.wv[word]

# Create a PyTorch embedding layer
embedding_layer = torch.nn.Embedding.from_pretrained(torch.FloatTensor(weights_matrix))

# Embed the input data
embedded_input = embedding_layer(input_Tensor)
