
# Reshape A and B to [B,N,1,S] and [B,1,N,S] respectively
A_reshape = tf.reshape(A, [tf.shape(A)[0], tf.shape(A)[1], 1, tf.shape(A)[2]])
B_reshape = tf.reshape(B, [tf.shape(B)[0], 1, tf.shape(B)[1], tf.shape(B)[2]])

# Use tf.matmul to perform the dot product
C = tf.matmul(A_reshape, B_reshape)

# Reshape C to [B,B,N]
C = tf.reshape(C, [tf.shape(A)[0], tf.shape(B)[0], tf.shape(A)[1]])
