
    return [tf.io.decode_raw(i, tf.uint8).numpy().tostring().decode('utf-8') for i in x]
