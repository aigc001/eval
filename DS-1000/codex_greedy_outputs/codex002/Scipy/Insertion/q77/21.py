
def dN1_dt_time_varying(t, N1):
    return -100 * N1 + np.sin(t)

time_points = np.linspace(time_span[0], time_span[1], 1000)
sol = scipy.integrate.solve_ivp(fun=dN1_dt_time_varying, t_span=time_span, y0=[N0,], t_eval=time_points)

import matplotlib.pyplot as plt
plt.plot(sol.t, sol.y[0])
plt.xlabel('t')
plt.ylabel('N1')
plt.show()
