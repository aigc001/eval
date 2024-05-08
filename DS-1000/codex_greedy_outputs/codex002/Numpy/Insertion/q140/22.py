
# Calculate the mean and standard deviation
mean = np.mean(a)
std = np.std(a)

# Define the 2nd standard deviation interval
lower_bound = mean - 2 * std
upper_bound = mean + 2 * std

# Create a boolean array where True indicates an outlier
outliers = (a < lower_bound) | (a > upper_bound)
