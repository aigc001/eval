
def func(x, A, B, C):
    return A * np.exp(B * x) + C

popt, pcov = scipy.optimize.curve_fit(func, x, y, p0=p0)

print(popt)
