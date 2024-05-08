
    # Mask the padded values
    mask = tf.cast(tf.not_equal(x, 0), tf.float32)

    # Calculate the sum of the non-zero entries
    sum_non_zero = tf.reduce_sum(x * mask, axis=-2, keepdims=True)

    # Calculate the count of the non-zero entries
    count_non_zero = tf.reduce_sum(mask, axis=-2, keepdims=True)

    # Average the non-zero entries
    avg_non_zero = tf.divide(sum_non_zero, count_non_zero)

    # Replace the zero entries with the average of the non-zero entries
    result = tf.where(tf.equal(x, 0), avg_non_zero, x)

    return result
