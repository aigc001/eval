
from scipy.optimize import fminbound
popt = np.array([fminbound(e, pmin[i], pmax[i], args=(x,y[i])) for i in range(len(pmin))])
