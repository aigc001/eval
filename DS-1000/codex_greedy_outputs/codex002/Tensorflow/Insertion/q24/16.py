
  diff = tf.square(tf.subtract(A, B))
  l2_norm = tf.reduce_sum(diff, axis=1)
  return l2_norm
