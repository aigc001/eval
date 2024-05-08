
# Create a tensor with the shape of the required tensor
required_tensor = tf.zeros((len(labels), 10), dtype=tf.int32)

# Iterate over the list of labels
for i, label in enumerate(labels):
    # Set the label index to 1 in the required tensor
    required_tensor[i, label] = 1

print(required_tensor)
