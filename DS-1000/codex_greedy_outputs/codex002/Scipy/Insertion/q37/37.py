
def fourier(x, *a):
    return sum(a[i] * np.cos(i * np.pi / tau * x) for i in range(len(a)))

popt, pcov = curve_fit(fourier, z, Ua, p0=[1]*degree)
