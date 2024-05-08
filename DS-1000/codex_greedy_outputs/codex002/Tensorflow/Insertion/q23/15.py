
diff = tf.square(tf.subtract(a, b))
dist = tf.reduce_sum(diff, axis=0)
