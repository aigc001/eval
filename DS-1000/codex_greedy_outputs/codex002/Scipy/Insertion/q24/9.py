
def cost(x):
    return np.sum(np.abs(points1 - points2[x]))

def constraint(x):
    return np.bincount(x) - 1

x0 = np.zeros(N, dtype=int)
res = scipy.optimize.minimize(cost, x0, constraints={'type': 'eq', 'fun': constraint}, method='SLSQP')
assignment = res.x
