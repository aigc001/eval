
def dN_dt(t, N):
    return -100 * N + np.sin(t)

def N(t):
    return N0 + scipy.integrate.quad(dN_dt, 0, t)[0]

t = np.linspace(0, 10, 1000)
N_values = [N(ti) for ti in t]
