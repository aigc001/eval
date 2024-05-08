
pad_width = length - len(A)
if pad_width > 0:
    A = np.pad(A, (0, pad_width), 'constant')
