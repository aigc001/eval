
# Mask the padded values
mask = tf.cast(tf.not_equal(x, 0), tf.float32)

# Calculate the sum of non-zero entries
sum_non_zero = tf.reduce_sum(x * mask, axis=-1, keepdims=True)

# Calculate the count of non-zero entries
count_non_zero = tf.reduce_sum(mask, axis=-1, keepdims=True)

# Average the non-zero entries
y = sum_non_zero / count_non_zero

# Replace the zero entries with the averages
y = tf.where(tf.equal(x, 0), y, x)
