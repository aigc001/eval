
# Create a tensor of ones with shape (sum of lengths, 8)
ones = tf.ones((sum(lengths), 8), dtype=tf.int32)

# Create a tensor of zeros with shape (sum of lengths, max_length - lengths)
zeros = tf.zeros((sum(lengths), 8 - max(lengths)), dtype=tf.int32)

# Concatenate ones and zeros along the second axis
mask = tf.concat([ones, zeros], axis=1)

# Reshape mask to the final shape (length of lengths, max_length, 8)
mask = tf.reshape(mask, (len(lengths), max(lengths), 8))

# Create a mask of 1s and 0s whose number of 0s correspond to the entries to the lengths tensor
final_mask = tf.concat([tf.ones((1, 8), dtype=tf.int32), mask], axis=0)

# Print the final mask
print(final_mask)
