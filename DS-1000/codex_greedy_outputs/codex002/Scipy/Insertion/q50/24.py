
# Calculate the mean
mean = np.mean(a)

# Calculate the fourth moment about the mean
fourth_moment = np.mean((a - mean)**4)

# Calculate the square of the variance
variance_squared = np.var(a)**2

# Calculate the excess kurtosis
kurtosis = fourth_moment / variance_squared - 3

print(kurtosis)
