
    def integrand(x):
        return 2 * x * c

    result, error = scipy.integrate.quad(integrand, low, high)
    return result

c_values = [1, 2, 3, 4, 5]
integral_values = [f(c=c) for c in c_values]
