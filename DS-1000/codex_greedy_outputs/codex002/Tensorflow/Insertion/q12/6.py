
    max_length = 8
    mask = []
    for length in lengths:
        mask.append([1]*length + [0]*(max_length - length))
    return tf.convert_to_tensor(mask)
