
# Create a tensor with the shape of the one hot vectors and the type of the labels
one_hot_labels = tf.zeros((len(labels), max(labels)+1), dtype=tf.int32)

# Iterate over the labels and set the corresponding index to 1
for i, label in enumerate(labels):
    one_hot_labels[i, label] = 1

print(one_hot_labels)
