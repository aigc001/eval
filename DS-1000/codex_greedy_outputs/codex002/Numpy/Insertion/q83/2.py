
def ecdf(x):
    x = np.sort(x)
    n = len(x)
    def _ecdf(v):
        return (np.searchsorted(x, v, side='right') + 1) / n
    return _ecdf

ecdf_func = ecdf(grades)

ecdf_values = ecdf_func(eval)

print(ecdf_values)
