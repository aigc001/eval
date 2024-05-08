
# Convert the list of integers to a tensor
labels_tensor = tf.constant(labels, dtype=tf.int32)

# Create a tensor of zeros with the same shape as the labels tensor
zeros_tensor = tf.zeros_like(labels_tensor)

# Create a tensor of ones with the same shape as the labels tensor
ones_tensor = tf.ones_like(labels_tensor)

# Create a tensor of shape (len(labels), max(labels) + 1) filled with zeros
output_tensor = tf.zeros((len(labels), max(labels) + 1), dtype=tf.int32)

# Modify the output tensor to have ones in the positions corresponding to the labels
output_tensor = tf.tensor_scatter_nd_update(output_tensor, tf.expand_dims(labels_tensor, 1), ones_tensor)

print(output_tensor)
