
dev = abs((x-u)/o2)
P_inner = scipy.integrate.quad(NDfx,-dev,dev)
P_outer = 1 - P_inner[0]
P = P_inner[0] + P_outer/2
print(P)
