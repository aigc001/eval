
a_solutions = []
for x, b in zip(xdata, bdata):
    a_root = fsolve(eqn, x0=0.5, args=(x, b))
    a_solutions.append(a_root)
a_solutions = np.array(a_solutions)
