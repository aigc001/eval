
def dN1_dt_complex(t, N1):
    return -100 * N1 - np.cos(t)

def N1_solution(t):
    return N0 * np.exp(-100 * t) - np.sin(t) + np.cos(t)

t = np.linspace(time_span[0], time_span[1], 1000)
sol = scipy.integrate.solve_ivp(fun=dN1_dt_complex, t_span=time_span, y0=[N0,])

plt.plot(t, N1_solution(t), label='Expected')
plt.plot(sol.t, sol.y[0], label='Solution')
plt.legend()
plt.xlabel('t')
plt.ylabel('N1')
plt.show()
