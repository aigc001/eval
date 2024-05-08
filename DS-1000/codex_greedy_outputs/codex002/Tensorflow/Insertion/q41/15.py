
tf.random.set_seed(seed_x)

# Create a tensor with 10 random integers from 1 to 4
result = tf.random.uniform([10], minval=1, maxval=5, dtype=tf.int32)
