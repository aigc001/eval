
# Create a tensor of ones with shape (len(lengths), max(lengths))
mask = tf.ones((len(lengths), max(lengths)))

# Create a tensor of zeros with shape (len(lengths),)
zeros = tf.zeros((len(lengths),))

# Assign the zeros to the positions in the mask tensor specified by the lengths
mask = tf.tensor_scatter_nd_update(mask, tf.expand_dims(tf.range(len(lengths)), 1), tf.expand_dims(zeros, 1))

# Assign the lengths to the positions in the mask tensor specified by the lengths
mask = tf.tensor_scatter_nd_update(mask, tf.expand_dims(tf.range(len(lengths)), 1), tf.expand_dims(lengths, 1))

# Print the mask tensor
print(mask)
