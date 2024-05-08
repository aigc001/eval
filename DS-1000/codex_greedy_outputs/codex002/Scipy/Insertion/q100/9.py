
# Convert lists to numpy arrays
x = np.array(x)
y = np.array(y)
eval = np.array(eval)

# Use griddata for interpolation
result = scipy.interpolate.griddata(x, y, eval, method='linear')

print(result)
