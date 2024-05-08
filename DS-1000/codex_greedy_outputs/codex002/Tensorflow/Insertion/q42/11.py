
tf.random.set_seed(seed_x)

# Generate 114 random integers in the range [2, 5]
result = tf.random.uniform([114], minval=2, maxval=5, dtype=tf.int32)
