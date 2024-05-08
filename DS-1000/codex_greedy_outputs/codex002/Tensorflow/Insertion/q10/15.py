
# Create a tensor of ones with shape (sum(lengths),)
ones = tf.ones(sum(lengths))

# Create a tensor of zeros with shape (8 - sum(lengths),)
zeros = tf.zeros(8 - sum(lengths))

# Concatenate the ones and zeros
mask = tf.concat([zeros, ones], axis=0)

# Reshape the mask to shape (4, 8)
mask = tf.reshape(mask, (4, 8))

# Create a cumulative sum of the lengths
cumulative_lengths = tf.cumsum(lengths)

# Create a mask for each row
row_masks = tf.split(mask, cumulative_lengths)

# Create the final mask by concatenating the row masks
final_mask = tf.concat([tf.pad(row_mask, [[0, 0], [0, 8 - lengths[i]]]) for i, row_mask in enumerate(row_masks)], axis=0)

print(final_mask)
