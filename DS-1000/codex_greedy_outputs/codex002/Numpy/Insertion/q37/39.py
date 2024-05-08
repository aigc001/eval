
def pad(A, length):
    size = A.size
    pad_size = length - size
    padded_array = np.pad(A, (0, pad_size), 'constant')
    return padded_array

A = np.array([1,2,3,4,5])
length = 8
print(pad(A, length))
