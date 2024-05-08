
# Calculate the mean and standard deviation
mean = np.mean(a)
std = np.std(a)

# Calculate the 3rd standard deviation
third_std = 3 * std

# Calculate the start and end of the 3rd standard deviation interval
start = mean - third_std
end = mean + third_std

# Return the result as a tuple
result = (start, end)
