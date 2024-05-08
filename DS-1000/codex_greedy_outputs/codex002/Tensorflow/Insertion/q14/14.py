
# Use tf.reshape and tf.tile to repeat 'a' and 'b' enough times to get all combinations
a_repeated = tf.reshape(tf.tile(a, [tf.size(b)]), [tf.size(b), tf.size(a)])
b_repeated = tf.reshape(tf.tile(b, [tf.size(a)]), [tf.size(a), tf.size(b)])
b_repeated = tf.transpose(b_repeated)

# Combine 'a_repeated' and 'b_repeated' to get all combinations
combinations = tf.concat([tf.expand_dims(a_repeated, 2), tf.expand_dims(b_repeated, 2)], axis=2)

# Reshape 'combinations' to get a flat tensor of all combinations
combinations = tf.reshape(combinations, [tf.size(a)*tf.size(b), 2])
