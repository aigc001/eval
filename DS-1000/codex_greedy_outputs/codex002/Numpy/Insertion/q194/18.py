
# Reshape B to be (1, 3, 3)
B = B.reshape(1, 3, 3)

# Use np.matmul to perform matrix multiplication
result = np.matmul(A, B)
