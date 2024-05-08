
    return z

# Create a grid of points
s_grid, t_grid = np.meshgrid(example_s, example_t)

# Create an interpolator
interp = scipy.interpolate.interp2d(s_grid, t_grid, f(s_grid, t_grid), kind='cubic')

# Create a list of points to interpolate
s_values = np.array([-0.5, 0.5])
t_values = np.array([-1, -0.5])

# Interpolate the points
interpolated_values = interp(s_values, t_values)

print(interpolated_values)
