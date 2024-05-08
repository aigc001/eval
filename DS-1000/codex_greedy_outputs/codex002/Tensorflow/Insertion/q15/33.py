
  # Create a grid of indices
  indices_a = tf.tile(tf.expand_dims(tf.range(tf.size(a)), 1), [1, tf.size(b)])
  indices_b = tf.tile(tf.expand_dims(tf.range(tf.size(b)), 0), [tf.size(a), 1])

  # Gather elements from a and b based on the indices
  result = tf.stack([tf.gather(a, indices_a), tf.gather(b, indices_b)], axis=-1)

  return result
