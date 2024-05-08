
f = scipy.interpolate.interp2d(s, t, z, kind='cubic')
s_values = np.array([-0.5, 0.5])
t_values = np.array([-1, -0.5])
result = f(s_values, t_values)
