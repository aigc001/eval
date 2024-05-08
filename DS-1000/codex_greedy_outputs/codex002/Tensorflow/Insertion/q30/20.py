
# Convert the list of bytes to a Tensor
x_tensor = tf.constant(x)

# Decode the bytes to strings
x_strings = tf.strings.decode(x_tensor, 'utf-8')

# Convert the Tensor to a list of strings
x_list = x_strings.numpy().tolist()

print(x_list)
