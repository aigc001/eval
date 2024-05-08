
# Create a tensor of zeros with shape (len(lengths), 8)
mask = tf.zeros((len(lengths), 8), dtype=tf.float32)

# Set the first 'length' elements of each row to 1
for i, length in enumerate(lengths):
    mask[i, :length] = 1.

print(mask)
