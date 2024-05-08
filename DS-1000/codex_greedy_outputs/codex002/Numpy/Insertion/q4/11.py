
max_val = np.max(a)
b = np.zeros((a.size, max_val + 1))
b[np.arange(a.size), a] = 1
