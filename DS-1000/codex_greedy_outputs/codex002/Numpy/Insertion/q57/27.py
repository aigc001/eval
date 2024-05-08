
_, s, v = np.linalg.svd(a)
max_set = v[:s.size]
