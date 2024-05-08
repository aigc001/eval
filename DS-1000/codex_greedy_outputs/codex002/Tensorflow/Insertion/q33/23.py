
# Mask the padded values
mask = tf.cast(tf.not_equal(x, 0), tf.float32)

# Calculate the mean
mean = tf.reduce_sum(x * mask, axis=-1) / tf.reduce_sum(mask, axis=-1)

# Calculate the variance
variance = tf.reduce_sum((x - mean[:, :, :, tf.newaxis]) ** 2 * mask, axis=-1) / tf.reduce_sum(mask, axis=-1)

# Print the result
print(variance.numpy())
