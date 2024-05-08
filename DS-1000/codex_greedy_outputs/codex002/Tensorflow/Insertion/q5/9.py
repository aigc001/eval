
    # Create a tensor with the shape of the labels and the same type
    tensor = tf.zeros(shape=(len(labels), 10), dtype=tf.int32)

    # Iterate over the labels and set the corresponding index to 1
    for i, label in enumerate(labels):
        tensor[i][label] = 1

    return tensor
