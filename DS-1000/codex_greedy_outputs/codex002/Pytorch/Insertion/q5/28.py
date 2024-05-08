
    # Convert the input tensor to a list of words
    words = [word for sentence in input_Tensor for word in sentence]

    # Get the word vectors from word2vec
    word_vectors = [word2vec.wv[word] for word in words]

    # Convert the word vectors to a tensor
    embedded_input = torch.tensor(word_vectors)

    return embedded_input
