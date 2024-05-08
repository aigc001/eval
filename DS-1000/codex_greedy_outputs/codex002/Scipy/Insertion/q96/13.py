
result = []
for x, a in zip(xdata, adata):
    root = fsolve(eqn, x0=0.5, args=(x, a))
    root.sort()
    result.append(root)
