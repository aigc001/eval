
B = pd.Series(index=A.index)
B[0] = a * A[0]
B[1] = a * A[1] + b * B[0]
for t in range(2, len(A)):
    B[t] = a * A[t] + b * B[t-1] + c * B[t-2]
