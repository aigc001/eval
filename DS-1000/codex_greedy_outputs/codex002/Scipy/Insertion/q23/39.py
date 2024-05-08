
def cost(x):
    return np.sum(np.sqrt(np.sum((points1-points2[x])**2, axis=1)))

res = scipy.optimize.minimize(cost, range(N), method='powell')
