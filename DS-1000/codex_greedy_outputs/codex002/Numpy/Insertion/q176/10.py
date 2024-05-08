
def rolling_window(a, size):
    shape = (a.shape[0] - size[0] + 1,) + (a.shape[1] - size[1] + 1,) + size
    strides = a.strides + a.strides
    return np.lib.stride_tricks.as_strided(a, shape=shape, strides=strides)

windows = rolling_window(a, size)
