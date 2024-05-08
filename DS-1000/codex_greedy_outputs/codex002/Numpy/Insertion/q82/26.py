
def ecdf(x):
    x = np.sort(x)
    n = len(x)
    y = np.arange(1, n + 1) / n
    return x, y

x, y = ecdf(grades)
