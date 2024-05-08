
# Convert the list of integers to a tensor
labels_tensor = tf.constant(labels, dtype=tf.int32)

# Create a tensor of zeros with the same shape as the labels tensor
zeros_tensor = tf.zeros_like(labels_tensor)

# Create a tensor of ones with the same shape as the labels tensor
ones_tensor = tf.ones_like(labels_tensor)

# Create a tensor of zeros with the same shape as the labels tensor, except for the last dimension
# which is increased by one to accommodate the extra dimension required for the one-hot encoding
zeros_expanded_tensor = tf.expand_dims(zeros_tensor, axis=-1)

# Create a tensor of ones with the same shape as the labels tensor, except for the last dimension
# which is increased by one to accommodate the extra dimension required for the one-hot encoding
ones_expanded_tensor = tf.expand_dims(ones_tensor, axis=-1)

# Create a tensor of zeros with the same shape as the labels tensor, except for the last dimension
# which is increased by one to accommodate the extra dimension required for the one-hot encoding
labels_expanded_tensor = tf.expand_dims(labels_tensor, axis=-1)

# Create a tensor of zeros with the same shape as the labels tensor, except for the last dimension
# which is increased by one to accommodate the extra dimension required for the one-hot encoding
one_hot_tensor = tf.scatter_nd(labels_expanded_tensor, ones_expanded_tensor, tf.shape(zeros_expanded_tensor))

print(one_hot_tensor)
