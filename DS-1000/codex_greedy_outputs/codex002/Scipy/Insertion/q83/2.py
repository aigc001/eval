
def integrand(x):
    return 2 * x * c

result, error = scipy.integrate.quad(integrand, low, high)
print(result)
