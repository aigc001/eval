
def func(x, a):
    return a.dot(x ** 2)

def residual(x, a, y):
    return func(x, a) - y

res = scipy.optimize.minimize(residual, x0, args=(a, y))
x_opt = res.x
