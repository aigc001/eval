
# Calculate the fourth moment (Fisher's definition)
m4 = np.mean((a - np.mean(a))**4)

# Calculate the square of the variance
var_squared = np.var(a)**2

# Calculate the excess kurtosis
kurt = m4/var_squared - 3

print("Excess kurtosis: ", kurt)
